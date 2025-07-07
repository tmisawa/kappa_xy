import numpy as np
import os
import sys
import copy
import math
import cmath
import itertools
import read    #using read.py#
import hphi_io #using hphi_io.py#
import CalcLM  #using CalcLM.py#

#[s] set modpara
max_set    = int(sys.argv[1])
dir_Phys = sys.argv[2]
list_mod  =['Lanczos_max','NumAve','ExpecInterval','Nsite'] # list for int. parameters
dict_mod  = read.func_mod("modpara_tpq.def",list_mod)     # read param.txt
max_eigen = int(dict_mod['Lanczos_max']) 
dstep     = int(dict_mod['ExpecInterval']) 
Nsite     = int(dict_mod['Nsite']) 
print('max_eigen',max_eigen)
print('max_set',max_set)
print('dstep',dstep)
#[e] set modpara
#[s] set param.
#[e] set param.
#sys.exit()

#[s] get temperature
inv_temp = np.zeros([max_set,max_eigen],dtype=np.float)
ene      = np.zeros([max_set,max_eigen],dtype=np.float)
ene2     = np.zeros([max_set,max_eigen],dtype=np.float)
for cnt_set in range(0,max_set):
    file_name  = "output/SS_rand{}.dat".format(cnt_set)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
    for i in range(1,max_eigen+1):
        if data[i]: # if data[i] is not empty
            tmp            = data[i].split()
            cnt            = int(tmp[5])
            inv_temp[cnt_set][cnt]  = float(tmp[0])
            ene[cnt_set][cnt]       = float(tmp[1])
            ene2[cnt_set][cnt]      = float(tmp[2])
#[e] get temperatute

#for x0,x1,x2 in itertools.product(flag,flag,flag):
#    print(x0,x1,x2,LeviCivita[x0][x1][x2])
#
tmp_sdt  = "green1.txt"
tmp_num   = read.func_count(tmp_sdt)
print('tmp_num=',tmp_num)
in_G1site0  = np.zeros([tmp_num],dtype=np.int)
in_G1spin0  = np.zeros([tmp_num],dtype=np.unicode)
in_G1Int0   = np.zeros([tmp_num],dtype=np.float)
in_G1Int1   = np.zeros([tmp_num],dtype=np.float)
in_G1sign   = np.zeros([tmp_num],dtype=np.float)
val_x      = np.zeros([Nsite],dtype=np.float)
val_y      = np.zeros([Nsite],dtype=np.float)
val_z      = np.zeros([Nsite],dtype=np.float)
read.func_green1(tmp_sdt,in_G1site0,in_G1spin0,in_G1Int0,in_G1Int1,in_G1sign)
#
for cnt_set in range(0,max_set):
    with open("%s/all_1_set%d.dat" % (dir_Phys,cnt_set) , 'w') as f:
        print(" # ", file=f)
    #
    for cnt_eigen in range(0,max_eigen,dstep):
        if inv_temp[cnt_set][cnt_eigen] < 1e-8:
            temp     = 1e10
        else:
            temp     = 1.0/inv_temp[cnt_set][cnt_eigen]
        tmp_ene  = ene[cnt_set][cnt_eigen]
        spc_heat = (ene2[cnt_set][cnt_eigen]-tmp_ene*tmp_ene)*inv_temp[cnt_set][cnt_eigen]*inv_temp[cnt_set][cnt_eigen]
        print("1-body ",cnt_eigen)
        tmp_sdt  = "output/zvo_cisajs_set%dstep%d.dat" % (cnt_set,cnt_eigen)
        #read.val_green1(tmp_sdt,in_G1spin0,val)
        read.mod_val_green1(tmp_sdt,in_G1spin0,val_x,val_y,val_z)
        with open("%s/all_1_set%d.dat" % (dir_Phys,cnt_set) , 'a') as f:
            print(" %12.8f %12.8f %12.8f " % (temp,tmp_ene,spc_heat),end="", file=f)
            for tmp_cnt in range(0,Nsite):
                print(" %12.8f %12.8f %12.8f " % (val_x[tmp_cnt],val_y[tmp_cnt],val_z[tmp_cnt]),end = "", file=f)
            print(" ",file=f)
