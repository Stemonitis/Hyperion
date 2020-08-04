# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:18:02 2020

@author: mysh
"""

'''Due to low signal for some channels, and to reduce the VNIR-SWIR
overlap region, some of these spectral channels are not calibrated. The uncalibrated channels are
set to zero. The channels are not removed from the file so the final data set is the same size as the
initial data set. '''
#%%Reading libraries and modules

import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD,SDC #utility to read hdf files, tutorial: https://www.hdfeos.org/software/pyhdf.php
from matplotlib.mlab import PCA #for PCA
#%%

def remove_non_calibrated(spectra3D):
    #now n is an array that has indices with all of the channels set to zero
    #Calibrated channels are 8-57 for the VNIR, and 77-224 for the SWIR
    concatenated = (*range(0,9), *range(59, 78), *range(226, 243))
    calibrated=np.delete(spectra3D, concatenated, axis=1)
    return calibrated
    
def remove_zero(spectra3D):
    #now n is an array that has indices with all of the channels set to zero
    l=spectra3D[15,:,:]
    non_calibrated=[]
    for i in range(0,len(l[:,0])):
       if not l[i,:].any():
           non_calibrated.append(i)
    return np.delete(spectra3D, (non_calibrated), axis=1)
    

    
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
   
          
def remove_dead_and_zer0_pixels(spectra2D):
    n=[]
    for i in range(0,np.shape(spectra2D)[0]):
        for j in range(0,np.shape(spectra2D)[1]):
            if spectra2D[i,j]<0 or spectra2D[i,j]==0:
              n.append(i)
    n=set(n)
    m=np.array(list(n))
    return np.delete(spectra2D,(m),axis=0)
    
def calculate_actualwavelength_vector(clean2Ddata):
    v=clean2Ddata[200,:]
    bandwidth=(2406.-436)/(len(v)-1) #has to be precisely 10
    nm=[]
    for i in range(0, len(v)):
        k=436+(i*bandwidth)
        nm.append(k)
    return nm