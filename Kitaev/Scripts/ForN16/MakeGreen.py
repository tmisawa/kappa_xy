import numpy as np
import os
import copy
import math
import cmath
import itertools
import CalcLM  #using CalcLM.py#
import toml
import sys

def main():
    #[s] tolm load
    input_file  = sys.argv[1]
    input_dict  = toml.load(input_file)
    #[e] tolm load
    #[s]define constants
    Kitaev       = float(input_dict["param"]["K"])  
    Gamma        = float(input_dict["param"]["G"])   
    GammaPR      = float(input_dict["param"]["GP"])  
    J            = float(input_dict["param"]["J"])  
    Lx           = int(input_dict["param"]["Lx"])  
    Ly           = int(input_dict["param"]["Ly"])  
    All_N        = Lx*Ly
 
    spin_flag      = list(range(3))
    spin_flag[0]   = 'x'
    spin_flag[1]   = 'y'
    spin_flag[2]   = 'z'
    #
    with open("green1.txt" , 'w') as f:
        for all_i in range(0,All_N):
            print(" %d %s 0 0 0" % (all_i,'x'), file=f)
            print(" %d %s 0 0 0" % (all_i,'z'), file=f)
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
    #
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

    with open("green6.txt" , 'w') as f:
        print(" %d %s %d %s %d %s %d %s %d %s %d %s 0 0 0" % (0,"z",1,"y",7,"x",6,"z",11,"y",5,"x"), file=f)
        print(" %d %s %d %s %d %s %d %s %d %s %d %s 0 0 0" % (2,"z",3,"y",9,"x",8,"z",7,"y",1,"x"), file=f)
        print(" %d %s %d %s %d %s %d %s %d %s %d %s 0 0 0" % (4,"z",5,"y",11,"x",10,"z",9,"y",3,"x"), file=f)
        print(" %d %s %d %s %d %s %d %s %d %s %d %s 0 0 0" % (7,"z",8,"y",14,"x",13,"z",12,"y",6,"x"), file=f)
        print(" %d %s %d %s %d %s %d %s %d %s %d %s 0 0 0" % (9,"z",10,"y",16,"x",15,"z",14,"y",8,"x"), file=f)
        print(" %d %s %d %s %d %s %d %s %d %s %d %s 0 0 0" % (11,"z",6,"y",12,"x",17,"z",16,"y",10,"x"), file=f)


if __name__ == "__main__":
    main()
