import numpy as np
import os
import copy
import math
import cmath
import sys
import read    #using read.py#
import hphi_io #using hphi_io.py#

max_site = 24
All_N    = max_site
#mag_h    = float(sys.argv[1])
#print(mag_h)
#mag_h    =  float(dict_param['h'])/math.sqrt(3.0)
cnt_name = "test"
output_dir = "dir_"+"{}".format(cnt_name)
os.makedirs(output_dir,exist_ok=True)
#[e] set param.
#

tmp_sdt  = "green6.txt"
tmp_num  = read.func_count(tmp_sdt)
print('tmp_num=',tmp_num)
G6site0  = np.zeros([tmp_num],dtype=np.int)
G6spin0  = np.zeros([tmp_num],dtype=np.unicode)
G6site1  = np.zeros([tmp_num],dtype=np.int)
G6spin1  = np.zeros([tmp_num],dtype=np.unicode)
G6site2  = np.zeros([tmp_num],dtype=np.int)
G6spin2  = np.zeros([tmp_num],dtype=np.unicode)
G6site3  = np.zeros([tmp_num],dtype=np.int)
G6spin3  = np.zeros([tmp_num],dtype=np.unicode)
G6site4  = np.zeros([tmp_num],dtype=np.int)
G6spin4  = np.zeros([tmp_num],dtype=np.unicode)
G6site5  = np.zeros([tmp_num],dtype=np.int)
G6spin5  = np.zeros([tmp_num],dtype=np.unicode)
G6Int0   = np.zeros([tmp_num],dtype=np.float)
G6Int1   = np.zeros([tmp_num],dtype=np.float)
G6sign   = np.zeros([tmp_num],dtype=np.float)
read.func_green6(tmp_sdt,G6site0,G6spin0,G6site1,G6spin1,G6site2,G6spin2,G6site3,G6spin3,G6site4,G6spin4,G6site5,G6spin5,G6Int0,G6Int1,G6sign)
hphi_io.func_g6("./{}/".format(output_dir)+"green6.def",G6site0,G6spin0,G6site1,G6spin1,G6site2,G6spin2,G6site3,G6spin3,G6site4,G6spin4,G6site5,G6spin5)
