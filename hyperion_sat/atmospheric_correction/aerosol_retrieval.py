#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:49:00 2020

@author: stemonitis
"""

"""Aerosol retrieval"""


import numpy as np
import scipy as sc
from skimage.transform import resize
from sklearn.linear_model import LinearRegression


"""Choose from the 4 aerosol types rural, urban, maritime, desert"""



def calculate_red_TOA(d,sza,L):
    """closest to 660nm"""
    rho_red_TOA=np.pi*(d**2)*L[:,23,:]/(1.58*np.cos(sza))
    return rho_red_TOA
def calculate_blue_TOA(d,sza,L):
    """closest to 420 nm"""
    rho_blue_TOA=np.pi*(d**2)*L[:,0,:]/(1.57*np.cos(sza))
    return rho_blue_TOA
def calculate_NIR_TOA(d,sza,L):
    """closest to 850 nm"""
    rho_NIR_TOA=np.pi*(d**2)*L[:,42,:]/(0.743*np.cos(sza))
    return rho_NIR_TOA
def calculate_SW1_TOA(d,sza,L):
    """closest to 1600 nm"""
    rho_SW1_TOA=np.pi*(d**2)*L[:,123,:]/(0.253*np.cos(sza))
    return rho_SW1_TOA
def calculate_SWIR2_TOA(d,sza,L):
    """closest to 2200 nm"""
    rho_SWIR2_TOA=np.pi*(d**2)*L[:,178,:]/(0.0825*np.cos(sza))
    return rho_SWIR2_TOA


def search_ddv(cloud_mask, rho_SW1_TOA):
    """at least 500 meters away from the clouds, which is 500/30=17 pixels"""
    cloud_unaffected_mask=
    return ddv