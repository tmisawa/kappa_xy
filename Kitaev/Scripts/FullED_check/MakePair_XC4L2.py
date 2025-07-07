import numpy as np
import os
import copy
import math
import cmath
import read    #using read.py#
import hphi_io #using hphi_io.py#

num_site  =  16
#[s] set param.
list_param =['K','J','G','GP','h'] # list for int. parameters
dict_param = read.func_param(list_param)     # read param.txt
print(dict_param['K'])
print(dict_param['G'])
print(dict_param['GP'])
print(dict_param['J'])
print(dict_param['h'])
Kitaev    =  float(dict_param['K'])
Gamma     =  float(dict_param['G'])
GammaPR   =  float(dict_param['GP'])
J         =  float(dict_param['J'])
#[e] set param.

IntType   = np.zeros([num_site,num_site],dtype=np.unicode)
# x bond
IntType[0][1]     = "x"
IntType[2][3]     = "x"
IntType[5][6]     = "x"
IntType[4][7]     = "x"
IntType[8][9]     = "x"
IntType[10][11]   = "x"
IntType[13][14]   = "x"
IntType[12][15]   = "x"
# y bond
IntType[1][2]    = "y"
IntType[0][3]    = "y"
IntType[4][5]    = "y"
IntType[6][7]    = "y"
IntType[9][10]   = "y"
IntType[8][11]   = "y"
IntType[12][13]  = "y"
IntType[14][15]  = "y"
# z bond
IntType[1][5]    = "z"
IntType[3][7]    = "z"
IntType[4][8]    = "z"
IntType[6][10]   = "z"
IntType[9][13]   = "z"
IntType[11][15]  = "z"
#IntType[0][12]   = "z" #for periodic
#IntType[2][14]   = "z" #for periodic
#print(IntType)

f        = open("pair.txt", 'wt')
for cnt_i in range(num_site):
    for cnt_j in range(num_site):
        if len(IntType[cnt_i][cnt_j])>0:
            if IntType[cnt_i][cnt_j] == "x":
                # xx
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" x "+" {} ".format(Kitaev+J)+"\n")
                # yy
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" y "+" y "+" {} ".format(J)+"\n")
                # zz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" z "+" z "+" {} ".format(J)+"\n")
                # xy
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" y "+" {} ".format(GammaPR)+"\n")
                # xz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" z "+" {} ".format(GammaPR)+"\n")
                # yz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" y "+" z "+" {} ".format(Gamma)+"\n")
            if IntType[cnt_i][cnt_j] == "y":
                # xx
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" x "+" {} ".format(J)+"\n")
                # yy
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" y "+" y "+" {} ".format(Kitaev+J)+"\n")
                # zz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" z "+" z "+" {} ".format(J)+"\n")
                # xy
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" y "+" {} ".format(GammaPR)+"\n")
                # xz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" z "+" {} ".format(Gamma)+"\n")
                # yz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" y "+" z "+" {} ".format(GammaPR)+"\n")
            if IntType[cnt_i][cnt_j] == "z":
                # xx
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" x "+" {} ".format(J)+"\n")
                # yy
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" y "+" y "+" {} ".format(J)+"\n")
                # zz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" z "+" z "+" {} ".format(Kitaev+J)+"\n")
                # xy
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" y "+" {} ".format(Gamma)+"\n")
                # xz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" x "+" z "+" {} ".format(GammaPR)+"\n")
                # yz
                f.write("  {0:8d} ".format(cnt_i)
                        +" {0:8d} ".format(cnt_j)
                        +" y "+" z "+" {} ".format(GammaPR)+"\n")
