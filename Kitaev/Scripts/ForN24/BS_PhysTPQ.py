import numpy as np
import os
import copy
import math
import cmath
import random
import sys

def main(): 
    max_set    = int(sys.argv[1])
    max_BS     = int(sys.argv[2])
    dir_Phys   = sys.argv[3]
    header     = sys.argv[4]
    #[s] set modpara
    print(max_BS)
    BS_sample = max_set
    #dstep     = int(dict_mod['ExpecInterval']) 
    #[e] set param.
    Phys = read_phys(max_set,dir_Phys,header)
    max_eigen = Phys.shape[1]
    num_phys = Phys.shape[2]
    print("num_phys",num_phys)
    BS_Z         = np.zeros([max_BS,max_eigen],dtype=np.float)
    ave_BS_Z     = np.zeros([max_eigen],dtype=np.float)
    err_BS_Z     = np.zeros([max_eigen],dtype=np.float)
    BS_Phys      = np.zeros([max_BS,max_eigen,num_phys],dtype=np.float)
    ave_BS_Phys  = np.zeros([max_eigen,num_phys],dtype=np.float)
    err_BS_Phys  = np.zeros([max_eigen,num_phys],dtype=np.float)


    for set_BS in range(0,max_BS):
        print(set_BS)
        for cnt in range(0,max_eigen):
            tmp_z    = 0.0
            tmp_ene  = 0.0
            tmp_ene2 = 0.0
            tmp_phys     = np.zeros([num_phys],dtype=np.float)
            for cnt_BS in range(0,BS_sample):
                rand_set  = random.randrange(max_set)
                for cnt_phys in range(0,num_phys):
                    tmp_phys[cnt_phys]  += Phys[rand_set][cnt][cnt_phys]
            #print(tmp_z)
            tmp_z                = tmp_phys[1]
            BS_Z[set_BS][cnt]    = tmp_z/BS_sample
            for cnt_phys in range(0,num_phys):
                BS_Phys[set_BS][cnt][cnt_phys]  = tmp_phys[cnt_phys]/tmp_z

    ave_BS_Z    = np.mean(BS_Z,axis=0)
    err_BS_Z    = np.std(BS_Z,axis=0,ddof=1)
    ave_BS_Phys = np.mean(BS_Phys,axis=0)
    err_BS_Phys = np.std(BS_Phys,axis=0,ddof=1)

    print("num_phys=",num_phys)
    with open("Norm_%s_MaxBS%d.dat" % (header,max_BS), 'w') as f:
        for cnt in range(0,max_eigen-1):
            temp    = Phys[0][cnt][2]
            
            print(" %.16f  " % (temp), end="", file=f)#1
            for cnt_phys in range(3,num_phys):
                print(" %.16f  " % (ave_BS_Phys[cnt][cnt_phys]), end="", file=f)
                print(" %.16f  " % (err_BS_Phys[cnt][cnt_phys]), end="", file=f) 
            print(" %.16f  " % (ave_BS_Z[cnt]), end="", file=f) 
            print(" %.16f  " % (err_BS_Z[cnt]), end="", file=f) 
            print(" ", file=f)

    if header == "JE_tpq":
        with open("Norm_Kappa_MaxBS%d.dat" % (max_BS), 'w') as f:
            for cnt in range(0,max_eigen-1):
                temp    = Phys[0][cnt][2]
                
                print(" %.16f  " % (temp), end="", file=f)#1
                print(" %.16f  " % (ave_BS_Phys[cnt][10]), end="", file=f) #2 tot
                print(" %.16f  " % (err_BS_Phys[cnt][10]), end="", file=f) #3 tot
                print(" %.16f  " % (ave_BS_Phys[cnt][9]), end="", file=f)  #4 M
                print(" %.16f  " % (err_BS_Phys[cnt][9]), end="", file=f)  #5 M
                print(" %.16f  " % (ave_BS_Phys[cnt][8]), end="", file=f)  #6 L
                print(" %.16f  " % (err_BS_Phys[cnt][8]), end="", file=f)  #7 L
                print(" %.16f  " % (ave_BS_Z[cnt]), end="", file=f)  #8
                print(" %.16f  " % (err_BS_Z[cnt]), end="", file=f)  #9
                print(" ", file=f)


def read_phys(num_sample,dir_Phys,header):
    in_file = "%s/Norm_%s_set0.dat" % (dir_Phys,header)
    print(in_file)

    with open("%s" % (in_file)) as f:
        data      = f.read()
        data      = data.split("\n")
    num_step    = int(len(data)-2)
    tmp         = data[1].split()
    num_phys    = len(tmp)
    print(num_step)
    print(num_phys)
    print(tmp)
    Phys    = np.zeros([num_sample,num_step,num_phys],dtype=np.float)

    for cnt_samp in range(num_sample):
        in_file = "%s/Norm_%s_set%d.dat" % (dir_Phys,header,cnt_samp)
        with open("%s" % (in_file)) as f:
            data      = f.read()
            data      = data.split("\n")
            #print(len(data))
        for i in range(1,num_step+1):
            cnt        = i-1
            tmp        = data[i].split()
            for cnt_phys in range(len(tmp)):
                Phys[cnt_samp][cnt][cnt_phys]  = float(tmp[cnt_phys])
    return  Phys


if __name__ == "__main__":
    main()
