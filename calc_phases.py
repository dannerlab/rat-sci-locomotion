# 
# This file is part of https://github.com/dannerlab/rat-sci-locomotion.
# Copyright (c) 2023 Simon M. Danner.
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
import pandas as pd
import numpy as np

limb_names = ['lh','rh','lf','rf']

# use left hindlimb as reference limb
ref_leg=0    
phase_diffs = [(0,1),(0,2),(0,3)]

# uncomment to use right hindlimb as reference limb
#ref_leg=1      
#phase_diffs = [(1,0),(1,3),(1,2)]


phase_names = ['LR_h','hl','diag']
crit = 'midstance'
def calc_sup(df):
    now = 0
    res = list()
    stack = list()
    for i, (index,row) in enumerate(df.iterrows()):
        new = row
        while(True):
            if (len(stack)>0) and (stack[0][0].offset < new.onset):
                res.append((stack[0][0].offset,now,stack[0][0].leg,stack[0][1],'off'))
                now -=1
                stack.pop(0)
                continue
            else:
                res.append((new.onset,now,new.leg,index,'on'))
                now += 1
                break
        stack.append((new,index))
        stack = sorted(stack,key=lambda x:x[0].offset)
    res.append((new.offset,0,new.leg,len(df)-1,'off'))
    return pd.DataFrame(res,columns=['t', 'n', 'leg', 'ind','type'])

def calc_phase_df(df):
    df_out = pd.DataFrame({})
    if np.sum(np.diff(df.iloc[:4][crit])) < 0.01:
        df=df[4:]
    ref=df[df.leg==ref_leg].iloc[:-1]
    #if not np.all(np.isin(np.setdiff1d([0,1,2,3],ref_leg),df[ref.tail(1).index.item():].leg)):
    #    ref=ref.iloc[:-1]                                         
    phase_dur = ref.swing_dur+ref.stance_dur
    M=np.ones((len(ref),4))*np.nan
    for i, (index,row) in enumerate(ref.iterrows()):
        M[i][ref_leg] = index
        for l in np.setdiff1d([0,1,2,3],ref_leg):
            for k in range(15):
                if not np.isin(k+index+1, df.index):
                    #print(i,index,l,k,k+index+1,'b')
                    break
                nr = df.loc[index+k+1]
                if int(nr.leg) == l:
                    M[i][l] = k+index+1
                    break
    
    phases=np.zeros((len(ref),len(phase_diffs)))
    for i,(x,y) in enumerate(phase_diffs):
        with np.errstate(invalid='ignore'):
            df_out[phase_names[i]] =((np.array(df.reindex(M[:,y])[crit])-np.array(df.reindex(M[:,x])[crit]))/np.array(phase_dur)) % 1.0
    for i in range(len(limb_names)):
        df_out['swing_dur_'+limb_names[i]] = np.array(df.reindex(M[:,i]).swing_dur)
        df_out['stance_dur_'+limb_names[i]] = np.array(df.reindex(M[:,i]).stance_dur)
        df_out['step_width_x_'+limb_names[i]] = np.array(df.reindex(M[:,i]).step_width_x)
        df_out['step_width_y_'+limb_names[i]] = np.array(df.reindex(M[:,i]).step_width_y)
        df_out['x_stance_'+limb_names[i]] = np.array(df.reindex(M[:,i]).x_stance)
        df_out['y_stance_'+limb_names[i]] = np.array(df.reindex(M[:,i]).y_stance)
        df_out['onset_'+limb_names[i]] = np.array(df.reindex(M[:,i]).onset)
        df_out['offset_'+limb_names[i]] = np.array(df.reindex(M[:,i]).offset)
        df_out['midstance_'+limb_names[i]] = np.array(df.reindex(M[:,i]).midstance)
    df_out['phase_dur'] = np.array(phase_dur)
    res = calc_sup(df)
    ins = res[(res.leg==ref_leg)&(res.type=='on')].index 
    dsup=np.zeros((len(df_out),5))
    for i in range(len(ins[:-1])):
        dsup_=np.zeros((5,))
        rs = res[ins[i]:ins[i+1]+1].values
        for j in range(len(rs)-1):
            dsup_[rs[j+1][1]] += rs[j+1][0]-rs[j][0]
        dsup[i]=dsup_/(rs[-1][0]-rs[0][0])
    dsup=pd.DataFrame(dsup,columns=['nolimb','onelimb','twolimb','threelimb','fourlimb'])
    df_out=pd.concat([df_out,dsup],axis=1)                                                                                                    
    return df_out

df_raw = pd.read_hdf("./data/df_raw.h5",key='df_raw')
df_raw['midstance']=(df_raw.onset+df_raw.offset)*0.5
df_phases = pd.DataFrame({})
for id in pd.unique(df_raw.ID):
    df_id=df_raw[df_raw.ID==id]
    for rid in pd.unique(df_id.RID):
        df_rid = df_id[df_id['RID']==rid]
        df2_ = pd.DataFrame({})
        for i, bout in enumerate(pd.unique(df_rid.bout)):
            df_bout = df_rid[df_rid.bout == bout]
            if len(df_bout)>10:
                df_phase = calc_phase_df(df_bout)
                df_phase['bout']=bout
                df2_ = pd.concat([df2_,df_phase],ignore_index=True)

        df2_['ID'] = id
        df2_['RID'] = rid
        df2_['SCI'] = df_bout['SCI'].iloc[0]
        df2_=df2_[df2_.columns[-3:].append(pd.Index([df2_.columns[-4]]).append(df2_.columns[:-4]))]
        df2_['filename'] = df_bout['filename'].iloc[0]
        df_phases = pd.concat([df_phases,df2_],ignore_index=True)  
df_phases['frequency']=1.0/df_phases.phase_dur
df_phases['LR_f']=(df_phases.diag-df_phases.hl) %1.0
df_phases['hl_r']=(df_phases.diag-df_phases.LR_h) %1.0
df_phases['diag_2']=(df_phases.hl-df_phases.LR_h) %1.0


from classify_gait import classify_gait

for l in ['lh', 'rh', 'lf', 'rf']:
    df_phases['duty_factor_' + l] = df_phases['stance_dur_' + l] / (
        df_phases['stance_dur_' + l] + df_phases['swing_dur_' + l])

df_phases['duty_factor'] = df_phases[[
    'duty_factor_lh', 'duty_factor_rh', 'duty_factor_lf', 'duty_factor_rf'
    ]].mean(axis=1,skipna=True)
df_phases['duty_factor_h']=(df_phases.duty_factor_lh+df_phases.duty_factor_rh)*0.5
df_phases['duty_factor_f']=(df_phases.duty_factor_lf+df_phases.duty_factor_rf)*0.5

df_phases['swing_dur_h']=(df_phases.swing_dur_lh+df_phases.swing_dur_rh)*0.5
df_phases['swing_dur_f']=(df_phases.swing_dur_lf+df_phases.swing_dur_rf)*0.5


df_phases['stance_dur_h']=(df_phases.stance_dur_lh+df_phases.stance_dur_rh)*0.5
df_phases['stance_dur_f']=(df_phases.stance_dur_lf+df_phases.stance_dur_rf)*0.5

dist_l = np.sqrt([df_phases['step_width_x_' + leg]**2.0 + df_phases['step_width_y_' + leg]**2.0    
                          for leg in ['lh','rh','lf','rf']])
df_phases['stride_len'] = np.nanmean(dist_l,axis=0)
df_phases['stride_len_h'] = np.nanmean(np.sqrt([df_phases['step_width_x_' + leg]**2.0 + df_phases['step_width_y_' + leg]**2.0    
                          for leg in ['lh','rh']]),axis=0)
df_phases['stride_len_f'] = np.nanmean(np.sqrt([df_phases['step_width_x_' + leg]**2.0 + df_phases['step_width_y_' + leg]**2.0    
                          for leg in ['lf','rf']]),axis=0)
for leg in ['lh','rh','lf','rf']:
    df_phases['stride_len_'+leg] = np.sqrt(df_phases['step_width_x_' + leg]**2.0 + df_phases['step_width_y_' + leg]**2.0)

classify_gait(df_phases)
df_phases.loc[(pd.isna(df_phases.gaits_all))|(pd.isna(df_phases.duty_factor)),['stride_len']]=np.nan

df_phases['speed'] = df_phases.stride_len/df_phases.phase_dur
df_phases.loc[(df_phases.frequency<2.0)|(df_phases.frequency>10.0),['frequency']]=np.nan
df_phases.loc[(df_phases.speed<10.0)|(df_phases.speed>280.0),['speed']]=np.nan

df_phases.to_hdf("./data/df_phases.h5",key='df_phases',format='t')