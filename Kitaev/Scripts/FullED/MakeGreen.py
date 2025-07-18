import numpy as np
import os
import copy
import math
import cmath
import itertools
#import read    #using read.py#
#import hphi_io #using hphi_io.py#
import CalcLM  #using CalcLM.py#

#[s] set param.
Lx        = 4
Ly        = 4  
max_site  = Lx*Ly
spin_flag      = list(range(3))
spin_flag[0]   = 'x'
spin_flag[1]   = 'y'
spin_flag[2]   = 'z'
#
with open("green2.txt" , 'w') as f:
    for i_x in range(0,int(Lx/2)):
        if i_x%2 == 0:
            all_i = i_x*Ly
        else:      
            all_i = CalcLM.trans(i_x*Ly,Lx,Ly,0,1)
        all_j = CalcLM.trans(all_i,Lx,Ly,0,1)
        all_k = CalcLM.trans(all_i,Lx,Ly,0,2)
        all_l = CalcLM.trans(all_i,Lx,Ly,1,0)
        all_m = CalcLM.trans(all_i,Lx,Ly,1,1)
        for a0,a1 in itertools.product(spin_flag,spin_flag):
            print(" %d %s %d %s 0 0 0" % (all_i,a0,all_j,a1), file=f)
        for a0,a1 in itertools.product(spin_flag,spin_flag):
            print(" %d %s %d %s 0 0 0" % (all_j,a0,all_k,a1), file=f)
        for a0,a1 in itertools.product(spin_flag,spin_flag):
            print(" %d %s %d %s 0 0 0" % (all_i,a0,all_l,a1), file=f)
        for a0,a1 in itertools.product(spin_flag,spin_flag):
            print(" %d %s %d %s 0 0 0" % (all_j,a0,all_m,a1), file=f)

with open("green3.txt" , 'w') as f:
    for i_x in range(0,int(Lx/2)):
        if i_x%2 == 0:
            ini_i = i_x*Ly
        else:
            ini_i = CalcLM.trans(i_x*Ly,Lx,Ly,0,1)
        # 
        tmp_i = ini_i
        tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1 = CalcLM.func_MakeL0_0(tmp_i,Lx,Ly)
        for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
            print(" %d %s %d %s %d %s 0 0 0" % (tmp_site_i,a0,tmp_site_j,a1,tmp_site_k,a2), file=f)
        #
        tmp_i = CalcLM.trans(ini_i,Lx,Ly,0,1)
        tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1 = CalcLM.func_MakeL0_1(tmp_i,Lx,Ly)
        for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
            print(" %d %s %d %s %d %s 0 0 0" % (tmp_site_i,a0,tmp_site_j,a1,tmp_site_k,a2), file=f)
        #
        tmp_i = ini_i
        tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1 = CalcLM.func_MakeL1_0(tmp_i,Lx,Ly)
        for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
            print(" %d %s %d %s %d %s 0 0 0" % (tmp_site_i,a0,tmp_site_j,a1,tmp_site_k,a2), file=f)
        #
        tmp_i = CalcLM.trans(ini_i,Lx,Ly,1,1)
        tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1 = CalcLM.func_MakeL1_1(tmp_i,Lx,Ly)
        for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
            print(" %d %s %d %s %d %s 0 0 0" % (tmp_site_i,a0,tmp_site_j,a1,tmp_site_k,a2), file=f)
        #
        tmp_i = CalcLM.trans(ini_i,Lx,Ly,0,1)
        tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1 = CalcLM.func_MakeL2_0(tmp_i,Lx,Ly)
        for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
            print(" %d %s %d %s %d %s 0 0 0" % (tmp_site_i,a0,tmp_site_j,a1,tmp_site_k,a2), file=f)
        #
        tmp_i = CalcLM.trans(ini_i,Lx,Ly,1,2)
        tmp_site_i,tmp_site_j,tmp_site_k,tmp_spin_0,tmp_spin_1 = CalcLM.func_MakeL2_1(tmp_i,Lx,Ly)
        for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
            print(" %d %s %d %s %d %s 0 0 0" % (tmp_site_i,a0,tmp_site_j,a1,tmp_site_k,a2), file=f)
