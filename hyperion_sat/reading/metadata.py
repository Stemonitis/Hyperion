# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:16:18 2020

@author: mysh
"""
#%%Reading libraries and modules
import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD,SDC #utility to read hdf files, tutorial: https://www.hdfeos.org/software/pyhdf.php

def read_metadata(path_AUX):
    '''Read metadata'''
    #metadata is another hdf file in the same folder with extension .AUX
    #for example: path='/home/mysh/colours/priorstats/hyper/EO1H0200392001336112K0/EO1H0200392001336112K0.AUX'
    #Metasata contains mask file 
    return SD(path_AUX,SDC.READ)
    
def show_metadata_datasets(meta):
    #example output
    #{'Spectral Bandwidths': (('fakeDim2', 'fakeDim3'), (242, 256), 5, 1), 
    #'Flag Mask': (('fakeDim6', 'fakeDim7', 'fakeDim8'), (5809, 242, 256), 21, 3), 
    #'Gain Coefficients': (('fakeDim4', 'fakeDim5'), (242, 256), 5, 2), 
    #'Spectral Center Wavelengths': (('fakeDim0', 'fakeDim1'), (242, 256), 5, 0)}
    return meta.datasets()
'''Reading spectral center wavelength datafile'''

def read_spectral_center(meta):
    DATAFIELD_NAME='Spectral Center Wavelengths'
    spbandshdf=meta.select(DATAFIELD_NAME)
    #spbandshdf.dimensions()
    '''Save bandwidth as a numpy array'''
    return np.array(spbandshdf[:,:])
    #spbands.shape
    #(242, 256)
    #matshow(spbands.T, cmap='spectral')
    #plt.colorbar()   
    
def read_and_plot_spectral_center(meta):
    DATAFIELD_NAME='Spectral Center Wavelengths'
    spcenterhdf=meta.select(DATAFIELD_NAME)
    spcenter=np.array(spcenterhdf[:,:])
    #spbandshdf.dimensions()
    plt.matshow(spcenter.T, cmap='rainbow')
    plt.colorbar()
    '''Save bandwidth as a numpy array'''
    return spcenter
    #spbands.shape
    #(242, 256)
    
'''Reading spectral bandwidth datafile'''
def read_spectral_bandwidth(meta):
    DATAFIELD_NAME='Spectral Bandwidths'
    spbandshdf=meta.select(DATAFIELD_NAME)
    #spbandshdf.dimensions()
    '''Save bandwidth as a numpy array'''
    return np.array(spbandshdf[:,:])
    #spbands.shape
    #(242, 256)
    #matshow(spbands.T, cmap='spectral')
    #plt.colorbar()   
    
def read_and_plot_spectral_bandwidth(meta):
    DATAFIELD_NAME='Spectral Bandwidths'
    spbandshdf=meta.select(DATAFIELD_NAME)
    spbands=np.array(spbandshdf[:,:])
    #spbandshdf.dimensions()
    plt.matshow(spbands.T, cmap='rainbow')
    plt.colorbar()
    return spbands
    #spbands.shape
    #(242, 256)

'''Reading mask datafile'''
def read_mask(meta):
    DATAFIELD_NAME1='Flag Mask'
    maskhdf=meta.select(DATAFIELD_NAME1)
    #maskhdf.dimensions()
    #functions available :dir()
    return np.array(maskhdf[:,:,:])

'''Reading gain data file'''

'Gain Coefficients'
def read_gain(meta):
    DATAFIELD_NAME2='Gain Coefficients'
    gainhdf=meta.select(DATAFIELD_NAME2)
    gainhdf.dimensions()
    return np.array(gainhdf[:,:])

def read_and_plot_gain(meta):
    DATAFIELD_NAME2='Gain Coefficients'
    gainhdf=meta.select(DATAFIELD_NAME2)
    gain=np.array(gainhdf[:,:])
    plt.matshow(gain.T, cmap='rainbow')
    plt.colorbar()
    return gain

def get_doy(meta):
    doy=meta.ImageStartTime[4:7]
    return int(doy)

def get_hour(meta):
    hour=float(meta.ImageStartTime[7:9])
    minute=float(meta.ImageStartTime[9:11])*5/3/100
    return hour+minute

def get_local_latitude(path_MET):
    latitude_str=open(path_MET, "r").readlines()[1]
    print(latitude_str.strip("Site Latitude").strip("\n").strip())
    return float(latitude_str.strip("Site Latitude").strip("\n").strip())

def get_local_longitude(path_MET):
    longitude_str=open(path_MET, "r").readlines()[2]
    return float(longitude_str.strip("Site Longitude").strip("\n").strip())

    
'''Due to low signal for some channels, and to reduce the VNIR-SWIR
overlap region, some of these spectral channels are not calibrated. The uncalibrated channels are
set to zero. The channels are not removed from the file so the final data set is the same size as the
initial data set. '''