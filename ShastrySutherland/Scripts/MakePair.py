import numpy as np
import os
import copy
import math
import cmath
import toml
import sys
import itertools
import lattice

def main():
    #[s] tolm load
    input_file  = sys.argv[1]
    input_dict  = toml.load(input_file)
    #[e] tolm load
    #[s]define constants
    J       = float(input_dict["param"]["J"])  
    Jp      = float(input_dict["param"]["Jp"])   
    D       = float(input_dict["param"]["D"])  
    Dp_x    = float(input_dict["param"]["Dp_x"])  
    Dp_y    = float(input_dict["param"]["Dp_y"])  
    Dp_z    = float(input_dict["param"]["Dp_z"])  
    Lx      = int(input_dict["param"]["Lx"])  
    Ly      = int(input_dict["param"]["Ly"])  
    orb_num = int(input_dict["param"]["orb_num"])  
    BC      = input_dict["param"]["boundary"]
    All_N   = Lx*Ly*orb_num

    with open("pair.txt", 'w') as f:
        for all_i in range(All_N): #all_i = orb_i+orb_num*site_i, site_i=y_i+x_i*Ly
            x_i,y_i,orb_i = lattice.site2d_ymajor(all_i,Lx,Ly,orb_num)
            print(all_i,x_i,y_i,orb_i)
            if (x_i%2==0):
                all_x("even",all_i,orb_i,Lx,Ly,orb_num,J,Jp,D,Dp_x,Dp_y,Dp_z,f,BC)
            elif (x_i%2==1):
                all_x("odd",all_i,orb_i,Lx,Ly,orb_num,J,Jp,D,Dp_x,Dp_y,Dp_z,f,BC)

def print_Heisenberg(all_i,all_j,J_exc,f):
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"x","x",J_exc),file=f)
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"y","y",J_exc),file=f)
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"z","z",J_exc),file=f)

def print_DA(all_i,all_j,D,f):
    print("  %8d %8d %s %s %.12f "%(all_j,all_i,"x","z",D),file=f)
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"x","z",-D),file=f)
    # D_A = (0,D,0)
    # z_i*x_j-x_i*z_j = x_j*z_i-x_i*z_j

def print_DB(all_i,all_j,D,f):
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"y","z",-D),file=f)
    print("  %8d %8d %s %s %.12f "%(all_j,all_i,"y","z",D),file=f)
    # D_B = (-D,0,0)
    # y_i*z_j-z_i*y_j = y_i*z_j-y_j*z_j
    # NB: ncom (i,j)=(3,2) 

def print_Dp(all_i,all_j,Dp_x,Dp_y,Dp_z,f):
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"y","z",Dp_x),file=f)
    print("  %8d %8d %s %s %.12f "%(all_j,all_i,"y","z",-Dp_x),file=f)
    #
    print("  %8d %8d %s %s %.12f "%(all_j,all_i,"x","z",Dp_y),file=f)
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"x","z",-Dp_y),file=f)
    # z_i*x_j-x_i*z_j = x_j*z_i-x_i*z_j
    #
    print("  %8d %8d %s %s %.12f "%(all_i,all_j,"x","y",Dp_z),file=f)
    print("  %8d %8d %s %s %.12f "%(all_j,all_i,"x","y",-Dp_z),file=f)

def all_x(parity,all_i,orb_i,Lx,Ly,orb_num,J,Jp,D,Dp_x,Dp_y,Dp_z,f,BC):
    x_i,y_i,orb_i = lattice.site2d_ymajor(all_i,Lx,Ly,orb_num)
    if orb_i == 0:
        dx    = 0
        dy    = 0
        orb_j = 1
        all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
        print_Heisenberg(all_i,all_j,J,f)
        print_DA(all_i,all_j,D,f)
        #
        if parity=="even":
            dx    = 0
            dy    = 0
        elif parity=="odd":
            dx    = 0
            dy    = 1
        orb_j = 2
        all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
        print_Heisenberg(all_i,all_j,Jp,f)
        print_Dp(all_i,all_j,Dp_x,Dp_y,Dp_z,f)
        #
        if parity=="even":
            dx    = 0
            dy    = -1
        elif parity=="odd":
            dx    = 0
            dy    = 0
        orb_j = 3
        all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
        print_Heisenberg(all_i,all_j,Jp,f)
        print_Dp(all_i,all_j,-Dp_x,Dp_y,-Dp_z,f)
    if orb_i == 1:
        if x_i == (Lx-1) or BC == "open":
            print("open")
        else:
            dx    = 1
            dy    = 0
            orb_j = 2
            all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
            print_Heisenberg(all_i,all_j,Jp,f)
            print_Dp(all_j,all_i,-Dp_y,-Dp_x,-Dp_z,f)
            #
            dx    = 1
            dy    = 0
            orb_j = 3
            all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
            print_Heisenberg(all_i,all_j,Jp,f)
            print_Dp(all_j,all_i,Dp_y,-Dp_x,Dp_z,f)
    if orb_i == 2:
        dx    = 0
        dy    = 0
        orb_j = 3
        all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
        print_Heisenberg(all_i,all_j,J,f)
        #
        if parity=="even":
            dx    = 0
            dy    = 0
        elif parity=="odd":
            dx    = 0
            dy    = -1
        orb_j = 1
        all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
        print_Heisenberg(all_i,all_j,Jp,f)
        print_Dp(all_j,all_i,Dp_x,-Dp_y,-Dp_z,f)
        #
        if x_i == (Lx-1) or BC == "open":
            print("open")
        else:
            dx    = 1
            dy    = 0
            orb_j = 0
            all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
            print_Heisenberg(all_i,all_j,Jp,f)
            print_Dp(all_i,all_j,Dp_y,Dp_x,-Dp_z,f)
    if orb_i == 3:
        print_DB(all_i,all_j,D,f)
        if x_i == (Lx-1) or BC == "open":
            print("open")
        else:
            dx    = 1
            dy    = 0
            orb_j = 0
            all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
            print_Heisenberg(all_i,all_j,Jp,f)
            print_Dp(all_i,all_j,-Dp_y,Dp_x,Dp_z,f)
        #
        if parity=="even":
            dx    = 0
            dy    = 1
        elif parity=="odd":
            dx    = 0
            dy    = 0
        orb_j = 1
        all_j = lattice.get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num)
        print_Heisenberg(all_i,all_j,Jp,f)
        print_Dp(all_j,all_i,-Dp_x,-Dp_y,Dp_z,f)

if __name__ == "__main__":
    main()
