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

with open("all_3.dat") as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     #[s] count not empty elements
     cnt = 0
     for i in range(0,len(data)):
         tmp        = data[i].split()
         #print(tmp)
         if len(tmp)>1: # if data[i] is not empty
             for tmp_cnt in range(0,int(Lx/2)): 
                 off_set              = tmp_cnt*6+1 
                 JL1[tmp_cnt][cnt]    = (float(tmp[0+off_set])+float(tmp[1+off_set]))/2.0
                 JL2[tmp_cnt][cnt]    = (float(tmp[2+off_set])+float(tmp[3+off_set]))/4.0
                 JL2[tmp_cnt][cnt]   += (float(tmp[4+off_set])+float(tmp[5+off_set]))/4.0
             cnt += 1

with open("all_2.dat") as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     #[s] count not empty elements
     cnt = 0
     for i in range(0,len(data)):
         tmp        = data[i].split()
         #print(tmp)
         if len(tmp)>1: # if data[i] is not empty
             for tmp_cnt in range(0,int(Lx/2)): 
                 off_set              = tmp_cnt*3+1
                 JM[tmp_cnt][cnt]     = (float(tmp[0+off_set])+float(tmp[1+off_set]))/4.0
             cnt += 1

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
             mag[cnt]      = float(tmp[1])
             mag_x[cnt]    = float(tmp[2])
             mag_y[cnt]    = float(tmp[3])
             mag_z[cnt]    = float(tmp[4])
             cnt += 1

with open("JE.dat", 'w') as f:
    e_temp   = -4
    int_temp =  0
    temp     = -1
    p_N      = 50
    #while temp < 100:
    while temp < 100:
        if int_temp == p_N:
            int_temp  = 0
            e_temp   += 1
        temp     = (1+(9.0/(1.0*p_N)*int_temp))*pow(10,e_temp)
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
        for tmp_cnt in range(0,int(Lx/2)): 
            all_JL1[tmp_cnt]   = 0.0
            all_JL2[tmp_cnt]   = 0.0
            all_JM[tmp_cnt]   = 0.0
        for cnt in range(0,max_eigen):
            norm_ene  = Energy[cnt]-Energy[0]
            Z        += math.exp(-beta*norm_ene)
            all_E    += Energy[cnt]*math.exp(-beta*norm_ene)
            all_E2   += (Energy[cnt]**2)*math.exp(-beta*norm_ene)
            all_mag  += (mag[cnt])*math.exp(-beta*norm_ene)
            all_mag_x  += (mag_x[cnt])*math.exp(-beta*norm_ene)
            all_mag_y  += (mag_y[cnt])*math.exp(-beta*norm_ene)
            all_mag_z  += (mag_z[cnt])*math.exp(-beta*norm_ene)
            for tmp_cnt in range(0,int(Lx/2)): 
               all_JL1[tmp_cnt]  += JL1[tmp_cnt][cnt]*math.exp(-beta*norm_ene)
               all_JL2[tmp_cnt]  += JL2[tmp_cnt][cnt]*math.exp(-beta*norm_ene)
               all_JM[tmp_cnt]   += JM[tmp_cnt][cnt]*math.exp(-beta*norm_ene)
               all_JL1E          += JL1[tmp_cnt][cnt]*Energy[cnt]*math.exp(-beta*norm_ene) 
               all_JL2E          += JL2[tmp_cnt][cnt]*Energy[cnt]*math.exp(-beta*norm_ene) 
               all_JME           += JM[tmp_cnt][cnt]*Energy[cnt]*math.exp(-beta*norm_ene) 
        for tmp_cnt in range(0,int(Lx/2)): 
            tmp_JL1          += all_JL1[tmp_cnt]/Z 
            tmp_JL2          += all_JL2[tmp_cnt]/Z 
            tmp_JM           += all_JM[tmp_cnt]/Z 
            all_JL1[tmp_cnt]  = all_JL1[tmp_cnt]/Z
            all_JL2[tmp_cnt]  = all_JL2[tmp_cnt]/Z
            all_JM[tmp_cnt]   = all_JM[tmp_cnt]/Z
        tmp_E   = all_E/Z
        tmp_mag = all_mag/Z
        tmp_mag_x = all_mag_x/Z
        tmp_mag_y = all_mag_y/Z
        tmp_mag_z = all_mag_z/Z
        tmp_C   = beta*beta*(all_E2/Z-(all_E/Z)**2)
        tmp_DL1 = beta*beta*(all_JL1E/Z-tmp_E*tmp_JL1)
        tmp_DL2 = beta*beta*(all_JL2E/Z-tmp_E*tmp_JL2)
        tmp_DM  = beta*beta*(all_JME/Z-tmp_E*tmp_JM)
        print(" %.16f  " % (1.0/beta), end="", file=f)
        print(" %.16f  " % (tmp_E)   , end="", file=f)
        print(" %.16f  " % (tmp_C)   , end="", file=f)
        print(" %.16f  " % (tmp_JL1) , end="", file=f)
        print(" %.16f  " % (tmp_JL2) , end="", file=f)
        print(" %.16f  " % (tmp_JM)  , end="", file=f)
        print(" %.16f  " % (tmp_DL1), end="", file=f)
        print(" %.16f  " % (tmp_DL2), end="", file=f)
        print(" %.16f  " % (tmp_DM), end="", file=f)
        print(" %.16f  " % (tmp_mag), end="", file=f)
        print(" %.16f  " % (tmp_mag_x), end="", file=f)
        print(" %.16f  " % (tmp_mag_y), end="", file=f)
        print(" %.16f  " % (tmp_mag_z), end="", file=f)
        for tmp_cnt in range(0,int(Lx/2)): 
            print(" %.16f  " % (all_JL1[tmp_cnt]), end="", file=f)
            print(" %.16f  " % (all_JL2[tmp_cnt]), end="", file=f)
            print(" %.16f  " % (all_JM[tmp_cnt]), end="", file=f)
        print(" ", file=f)
