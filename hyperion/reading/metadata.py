# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:16:18 2020

@author: mysh
"""
#%%Reading libraries and modules

import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD,SDC #utility to read hdf files, tutorial: https://www.hdfeos.org/software/pyhdf.php
from matplotlib.mlab import PCA #for PCA
#%%
def read_metadata(path):
    '''Read metadata'''
    #metadata is another hdf file in the same folder with extension .AUX
    #for example: path='/home/mysh/colours/priorstats/hyper/EO1H0200392001336112K0/EO1H0200392001336112K0.AUX'
    #Metasata contains mask file 
    return SD(path,SDC.READ)
    
def show_metadata_datasets(meta):
    #example output
    #{'Spectral Bandwidths': (('fakeDim2', 'fakeDim3'), (242, 256), 5, 1), 
    #'Flag Mask': (('fakeDim6', 'fakeDim7', 'fakeDim8'), (5809, 242, 256), 21, 3), 
    #'Gain Coefficients': (('fakeDim4', 'fakeDim5'), (242, 256), 5, 2), 
    #'Spectral Center Wavelengths': (('fakeDim0', 'fakeDim1'), (242, 256), 5, 0)}
    return meta.datasets()
    
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
    return np.array(gainhdf[:,:,:])

'''Due to low signal for some channels, and to reduce the VNIR-SWIR
overlap region, some of these spectral channels are not calibrated. The uncalibrated channels are
set to zero. The channels are not removed from the file so the final data set is the same size as the
initial data set. '''
