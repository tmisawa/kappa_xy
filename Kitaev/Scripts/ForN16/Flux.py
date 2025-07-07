import numpy as np
import os
import copy
import math
import cmath
import read    #using read.py#
import hphi_io #using hphi_io.py#

max_eigen   = 8 #int(1980/20)
tmp_sdt  = "green6.txt"
tmp_num   = read.func_count(tmp_sdt)
print('tmp_num=',tmp_num)
in_G6site0  = np.zeros([tmp_num],dtype=np.int)
in_G6spin0  = np.zeros([tmp_num],dtype=np.unicode)
in_G6site1  = np.zeros([tmp_num],dtype=np.int)
in_G6spin1  = np.zeros([tmp_num],dtype=np.unicode)
in_G6site2  = np.zeros([tmp_num],dtype=np.int)
in_G6spin2  = np.zeros([tmp_num],dtype=np.unicode)
in_G6site3  = np.zeros([tmp_num],dtype=np.int)
in_G6spin3  = np.zeros([tmp_num],dtype=np.unicode)
in_G6site4  = np.zeros([tmp_num],dtype=np.int)
in_G6spin4  = np.zeros([tmp_num],dtype=np.unicode)
in_G6site5  = np.zeros([tmp_num],dtype=np.int)
in_G6spin5  = np.zeros([tmp_num],dtype=np.unicode)
in_G6Int0   = np.zeros([tmp_num],dtype=np.float)
in_G6Int1   = np.zeros([tmp_num],dtype=np.float)
in_G6sign   = np.zeros([tmp_num],dtype=np.float)
val         = np.zeros([tmp_num],dtype=np.complex)
read.func_green6(tmp_sdt,in_G6site0,in_G6spin0,in_G6site1,in_G6spin1,in_G6site2,in_G6spin2,in_G6site3,in_G6spin3,in_G6site4,in_G6spin4,in_G6site5,in_G6spin5,in_G6Int0,in_G6Int1,in_G6sign)
#
for cnt_eigen in range(0,max_eigen):
    tmp_sdt  = "output/zvo_SixBody_eigen{}.dat".format(cnt_eigen)
    print(cnt_eigen,tmp_sdt)
    read.val_green6(tmp_sdt,in_G6spin0,in_G6spin1,in_G6spin2,in_G6spin3,in_G6spin4,in_G6spin5,val)
    #val = val*64.0
    print(val.real,val.imag)
    #tmp_val2 = 0.0
    #for tot_cnt in range(0,tmp_num):
    #    tmp_val2   += in_Int0[tot_cnt]*in_Int1[tot_cnt]*in_sign[tot_cnt]*val[tot_cnt]
    #val2[cnt_eigen] = tmp_val2
#
#
#hphi_io.val_g3("./{}/".format(output_dir)+"out_green3.dat",G3siteI,G3spinI,G3siteJ,G3spinJ,G3siteK,G3spinK)
f        = open("all_result.dat", 'wt')
for cnt_eigen in range(0,max_eigen):
    #tmp_sdt  = "output/zvo_cisajscktalt_eigen{}.dat".format(cnt_eigen)
    tmp_sdt  = "output/zvo_SixBody_eigen{}.dat".format(cnt_eigen)
    read.val_green6(tmp_sdt,in_G6spin0,in_G6spin1,in_G6spin2,in_G6spin3,in_G6spin4,in_G6spin5,val)
    #val = val*64.0
    f.write(" {0:8d} ".format(cnt_eigen) \
    +" {0:.16f}   ".format(val[0].real)   \
    +" {0:.16f}   ".format(val[0].imag)   \
    +" {0:.16f}   ".format(val[1].real)   \
    +" {0:.16f}   ".format(val[1].imag)   \
    +" {0:.16f}   ".format(val[2].real)   \
    +" {0:.16f}   ".format(val[2].imag)   \
    +" {0:.16f}   ".format(val[3].real)   \
    +" {0:.16f}   ".format(val[3].imag)   \
    +" {0:.16f}   ".format(val[4].real)   \
    +" {0:.16f}   ".format(val[4].imag)   \
    +" {0:.16f}   ".format(val[5].real)   \
    +" {0:.16f}   ".format(val[5].imag)   \
    +"\n")
    tmp = (val[0].real+val[1].real+val[2].real+val[3].real)/4.0
    print(tmp)
f.close()

