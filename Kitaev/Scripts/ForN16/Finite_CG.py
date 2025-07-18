import numpy as np
import os
import copy
import math
import cmath
import read

list_param =['K','J','G','GP','h','Lx','Ly','exct'] # list for int. parameters
dict_param = read.func_param(list_param)     # read param.txt
exct = int(dict_param['exct'])
max_eigen = exct

Energy     = np.zeros([max_eigen],dtype=np.float)
Flux       = np.zeros([max_eigen],dtype=np.float)
with open("output/CG_Eigenvalue.dat") as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     #[s] count not empty elements
     cnt = 0
     for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           tmp        = data[i].split()
           Energy[cnt] = float(tmp[1])
           cnt       += 1
        #print(cnt)

with open("all_result.dat") as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     #[s] count not empty elements
     cnt = 0
     for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           tmp        = data[i].split()
           Flux[cnt]  = float(tmp[1])+float(tmp[3])
           Flux[cnt]  += float(tmp[5])+float(tmp[7])
           Flux[cnt]  += float(tmp[9])+float(tmp[11])
           Flux[cnt]  = Flux[cnt]/6.0 

           cnt       += 1
        #print(cnt)

print(Energy)
f        = open("Flux.dat", 'wt')
for temp in range(1,1000):
    if temp < 500:
      beta     = 1.0/(temp*0.0002)
    else:
      beta     = 1.0/(0.1+(temp-500)*0.01)
    Z        = 0.0
    all_Flux = 0.0
    all_E    = 0.0
    all_E2   = 0.0
    for cnt in range(0,max_eigen):
        norm_ene  = Energy[cnt]-Energy[0]
        all_Flux += Flux[cnt]*math.exp(-beta*norm_ene)
        all_E    += Energy[cnt]*math.exp(-beta*norm_ene)
        all_E2   += (Energy[cnt]**2)*math.exp(-beta*norm_ene)
        Z        += math.exp(-beta*norm_ene)
    tmp_F = all_Flux/Z
    tmp_e = all_E/Z
    tmp_C = beta*beta*(all_E2/Z-(all_E/Z)**2)
    f.write(" {0:16f} ".format(1.0/beta) \
    +" {0:.16f}   ".format(tmp_e)         \
    +" {0:.16f}   ".format(tmp_F)           \
    +" {0:.16f}   ".format(tmp_C)           \
    +" {0:.16f}   ".format(beta)          \
    +"\n")
    #print(beta,tmp)
f.close()
