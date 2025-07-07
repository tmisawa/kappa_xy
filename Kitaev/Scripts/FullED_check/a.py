import numpy as np
import os
import copy
import math
import cmath

max_eigen = 65536
Lx        = 4
Ly        = 4 # Ly will not be used

Energy     = np.zeros([max_eigen],dtype=np.float)
JL1        = np.zeros([int(Lx/2),max_eigen],dtype=np.float)
JL2        = np.zeros([int(Lx/2),max_eigen],dtype=np.float)
JM         = np.zeros([int(Lx/2),max_eigen],dtype=np.float)
mag        = np.zeros([max_eigen],dtype=np.float)
mag_x      = np.zeros([max_eigen],dtype=np.float)
mag_y      = np.zeros([max_eigen],dtype=np.float)
mag_z      = np.zeros([max_eigen],dtype=np.float)
all_JL1    = np.zeros([int(Lx/2)],dtype=np.float)
all_JL2    = np.zeros([int(Lx/2)],dtype=np.float)
all_JM     = np.zeros([int(Lx/2)],dtype=np.float)
with open("output/Eigenvalue.dat") as f:
#with open("Eigenvalue.dat") as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     #[s] count not empty elements
     cnt = 0
     for i in range(0,len(data)):
         tmp        = data[i].split()
         #print(len(tmp))
         if len(tmp)>1: # if data[i] is not empty
             Energy[cnt] = float(tmp[1])
             cnt        += 1

with open("all_1.dat") as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     #[s] count not empty elements
     cnt = 0
     for i in range(0,len(data)):
         tmp        = data[i].split()
         #print(tmp)
         if len(tmp)>1: # if data[i] is not empty
             mag[cnt]      = float(tmp[2])**2+float(tmp[3])**2+float(tmp[4])**2
             mag_x[cnt]    = float(tmp[2])
             mag_y[cnt]    = float(tmp[3])
             mag_z[cnt]    = float(tmp[4])
             cnt += 1



with open("JE.dat", 'w') as f:
    e_temp   = -4
    int_temp =  1
    temp     = -1
    while temp < 100:
        if int_temp == 19:
            int_temp  = 1
            e_temp   += 1
        temp     = (int_temp/2.0+0.5)*pow(10,e_temp)
        print(int_temp,e_temp,temp)
        beta     = 1.0/(temp)
        int_temp += 1
    
        Z        = 0.0
        all_E    = 0.0
        all_E2   = 0.0
        all_JL1E = 0.0
        all_JL2E = 0.0
        all_JME  = 0.0
        all_mag  = 0.0
        all_mag_x  = 0.0
        all_mag_y  = 0.0
        all_mag_z  = 0.0
        tmp_JL1  = 0.0
        tmp_JL2  = 0.0
        tmp_JM   = 0.0
        for cnt in range(0,max_eigen):
            norm_ene  = Energy[cnt]-Energy[0]
            Z        += math.exp(-beta*norm_ene)
            all_E    += Energy[cnt]*math.exp(-beta*norm_ene)
            all_E2   += (Energy[cnt]**2)*math.exp(-beta*norm_ene)
            all_mag  += (mag[cnt])*math.exp(-beta*norm_ene)
            all_mag_x  += (mag_x[cnt])*math.exp(-beta*norm_ene)
            all_mag_y  += (mag_y[cnt])*math.exp(-beta*norm_ene)
            all_mag_z  += (mag_z[cnt])*math.exp(-beta*norm_ene)
        tmp_E   = all_E/Z
        tmp_mag = all_mag/Z
        tmp_mag_x = all_mag_x/Z
        tmp_mag_y = all_mag_y/Z
        tmp_mag_z = all_mag_z/Z
        tmp_C   = beta*beta*(all_E2/Z-(all_E/Z)**2)
        print(" %.16f  " % (1.0/beta), end="", file=f)
        print(" %.16f  " % (tmp_E)   , end="", file=f)
        print(" %.16f  " % (tmp_C)   , end="", file=f)
        print(" %.16f  " % (tmp_mag), end="", file=f)
        print(" %.16f  " % (tmp_mag_x), end="", file=f)
        print(" %.16f  " % (tmp_mag_y), end="", file=f)
        print(" %.16f  " % (tmp_mag_z), end="", file=f)
        print(" ", file=f)
