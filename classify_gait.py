import numpy as np
import pandas as pd

def classify_gait(df):
    gaits = {
            'pronk': np.array([0.0,0.0,0.0]),
        
            'trot': np.array([0.5,0.5,0.0]),
            'bound': np.array([0.0,0.5,0.5]),
            'bound_2': np.array([0.0,2/3,2/3]),
            'pace': np.array([0.5,1.0,0.5]),
        
            'hbound': np.array([0.0,1/3,2/3]),
            'hbound_2': np.array([0.0,2/3,1/3]),
        
            'canter': np.array([2/3,1/3,0]),
            'canter_2': np.array([1/3,1/3,2/3]),
            'canter_3': np.array([1/3,2/3,0]),
            'canter_4': np.array([2/3,2/3,1/3]),
        
            'rhbound': np.array([1/3,2/3,2/3]),
            'rhbound_2': np.array([2/3,1/3,1/3]),
        
            'lcanter': np.array([1/3,0,2/3]),
            'lcanter_2': np.array([2/3,0,1/3]),
            'lcanter_3': np.array([1/3,2/3,1/3]),
            'lcanter_4': np.array([2/3,1/3,2/3]),
            
            'rot_1': np.array([0.75,0.25,0.5]),
            'rot_2': np.array([0.25,0.75,0.5]),
            'lat_seq': np.array([0.5,0.25,0.75]),
            'diag_seq': np.array([0.5,0.75,0.25]),
            'trans_1': np.array([0.75,0.5,0.25]),
            'trans_2': np.array([0.25,0.5,0.75]),
            }
    
    D = df[['LR_h','hl','diag']]
    temp = pd.DataFrame()
    for gait, m_gait in gaits.items():
        tp=np.abs(m_gait-D)
        tp[tp>0.5]=tp[tp>0.5]-1
        temp[gait] = np.sum((tp)**2.0,axis=1)
    gaits=temp.idxmin(axis=1)
    gaits[np.any(pd.isna(D),axis=1)]=np.nan
    gaits[gaits=='bound_2'] = 'bound'

    gaits[(df.duty_factor>=0.5)&(gaits=='lat_seq')]='walk_lat'
    gaits[(df.duty_factor>=0.5)&(gaits=='diag_seq')]='walk_diag'
    gaits[(df.duty_factor<0.5)&((gaits=='lat_seq'))]='run_lat'
    gaits[(df.duty_factor<0.5)&((gaits=='diag_seq'))]='run_diag'
    
    
    gaits[(df.duty_factor>=0.5)&((gaits=='rot_1')|(gaits=='rot_2'))]='walk_rot'
    gaits[(df.duty_factor>=0.5)&((gaits=='trans_1')|(gaits=='trans_2'))]='walk_trans'
    df['gaits_all2'] = pd.Categorical(
        gaits)
    gaits[(df.duty_factor<0.5)&((gaits=='rot_1')|(gaits=='rot_2'))]='gallop_rot'
    gaits[(df.duty_factor<0.5)&((gaits=='trans_1')|(gaits=='trans_2'))]='gallop_trans'
    gaits[gaits=='hbound_2'] = 'hbound'
    gaits[gaits=='rhbound_2'] = 'rhbound'
    gaits[gaits=='canter_2'] = 'canter'
    gaits[gaits=='canter_3'] = 'rcanter'
    gaits[gaits=='canter_4'] = 'rcanter'
    gaits[gaits=='lcanter_2'] = 'lcanter'
    gaits[gaits=='lcanter_3'] = 'lcanter'
    gaits[gaits=='lcanter_4'] = 'lcanter'
    
    gaits[(df.duty_factor>=0.5)&(gaits=='bound')]='hop'
    gaits[(df.duty_factor>=0.5)&(gaits=='hbound')]='hop'
    
    df['gaits_all'] = pd.Categorical(
        gaits)
    df['gaits'] = pd.Categorical(
        ['nd'] * len(df), ['nd', 'walk', 'trot','run','pace','canter','gallop', 'hbound', 'bound'])

    df.gaits[df.gaits_all=='walk_trans'] = 'walk'
    df.gaits[df.gaits_all=='walk_rot'] = 'walk'
    df.gaits[df.gaits_all=='walk_lat'] = 'walk'
    df.gaits[df.gaits_all=='walk_diag'] = 'walk'
    df.gaits[df.gaits_all=='trot'] = 'trot'
    df.gaits[df.gaits_all=='run_lat'] = 'run'
    df.gaits[df.gaits_all=='run_diag'] = 'run'
    df.gaits[df.gaits_all=='gallop_trans'] = 'gallop'
    df.gaits[df.gaits_all=='gallop_rot'] = 'gallop'
    df.gaits[df.gaits_all=='hbound'] = 'hbound'
    df.gaits[df.gaits_all=='bound'] = 'bound'
    df.gaits[df.gaits_all=='canter'] = 'canter'
    df.gaits[df.gaits_all=='pace'] = 'pace'
    return df