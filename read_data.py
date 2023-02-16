
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_files import file_desc
import seaborn as sns; sns.set(style="white", color_codes=True)
limb_names = ['lh','rh','lf','rf']


bout_threshold = .15 # seconds

def load_file_df(filename,c_names,sample_rate,ID,SCI):
    df = pd.read_excel(filename, sheet_name='Sheet1')
    df_times = pd.DataFrame({})
    time_points = np.array(df[df.columns[0]])
    if not c_names['X'][0] in df:
        print(filename,df.columns)

    for i,c_name in enumerate(c_names['X']):
        diff = np.diff(np.isnan(df[c_name]).astype(np.int32))
        onsets = time_points[:-1][diff==-1]
        offsets = time_points[:-1][diff==1]

        if onsets[0]>offsets[0]:
            print('something wrong while reading file')
        if onsets.shape != offsets.shape:
            print('something wrong while reading file')

        x_stance=np.array([np.median(df[c_name][o[0]:o[1]]) for o in zip(onsets,offsets-1)])
        y_stance=np.array([np.median(df[c_names['Y'][i]][o[0]:o[1]]) for o in zip(onsets,offsets-1)])
        
        df_ = pd.DataFrame({'leg':np.ones((len(onsets),),dtype=np.int32)*i,
                            'onset': onsets/sample_rate,
                            'offset': offsets/sample_rate,
                            'x_stance':x_stance, 
                            'y_stance':y_stance, 
                            'stance_dur': (offsets-onsets)/sample_rate,
                            'swing_dur': np.concatenate(((onsets[1:]-offsets[:-1])/sample_rate,[np.nan])),
                            'step_width_x': np.concatenate((np.diff(x_stance),[np.nan])),
                            'step_width_y': np.concatenate((np.diff(y_stance),[np.nan]))
                            })
        
        df_times = pd.concat([df_times,df_],ignore_index=True)
    df_times=df_times.sort_values('onset')
    d_bouts = np.where((np.array(df_times.onset)[1:]-np.array(df_times.offset)[:-1]) > bout_threshold)[0]+1
    d_bouts = np.concatenate(([0],d_bouts,[df_times.shape[0]]))
    
    in_bouts = np.zeros((df_times.shape[0],1),dtype=int)
    for i in range(len(d_bouts)-1):
        in_bouts[d_bouts[i]:d_bouts[i+1]] = int(i)
    df_times['bout'] = in_bouts
    df_times=df_times.reset_index(drop=True)
    for bout in pd.unique(df_times['bout']):
        for i in range(len(limb_names)):
            tmp=df_times.loc[np.logical_and(df_times['bout']==bout,df_times['leg']==i),['swing_dur']]
            if len(tmp)>0:
                tmp.iloc[-1]=np.nan
                df_times.loc[np.logical_and(df_times['bout']==bout,df_times['leg']==i),['swing_dur']]=tmp
    return  df_times


rid_list={}
df_raw = pd.DataFrame({})
for fd in file_desc:
    if fd['ID'] in rid_list:
        rid = rid_list[fd['ID']] + 1
        rid_list[fd['ID']] = rid_list[fd['ID']] + 1
    else:
        rid = 0
        rid_list[fd['ID']] = 0

    df1_ = load_file_df(**fd)
    df1_['ID'] = int(fd['ID'])
    df1_['RID'] = rid
    df1_['SCI'] = fd['SCI']
    df1_=df1_[df1_.columns[-3:].append(pd.Index([df1_.columns[-4]]).append(df1_.columns[:-4]))]
    df1_['filename'] = fd['filename']
    df_raw = pd.concat([df_raw,df1_],ignore_index=True)


df_raw.to_hdf("./df_raw.h5",key='df_raw')

