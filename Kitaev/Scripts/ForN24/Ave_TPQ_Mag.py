import numpy as np
import os
import copy
import math
import cmath
import read
import sys

max_set   = int(sys.argv[1])
dir_Phys = sys.argv[2]
#[s] set modpara
list_mod  =['Lanczos_max','NumAve','ExpecInterval','Nsite'] # list for int. parameters
dict_mod  = read.func_mod("modpara_tpq.def",list_mod)     # read param.txt
tmp_max_eigen = int(dict_mod['Lanczos_max']) 
#max_set   = int(dict_mod['NumAve']) 
dstep     = int(dict_mod['ExpecInterval']) 
Nsite     = int(dict_mod['Nsite']) 
max_eigen = int(tmp_max_eigen/dstep)
print('max_eigen',max_eigen)
print('max_set',max_set)
print('dstep',dstep)
#[e] set modpara


Temp       = np.zeros([max_set,max_eigen],dtype=np.float)
ave_Temp   = np.zeros([max_eigen],dtype=np.float)
err_Temp   = np.zeros([max_eigen],dtype=np.float)
Ene        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_Ene    = np.zeros([max_eigen],dtype=np.float)
err_Ene    = np.zeros([max_eigen],dtype=np.float)
Spc        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_Spc    = np.zeros([max_eigen],dtype=np.float)
err_Spc    = np.zeros([max_eigen],dtype=np.float)
Mag        = np.zeros([max_set,max_eigen],dtype=np.float)
Mag_x      = np.zeros([max_set,max_eigen],dtype=np.float)
Mag_y      = np.zeros([max_set,max_eigen],dtype=np.float)
Mag_z      = np.zeros([max_set,max_eigen],dtype=np.float)
ave_Mag    = np.zeros([max_eigen],dtype=np.float)
ave_Mag_x  = np.zeros([max_eigen],dtype=np.float)
ave_Mag_y  = np.zeros([max_eigen],dtype=np.float)
ave_Mag_z  = np.zeros([max_eigen],dtype=np.float)
err_Mag    = np.zeros([max_eigen],dtype=np.float)
err_Mag_x  = np.zeros([max_eigen],dtype=np.float)
err_Mag_y  = np.zeros([max_eigen],dtype=np.float)
err_Mag_z  = np.zeros([max_eigen],dtype=np.float)

for cnt_set in range(0,max_set):
    with open("%s/all_1_set%d.dat" % (dir_Phys,cnt_set)) as f:
        data      = f.read()
        data      = data.split("\n")
        #print(len(data))
        #[s] count not empty elements
        for i in range(2,len(data)):
            tmp_i              = i-2
            tmp                = data[i].split()
            #print(tmp)
            if len(tmp)>1: # if data[i] is not empty
                Temp[cnt_set][tmp_i]   = tmp[0]
                Ene[cnt_set][tmp_i]    = tmp[1]
                Spc[cnt_set][tmp_i]    = tmp[2]
                loc_Mag_x = 0.0
                loc_Mag_y = 0.0
                loc_Mag_z = 0.0
                for tmp_cnt in range(0,3*Nsite,3): 
                    loc_Mag_x  += float(tmp[3+tmp_cnt])
                    loc_Mag_y  += float(tmp[3+tmp_cnt+1])
                    loc_Mag_z  += float(tmp[3+tmp_cnt+2])
                Mag[cnt_set][tmp_i]   = math.sqrt((loc_Mag_x/Nsite)**2+(loc_Mag_y/Nsite)**2+(loc_Mag_z/Nsite)**2)
                Mag_x[cnt_set][tmp_i] = loc_Mag_x/(Nsite)
                Mag_y[cnt_set][tmp_i] = loc_Mag_y/(Nsite)
                Mag_z[cnt_set][tmp_i] = loc_Mag_z/(Nsite)

ave_Temp  = np.mean(Temp,axis=0)
err_Temp  = np.std(Temp,axis=0,ddof=1)
ave_Ene   = np.mean(Ene,axis=0)
err_Ene   = np.std(Ene,axis=0,ddof=1)
ave_Spc   = np.mean(Spc,axis=0)
err_Spc   = np.std(Spc,axis=0,ddof=1)
ave_Mag  = np.mean(Mag,axis=0)
err_Mag  = np.std(Mag,axis=0,ddof=1)
#print(ave_Temp)
#print(err_Temp)

for cnt_set in range(0,max_set):
    with open("%s/Mag_tpq_set%d.dat" % (dir_Phys,cnt_set), 'w') as f:
        for cnt in range(0,max_eigen-1):
            true_cnt = dstep*(cnt+1)
            print(" %8d    " % (true_cnt), end="", file=f)          #1
            print(" %.16f  " % (Temp[cnt_set][cnt]), end="", file=f)#2
            print(" %.16f  " % (Mag[cnt_set][cnt]), end="", file=f)#3
            print(" %.16f  " % (Mag_x[cnt_set][cnt]), end="", file=f)#4
            print(" %.16f  " % (Mag_y[cnt_set][cnt]), end="", file=f)#5
            print(" %.16f  " % (Mag_z[cnt_set][cnt]), end="", file=f)#6
            print(" ", file=f)

with open("%s/Mag_tpq.dat" % (dir_Phys), 'w') as f:
    for cnt in range(0,max_eigen-1):
        print(" %.16f  " % (ave_Temp[cnt]), end="", file=f)#1
        print(" %.16f  " % (err_Temp[cnt]), end="", file=f)#2
        print(" %.16f  " % (ave_Ene[cnt]), end="", file=f) #3
        print(" %.16f  " % (err_Ene[cnt]), end="", file=f) #4
        print(" %.16f  " % (ave_Spc[cnt]), end="", file=f) #5
        print(" %.16f  " % (err_Spc[cnt]), end="", file=f) #6
        print(" %.16f  " % (ave_Mag[cnt]), end="", file=f) #7
        print(" %.16f  " % (err_Mag[cnt]), end="", file=f) #8
        print(" ", file=f)
