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
    J      = float(input_dict["param"]["J"])  
    Jp     = float(input_dict["param"]["Jp"])   
    D      = float(input_dict["param"]["D"])  
    Dp_x   = float(input_dict["param"]["Dp_x"])  
    Dp_y   = float(input_dict["param"]["Dp_y"])  
    Dp_z   = float(input_dict["param"]["Dp_z"])  
    Lx           = int(input_dict["param"]["Lx"])  
    Ly           = int(input_dict["param"]["Ly"])  
    orb_num      = int(input_dict["param"]["orb_num"])  
    All_N        = Lx*Ly*orb_num
 
    spin_flag      = list(range(3))
    spin_flag[0]   = 'x'
    spin_flag[1]   = 'y'
    spin_flag[2]   = 'z'
    #
    with open("green1.txt" , 'w') as f:
        for all_i in range(0,All_N):
            print(" %d %s 0 0 0" % (all_i,'x'), file=f)
            print(" %d %s 0 0 0" % (all_i,'z'), file=f)
    #[s] def Phys_2
    Phys_2_site_i    = np.zeros([10],dtype=np.int)
    Phys_2_site_j    = np.zeros([10],dtype=np.int)
    Phys_2_site_i[0] = 0
    Phys_2_site_j[0] = 1
    # 
    Phys_2_site_i[1] = 0
    Phys_2_site_j[1] = 2
    #
    Phys_2_site_i[2] = 1
    Phys_2_site_j[2] = 8
    # 
    Phys_2_site_i[3] = 1
    Phys_2_site_j[3] = 9
    #
    Phys_2_site_i[4] = 1
    Phys_2_site_j[4] = 2
    #
    Phys_2_site_i[5] = 2
    Phys_2_site_j[5] = 3
    #
    Phys_2_site_i[6] = 2
    Phys_2_site_j[6] = 10
    #
    Phys_2_site_i[7] = 3
    Phys_2_site_j[8] = 10
    #
    Phys_2_site_i[8] = 3
    Phys_2_site_j[8] = 4
    #
    Phys_2_site_i[9] = 3
    Phys_2_site_j[9] = 5
    #[e] def Phys_2
    with open("Phys2.txt" , 'w') as f:
        for all_i in range(len(Phys_2_site_i)):
            print(" %d %d " % (Phys_2_site_i[all_i],Phys_2_site_j[all_i]), file=f)

    with open("green2.txt" , 'w') as f:
        #[s] for conventional Sq
        for all_i in range(0,All_N):
            for all_j in range(0,All_N):
                print(" %d %s %d %s 0 0 0" % (all_i,'x',all_j,'x'), file=f)
                print(" %d %s %d %s 0 0 0" % (all_i,'y',all_j,'y'), file=f)
                print(" %d %s %d %s 0 0 0" % (all_i,'z',all_j,'z'), file=f)
        #[e] for conventional Sq
        for all_i in range(len(Phys_2_site_i)):
            site_i = Phys_2_site_i[all_i]
            site_j = Phys_2_site_j[all_i]
            for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
                print(" %d %s %d %s 0 0 0" % (site_i,a0,site_j,a1), file=f)
            #
    #[s] def Phys_3
    Phys_3_site_i    = np.zeros([8],dtype=np.int)
    Phys_3_site_j    = np.zeros([8],dtype=np.int)
    Phys_3_site_k    = np.zeros([8],dtype=np.int)
    #
    Phys_3_site_i[0] = 0
    Phys_3_site_j[0] = 1
    Phys_3_site_k[0] = 2
    # 
    Phys_3_site_i[1] = 0
    Phys_3_site_j[1] = 2
    Phys_3_site_k[1] = 3
    #
    Phys_3_site_i[2] = 1
    Phys_3_site_j[2] = 2
    Phys_3_site_k[2] = 3
    #
    Phys_3_site_i[3] = 2
    Phys_3_site_j[3] = 3
    Phys_3_site_k[3] = 4
    #
    Phys_3_site_i[4] = 2
    Phys_3_site_j[4] = 3
    Phys_3_site_k[4] = 5
    #
    Phys_3_site_i[5] = 3
    Phys_3_site_j[5] = 4
    Phys_3_site_k[5] = 5
    #
    Phys_3_site_i[6] = 3
    Phys_3_site_j[6] = 4
    Phys_3_site_k[6] = 6
    #
    Phys_3_site_i[7] = 3
    Phys_3_site_j[7] = 5
    Phys_3_site_k[7] = 6
    #[e] def Phys_2
    with open("Phys3.txt" , 'w') as f:
        for all_i in range(len(Phys_3_site_i)):
            print(" %d %d %d " % (Phys_3_site_i[all_i],Phys_3_site_j[all_i],Phys_3_site_k[all_i]), file=f)
    #
    with open("green3.txt" , 'w') as f:
        for all_i in range(len(Phys_3_site_i)):
            site_i = Phys_3_site_i[all_i]
            site_j = Phys_3_site_j[all_i]
            site_k = Phys_3_site_k[all_i]
            for a0,a1,a2 in itertools.product(spin_flag,spin_flag,spin_flag):
                print(" %d %s %d %s %d %s 0 0 0" % (site_i,a0,site_j,a1,site_k,a2), file=f)
 


if __name__ == "__main__":
    main()
