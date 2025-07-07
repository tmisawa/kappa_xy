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

def main():
    #[s] set modpara
    #[s] tolm load
    input_file  = sys.argv[1]
    input_dict  = toml.load(input_file)
    #[e] tolm load
    #[s] set param.
    mag_h    = float(input_dict["param"]["mag_h"])  #NB sign is changed
    Lx       = int(input_dict["param"]["Lx"])  
    Ly       = int(input_dict["param"]["Ly"])  
    orb_num  = int(input_dict["param"]["orb_num"])  
    All_N    = Lx*Ly*orb_num
    max_site = Lx*Ly*orb_num
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
    all_h[0] = 0
    all_h[1] = 0
    all_h[2] = mag_h

    All_J  = np.zeros([All_N,All_N,3,3],dtype=np.float)
    dict_spin     = {'x':0,'y':1,'z':2}
    inv_dict_spin = {0:'x',1:'y',2:'z'}
    print(dict_spin)
    print(inv_dict_spin)
    with open('pair.txt') as f:
        data = f.read()
        data = data.split("\n")
        #print('check input',data)
        print(len(data))
    for i in data:
        tmp = i.split()
        if(len(tmp)>0):
            i_site  = int(tmp[0])
            j_site  = int(tmp[1])
            i_spin  = dict_spin[tmp[2]]
            j_spin  = dict_spin[tmp[3]]
            All_J[i_site][j_site][i_spin][j_spin] = float(tmp[4])
            All_J[j_site][i_site][j_spin][i_spin] = float(tmp[4])
            print(i_site,j_site,i_spin,j_spin)

    print(All_J[0][2])
    Thermal_Phys_3  = np.zeros([15],dtype=np.complex)

    #[s] Thermal_Phys_2 
    max_JE          = 1
    Thermal_Phys_2  = np.zeros([max_JE],dtype=np.complex)
    Phys_2_site_i   = np.zeros([max_JE],dtype=np.int)
    Phys_2_site_j   = np.zeros([max_JE],dtype=np.int)
    Phys_2_site_i[0]  = 2
    Phys_2_site_j[0]  = 3
    #[e] Thermal_Phys_2 
    #[s] Thermal_Phys_3 
    Thermal_Phys_3  = np.zeros([max_JE],dtype=np.complex)
    Phys_3_site_i   = np.zeros([max_JE],dtype=np.int)
    Phys_3_site_j   = np.zeros([max_JE],dtype=np.int)
    Phys_3_site_k   = np.zeros([max_JE],dtype=np.int)
    Phys_3_site_i[0]   = 2
    Phys_3_site_j[0]   = 3
    Phys_3_site_k[0]   = 4
    #[e] Thermal_Phys_3 

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
    all_val2    = np.zeros([All_N,3,All_N,3],dtype=np.complex)
    read.func_green2(tmp_sdt,in_G2siteI,in_G2spinI,in_G2siteJ,in_G2spinJ,in_Int0,in_Int1,in_sign)
    #
    
    max_eigen = 16
    dstep     = 1
    print("read & write 2body")
    with open("all_2.dat" , 'w') as f:
        print(" # ", file=f)
    for cnt_eigen in range(0,max_eigen,dstep):
        tmp_sdt  = "output/zvo_cisajscktalt_eigen%d.dat" % (cnt_eigen)
        read.val_green2(tmp_sdt,in_G2spinI,in_G2spinJ,val)
        for tot_cnt in range(0,tmp_num):
            siteI =in_G2siteI[tot_cnt]
            siteJ =in_G2siteJ[tot_cnt]
            spinI =dict_spin[in_G2spinI[tot_cnt]]
            spinJ =dict_spin[in_G2spinJ[tot_cnt]]
            #print(siteI,siteJ,spinI,spinJ,val[tot_cnt])
            all_val2[siteI][spinI][siteJ][spinJ] = val[tot_cnt]
        #
        for tmp_cnt in range(0,max_JE):
            tmp_site_i              = Phys_2_site_i[tmp_cnt]
            tmp_site_j              = Phys_2_site_j[tmp_cnt]
            #print(tmp_cnt,tmp_site_i,tmp_site_j,tmp_spin)
            Thermal_Phys_2[tmp_cnt] = CalcLM.func_calc2(flag,LeviCivita,All_J,all_h,all_val2,dict_spin,tmp_site_i,tmp_site_j)
        with open("all_2.dat" ,'a') as f:
            for tmp_cnt in range(0,max_JE):
                print(" %12.8f " % (np.real(Thermal_Phys_2[tmp_cnt])),end = "", file=f)
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
    all_val3    = np.zeros([All_N,3,All_N,3,All_N,3],dtype=np.complex)
    read.func_green3(tmp_sdt,in_G3siteI,in_G3spinI,in_G3siteJ,in_G3spinJ,in_G3siteK,in_G3spinK,in_Int0,in_Int1,in_sign)
    #
    print("read & write 3body")
    with open("all_3.dat" , 'w') as f:
        print(" # ", file=f)
    for cnt_eigen in range(0,max_eigen,dstep):
        tmp_sdt  = "output/zvo_ThreeBody_eigen%d.dat" % (cnt_eigen)
        read.val_green3(tmp_sdt,in_G3spinI,in_G3spinJ,in_G3spinK,val)
        for tot_cnt in range(0,tmp_num):
            siteI = in_G3siteI[tot_cnt]
            siteJ = in_G3siteJ[tot_cnt]
            siteK = in_G3siteK[tot_cnt]
            spinI = dict_spin[in_G3spinI[tot_cnt]]
            spinJ = dict_spin[in_G3spinJ[tot_cnt]]
            spinK = dict_spin[in_G3spinK[tot_cnt]]
            all_val3[siteI][spinI][siteJ][spinJ][siteK][spinK] =  val[tot_cnt]
            print(siteI,siteJ,siteK,spinI,spinJ,spinK,val[tot_cnt])
        #
        for tmp_cnt in range(0,max_JE):
            tmp_site_i              = Phys_3_site_i[tmp_cnt]
            tmp_site_j              = Phys_3_site_j[tmp_cnt]
            tmp_site_k              = Phys_3_site_k[tmp_cnt]
            Thermal_Phys_3[tmp_cnt] \
            = CalcLM.func_calc3(flag, LeviCivita,All_J,all_val3,dict_spin,tmp_site_i,tmp_site_j,tmp_site_k)
        #
        with open("all_3.dat" , 'a') as f:
            for tmp_cnt in range(0,max_JE):
                print(" %12.8f " % (np.real(Thermal_Phys_3[tmp_cnt])),end = "", file=f)
            print(" ",file=f)

if __name__ == "__main__":
    main()
