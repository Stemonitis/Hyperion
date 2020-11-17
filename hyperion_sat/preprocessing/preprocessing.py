# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:18:02 2020

@author: mysh
"""

'''Due to low signal for some channels, and to reduce the VNIR-SWIR
overlap region, some of these spectral channels are not calibrated. The uncalibrated channels are
set to zero. The channels are not removed from the file so the final data set is the same size as the
initial data set. '''

import numpy as np
from scipy.signal import convolve2d



def apply_flag_mask(L,flag):
    """we can not just delete the dead pixels from the array, because it will fuck up our images"""
    """so we will just reinstate the wrong pixels with the average of the pixels around"""
    mask=(flag!=0) # the mask boolean mask of the dead pixels
    ones=np.ones((3,3))
    L[mask]=0.1
    L[(L<0)]=0
    L_conv=np.zeros(L.shape)
    for i in range(L.shape[1]):
      L_conv[:,i,:]=convolve2d(L[:,i,:], ones, mode='same')
    """here we have convolved array"""
    L_new=np.where(((L==0.1) | (L==0) | (L<0)),L_conv,L)
    return L_new
   
    
def remove_non_calibrated_channels(L):
    #now n is an array that has indices with all of the channels set to zero
    #Calibrated channels are 8-57 for the VNIR, and 77-224 for the SWIR
    concatenated = (*range(0,7), *range(57, 76), *range(224, 242))
    calibrated=np.delete(L, concatenated, axis=1)
    return calibrated

def apply_gains(L):
    L_scaled=np.zeros(np.shape(L))
    for i in range(np.shape(L)[1]):
        if i>49:
            L_scaled[:,i,:]=L[:,i,:]/40
        else:
            L_scaled[:,i,:]=L[:,i,:]/80
    return L_scaled

def trim_the_bottom_edge(L):
    return L[:-1,:,:]
    
def destripe(L):
    return L_destriped


def get_average_wv_for_each_calibrated_channel(spectral_center):
    average_array=np.zeros((np.shape(spectral_center)[0]))
    for i in range(np.shape(spectral_center)[0]):
        average_array[i]=np.mean(spectral_center[i,:])
    concatenated = (*range(0,7), *range(57, 76), *range(224, 242))
    return np.delete(average_array, concatenated)
    
def flatten_data(spectra3D):
    spectra2D=np.zeros((np.shape(spectra3D)[0]*np.shape(spectra3D)[2],np.shape(spectra3D)[1]))
    l=0
    for i in range(0,np.shape(spectra3D)[0]-2):
        for j in range(0,np.shape(spectra3D)[2]-2):
             spectra2D[l,:]=spectra3D[i,:,j]
             l+=1
    return spectra2D
#water_and_land=flatten_data(spectra3Dclean[:300, :36, :]) #water and land pixels from guadelupe


def back_to_3D(array, or_shape):
    three_d=np.zeros((or_shape[0], or_shape[1],or_shape[2]))
    l=0
    for i in range(0,or_shape[0]):
        for j in range(0,or_shape[2]):
            three_d[i,:,j]=array[l,:]
            l+=1
    return three_d
   
          
