import numpy as np
import os
import copy
import math
import cmath
import toml
import sys
import itertools

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
    IntType      = XC6L2_MakeIntType(All_N,"open")

    with open("pair.txt", 'w') as f:
        flag   = list(range(All_N))    
        cnt_x  = 0
        cnt_y  = 0
        cnt_z  = 0
        for cnt_i,cnt_j in itertools.product(flag,flag):
            if IntType[cnt_i][cnt_j] == "x":
                cnt_x+=1 
                # xx
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","x",Kitaev+J),file=f)
                # yy
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"y","y",J),file=f)
                # zz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"z","z",J),file=f)
                # xy
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","y",GammaPR),file=f)
                # xz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","z",GammaPR),file=f)
                # yz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"y","z",Gamma),file=f)
            if IntType[cnt_i][cnt_j] == "y":
                cnt_y+=1 
                # xx
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","x",J),file=f)
                # yy
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"y","y",Kitaev+J),file=f)
                # zz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"z","z",J),file=f)
                # xy
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","y",GammaPR),file=f)
                # xz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","z",Gamma),file=f)
                # yz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"y","z",GammaPR),file=f)
            if IntType[cnt_i][cnt_j] == "z":
                cnt_z+=1 
                # xx
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","x",J),file=f)
                # yy
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"y","y",J),file=f)
                # zz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"z","z",Kitaev+J),file=f)
                # xy
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","y",Gamma),file=f)
                # xz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"x","z",GammaPR),file=f)
                # yz
                print("  %8d %8d %s %s %.12f "%(cnt_i,cnt_j,"y","z",GammaPR),file=f)
        print("  x bond= %d, y bond= %d, z bond= %d " %(cnt_x,cnt_y,cnt_z))

def XC6L2_MakeIntType(All_N,boundary):
    print("  check: XC6L2, boundary=%s" % (boundary))
    IntType   = np.zeros([All_N,All_N],dtype=np.unicode)
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
    if boundary == "periodic":
        IntType[0][18]  = "z" #for periodic
        IntType[2][20]  = "z" #for periodic
        IntType[4][22]  = "z" #for periodic
    return IntType

def XC4L3_MakeIntType(All_N,boundary):
    print("  check: XC4L3, boundary=%s" % (boundary))
    IntType   = np.zeros([All_N,All_N],dtype=np.unicode)
    # x bond
    IntType[0][1]     = "x"
    IntType[2][3]     = "x"
    IntType[5][6]     = "x"
    IntType[4][7]     = "x"
    IntType[8][9]     = "x"
    IntType[10][11]   = "x"
    IntType[13][14]   = "x"
    IntType[12][15]   = "x"
    IntType[16][17]   = "x"
    IntType[18][19]   = "x"
    IntType[20][23]   = "x"
    IntType[21][22]   = "x"
    # y bond
    IntType[1][2]    = "y"
    IntType[0][3]    = "y"
    IntType[4][5]    = "y"
    IntType[6][7]    = "y"
    IntType[9][10]   = "y"
    IntType[8][11]   = "y"
    IntType[12][13]  = "y"
    IntType[14][15]  = "y"
    IntType[16][19]  = "y"
    IntType[17][18]  = "y"
    IntType[20][21]  = "y"
    IntType[22][23]  = "y"
    # z bond
    IntType[1][5]    = "z"
    IntType[3][7]    = "z"
    IntType[4][8]    = "z"
    IntType[6][10]   = "z"
    IntType[9][13]   = "z"
    IntType[11][15]  = "z"
    IntType[12][16]  = "z"
    IntType[14][18]  = "z"
    IntType[17][21]  = "z"
    IntType[19][23]  = "z"
    if boundary == "periodic":
        IntType[0][20]   = "z" #for periodic  
        IntType[2][22]   = "z" #for periodic
    return IntType

def XC4L2_MakeIntType(All_N,boundary):
    print("  check: XC4L2, boundary=%s" % (boundary))
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
    if boundary == "periodic":
        IntType[0][12]   = "z" #for periodic
        IntType[2][14]   = "z" #for periodic
    return IntType

if __name__ == "__main__":
    main()