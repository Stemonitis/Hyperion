#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:06:12 2020

@author: stemonitis
"""

"""UVspec"""

"""List of things that we need"""


"""LUTs for the solar spectrum"""


"""Wavelengths"""  """198 in total"""

wv_string="426.8157959 ,  436.99102783,  447.16650391,  457.34173584,
        467.51715088,  477.69229126,  487.86782837,  498.04284668,
        508.21844482,  518.39379883,  528.5690918 ,  538.74420166,
        548.91925049,  559.09442139,  569.26977539,  579.44537354,
        589.62036133,  599.79589844,  609.97125244,  620.1463623 ,
        630.32202148,  640.49743652,  650.67266846,  660.84771729,
        671.02282715,  681.19830322,  691.37365723,  701.54870605,
        711.72381592,  721.89953613,  732.074646  ,  742.24993896,
        752.42510986,  762.6005249 ,  772.77612305,  782.95141602,
        793.12677002,  803.30200195,  813.47717285,  823.65252686,
        833.82781982,  844.00305176,  854.17828369,  864.35333252,
        874.52862549,  884.7043457 ,  894.87939453,  905.05456543,
        915.22998047,  925.40539551,  912.45214844,  922.54089355,
        932.6394043 ,  942.72796631,  952.81652832,  962.9050293 ,
        972.9934082 ,  983.08166504,  993.17034912, 1003.29943848,
       1013.29827881, 1023.39648438, 1033.49536133, 1043.59326172,
       1053.69189453, 1063.79052734, 1073.88879395, 1083.98779297,
       1094.08618164, 1104.18505859, 1114.18383789, 1124.28259277,
       1134.38012695, 1144.47900391, 1154.5769043 , 1164.67602539,
       1174.77490234, 1184.87365723, 1194.97253418, 1205.07080078,
       1215.16894531, 1225.16723633, 1235.26586914, 1245.36425781,
       1255.46313477, 1265.56201172, 1275.66101074, 1285.75952148,
       1295.85742188, 1305.95629883, 1316.05456543, 1326.05273438,
       1336.15161133, 1346.25073242, 1356.34985352, 1366.44750977,
       1376.54553223, 1386.64453125, 1396.7434082 , 1406.84240723,
       1416.94067383, 1426.93884277, 1437.03686523, 1447.13562012,
       1457.234375  , 1467.33325195, 1477.43188477, 1487.53063965,
       1497.62915039, 1507.72692871, 1517.82592773, 1527.92419434,
       1537.92285156, 1548.02148438, 1558.11999512, 1568.21875   ,
       1578.3170166 , 1588.41577148, 1598.51416016, 1608.61315918,
       1618.71191406, 1628.81018066, 1638.80810547, 1648.90673828,
       1659.0057373 , 1669.10449219, 1679.20288086, 1689.30151367,
       1699.39990234, 1709.4987793 , 1719.59729004, 1729.69580078,
       1739.69445801, 1749.79284668, 1759.89111328, 1769.98974609,
       1780.08813477, 1790.18701172, 1800.28613281, 1810.38452148,
       1820.48254395, 1830.58129883, 1840.58007812, 1850.67871094,
       1860.77734375, 1870.87451172, 1880.97363281, 1891.07250977,
       1901.17150879, 1911.27050781, 1921.36804199, 1931.46679688,
       1941.56567383, 1951.56408691, 1961.66296387, 1971.76074219,
       1981.85913086, 1991.95800781, 2002.0567627 , 2012.15551758,
       2022.25390625, 2032.35253906, 2042.4510498 , 2052.44970703,
       2062.54858398, 2072.64648438, 2082.74536133, 2092.84375   ,
       2102.94213867, 2113.04101562, 2123.1394043 , 2133.23828125,
       2143.33666992, 2153.33496094, 2163.43408203, 2173.5324707 ,
       2183.63085938, 2193.72949219, 2203.82788086, 2213.92626953,
       2224.02490234, 2234.1237793 , 2244.22265625, 2254.22143555,
       2264.31958008, 2274.41796875, 2284.51635742, 2294.61499023,
       2304.71386719, 2314.8125    , 2324.91064453, 2335.00927734,
       2345.10766602, 2355.20654297, 2365.20483398, 2375.30322266,
       2385.40234375, 2395.50048828"




""" 4 aerosol types"""

"""rural, maritime, urban, desert"""


"""6 water vapor columns"""


""""at sea level:  0.4, 1.0, 2.0, 2.9, 4.0, 5.0cm"""


"""symbolic satellite height 100km"""

"""visibility"""

""""7,10,15,23,40,80,120"""

"""sza"""

0.4, 1.0, 2.0, 2.9, 4.0, 5.0 cm


"""0,10,20,30,40,50,60,70"""


"""relative azimuth"""

"""0,30,60,90,120,150,180"""


"""sensor earth relative angle"""

"""0,10,20,30,40"""

"""water vapor column"""

"""ground elevation"""

"""0,0.7,1.5,2.5,4"""




"""Output"""


"""
1)Path radiance
2)Diffuse solar flux (at sensor)
3)Direct ground to sensor transmittance
4)Diffuse ground to sensor transmittance
5)Spherical albedo
6)Direct sun to ground transmittance
"""




"""What libradtran outputs"""

"""Per default, uvspec provides direct, diffuse downward and diffuse upward solar irradiance and actinic flux at the surface"""






"""calculate upward or path radiance"""



"""sdist"""




import subprocess
import numpy as np
import os

#specifying the path for the input file we use to generate the fortran data
#specifying the path to execute the fortran script
path="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec"
path1="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/hyperion.inp"
path2="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec.out"
#specifying the path to execute read in generated data
path3="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/verbose.txt"



call([path, "<"+path1+">", path2, path3])





"""obtain path radiance"""

"""albedo=0 as per default"""
"""put inputs as arrays of strings"""
sza=[0.1,10,20,30,40,50,60,70]
aerosol_type=[1,4,5,6]
aerosol_visibility=[7,10,15,23,40,80,120]
water_vapor_column=[4, 10, 20, 29, 40, 50]
relative_azimuth=[0,30,60,90,120,150,180]
#sensor-earth_incidence_angle=[0,10,20,30,40]
#ground_elevation=[0,0.7,1.5,2.5,4]


n=[]

for i in range(len(sza)*len(aerosol_type)*len(aerosol_visibility)*len(water_vapor_column)*len(relative_azimuth)):
    #to write
    l=[]
    l.append("rte_solver sdisort")
    l.append("wavelength 450.0 2400.0")
    l.append("sza "+str(sza[int(i/1176)%8]))
    l.append("aerosol_haze "+str(aerosol_type[(int(i/294)%4)]))
    l.append("aerosol_season 1")
    l.append("aerosol_vulcan 1")
    l.append("aerosol_visibility "+str(aerosol_visibility[int(i/42)%7]))
    l.append("mol_modify H2O "+str(water_vapor_column[int(i/7)%6])+" MM")
    l.append("phi 0") #satellite azimuth is zero because the satellite views stuff right beneath it
    l.append("umu 1") #cosine of the viewing zenith is cos(0), because the satellite is lookign downwards
    l.append("phi0 "+str(relative_azimuth[int(i%7)])) #this is the sun azimuth
    l.append("zout TOA")
    n.append(l)
    
    
import os
import numpy as np
dic_path={}
for i in range(len(n)):
    call(["rm", path1])
    os.chdir("/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin")
    input=open("hyperion.inp", "a")
    [input.write(l+"\n") for l in n[i]]
    input.close()
    call(["./uvspec", "<hyperion.inp>", "uvspec.out"])
    dic_path[i]=np.loadtxt("uvspec.out", usecols=range(1,7), dtype=np.float32)[:,1]
    
    
colmns=["lambda", "edir", "edn", "eup", "uavgdir", "uavgdn", "uavgup"]

        
        



albedo0_1_TOA=np.loadtxt("/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec.out", usecols=range(0,7), dtype=np.float32)




import matplotlib.pyplot as plt
plt.scatter(albedo0_1_TOA[:,0], albedo0_1_TOA[:,1])
plt.scatter(albedo0_1_TOA[:,0], albedo0_1_TOA[:,2])
plt.scatter(albedo0_1_TOA[:,0], albedo0_1_TOA[:,3])
plt.scatter(albedo0_1_TOA[:,0], albedo0_1_TOA[:,4])
plt.scatter(albedo0_1_TOA[:,0], albedo0_1_TOA[:,5])
plt.scatter(albedo0_1_TOA[:,0], albedo0_1_TOA[:,6])




albedo1_surface=np.loadtxt("/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec.out", usecols=range(0,7), dtype=np.float32)


plt.scatter(albedo1_surface[:,0], albedo1_surface[:,1])
plt.scatter(albedo1_surface[:,0], albedo1_surface[:,2])
plt.scatter(albedo1_surface[:,0], albedo1_surface[:,3])
plt.scatter(albedo1_surface[:,0], albedo1_surface[:,4])
plt.scatter(albedo1_surface[:,0], albedo1_surface[:,5])
plt.scatter(albedo1_surface[:,0], albedo1_surface[:,6])





albedo0_TOA=np.loadtxt("/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec.out", usecols=range(0,7), dtype=np.float32)


plt.scatter(albedo0_TOA[:,0], albedo0_TOA[:,1])
plt.scatter(albedo0_TOA[:,0], albedo0_TOA[:,2])
plt.scatter(albedo0_TOA[:,0], albedo0_TOA[:,3])
plt.scatter(albedo0_TOA[:,0], albedo0_TOA[:,4])
plt.scatter(albedo0_TOA[:,0], albedo0_TOA[:,5])
plt.scatter(albedo0_TOA[:,0], albedo0_TOA[:,6])



albedo0_surface=np.loadtxt("/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec.out", usecols=range(0,7), dtype=np.float32)



plt.scatter(albedo0_surface[:,0], albedo0_surface[:,1])
plt.scatter(albedo0_surface[:,0], albedo0_surface[:,2])
plt.scatter(albedo0_surface[:,0], albedo0_surface[:,3])
plt.scatter(albedo0_surface[:,0], albedo0_surface[:,4])
plt.scatter(albedo0_surface[:,0], albedo0_surface[:,5])
plt.scatter(albedo0_surface[:,0], albedo0_surface[:,6])





"""Generating the path radiance"""


"""to obtain diffuse upwelling radiance one must set the the sensor altititude to the TOA, albedo to 0 and get the upwelling diffuse radiance."""

"""generate the dictionaries with strings"""
#%%
sza=[0.1,10,20,30,40,50,60,70]
aerosol_type=[1,4,5,6]
aerosol_visibility=[7,10,15,23,40,80,120]
water_vapor_column=[4, 10, 20, 29, 40, 50]
relative_azimuth=[0,30,60,90,120,150,180]
#sensor-earth_incidence_angle=[0,10,20,30,40]
#ground_elevation=[0,0.7,1.5,2.5,4]


n=[]

for i in range(len(sza)*len(aerosol_type)*len(aerosol_visibility)*len(water_vapor_column)*len(relative_azimuth)):
    #to write
    l=[]
    l.append("rte_solver disort")
    l.append("wavelength 450.0 2400.0 1")
    l.append("sza "+str(sza[int(i/1176)%8]))
    l.append("aerosol_haze "+str(aerosol_type[(int(i/294)%4)]))
    l.append("aerosol_season 1")
    l.append("aerosol_vulcan 1")
    l.append("aerosol_visibility "+str(aerosol_visibility[int(i/42)%7]))
    l.append("mol_modify H2O "+str(water_vapor_column[int(i/7)%6])+" MM")
    l.append("phi 0") #satellite azimuth is zero because the satellite views stuff right beneath it
    l.append("umu 1") #cosine of the viewing zenith is cos(0), because the satellite is looking downwards
    l.append("phi0 "+str(relative_azimuth[int(i%7)])) #this is the sun azimuth
    l.append("zout TOA")
    l.append("output_user lambda edir eglo edn eup enet esum")
    n.append(l)


#%%
from subprocess import call
import os
import numpy as np
import time 
#specifying the path for the input file we use to generate the fortran data
#specifying the path to execute the fortran script
path="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec"
path1="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/hyperion.inp"
path2="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/uvspec.out"
#specifying the path to execute read in generated data
path3="/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin/verbose.txt"
os.chdir("/home/stemonitis/colours/scripts/libRadtran-2.0.3/bin")
dic_path={}
for i in range(1358,len(n)):
    call(["rm", "hyperion.inp"])
    input=open("hyperion.inp", "a")
    [input.write(l+"\n") for l in n[i]]
    input.close()
    call("./uvspec <hyperion.inp> uvspec.out", shell=True)
    """while not os.path.exists("uvspec.out"):
        time.sleep(1)"""
    dic_path[i]=np.loadtxt("uvspec.out", usecols=range(1,7), dtype=np.float32)[:,4]
    print("done")
    call(["rm", "uvspec.out"])


#%%



""" obtain diffuse solar flux (at sensor)"""



dic_path0_1358=dic_path
np.save("/home/stemonitis/colours/scripts/Hyperion/dic_path0_1358",dic_path0_1358)
dic_path_1358_6244=dic_path
np.save("/home/stemonitis/colours/scripts/Hyperion/dic_path_1358_6244",dic_path_1358_6244)

first420=dic_path[:420,:]



















