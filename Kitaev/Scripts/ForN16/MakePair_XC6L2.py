import numpy as np
import os
import copy
import math
import cmath
import read    #using read.py#
import hphi_io #using hphi_io.py#

num_site  =  24
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
IntType[4][5]     = "x"
IntType[6][11]    = "x"
IntType[7][8]     = "x"
IntType[9][10]    = "x"
IntType[12][13]   = "x"
IntType[14][15]   = "x"
IntType[16][17]   = "x"
IntType[18][23]   = "x"
IntType[19][20]   = "x"
IntType[21][22]   = "x"
# y bond
IntType[0][5]    = "y"
IntType[1][2]    = "y"
IntType[3][4]    = "y"
IntType[6][7]    = "y"
IntType[8][9]    = "y"
IntType[10][11]  = "y"
IntType[12][17]  = "y"
IntType[13][14]  = "y"
IntType[15][16]  = "y"
IntType[18][19]  = "y"
IntType[20][21]  = "y"
IntType[22][23]  = "y"
# z bond
IntType[1][7]    = "z"
IntType[3][9]    = "z"
IntType[5][11]   = "z"
IntType[6][12]   = "z"
IntType[8][14]   = "z"
IntType[10][16]  = "z"
IntType[13][19]  = "z"
IntType[15][21]  = "z"
IntType[17][23]  = "z"
#IntType[0][18]  = "z" #for periodic
#IntType[2][20]  = "z" #for periodic
#IntType[4][22]  = "z" #for periodic
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
