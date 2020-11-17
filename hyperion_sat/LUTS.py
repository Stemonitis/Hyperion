#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:03:37 2020

@author: stemonitis
"""

"""Transmittance calculations"""

"""Sensor elevation for Hyperion is 705.0 kilometers.
 """




"""
Total Radiance = atmosphere rad. or boundary rad. + atm. scat. or boundary refl.
Lowtran outputs W cm^-2 ster^-1 micron^-1
we want photons cm^-2 s^-1 ster^-1 micron^-1
1 W cm^-2 = 10000 W m^-2
h = 6.62607004e-34 m^2 kg s^-1
I: irradiance
Np: numer of photons
Np = (Ilowtran*10000)*lambda_m/(h*c)
"""
import sys
sys.path.append("/home/stemonitis/lowtran/src/lowtran/")
from pathlib import Path
from matplotlib.pyplot import show
try:
    import seaborn as sns
    sns.set_context('talk')
except ImportError:
    pass
from argparse import ArgumentParser
import lowtran 
from lowtran.plots import plotscatter

def main():
    p = ArgumentParser(description='Lowtran 7 interface')
    p.add_argument('-z', '--obsalt', help='altitude of observer [km]', type=float, default=0.)
    p.add_argument('-a', '--zenang', help='Observer zenith angle [deg] ', nargs='+', type=float, default=[0., 60, 80])
    p.add_argument('-s', '--short', help='shortest wavelength nm ', type=float, default=400)
    p.add_argument('-l', '--long', help='longest wavelength nm ', type=float, default=700)
    p.add_argument('-step', help='wavelength step size cm^-1', type=float, default=20)
    p.add_argument('-o', '--outfn', help='NetCDF4 file to write')
    p.add_argument('--model', help='0-6, see Card1 "model" reference. 5=subarctic winter', type=int, default=5)

    P = p.parse_args()

    c1 = {'model': P.model,
          'h1': P.obsalt,  # of observer
          'angle': P.zenang,  # of observer
          'wlshort': P.short,
          'wllong': P.long,
          'wlstep': P.step,
          }
    TR = lowtran.scatter(c1)
    if P.outfn:
        outfn = Path(P.outfn).expanduser()
        print('writing', outfn)
        TR.to_netcdf(outfn)
        
    plotscatter(TR, c1)
    show()



#%%

p = ArgumentParser(description='Lowtran 7 interface')
p.add_argument('-z', '--obsalt', help='altitude of observer [km]', type=float, default=70.)
p.add_argument('-a', '--zenang', help='Observer zenith angle [deg] ', nargs='+', type=float, default=[0., 30, 80])
p.add_argument('-s', '--short', help='shortest wavelength nm ', type=float, default=400)
p.add_argument('-l', '--long', help='longest wavelength nm ', type=float, default=700)
p.add_argument('-step', help='wavelength step size cm^-1', type=float, default=10)
p.add_argument('-o', '--outfn', help='NetCDF4 file to write')
p.add_argument('--model', help='0-6, see Card1 "model" reference. 5=subarctic winter', type=int, default=3)

P = p.parse_args()

c1 = {'model': P.model,
      'h1': P.obsalt,  # of observer
      'angle': P.zenang,  # of observer
      'wlshort': P.short,
      'wllong': P.long,
      'wlstep': P.step,
      }

TR = lowtran.scatter(c1)
if P.outfn:
    outfn = Path(P.outfn).expanduser()
    print('writing', outfn)
    TR.to_netcdf(outfn)
    
plotscatter(TR, c1)
show()




























#%%

"""
For Irradiance, the zenith angle is locked to the zenith angle of the sun.
Implicitly, your sensor is looking at the sun and that's the only choice per
Lowtran manual p. 36 s3.2.3.1
"""
from matplotlib.pyplot import show
from argparse import ArgumentParser
import lowtran
from lowtran.plots import plotirrad


def main():
    p = ArgumentParser(description='Lowtran 7 interface')
    p.add_argument('-z', '--obsalt', help='altitude of observer [km]', type=float, default=705.)
    p.add_argument('-a', '--zenang', help='zenith angle [deg]  of sun or moon', nargs='+', type=float, default=[0, 60, 80])
    p.add_argument('-s', '--short', help='shortest wavelength nm ', type=float, default=200)
    p.add_argument('-l', '--long', help='longest wavelength nm ', type=float, default=30000)
    p.add_argument('-step', help='wavelength step size cm^-1', type=float, default=20)
    p.add_argument('--model', help='0-6, see Card1 "model" reference. 5=subarctic winter', type=int, default=5)
    P = p.parse_args()

    c1 = {'model': P.model,
          'h1': P.obsalt,
          'angle': P.zenang,  # zenith angle of sun or moon
          'wlshort': P.short,
          'wllong': P.long,
          'wlstep': P.step,
          }

    irr = lowtran.irradiance(c1)

    plotirrad(irr, c1, True)

    show()



"""
Total Radiance = atmosphere rad. or boundary rad. + atm. scat. or boundary refl.
Lowtran outputs W cm^-2 ster^-1 micron^-1
we want photons cm^-2 s^-1 ster^-1 micron^-1
1 W cm^-2 = 10000 W m^-2
h = 6.62607004e-34 m^2 kg s^-1
I: irradiance
Np: numer of photons
Np = (Ilowtran*10000)*lambda_m/(h*c)
"""
from pathlib import Path
from matplotlib.pyplot import show
from argparse import ArgumentParser
import lowtran
from lowtran.plots import plotradiance


def main():
    p = ArgumentParser(description='Lowtran 7 interface')
    p.add_argument('-z', '--obsalt', help='altitude of observer [km]', type=float, default=705.)
    p.add_argument('-a', '--zenang', help='Observer zenith angle [deg] ', nargs='+', type=float, default=[0., 60, 80])
    p.add_argument('-s', '--short', help='shortest wavelength nm ', type=float, default=200)
    p.add_argument('-l', '--long', help='longest wavelength nm ', type=float, default=30000)
    p.add_argument('-step', help='wavelength step size cm^-1', type=float, default=20)
    p.add_argument('-o', '--outfn', help='HDF5 file to write')
    p.add_argument('--model', help='0-6, see Card1 "model" reference. 5=subarctic winter', type=int, default=5)

    P = p.parse_args()

    c1 = {'model': P.model,
          'h1': P.obsalt,  # of observer
          'angle': P.zenang,  # of observer
          'wlshort': P.short,
          'wllong': P.long,
          'wlstep': P.step,
          }

    TR = lowtran.radiance(c1)
# %%
    if P.outfn:
        outfn = Path(P.outfn).expanduser()
        print('writing', outfn)
        TR.to_netcdf(outfn)

    plotradiance(TR, c1, True)
    
    
#%%













