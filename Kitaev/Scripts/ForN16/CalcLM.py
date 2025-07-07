import numpy as np
import os
import copy
import math
import cmath
import itertools
#import read    #using read.py#
#import hphi_io #using hphi_io.py#

def trans(all_i,Lx,Ly,trans_x,trans_y):
    i_y   = all_i%Ly
    i_x   = int((all_i-i_y)/Ly)
    j_y   = (i_y+trans_y+Ly)%Ly
    j_x   = (i_x+trans_x+Lx)%Lx
    all_j = j_y+j_x*Ly
    return all_j
    
def func_MakeL0_0(ini_i,Lx,Ly):
    tmp_site_i = ini_i 
    tmp_site_j = trans(ini_i,Lx,Ly,0,1) 
    tmp_site_k = trans(ini_i,Lx,Ly,0,2)
    tmp_spin_0 = 'x'
    tmp_spin_1 = 'y'
    return tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1

def func_MakeL0_1(ini_i,Lx,Ly):
    tmp_site_i = ini_i 
    tmp_site_j = trans(ini_i,Lx,Ly,0,1) 
    tmp_site_k = trans(ini_i,Lx,Ly,0,2)
    tmp_spin_0 = 'y'
    tmp_spin_1 = 'x'
    return tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1

def func_MakeL1_0(ini_i,Lx,Ly):
    tmp_site_i = ini_i 
    tmp_site_j = trans(ini_i,Lx,Ly,0,1)
    tmp_site_k = trans(ini_i,Lx,Ly,1,1)
    tmp_spin_0 = 'x'
    tmp_spin_1 = 'z'
    return tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1

def func_MakeL1_1(ini_i,Lx,Ly):
    tmp_site_i = ini_i 
    tmp_site_j = trans(ini_i,Lx,Ly,-1,0) 
    tmp_site_k = trans(ini_i,Lx,Ly,-1,1)
    tmp_spin_0 = 'z'
    tmp_spin_1 = 'y'
    return tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1

def func_MakeL2_0(ini_i,Lx,Ly):
    tmp_site_i = ini_i 
    tmp_site_j = trans(ini_i,Lx,Ly,1,0)
    tmp_site_k = trans(ini_i,Lx,Ly,1,1)
    tmp_spin_0 = 'z'
    tmp_spin_1 = 'x'
    return tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1

def func_MakeL2_1(ini_i,Lx,Ly):
    tmp_site_i = ini_i 
    tmp_site_j = trans(ini_i,Lx,Ly,0,1)
    tmp_site_k = trans(ini_i,Lx,Ly,-1,1)
    tmp_spin_0 = 'y'
    tmp_spin_1 = 'z'
    return tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1

def func_calc3(flag,LeviCivita,all_J,all_val3,dict_spin,siteI,siteJ,siteK,spin0,spin1):
    int_spin0 = dict_spin[spin0]
    int_spin1 = dict_spin[spin1]
    tmp=0.0
    for a0, a1, b0, b1, c0 in itertools.product(flag, flag, flag, flag, flag):
        tmp_val  = all_val3[siteI][b0][siteJ][c0][siteK][b1]
        #print(tmp_val)
        tmp     += LeviCivita[a0][c0][a1] * tmp_val * all_J[int_spin0][a0][b0] * all_J[int_spin1][a1][b1]
    return tmp

def func_calc2(flag,LeviCivita,all_J,all_h,all_val2,dict_spin,siteI,siteJ,spin0):
    int_spin0 = dict_spin[spin0]
    tmp = 0.0
    for a0,b0,c0,c1 in itertools.product(flag,flag,flag,flag):
        tmp_val = all_val2[siteI][c1][siteJ][b0]-all_val2[siteI][b0][siteJ][c1]
        tmp    += LeviCivita[c0][a0][c1]*tmp_val*all_J[int_spin0][a0][b0]*all_h[c0]
    return tmp


