#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:36:31 2020

@author: stemonitis
"""

"""Calculating sundata"""

import sys
sys.path.append("/home/stemonitis/colours/scripts/Hyperion/")
import hyperion_sat as hyp
import pandas as pd
import numpy as np
#%%
#First get the hyperion datasets spectral center vecor Wv

path_AUX="/home/stemonitis/colours/satellites/EO1H0050092001160111PP/EO1H0050092001160111PP.AUX"
metadata=hyp.read_metadata(path_AUX)
spectral_center=hyp.read_spectral_center(metadata)
Wv=hyp.get_average_wv_for_each_calibrated_channel(spectral_center)


#%%

#Obtain the raw sun extraterrestial spectra 

xl=pd.read_excel("/home/stemonitis/colours/scripts/Hyperion/Deriving_solar_spectra/Extraterrestial_solar_spectra/MCebKur.xlsx")
ES_raw=np.array(xl)
#%%

#Pick ou the closest wavelengthes from the data to fit our satellite image 

def find_closest(A, target):
    #A must be sorted
    idx = A.searchsorted(target)
    idx = np.clip(idx, 1, len(A)-1)
    left = A[idx-1]
    right = A[idx]
    idx -= target - left < right - target
    return idx

closest_index=find_closest(ES_raw[:,0],Wv)
an_closest_index=ES_raw[:,0].searchsorted(Wv)


compare_array=np.zeros((198,5))
compare_array[:,0]=Wv
compare_array[:,1]=ES_raw[closest_index,0]
compare_array[:,2]=ES_raw[an_closest_index,0]
compare_array[:,3]=ES_raw[closest_index,1]
compare_array[:,4]=ES_raw[an_closest_index,1]


ES=ES_raw[closest_index,1]
