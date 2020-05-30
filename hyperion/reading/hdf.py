# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:06:00 2020

@author: mysh
"""

#%%Reading libraries and modules

import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD,SDC #utility to read hdf files, tutorial: https://www.hdfeos.org/software/pyhdf.php
from matplotlib.mlab import PCA #for PCA
#%%


""""Functions for reading, loading and preprocessing multispectral data from EO1 Hyperion and metadata as well"""

""""Functions for reading, loading and preprocessing multispectral data from EO1 Hyperion and metadata as well"""


'''Loading the spectral data'''
def load_data_eo1hyperion(path):
    return SD(path,SDC.READ) #reads hdf file, attention: other hdf readers give an error: signature not found
'''Converting hdf to numpy array'''   
def hdf_to_numpy(hdf):
    #spectra.datasets() #Lists available SDS datasets (datasets in the hdf, here only one dataset)
    # example output {'EO1H0050092001160111PP.L1R': (('fakeDim0', 'fakeDim1', 'fakeDim2'), (5809, 242, 256), 22, 0)}
    DATAFIELD_NAME=list(hdf.datasets().keys())
    return hdf.select(DATAFIELD_NAME[0])[:,:,:]
    
def show_hdf_dimension(hdf):
    return hdf.dimensions()
    #dir(data3D) shows all functions available for the <pyhdf.SD.SDS object at 0x7f4a27181b90>
    #imshow(data3D.get()) display images from hdf file
def show_hdf_attributes(hdf):
    #Example output
    '''{'Data units': 'w/m^2/sr/micron',
    'Number of Along Track Pixels': 6702,
    'Number of Bands': 242,
    'Number of Cross Track Pixels': 256,
    'SWIR Scaling Factor': 'w/m^2/sr/micron * 80',
    'VNIR Scaling Factor': 'w/m^2/sr/micron * 40'}
    '''
    return hdf.attributes()
    
def show_available_functions(hdf):
       return dir(hdf)
