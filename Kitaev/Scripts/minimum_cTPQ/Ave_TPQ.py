import numpy as np
import os
import copy
import math
import cmath
import read
import sys
import toml

max_set   = int(sys.argv[1])
dir_Phys = sys.argv[2]
#[s] set modpara
list_mod  =['Lanczos_max','NumAve','ExpecInterval'] # list for int. parameters
dict_mod  = read.func_mod("modpara_tpq.def",list_mod)     # read param.txt
tmp_max_eigen = int(dict_mod['Lanczos_max']) 
dstep     = int(dict_mod['ExpecInterval']) 
max_eigen = int(tmp_max_eigen/dstep)
print('max_eigen',max_eigen)
print('max_set',max_set)
print('dstep',dstep)
#[e] set modpara
#[s] tolm load
input_file  = sys.argv[3]
input_dict  = toml.load(input_file)
#[e] tolm load
#[s] set param.
K       = float(input_dict["param"]["K"])  
G       = float(input_dict["param"]["G"])   
GP      = float(input_dict["param"]["GP"])  
J       = float(input_dict["param"]["J"])  
mag_h   = -1.0*float(input_dict["param"]["h"])/math.sqrt(3.0)  #NB sign is changed
Lx      = int(input_dict["param"]["Lx"])  
Ly      = int(input_dict["param"]["Ly"])  
All_N   = Lx*Ly
max_site = Lx*Ly
#[e] set param.




Temp       = np.zeros([max_set,max_eigen],dtype=np.float)
ave_Temp   = np.zeros([max_eigen],dtype=np.float)
err_Temp   = np.zeros([max_eigen],dtype=np.float)
Ene        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_Ene    = np.zeros([max_eigen],dtype=np.float)
err_Ene    = np.zeros([max_eigen],dtype=np.float)
Spc        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_Spc    = np.zeros([max_eigen],dtype=np.float)
err_Spc    = np.zeros([max_eigen],dtype=np.float)
JL1        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_JL1    = np.zeros([max_eigen],dtype=np.float)
err_JL1    = np.zeros([max_eigen],dtype=np.float)
JL2        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_JL2    = np.zeros([max_eigen],dtype=np.float)
err_JL2    = np.zeros([max_eigen],dtype=np.float)
JM         = np.zeros([max_set,max_eigen],dtype=np.float)
ave_JM     = np.zeros([max_eigen],dtype=np.float)
err_JM     = np.zeros([max_eigen],dtype=np.float)

KPL1        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_KPL1    = np.zeros([max_eigen],dtype=np.float)
err_KPL1    = np.zeros([max_eigen],dtype=np.float)
KPL2        = np.zeros([max_set,max_eigen],dtype=np.float)
ave_KPL2    = np.zeros([max_eigen],dtype=np.float)
err_KPL2    = np.zeros([max_eigen],dtype=np.float)
KPL         = np.zeros([max_set,max_eigen],dtype=np.float)
ave_KPL     = np.zeros([max_eigen],dtype=np.float)
err_KPL     = np.zeros([max_eigen],dtype=np.float)
KPM         = np.zeros([max_set,max_eigen],dtype=np.float)
ave_KPM     = np.zeros([max_eigen],dtype=np.float)
err_KPM     = np.zeros([max_eigen],dtype=np.float)
KP          = np.zeros([max_set,max_eigen],dtype=np.float)
ave_KP      = np.zeros([max_eigen],dtype=np.float)
err_KP      = np.zeros([max_eigen],dtype=np.float)



for cnt_set in range(0,max_set):
    with open("%s/all_3_set%d.dat" % (dir_Phys,cnt_set)) as f:
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
                tmp_JL1 = 0.0
                tmp_JL2 = 0.0
                for tmp_cnt in range(0,int(Lx/2)): 
                    off_set   = tmp_cnt*6+3 
                    tmp_JL1  += (float(tmp[0+off_set])+float(tmp[1+off_set]))/2.0
                    tmp_JL2  += (float(tmp[2+off_set])+float(tmp[3+off_set]))/4.0
                    tmp_JL2  += (float(tmp[4+off_set])+float(tmp[5+off_set]))/4.0
                JL1[cnt_set][tmp_i] = tmp_JL1
                JL2[cnt_set][tmp_i] = tmp_JL2

ave_Temp = np.mean(Temp,axis=0)
err_Temp = np.std(Temp,axis=0,ddof=1)
ave_Ene  = np.mean(Ene,axis=0)
err_Ene  = np.std(Ene,axis=0,ddof=1)
ave_Spc  = np.mean(Spc,axis=0)
err_Spc  = np.std(Spc,axis=0,ddof=1)
ave_JL1  = np.mean(JL1,axis=0)
err_JL1  = np.std(JL1,axis=0,ddof=1)
ave_JL2  = np.mean(JL2,axis=0)
err_JL2  = np.std(JL2,axis=0,ddof=1)
#print(ave_Temp)
#print(err_Temp)

for cnt_set in range(0,max_set):
    with open("%s/all_2_set%d.dat" % (dir_Phys,cnt_set)) as f:
        data      = f.read()
        data      = data.split("\n")
        #[s] count not empty elements
        for i in range(2,len(data)):
            tmp_i = i-2
            tmp   = data[i].split()
            if len(tmp)>1: # if data[i] is not empty
                tmp_JM = 0.0
                for tmp_cnt in range(0,int(Lx/2)): 
                    off_set  = tmp_cnt*3+3
                    tmp_JM   += (float(tmp[0+off_set])+float(tmp[1+off_set]))/4.0
                JM[cnt_set][tmp_i] = tmp_JM

ave_JM  = np.mean(JM,axis=0)
err_JM  = np.std(JM,axis=0,ddof=1)

for cnt_set in range(0,max_set):
    for cnt in range(0,max_eigen-2):
        dT                   = Temp[cnt_set][cnt+1] - Temp[cnt_set][cnt]
        #print(cnt+1,dT, Temp[cnt_set][cnt+1], Temp[cnt_set][cnt])
        dJL1                 = JL1[cnt_set][cnt+1]  - JL1[cnt_set][cnt]
        dJL2                 = JL2[cnt_set][cnt+1]  - JL2[cnt_set][cnt]
        dJM                  = JM[cnt_set][cnt+1]   - JM[cnt_set][cnt]
        KPL1[cnt_set][cnt]   = dJL1/dT
        KPL2[cnt_set][cnt]   = dJL2/dT
        KPL[cnt_set][cnt]    = (dJL1+dJL2)/dT
        KPM[cnt_set][cnt]    = dJM/dT
        KP[cnt_set][cnt]     = (dJL1+dJL2+dJM)/dT

for cnt_set in range(0,max_set):
    with open("%s/JE_tpq_set%d.dat" % (dir_Phys,cnt_set), 'w') as f:
        for cnt in range(0,max_eigen-2):
            true_cnt = dstep*(cnt+1)
            print(" %8d    " % (true_cnt), end="", file=f)          #1
            print(" %.16f  " % (Temp[cnt_set][cnt]), end="", file=f)#2
            print(" %.16f  " % (JL1[cnt_set][cnt]), end="", file=f)#3
            print(" %.16f  " % (JL2[cnt_set][cnt]), end="", file=f)#4
            print(" %.16f  " % (JM[cnt_set][cnt]), end="", file=f)#5
            print(" %.16f  " % (KPL1[cnt_set][cnt]), end="", file=f)#6
            print(" %.16f  " % (KPL2[cnt_set][cnt]), end="", file=f)#7
            print(" %.16f  " % (KPL[cnt_set][cnt]), end="", file=f)#8
            print(" %.16f  " % (KPM[cnt_set][cnt]), end="", file=f)#9
            print(" %.16f  " % (KP[cnt_set][cnt]), end="", file=f)#10
            print(" ", file=f)

ave_KPL1  = np.mean(KPL1,axis=0)
err_KPL1  = np.std(KPL1,axis=0,ddof=1)
ave_KPL2  = np.mean(KPL2,axis=0)
err_KPL2  = np.std(KPL2,axis=0,ddof=1)
ave_KPL   = np.mean(KPL,axis=0)
err_KPL   = np.std(KPL,axis=0,ddof=1)
ave_KPM   = np.mean(KPM,axis=0)
err_KPM   = np.std(KPM,axis=0,ddof=1)
ave_KP    = np.mean(KP,axis=0)
err_KP    = np.std(KP,axis=0,ddof=1)

with open("%s/JE_tpq.dat" % (dir_Phys), 'w') as f:
    for cnt in range(0,max_eigen-2):
        print(" %.16f  " % (ave_Temp[cnt]), end="", file=f)#1
        print(" %.16f  " % (err_Temp[cnt]), end="", file=f)#2
        print(" %.16f  " % (ave_Ene[cnt]), end="", file=f) #3
        print(" %.16f  " % (err_Ene[cnt]), end="", file=f) #4
        print(" %.16f  " % (ave_Spc[cnt]), end="", file=f) #5
        print(" %.16f  " % (err_Spc[cnt]), end="", file=f) #6
        print(" %.16f  " % (ave_JL1[cnt]), end="", file=f) #7
        print(" %.16f  " % (err_JL1[cnt]), end="", file=f) #8
        print(" %.16f  " % (ave_JL2[cnt]), end="", file=f) #9
        print(" %.16f  " % (err_JL2[cnt]), end="", file=f) #10
        print(" %.16f  " % (ave_JM[cnt]), end="", file=f)  #11
        print(" %.16f  " % (err_JM[cnt]), end="", file=f)  #12
        print(" %.16f  " % (ave_KPL1[cnt]), end="", file=f)#13
        print(" %.16f  " % (err_KPL1[cnt]), end="", file=f)#14
        print(" %.16f  " % (ave_KPL2[cnt]), end="", file=f)#15
        print(" %.16f  " % (err_KPL2[cnt]), end="", file=f)#16
        print(" %.16f  " % (ave_KPL[cnt]), end="", file=f) #17
        print(" %.16f  " % (err_KPL[cnt]), end="", file=f) #18
        print(" %.16f  " % (ave_KPM[cnt]), end="", file=f) #19
        print(" %.16f  " % (err_KPM[cnt]), end="", file=f) #20
        print(" %.16f  " % (ave_KP[cnt]), end="", file=f)  #21
        print(" %.16f  " % (err_KP[cnt]), end="", file=f)  #22
        print(" ", file=f)
