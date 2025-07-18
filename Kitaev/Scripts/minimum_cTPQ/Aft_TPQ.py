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
import toml

#[s] set modpara
max_set    = int(sys.argv[1])
dir_Phys = sys.argv[2]
list_mod  =['Lanczos_max','NumAve','ExpecInterval'] # list for int. parameters
dict_mod  = read.func_mod("modpara_tpq.def",list_mod)     # read param.txt
max_eigen = int(dict_mod['Lanczos_max'])
#max_set   = 10 #int(dict_mod['NumAve']) 
dstep     = int(dict_mod['ExpecInterval']) 
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

LeviCivita  = np.zeros([3,3,3],dtype=np.int)
LeviCivita[0][1][2] =  1
LeviCivita[0][2][1] = -1
LeviCivita[1][0][2] = -1
LeviCivita[1][2][0] =  1
LeviCivita[2][0][1] =  1 
LeviCivita[2][1][0] = -1
flag      = list(range(3))
flag[0]   = 0
flag[1]   = 1
flag[2]   = 2

all_h    = np.zeros([3],dtype=np.float)
all_h[0] = mag_h 
all_h[1] = mag_h
all_h[2] = mag_h

Jx     = np.zeros([3,3],dtype=np.float)
Jy     = np.zeros([3,3],dtype=np.float)
Jz     = np.zeros([3,3],dtype=np.float)
all_J  = np.zeros([3,3,3],dtype=np.float)
Thermal_Phys_3  = np.zeros([15],dtype=np.complex)
dict_spin     = {'x':0,'y':1,'z':2}
inv_dict_spin = {0:'x',1:'y',2:'z'}
print(dict_spin)
print(inv_dict_spin)

#[s] Thermal_Phys_2 
tmp_max         = int(Lx/2)
Thermal_Phys_2  = np.zeros([3,int(Lx/2)],dtype=np.complex)
Phys_2_site_i   = np.zeros([3,int(Lx/2)],dtype=np.int)
Phys_2_site_j   = np.zeros([3,int(Lx/2)],dtype=np.int)
Phys_2_spin     = np.zeros([3,int(Lx/2)],dtype=np.unicode)
cnt = 0
for i_x in range(0,int(Lx/2)):
    if i_x%2 == 0:
        i_0 = i_x*Ly
    else:      
        i_0 = CalcLM.trans(i_x*Ly,Lx,Ly,0,1)
    for i_spin in range(0,3):
        if i_spin == 0:
            Phys_2_site_i[i_spin][i_x]   = i_0
            Phys_2_site_j[i_spin][i_x]   = CalcLM.trans(i_0,Lx,Ly,0,1)
            Phys_2_spin[i_spin][i_x]     = inv_dict_spin[i_spin]
        elif i_spin == 1:
            Phys_2_site_i[i_spin][i_x]   = CalcLM.trans(i_0,Lx,Ly,0,1)
            Phys_2_site_j[i_spin][i_x]   = CalcLM.trans(i_0,Lx,Ly,0,2)
            Phys_2_spin[i_spin][i_x]     = inv_dict_spin[i_spin]
        elif i_spin == 2:
            Phys_2_site_i[i_spin][i_x]   = CalcLM.trans(i_0,Lx,Ly,0,1)
            Phys_2_site_j[i_spin][i_x]   = CalcLM.trans(i_0,Lx,Ly,1,1)
            Phys_2_spin[i_spin][i_x]     = inv_dict_spin[i_spin]
#[e] Thermal_Phys_2 

#[s] Thermal_Phys_3 
tmp_max         = int(Lx/2)
Thermal_Phys_3  = np.zeros([6,tmp_max],dtype=np.complex)
Phys_3_site_i   = np.zeros([6,tmp_max],dtype=np.int)
Phys_3_site_j   = np.zeros([6,tmp_max],dtype=np.int)
Phys_3_site_k   = np.zeros([6,tmp_max],dtype=np.int)
Phys_3_spin_0   = np.zeros([6,tmp_max],dtype=np.unicode)
Phys_3_spin_1   = np.zeros([6,tmp_max],dtype=np.unicode)
cnt = 0
for i_x in range(0,int(Lx/2)):
    if  i_x%2 == 0:
        i_0 = i_x*Ly
    else:
        i_0 = CalcLM.trans(i_x*Ly,Lx,Ly,0,1)
    for i_L in range(0,6):
        if  i_L == 0:
            ini_i = i_0
            Phys_3_site_i[i_L][i_x],Phys_3_site_j[i_L][i_x],Phys_3_site_k[i_L][i_x],\
            Phys_3_spin_0[i_L][i_x],Phys_3_spin_1[i_L][i_x] = CalcLM.func_MakeL0_0(i_0,Lx,Ly)
        elif i_L == 1:
            ini_i = CalcLM.trans(i_0,Lx,Ly,0,1)
            Phys_3_site_i[i_L][i_x],Phys_3_site_j[i_L][i_x],Phys_3_site_k[i_L][i_x],\
            Phys_3_spin_0[i_L][i_x],Phys_3_spin_1[i_L][i_x] = CalcLM.func_MakeL0_1(ini_i,Lx,Ly)
        elif i_L == 2:
            ini_i = CalcLM.trans(i_0,Lx,Ly,0,0)
            Phys_3_site_i[i_L][i_x],Phys_3_site_j[i_L][i_x],Phys_3_site_k[i_L][i_x],\
            Phys_3_spin_0[i_L][i_x],Phys_3_spin_1[i_L][i_x] = CalcLM.func_MakeL1_0(ini_i,Lx,Ly)
        elif i_L == 3:
            ini_i = CalcLM.trans(i_0,Lx,Ly,1,1)
            Phys_3_site_i[i_L][i_x],Phys_3_site_j[i_L][i_x],Phys_3_site_k[i_L][i_x],\
            Phys_3_spin_0[i_L][i_x],Phys_3_spin_1[i_L][i_x] = CalcLM.func_MakeL1_1(ini_i,Lx,Ly)
        elif i_L == 4:
            ini_i = CalcLM.trans(i_0,Lx,Ly,0,1)
            Phys_3_site_i[i_L][i_x],Phys_3_site_j[i_L][i_x],Phys_3_site_k[i_L][i_x],\
            Phys_3_spin_0[i_L][i_x],Phys_3_spin_1[i_L][i_x] = CalcLM.func_MakeL2_0(ini_i,Lx,Ly)
        elif i_L == 5:
            ini_i = CalcLM.trans(i_0,Lx,Ly,1,2)
            Phys_3_site_i[i_L][i_x],Phys_3_site_j[i_L][i_x],Phys_3_site_k[i_L][i_x],\
            Phys_3_spin_0[i_L][i_x],Phys_3_spin_1[i_L][i_x] = CalcLM.func_MakeL2_1(ini_i,Lx,Ly)
        #
#[e] Thermal_Phys_2 

#[s]Jx
Jx[0][0] = J+K
Jx[0][1] = GP
Jx[0][2] = GP
Jx[1][1] = J
Jx[1][2] = G
Jx[2][2] = J
for cnt_i in range(0,3):
    for cnt_j in range(cnt_i,3):
        Jx[cnt_j][cnt_i] = Jx[cnt_i][cnt_j]
#print(Jx)
#[e]Jxa
#[s]Jy
Jy[0][0] = J
Jy[0][1] = GP
Jy[0][2] = G
Jy[1][1] = J+K
Jy[1][2] = GP
Jy[2][2] = J
for cnt_i in range(0,3):
    for cnt_j in range(cnt_i,3):
        Jy[cnt_j][cnt_i] = Jy[cnt_i][cnt_j]
#print(Jy)
#[e]Jy
#[s]Jz
Jz[0][0] = J
Jz[0][1] = G
Jz[0][2] = GP
Jz[1][1] = J
Jz[1][2] = GP
Jz[2][2] = J+K
for cnt_i in range(0,3):
    for cnt_j in range(cnt_i,3):
        Jz[cnt_j][cnt_i] = Jz[cnt_i][cnt_j]
#print(Jz)
#[e]Jz
#[s]all_J
for cnt in range(0,3):
    if cnt == 0:
        tmp_J =copy.deepcopy(Jx)
    elif cnt == 1:
        tmp_J =copy.deepcopy(Jy)
    elif cnt == 2:
        tmp_J =copy.deepcopy(Jz)
    for cnt_i in range(0,3):
        for cnt_j in range(0,3):
            all_J[cnt][cnt_i][cnt_j] = tmp_J[cnt_i][cnt_j]
#print(all_J)
#[e]all_J
#[s] get temperature
inv_temp = np.zeros([max_set,max_eigen],dtype=np.float)
ene      = np.zeros([max_set,max_eigen],dtype=np.float)
ene2     = np.zeros([max_set,max_eigen],dtype=np.float)
for cnt_set in range(0,max_set):
    print("read SS",cnt_set)
    file_name  = "output/SS_rand{}.dat".format(cnt_set)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        #print(len(data))
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
tmp_sdt  = "green2.txt"
tmp_num   = read.func_count(tmp_sdt)
print('tmp_num=',tmp_num)
in_G2siteI  = np.zeros([tmp_num],dtype=np.int)
in_G2spinI  = np.zeros([tmp_num],dtype=np.unicode)
in_G2siteJ  = np.zeros([tmp_num],dtype=np.int)
in_G2spinJ  = np.zeros([tmp_num],dtype=np.unicode)
in_Int0     = np.zeros([tmp_num],dtype=np.float)
in_Int1     = np.zeros([tmp_num],dtype=np.float)
in_sign     = np.zeros([tmp_num],dtype=np.float)
val         = np.zeros([tmp_num],dtype=np.complex)
all_val2    = np.zeros([tmp_num,3,tmp_num,3],dtype=np.complex)
read.func_green2(tmp_sdt,in_G2siteI,in_G2spinI,in_G2siteJ,in_G2spinJ,in_Int0,in_Int1,in_sign)
#
#
for cnt_set in range(0,max_set):
    print("read & write 2body",cnt_set)
    with open("%s/all_2_set%d.dat" % (dir_Phys,cnt_set) , 'w') as f:
        print(" # ", file=f)
    #
    for cnt_eigen in range(0,max_eigen,dstep):
        if inv_temp[cnt_set][cnt_eigen] < 1e-8:
            temp     = 1e10
        else:
            temp     = 1.0/inv_temp[cnt_set][cnt_eigen]
        tmp_ene  = ene[cnt_set][cnt_eigen]
        spc_heat = (ene2[cnt_set][cnt_eigen]-tmp_ene*tmp_ene)*inv_temp[cnt_set][cnt_eigen]*inv_temp[cnt_set][cnt_eigen]
        #print("2-body ",cnt_eigen)
        tmp_sdt  = "output/zvo_cisajscktalt_set%dstep%d.dat" % (cnt_set,cnt_eigen)
        read.val_green2(tmp_sdt,in_G2spinI,in_G2spinJ,val)
        for tot_cnt in range(0,tmp_num):
            siteI =in_G2siteI[tot_cnt]
            siteJ =in_G2siteJ[tot_cnt]
            spinI =dict_spin[in_G2spinI[tot_cnt]]
            spinJ =dict_spin[in_G2spinJ[tot_cnt]]
            #print(siteI,siteJ,spinI,spinJ,val[tot_cnt])
            all_val2[siteI][spinI][siteJ][spinJ] = val[tot_cnt]
        #
        for tmp_cnt in range(0,int(Lx/2)):
            for i_spin in range(0,3):
                tmp_site_i              = Phys_2_site_i[i_spin][tmp_cnt]
                tmp_site_j              = Phys_2_site_j[i_spin][tmp_cnt]
                tmp_spin                = Phys_2_spin[i_spin][tmp_cnt]
                #print(tmp_cnt,tmp_site_i,tmp_site_j,tmp_spin)
                Thermal_Phys_2[i_spin][tmp_cnt] = CalcLM.func_calc2(flag,LeviCivita,all_J,all_h,all_val2,dict_spin,tmp_site_i,tmp_site_j,tmp_spin)
        with open("%s/all_2_set%d.dat" % (dir_Phys,cnt_set) , 'a') as f:
            print(" %12.8f %12.8f %12.8f " % (temp,tmp_ene,spc_heat),end="", file=f)
            for tmp_cnt in range(0,int(Lx/2)):
                for i_spin in range(0,3):
                    print(" %12.8f " % (np.real(Thermal_Phys_2[i_spin][tmp_cnt])),end = "", file=f)
            print(" ",file=f)
    #
#hphi_io.val_g3("./{}/".format(dir_Phys)+"out_green3.dat",G3siteI,G3spinI,G3siteJ,G3spinJ,G3siteK,G3spinK)
#
tmp_sdt  = "green3.txt"
tmp_num   = read.func_count(tmp_sdt)
print('tmp_num=',tmp_num)
in_G3siteI  = np.zeros([tmp_num],dtype=np.int)
in_G3spinI  = np.zeros([tmp_num],dtype=np.unicode)
in_G3siteJ  = np.zeros([tmp_num],dtype=np.int)
in_G3spinJ  = np.zeros([tmp_num],dtype=np.unicode)
in_G3siteK  = np.zeros([tmp_num],dtype=np.int)
in_G3spinK  = np.zeros([tmp_num],dtype=np.unicode)
in_Int0     = np.zeros([tmp_num],dtype=np.float)
in_Int1     = np.zeros([tmp_num],dtype=np.float)
in_sign     = np.zeros([tmp_num],dtype=np.float)
val         = np.zeros([tmp_num],dtype=np.complex)
all_val3    = np.zeros([tmp_num,3,tmp_num,3,tmp_num,3],dtype=np.complex)
read.func_green3(tmp_sdt,in_G3siteI,in_G3spinI,in_G3siteJ,in_G3spinJ,in_G3siteK,in_G3spinK,in_Int0,in_Int1,in_sign)
#
for cnt_set in range(0,max_set):
    print("read & write 3body",cnt_set)
    with open("%s/all_3_set%d.dat"%(dir_Phys,cnt_set) , 'w') as f:
        print(" # ", file=f)
        for cnt_eigen in range(0,max_eigen,dstep):
            if inv_temp[cnt_set][cnt_eigen] < 1e-8:
                temp     = 1e10
            else:
                temp     = 1.0/inv_temp[cnt_set][cnt_eigen]
            tmp_ene      = ene[cnt_set][cnt_eigen]
            spc_heat = (ene2[cnt_set][cnt_eigen]-tmp_ene*tmp_ene)*inv_temp[cnt_set][cnt_eigen]*inv_temp[cnt_set][cnt_eigen]
            #print("3-body ",cnt_eigen)
            tmp_sdt  = "output/zvo_ThreeBody_set%dstep%d.dat" % (cnt_set,cnt_eigen)
            read.val_green3(tmp_sdt,in_G3spinI,in_G3spinJ,in_G3spinK,val)
            for tot_cnt in range(0,tmp_num):
                siteI = in_G3siteI[tot_cnt]
                siteJ = in_G3siteJ[tot_cnt]
                siteK = in_G3siteK[tot_cnt]
                spinI = dict_spin[in_G3spinI[tot_cnt]]
                spinJ = dict_spin[in_G3spinJ[tot_cnt]]
                spinK = dict_spin[in_G3spinK[tot_cnt]]
                all_val3[siteI][spinI][siteJ][spinJ][siteK][spinK] =  val[tot_cnt]
                #print(siteI,siteJ,siteK,spinI,spinK,spinK,val[tot_cnt])
            #
            for tmp_cnt in range(0,int(Lx/2)):
                for i_L in range(0,6):
                    tmp_site_i              = Phys_3_site_i[i_L][tmp_cnt]
                    tmp_site_j              = Phys_3_site_j[i_L][tmp_cnt]
                    tmp_site_k              = Phys_3_site_k[i_L][tmp_cnt]
                    tmp_spin_0              = Phys_3_spin_0[i_L][tmp_cnt]
                    tmp_spin_1              = Phys_3_spin_1[i_L][tmp_cnt]
                    Thermal_Phys_3[i_L][tmp_cnt] \
                    = CalcLM.func_calc3(flag, LeviCivita,all_J,all_val3,dict_spin,tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1)
                    #print(tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1,Thermal_Phys_3[i_L][tmp_cnt])
            #
            with open("%s/all_3_set%d.dat" % (dir_Phys,cnt_set) , 'a') as f:
                print(" %12.8f %12.8f %12.8f " % (temp,tmp_ene,spc_heat),end="", file=f)
                for tmp_cnt in range(0,int(Lx/2)):
                    for i_L in range(0,6):
                        print(" %12.8f " % (np.real(Thermal_Phys_3[i_L][tmp_cnt])),end = "", file=f)
                print(" ",file=f)
            #
