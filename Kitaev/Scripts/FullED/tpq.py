import numpy as np
import os
import copy
import math
import cmath
import read    #using read.py#
import hphi_io #using hphi_io.py#

max_tpq  = 100000
del_tpq  = 20
max_set  = 3
max_cnt  = int(max_tpq/del_tpq)-1

all_temp = np.zeros([max_set,max_cnt],dtype=np.float)
all_JE_R = np.zeros([max_set,max_cnt],dtype=np.float)
all_JE_I = np.zeros([max_set,max_cnt],dtype=np.float)
#
ave_temp = np.zeros([max_cnt],dtype=np.float)
ave_JE_R = np.zeros([max_set,max_cnt],dtype=np.float)
ave_JE_I = np.zeros([max_set,max_cnt],dtype=np.float)
#
err_temp = np.zeros([max_cnt],dtype=np.float)
err_JE_R = np.zeros([max_set,max_cnt],dtype=np.float)
err_JE_I = np.zeros([max_set,max_cnt],dtype=np.float)

#[s] green2
tmp_sdt  = "green2.txt"
tmp_num   = read.func_count(tmp_sdt)
num_g2    = tmp_num
print('tmp_num=',tmp_num)
in_G2siteI  = np.zeros([tmp_num],dtype=np.int)
in_G2spinI  = np.zeros([tmp_num],dtype=np.unicode)
in_G2siteJ  = np.zeros([tmp_num],dtype=np.int)
in_G2spinJ  = np.zeros([tmp_num],dtype=np.unicode)
in_G2_Int0     = np.zeros([tmp_num],dtype=np.float)
in_G2_Int1     = np.zeros([tmp_num],dtype=np.float)
in_G2_sign     = np.zeros([tmp_num],dtype=np.float)
read.func_green2(tmp_sdt,in_G2siteI,in_G2spinI,in_G2siteJ,in_G2spinJ,in_G2_Int0,in_G2_Int1,in_G2_sign)
#[e] green2
#[s] green3
tmp_sdt  = "green3.txt"
tmp_num   = read.func_count(tmp_sdt)
num_g3    = tmp_num
print('tmp_num=',tmp_num)
in_G3siteI  = np.zeros([tmp_num],dtype=np.int)
in_G3spinI  = np.zeros([tmp_num],dtype=np.unicode)
in_G3siteJ  = np.zeros([tmp_num],dtype=np.int)
in_G3spinJ  = np.zeros([tmp_num],dtype=np.unicode)
in_G3siteK  = np.zeros([tmp_num],dtype=np.int)
in_G3spinK  = np.zeros([tmp_num],dtype=np.unicode)
in_G3_Int0     = np.zeros([tmp_num],dtype=np.float)
in_G3_Int1     = np.zeros([tmp_num],dtype=np.float)
in_G3_sign     = np.zeros([tmp_num],dtype=np.float)
#val         = np.zeros([tmp_num],dtype=np.complex)
#x_val3      = np.zeros(max_tpq,dtype=np.complex)
read.func_green3(tmp_sdt,in_G3siteI,in_G3spinI,in_G3siteJ,in_G3spinJ,in_G3siteK,in_G3spinK,in_G3_Int0,in_G3_Int1,in_G3_sign)
#[e] green3


#[s]loop set
for int_set in range(0,max_set):
    #[s] get temperature
    inv_temp = np.zeros([max_tpq],dtype=np.float)
    tmp_sdt  = "output/SS_rand{}.dat".format(int_set)
    read.func_readSS(tmp_sdt,inv_temp,max_tpq)
    #[e] get temperature
    #
    val2         = np.zeros([num_g2],dtype=np.complex)
    x_val2      = np.zeros(max_tpq,dtype=np.complex)
    # 
    for cnt_eigen in range(0,max_tpq,del_tpq):
        tmp_sdt  = "output/zvo_cisajscktalt_set{}step{}.dat".format(int_set,cnt_eigen)
        print("cnt_eigen=",cnt_eigen)
        read.val_green2(tmp_sdt,in_G2spinI,in_G2spinJ,val2)
        tmp_val2 = 0.0
        for tot_cnt in range(0,num_g2):
            tmp_val2   += in_G2_Int0[tot_cnt]*in_G2_Int1[tot_cnt]*in_G2_sign[tot_cnt]*val2[tot_cnt]
        x_val2[cnt_eigen] = tmp_val2
        #print(tmp)
    #
    val3         = np.zeros([num_g3],dtype=np.complex)
    x_val3      = np.zeros(max_tpq,dtype=np.complex)
    #  
    for cnt_eigen in range(0,max_tpq,del_tpq):
        tmp_sdt  = "output/zvo_ThreeBody_set{}step{}.dat".format(int_set,cnt_eigen)
        print("cnt_eigen=",cnt_eigen)
        read.val_green3(tmp_sdt,in_G3spinI,in_G3spinJ,in_G3spinK,val3)
        tmp_val3         =  0.0
        for tot_cnt in range(0,num_g3):
            tmp_val3        +=  in_G3_Int0[tot_cnt]*in_G3_Int1[tot_cnt]*in_G3_sign[tot_cnt]*val3[tot_cnt]
        x_val3[cnt_eigen] = tmp_val3

    cnt      = 0 
    tmp_sdt  = "x_all_result_set{}.dat".format(int_set)
    f        = open(tmp_sdt, 'wt')
    for cnt_eigen in range(0,max_tpq,del_tpq):
        tmp   = x_val3[cnt_eigen]+x_val2[cnt_eigen]
        if cnt > 0:
           all_temp[int_set][cnt-1] = 1.0/inv_temp[cnt_eigen]
           all_JE_R[int_set][cnt-1]   = tmp.real
           all_JE_I[int_set][cnt-1]   = tmp.imag
        cnt                   += 1 
        f.write(" {0:.16f} ".format(inv_temp[cnt_eigen]) \
        +" {0:.16f}   ".format(tmp.real)   \
        +" {0:.16f}   ".format(tmp.imag)   \
        +" {0:.16f}   ".format(x_val2[cnt_eigen].real)   \
        +" {0:.16f}   ".format(x_val2[cnt_eigen].imag)   \
        +" {0:.16f}   ".format(x_val3[cnt_eigen].real)   \
        +" {0:.16f}   ".format(x_val3[cnt_eigen].imag)   \
        +" {0:8d}   ".format(cnt_eigen)   \
        +"\n")
    f.close()

tmp_sdt  = "TPQ_JE.dat"
f        = open(tmp_sdt, 'wt')
ave_JE_R   = np.average(all_JE_R,axis=0)
ave_JE_I   = np.average(all_JE_I,axis=0)
ave_temp   = np.average(all_temp,axis=0)
err_JE_R   = np.std(all_JE_R,axis=0,ddof=1)
err_JE_I   = np.std(all_JE_I,axis=0,ddof=1)
err_temp   = np.std(all_temp,axis=0,ddof=1)
for cnt in range(0,max_cnt):
    out_ave_temp = ave_temp[cnt]
    out_err_temp = err_temp[cnt]/math.sqrt(max_set)
    out_ave_JE_R = ave_JE_R[cnt]
    out_err_JE_R = err_JE_R[cnt]/math.sqrt(max_set)
    out_ave_JE_I = ave_JE_I[cnt]
    out_err_JE_I = err_JE_I[cnt]/math.sqrt(max_set)
    f.write(" {0:.16f} ".format(out_ave_temp) \
    +" {0:.16f}   ".format(out_err_temp)   \
    +" {0:.16f}   ".format(out_ave_JE_R)   \
    +" {0:.16f}   ".format(out_err_JE_R)   \
    +" {0:.16f}   ".format(out_ave_JE_I)   \
    +" {0:.16f}   ".format(out_err_JE_I)   \
    +"\n")
f.close()
