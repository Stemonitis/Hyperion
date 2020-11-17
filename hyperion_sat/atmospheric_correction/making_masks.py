#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:35:07 2020

@author: stemonitis
"""

"""

Atmospheric correction

"""
import numpy as np
import scipy as sc
from skimage.transform import resize
from sklearn.linear_model import LinearRegression


"""Obtain necessary coeficients"""

"""Extraterrestial solar irradiance for our data"""
ES=[1.57  , 2.07  , 1.66  , 2.05  , 2.1   , 2.16  , 2.11  , 2.11  ,
       1.62  , 1.51  , 1.72  , 1.99  , 1.64  , 1.78  , 1.91  , 1.86  ,
       1.8   , 1.79  , 1.73  , 1.76  , 1.45  , 1.67  , 1.64  , 1.58  ,
       1.54  , 1.35  , 1.42  , 1.42  , 1.37  , 1.37  , 1.1   , 1.31  ,
       1.27  , 1.25  , 1.2   , 1.21  , 1.15  , 1.14  , 1.11  , 1.08  ,
       1.03  , 1.01  , 0.743 , 0.991 , 0.939 , 0.942 , 0.885 , 0.909 ,
       0.876 , 0.854 , 0.896 , 0.851 , 0.842 , 0.828 , 0.807 , 0.774 ,
       0.768 , 0.759 , 0.747 , 0.723 , 0.718 , 0.703 , 0.677 , 0.671 ,
       0.648 , 0.645 , 0.634 , 0.613 , 0.521 , 0.582 , 0.581 , 0.565 ,
       0.553 , 0.532 , 0.535 , 0.522 , 0.51  , 0.506 , 0.491 , 0.488 ,
       0.48  , 0.469 , 0.46  , 0.454 , 0.444 , 0.434 , 0.43  , 0.417 ,
       0.416 , 0.407 , 0.399 , 0.392 , 0.388 , 0.378 , 0.371 , 0.366 ,
       0.355 , 0.354 , 0.35  , 0.342 , 0.338 , 0.325 , 0.327 , 0.317 ,
       0.311 , 0.309 , 0.299 , 0.292 , 0.294 , 0.289 , 0.288 , 0.284 ,
       0.274 , 0.266 , 0.266 , 0.257 , 0.255 , 0.242 , 0.253 , 0.247 ,
       0.242 , 0.242 , 0.22  , 0.225 , 0.224 , 0.219 , 0.21  , 0.207 ,
       0.207 , 0.202 , 0.199 , 0.195 , 0.187 , 0.185 , 0.184 , 0.179 ,
       0.175 , 0.173 , 0.169 , 0.166 , 0.159 , 0.16  , 0.156 , 0.155 ,
       0.148 , 0.146 , 0.144 , 0.139 , 0.14  , 0.135 , 0.135 , 0.129 ,
       0.128 , 0.122 , 0.124 , 0.122 , 0.12  , 0.118 , 0.116 , 0.115 ,
       0.111 , 0.11  , 0.108 , 0.105 , 0.103 , 0.102 , 0.0997, 0.0969,
       0.0971, 0.0958, 0.0934, 0.0927, 0.091 , 0.0891, 0.0858, 0.086 ,
       0.0841, 0.0837, 0.0825, 0.081 , 0.0796, 0.0785, 0.0769, 0.0748,
       0.0741, 0.0731, 0.0717, 0.0692, 0.0695, 0.0682, 0.0657, 0.0655,
       0.0651, 0.063 , 0.063 , 0.0609, 0.0588, 0.0599]

def calculate_sun_earth_distance(doy):
    #The eccentricity of the Earth's orbit is currently about 0.0167 (wiki)
    """The orbital eccentricity of an astronomical object is a dimensionless parameter that determines the amount by which its orbit 
    around another body deviates from a perfect circle. """
    ec=0.0167
    d=1+ec*np.sin(2*np.pi*(doy-93.5)/365)
    return d

def calculate_cos_of_solar_zenith_angle(local_latitude, doy,hour):
    """formula according to wiki https://en.wikipedia.org/wiki/Position_of_the_Sun#Declination_of_the_Sun_as_seen_from_Earth"""
    current_declination_of_the_sun=-np.arcsin(0.39779*np.cos(0.98565*(doy+10)+1.914*np.sin(0.98565*(doy-2))))
    """The  second  angle  used  to  locate  the  sun  is  the  solar-hour  angle.  Its value  isbased  on  the  nominal  360◦rotation  of  
    Earth  occurring  in  24  hours.  Therefore,1 hour is equivalent to an angle of 15◦. The hour angle is measured from zero atsolar noon. 
    It is denoted by hsand is positive before solar noon and negative afternoon in accordance with the right-hand rule. For example 
    2:00pmcorrespondstohs=−30◦and 7:00amcorresponds tohs= +75◦. source: doi:10.1002/9780470209738"""
    hour_angle=15*(12-hour)
    return np.cos(local_latitude)*np.sin(current_declination_of_the_sun)+np.cos(local_latitude)*np.cos(current_declination_of_the_sun)*np.cos(hour_angle)
"""Calculate necessary TOA bands"""
def calculate_red_TOA(d,sza,L):
    """closest to 660nm"""
    rho_red_TOA=np.pi*(d**2)*L[:,23,:]/(1.58*np.cos(sza))
    return rho_red_TOA

def calculate_green_TOA(d,sza,L):
    """closest to 550nm"""
    rho_green_TOA=np.pi*(d**2)*L[:,12,:]/(1.64*np.cos(sza))
    return rho_green_TOA

def calculate_NIR_TOA(d,sza,L):
    """closest to 850 nm"""
    rho_NIR_TOA=np.pi*(d**2)*L[:,42,:]/(0.743*np.cos(sza))
    return rho_NIR_TOA

def calculate_SWIR1_TOA(d,sza,L):
    """closest to 1650 nm"""
    rho_SWIR1_TOA=np.pi*(d**2)*L[:,118,:]/(0.225*np.cos(sza))
    return rho_SWIR1_TOA
def calculate_SW1_TOA(d,sza,L):
    """closest to 1600 nm"""
    rho_SW1_TOA=np.pi*(d**2)*L[:,123,:]/(0.253*np.cos(sza))
    return rho_SW1_TOA
def calculate_SWIR2_TOA(d,sza,L):
    """closest to 2200 nm"""
    rho_SWIR2_TOA=np.pi*(d**2)*L[:,178,:]/(0.0825*np.cos(sza))
    return rho_SWIR2_TOA

def calculate_blue_TOA(d,sza,L):
    """closest to 420 nm"""
    rho_blue_TOA=np.pi*(d**2)*L[:,0,:]/(1.57*np.cos(sza))
    return rho_blue_TOA

def calculate_blue_haze_TOA(d,sza,L):
    """closest to 480 nm"""
    rho_blue_TOA=np.pi*(d**2)*L[:,5,:]/(2.16*np.cos(sza))
    return rho_blue_TOA

def calculate_cirrus_TOA(d,sza,L):
    """closest to 1380nm"""
    rho_cirrus_TOA=np.pi*(d**2)*L[:,96,:]/(0.355*np.cos(sza))
    return rho_cirrus_TOA

def calculate_1240_TOA(d,sza,L):
    rho_1240_TOA=np.pi*(d**2)*L[:,83,:]/(0.454*np.cos(sza))
    return rho_1240_TOA

def calculate_NDVI_TOA(rho_red_TOA, rho_NIR_TOA):
    """normalized vegetation index"""
    rho_NDVI_TOA=(rho_NIR_TOA-rho_red_TOA)/(rho_NIR_TOA+rho_red_TOA)
    return rho_NDVI_TOA

def calculate_NDSI_TOA(rho_green_TOA, rho_SWIR1_TOA):
    """Normalized-Difference Snow Index"""
    rho_NDSI_TOA=(rho_green_TOA-rho_SWIR1_TOA)/(rho_green_TOA+rho_SWIR1_TOA)
    return rho_NDSI_TOA


"""Perform decirrus"""

def perform_decirrus(L,rho_red_TOA,rho_cirrus_TOA, rho_NIR_TOA,rho_1240_TOA,water_mask):
    vegetation_pixel_mask=calculate_vegetation(rho_red_TOA, rho_NIR_TOA)
    gamma_land=LinearRegression().fit(rho_cirrus_TOA[vegetation_pixel_mask].reshape((-1,1)),rho_red_TOA[vegetation_pixel_mask]).coef_
    if water_mask.sum()!=0:
          gamma_water=LinearRegression().fit(rho_cirrus_TOA[water_mask].reshape((-1,1)),rho_1240_TOA[water_mask]).coef_
          L_decirred_water=L-(np.repeat(rho_cirrus_TOA[:,np.newaxis,:],repeats=198,axis=1)/gamma_water)
          L_decirred_land=L-(np.repeat(rho_cirrus_TOA[:,np.newaxis,:],repeats=198,axis=1)/gamma_land)
          L_decirred=np.where(water_mask,L_decirred_water,L_decirred_land)
    else:
        L_decirred=L-(np.repeat(rho_cirrus_TOA[:,np.newaxis,:],repeats=198,axis=1)/gamma_land)
    return L_decirred
    
"""Perform dehazing"""

def bright_pixels_without_cirrus(rho_red_TOA,rho_blue_haze_TOA,rho_NIR_TOA, rho_cirrus_TOA):
    T_red=rho_red_TOA+2*np.std(rho_red_TOA)
    T_blue=rho_blue_haze_TOA+2*np.std(rho_blue_haze_TOA)
    bright_pixels=((rho_NIR_TOA>=0.1) & (rho_blue_haze_TOA>=T_blue) & (rho_red_TOA>=T_red))
    return (bright_pixels & (rho_cirrus_TOA<0.015))

def calculate_HTM(L_band,w):
    """HTM=haze thickness mask"""
    minimum_array=np.zeros(((int(L_band.shape[0]/w),int(L_band.shape[1]/w))))
    for i in range(int(L_band.shape[0]/w)):
        for j in range(int(L_band.shape[1]/w)):
            minimum_array[i,j]=np.min(L_band[i*w,j*w])
    minimum_array_median=sc.ndimage.median_filter(minimum_array,3)
    cubic_interpolated=resize(minimum_array_median,(L_band.shape[0], L_band.shape[1]),order=3)
    return cubic_interpolated

def calculate_band_specific_HTM(L):
    index_11_bands=[2,5,13,23,31,42,59,68,122,178,197]
    HTM_extrapolated_blue=calculate_HTM((L[:,0,:]+(L[:,0,:]-0.95*L[:,5,:])),3)
    HTM_extrapolated_blue_coarse=calculate_HTM((L[:,0,:]+(L[:,0,:]-0.95*L[:,5,:])),21)
    HTM_haze_coarse_mask=HTM_extrapolated_blue_coarse>np.mean(HTM_extrapolated_blue_coarse)
    k=[]
    band_specific_HTM=np.zeros((L.shape[0],11,L.shape[2]))
    l=0
    for i in index_11_bands:
        band_HTM=calculate_HTM(L[:,i,:],7)
        k.append(LinearRegression().fit(HTM_extrapolated_blue[HTM_haze_coarse_mask].reshape((-1,1)), band_HTM[HTM_haze_coarse_mask]).coef_)
        band_specific_HTM[:,l,:]=k[-1]*band_HTM
        l+=1
    return band_specific_HTM,k

def perform_dehazing(L,band_specific_HTM):
    index_11_bands=[2,5,13,23,31,42,59,68,122,178,197]
    HTM_extrapolated=sc.interpolate.interp1d(index_11_bands, np.array(band_specific_HTM),axis=1, bounds_error=False,fill_value="extrapolate")(np.linspace(0,197,198))
    L_dehazed_preliminary=L-HTM_extrapolated
    L_dehazed=L_dehazed_preliminary+abs(L_dehazed_preliminary-L)
    return L_dehazed

def reconciliate_dehazing_decirrus(L_dehazed,L_decirred):
    L_dehazed_decirred=np.where((L_decirred<(0.9*L_dehazed)),((L_dehazed+L_decirred*3)/4),L_dehazed)
    return L_dehazed_decirred







"""Classify the pixels"""







def water_mask(rho_red_TOA,rho_NIR_TOA,rho_SW1_TOA,rho_NDVI_TOA):
    water_mask=((rho_red_TOA<0.2) & (rho_NIR_TOA>(rho_red_TOA+0.01)) & (rho_SW1_TOA<0.06) & (rho_NDVI_TOA<0.1))
    return water_mask
    
def water_cloud_mask(rho_red_TOA,rho_green_TOA,rho_blue_TOA,rho_NIR_TOA,rho_NDVI_TOA,rho_NDSI_TOA):
    water_cloud_mask=((rho_blue_TOA>0.25) & (rho_red_TOA>0.15) & (rho_NIR_TOA/rho_red_TOA<2) 
                      & (rho_NIR_TOA<1.7*rho_blue_TOA) & (rho_NIR_TOA>0.8*rho_red_TOA) & (rho_red_TOA<1.4*rho_blue_TOA) & (rho_NDSI_TOA<0.7) )
    return water_cloud_mask

def calculate_vegetation(rho_red_TOA, rho_NIR_TOA):
    vegetation=(((rho_NIR_TOA/rho_red_TOA)>2) & (rho_NIR_TOA>0.2))
    return vegetation


def thin_cirrus_water(rho_cirrus_TOA,water_mask):
    return ((0.01<rho_cirrus_TOA)<0.015) & water_mask
def medium_cirrus_water(rho_cirrus_TOA,water_mask):
    return ((0.015<rho_cirrus_TOA)<0.025)  & water_mask
def thick_cirrus_water(rho_cirrus_TOA,water_mask):
    return ((0.025<rho_cirrus_TOA)<0.04)  & water_mask
def thin_cirrus_land(rho_cirrus_TOA,water_mask):
    return ((0.01<rho_cirrus_TOA)<0.015)  & ~water_mask
def medium_cirrus_land(rho_cirrus_TOA,water_mask):
    return ((0.015<rho_cirrus_TOA)<0.025)  & ~water_mask
def thick_cirrus_land(rho_cirrus_TOA,water_mask):
    return ((0.025<rho_cirrus_TOA)<0.04) & ~water_mask
def cirrus_cloud(rho_cirrus_TOA):
    return ((0.04<rho_cirrus_TOA)<0.05)
def thick_cirrus_cloud(rho_cirrus_TOA):
    return (rho_cirrus_TOA<0.05)
def medium_cirrus(rho_cirrus_TOA):
    return (rho_cirrus_TOA>0.015)

def snow_ice_mask(rho_NDSI_TOA, rho_green_TOA, rho_SWIR2_TOA):
    snow_ice_mask=((rho_NDSI_TOA>0.4) & (rho_green_TOA>=0.22) | ((rho_NDSI_TOA>0.25) & (rho_green_TOA>=0.22) & ((rho_SWIR2_TOA/rho_green_TOA)<0.5)))
    return snow_ice_mask

def shadow_mask_pass1(rho_red_TOA, rho_NIR_TOA, cloud_mask,rho_cirrus_TOA):
    red_threshold=np.mean(rho_red_TOA)+0.1*np.std(rho_red_TOA)
    NIR_threshold=np.mean(rho_NIR_TOA)-np.std(rho_NIR_TOA)
    if (np.mean(rho_red_TOA)<=0.15):
        shadow_mask=((rho_red_TOA<red_threshold) & (rho_NIR_TOA<NIR_threshold) & (rho_cirrus_TOA<0.015))
    elif (NIR_threshold<red_threshold):
        NIR_threshold=red_threshold
        shadow_mask=((rho_red_TOA<red_threshold) & (rho_NIR_TOA<NIR_threshold) & (rho_cirrus_TOA<0.015))
    else:
        shadow_mask=(rho_red_TOA==0.00000000000001)
    return shadow_mask


def shadow_mask_pass2(shadow_mask_pass1, rho_red_TOA, rho_NIR_TOA):
    mean_red=np.mean(rho_red_TOA)
    shadow_mask_pass2=shadow_mask_pass1[((mean_red>0.28) & (rho_NIR_TOA<0.1)) | (mean_red<0.28) & (rho_NIR_TOA<0.15)]
    return shadow_mask_pass2

def reconciliate_water_or_shadow(water_mask, shadow_mask, rho_green_TOA, rho_NIR_TOA):
    ND1=(rho_green_TOA-rho_NIR_TOA)/(rho_green_TOA+rho_NIR_TOA)
    water_mask_new=np.where((water_mask==shadow_mask), (ND1>0.2), water_mask)
    shadow_mask_new=np.where((water_mask==shadow_mask), (ND1<=0.2), shadow_mask)
    return water_mask_new, shadow_mask_new
    
def bright_water_mask(water_mask, rho_green_TOA, rho_NIR_TOA, rho_SW1_TOA, rho_red_TOA):
    ND2=(rho_SW1_TOA-rho_red_TOA)/(rho_SW1_TOA+rho_red_TOA)
    bright_water_mask=((rho_green_TOA<0.25) & (rho_NIR_TOA<0.12) & (ND2<-0.2))
    return bright_water_mask



"""    
def calculate_mask(L,start_time):
    #start_time=
    
"""
    
    































    
    
    
    
    
    
    
    