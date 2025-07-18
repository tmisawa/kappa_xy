import numpy as np
import os
import copy
import math
import cmath
import read    #using read.py#
import hphi_io #using hphi_io.py#

mag_h     = 0.03/math.sqrt(3.0)
Gamma     = 0.01
Kitaev    = -1.0
max_site  = 24
max_eigen = 50
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
val2        = np.zeros([max_eigen],dtype=np.complex)
read.func_green2(tmp_sdt,in_G2siteI,in_G2spinI,in_G2siteJ,in_G2spinJ,in_Int0,in_Int1,in_sign)
#
for cnt_eigen in range(0,max_eigen):
    tmp_sdt  = "output/zvo_cisajscktalt_eigen{}.dat".format(cnt_eigen)
    read.val_green2(tmp_sdt,in_G2spinI,in_G2spinJ,val)
    tmp_val2 = 0.0
    for tot_cnt in range(0,tmp_num):
        tmp_val2   += in_Int0[tot_cnt]*in_Int1[tot_cnt]*in_sign[tot_cnt]*val[tot_cnt]
    val2[cnt_eigen] = tmp_val2
#
#hphi_io.val_g3("./{}/".format(output_dir)+"out_green3.dat",G3siteI,G3spinI,G3siteJ,G3spinJ,G3siteK,G3spinK)



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
val3        = np.zeros([max_eigen],dtype=np.complex)
read.func_green3(tmp_sdt,in_G3siteI,in_G3spinI,in_G3siteJ,in_G3spinJ,in_G3siteK,in_G3spinK,in_Int0,in_Int1,in_sign)
#
for cnt_eigen in range(0,max_eigen):
    tmp_sdt  = "output/zvo_ThreeBody_eigen{}.dat".format(cnt_eigen)
    read.val_green3(tmp_sdt,in_G3spinI,in_G3spinJ,in_G3spinK,val)
    tmp_val3         =  0.0
    for tot_cnt in range(0,tmp_num):
        tmp_val3        +=  in_Int0[tot_cnt]*in_Int1[tot_cnt]*in_sign[tot_cnt]*val[tot_cnt]
    val3[cnt_eigen]  =  tmp_val3 
#
#hphi_io.val_g3("./{}/".format(output_dir)+"out_green3.dat",G3siteI,G3spinI,G3siteJ,G3spinJ,G3siteK,G3spinK)
f        = open("all_result.dat", 'wt')
for cnt_eigen in range(0,max_eigen):
    tmp      = val3[cnt_eigen]+val2[cnt_eigen]
    f.write(" {0:8d} ".format(cnt_eigen) \
      +" {0:.16f}   ".format(tmp.real)   \
      +" {0:.16f}   ".format(tmp.imag)   \
      +" {0:.16f}   ".format(val3[cnt_eigen].real)   \
      +" {0:.16f}   ".format(val3[cnt_eigen].imag)   \
      +" {0:.16f}   ".format(val2[cnt_eigen].real)   \
      +" {0:.16f}   ".format(val2[cnt_eigen].imag)   \
      +"\n")
f.close()


