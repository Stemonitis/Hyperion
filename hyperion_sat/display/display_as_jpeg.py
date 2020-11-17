# -*- coding: utf-8 -*-
"""

@author: mysh
"""
#%%Reading libraries and modules

import matplotlib.pyplot as plt
import numpy as np

"""Functions for displaying multispectral data as rgb pictures"""

'''Greyscale image'''
'''A simple and reliable way to get a quick feel for the contents of the image is to display a gray scale
image of Band 40. This band in the VNIR is at about 753 nm. '''

def plot_greyscale(spectra3D):
    #dont use the whole image to display, instead use e.g. data3D[:500,50,:]
    #show data images
    plt.matshow(spectra3D,cmap='viridis')
    plt.colorbar()
    #plt.hist(data3D[:,30,:]
    #imshow(data2D)
    
#plot_greyscale(spectra3D[:500, 50, :])
    
#default arra is set to the rgb
def plot_color_image(spectra3D,band_array=[21,15,8]):
    rgbArray = np.zeros((np.shape(spectra3D)[0],np.shape(spectra3D)[2], 3))
    r=spectra3D[:,band_array[0],:]
    g=spectra3D[:,band_array[1],:]
    b=spectra3D[:,band_array[2],:]

    r=r.astype(float)/(r.max()-r.min())
    g=g.astype(float)/(g.max()-g.min())
    b=b.astype(float)/(b.max()-b.min())
    print(np.shape(r))
    rgbArray[..., 0] = r
    rgbArray[..., 1] = g
    rgbArray[..., 2] = b

    plt.imshow(rgbArray)
    plt.colorbar()
    
'''Color images'''
'''VNIR: visible RGB '''
'''To obtain a color image of the scene that represents true RGB the bands 29:23:16 for R:G:B are
typically used. This band combination corresponds to approximate wavelengths of 641 nm, 580
nm and 509 nm. Slight variations in the bands selected will not noticeably affect the RGB image. '''
#rgb=[29, 23,16]
#plot_color_image(spectra3D[:500, :, :])

'''VNIR Vegetation RGB '''
#vnir=[50,23,16]
#plot_color_image(spectra3D[:500, :, :], vnir)

'''SWIR RGB'''
'''To obtain a color image of the SWIR, bands 204:150:93 for R:G:B is a usable combination. The
corresponding wavelengths are 2194 nm, 1649 nm and 1074 nm. These bands are outside of the
region of the spectrum that is most significantly affected by atmospheric absorption. '''
'''When using the SWIR data it is important to know if the SWIR was at the proper
operational temperature. The proper operational temperature is when the SWIR FPE temperature is
–153.5 ± 1C. An HDF file delivered with the Hyperion data contains this parameter. This is
discussed further in chapter 3. The absolute calibration for the SWIR is only applicable at the
operational temperature. The SWIR has negligible response when fully warm. If the SWIR
image does not contain features consistent with the VNIR image then the SWIR was quite possibly
not at the operational temperature. However, it may not be clearly evident from the image if the 
SWIR is slightly off operational temperature. A table on the EO-1 web site also contains the on
and off times of the cryocooler. This may be used as a quick look tool. '''
#swir_rgb=[204, 150, 93]
#plot_color_image(spectra3D[:500, :, :], swir_rgb)

    