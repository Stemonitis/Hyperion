#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:13:01 2020

@author: stemonitis
"""
#%%
import sys
sys.path.append("/home/stemonitis/colours/scripts/Hyperion/")
import hyperion_sat as hyp
import matplotlib.pyplot as plt

"""Processing example"""
path_AUX="/home/stemonitis/colours/satellites/hyperion_madagascar/with water/EO1H1600712016232110PB/EO1H1600712016232110PB.AUX"
metadata=hyp.read_metadata(path_AUX)
spectral_center=hyp.read_spectral_center(metadata)
flag_mask=hyp.read_mask(metadata)
doy=hyp.get_doy(metadata)

path_L1R="/home/stemonitis/colours/satellites/hyperion_madagascar/with water/EO1H1600712016232110PB/EO1H1600712016232110PB.L1R"
L=hyp.trim_the_bottom_edge(hyp.apply_gains(hyp.remove_non_calibrated_channels((hyp.apply_flag_mask(hyp.hdf_to_numpy(hyp.load_data_eo1hyperion(path_L1R)),flag_mask)))))
#L=hyp.destripe(L)
Wv=hyp.get_average_wv_for_each_calibrated_channel(spectral_center)
path_MET="/home/stemonitis/colours/satellites/hyperion_madagascar/with water/EO1H1600712016232110PB/EO1H1600712016232110PB.MET"
local_latitude=hyp.get_local_latitude(path_MET)
local_longitude=hyp.get_local_longitude(path_MET)
doy=hyp.get_doy(metadata)
hour=hyp.get_hour(metadata)
d=hyp.calculate_sun_earth_distance(doy)
sza=hyp.calculate_cos_of_solar_zenith_angle(local_latitude,doy,hour)

red_TOA=hyp.calculate_red_TOA(d,sza,L)
green_TOA=hyp.calculate_green_TOA(d,sza,L)
blue_TOA=hyp.calculate_blue_TOA(d,sza,L)
NIR_TOA=hyp.calculate_NIR_TOA(d,sza,L)
SWIR1_TOA=hyp.calculate_SWIR1_TOA(d,sza,L)
SWIR2_TOA=hyp.calculate_SWIR2_TOA(d,sza,L)
SW1_TOA=hyp.calculate_SW1_TOA(d,sza,L)
cirrus_TOA=hyp.calculate_cirrus_TOA(d,sza,L)
rho_1240_TOA=hyp.calculate_1240_TOA(d,sza,L)
NDVI_TOA=hyp.calculate_NDVI_TOA(red_TOA,NIR_TOA)
NDSI_TOA=hyp.calculate_NDVI_TOA(green_TOA,SWIR1_TOA)
blue_haze_TOA=hyp.calculate_blue_haze_TOA(d,sza,L)
#%%
water_mask=hyp.water_mask(red_TOA,NIR_TOA,SW1_TOA,NDVI_TOA)
L_decirred=hyp.perform_decirrus(L,red_TOA,cirrus_TOA,NIR_TOA,rho_1240_TOA,water_mask)
bright_pixels_without_cirrus=hyp.bright_pixels_without_cirrus(red_TOA,blue_haze_TOA,NIR_TOA,cirrus_TOA)
band_specific_HTM,k=hyp.calculate_band_specific_HTM(L)
L_dehazed=hyp.perform_dehazing(L_decirred,band_specific_HTM)
L_dehazed_decirred=hyp.reconciliate_dehazing_decirrus(L_dehazed,L_decirred)

#%%









import numpy as np







water_cloud_mask=hyp.water_cloud_mask(red_TOA,green_TOA,blue_TOA,NIR_TOA,NDVI_TOA,NDSI_TOA)
thin_cirrus_water=hyp.thin_cirrus_water(cirrus_TOA,water_mask)
medium_cirrus_water=hyp.medium_cirrus_water(cirrus_TOA,water_mask)
thick_cirrus_water=hyp.thick_cirrus_water(cirrus_TOA,water_mask)
thin_cirrus_land=hyp.thin_cirrus_land(cirrus_TOA,water_mask)
medium_cirrus_land=hyp.medium_cirrus_land(cirrus_TOA,water_mask)
thick_cirrus_land=hyp.thick_cirrus_land(cirrus_TOA,water_mask)
cirrus_cloud=hyp.cirrus_cloud(cirrus_TOA)
thick_cirrus_cloud=hyp.thick_cirrus_cloud(cirrus_TOA)
medium_cirrus=hyp.medium_cirrus(cirrus_TOA)

bright_pixels_without_cirrus=hyp.bright_pixels_without_cirrus(red_TOA,blue_haze_TOA,NIR_TOA, cirrus_TOA)




#%%























































