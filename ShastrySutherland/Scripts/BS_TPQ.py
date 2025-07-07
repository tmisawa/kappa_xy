import numpy as np
import os
import copy
import sys
import math
import cmath
import random

def main():
    #[s] set modpara
    num_sample  = int(sys.argv[1]) 
    max_BS      = int(sys.argv[2]) 
    dir_Norm    = sys.argv[3] 
    max_eigen   = get_maxeigen("%s/TPQ_0.dat" % (dir_Norm))
    #
    max_set     = num_sample #int(dict_mod['NumAve']) 
    BS_sample   = num_sample
    #dstep     = int(dict_mod['ExpecInterval']) 
    #[e] set param.


    InvTemp      = np.zeros([max_set,max_eigen],dtype=np.float)
    ave_InvTemp  = np.zeros([max_eigen],dtype=np.float)
    err_InvTemp  = np.zeros([max_eigen],dtype=np.float)
    log_Z        = np.zeros([max_eigen],dtype=np.float)
    Z            = np.zeros([max_set,max_eigen],dtype=np.float)
    ave_Z        = np.zeros([max_eigen],dtype=np.float)
    Ene          = np.zeros([max_set,max_eigen],dtype=np.float)
    ave_Ene      = np.zeros([max_eigen],dtype=np.float)
    Ene2         = np.zeros([max_set,max_eigen],dtype=np.float)
    ave_Ene2     = np.zeros([max_eigen],dtype=np.float)
    #
    BS_Z         = np.zeros([max_BS,max_eigen],dtype=np.float)
    ave_BS_Z     = np.zeros([max_eigen],dtype=np.float)
    err_BS_Z     = np.zeros([max_eigen],dtype=np.float)
    BS_Ene       = np.zeros([max_BS,max_eigen],dtype=np.float)
    ave_BS_Ene   = np.zeros([max_eigen],dtype=np.float)
    err_BS_ene   = np.zeros([max_eigen],dtype=np.float)
    BS_Spc       = np.zeros([max_BS,max_eigen],dtype=np.float)
    ave_BS_Spc   = np.zeros([max_eigen],dtype=np.float)
    err_BS_Spc   = np.zeros([max_eigen],dtype=np.float)
    BS_Ent       = np.zeros([max_BS,max_eigen],dtype=np.float)
    ave_BS_Ent   = np.zeros([max_eigen],dtype=np.float)
    err_BS_Ent   = np.zeros([max_eigen],dtype=np.float)

    with open("%s/Norm.dat" %(dir_Norm)) as f:
        data      = f.read()
        data      = data.split("\n")
        #print(len(data))
        #[s] count not empty elements
        tmp       = data[1].split()
        org_log_Z = float(tmp[1])
        for i in range(0,len(data)):
            tmp_i              = i
            tmp                = data[i].split()
            #print(tmp)
            if len(tmp)>1: # if data[i] is not empty
                log_Z[tmp_i]      = float(tmp[1])-org_log_Z


    for cnt_set in range(0,max_set):
        with open("%s/TPQ_%d.dat" % (dir_Norm,cnt_set)) as f:
            data      = f.read()
            data      = data.split("\n")
            #print(len(data))
            #[s] count not empty elements
            for i in range(1,len(data)):
                tmp_i              = i-1
                tmp                = data[i].split()
                #print(tmp)
                if len(tmp)>1: # if data[i] is not empty
                    InvTemp[cnt_set][tmp_i]   = float(tmp[1])
                    Z[cnt_set][tmp_i]         = float(tmp[2])
                    Ene[cnt_set][tmp_i]       = float(tmp[3])
                    Ene2[cnt_set][tmp_i]      = float(tmp[4])

    ave_InvTemp = np.mean(InvTemp,axis=0)
    err_InvTemp = np.std(InvTemp,axis=0,ddof=1)
    ave_Z       = np.mean(Z,axis=0)
    ave_Ene     = np.mean(Ene,axis=0)
    ave_Ene2    = np.mean(Ene2,axis=0)
    #print(ave_Temp)
    #print(err_Temp)

    for set_BS in range(0,max_BS):
        print(set_BS)
        tmp_ent = 0.0
        for cnt in range(0,max_eigen-2):
            tmp_z    = 0.0
            tmp_ene  = 0.0
            tmp_ene2 = 0.0
            for cnt_BS in range(0,BS_sample):
                rand_set  = random.randrange(max_set)
                tmp_z    += Z[rand_set][cnt]
                tmp_ene  += Ene[rand_set][cnt]
                tmp_ene2 += Ene2[rand_set][cnt]
            #print(tmp_z)
            BS_Z[set_BS][cnt]    = tmp_z/BS_sample
            BS_Ene[set_BS][cnt]  = tmp_ene/tmp_z
            BS_Spc[set_BS][cnt]  = tmp_ene2/tmp_z-(tmp_ene/tmp_z)**2
            #print(cnt+1,InvTemp[0][cnt+1])
            #tmp_ent             += BS_Spc[set_BS][cnt]*(1-InvTemp[0][cnt]/InvTemp[0][cnt+1])*InvTemp[0][cnt]**2
            BS_Ent[set_BS][cnt]  = math.log(tmp_z/BS_sample)+tmp_ene/tmp_z*InvTemp[0][cnt]+log_Z[cnt]

    ave_BS_Z    = np.mean(BS_Z,axis=0)
    err_BS_Z    = np.std(BS_Z,axis=0,ddof=1)
    ave_BS_Ene  = np.mean(BS_Ene,axis=0)
    err_BS_Ene  = np.std(BS_Ene,axis=0,ddof=1)
    ave_BS_Spc  = np.mean(BS_Spc,axis=0)
    err_BS_Spc  = np.std(BS_Spc,axis=0,ddof=1)
    ave_BS_Ent  = np.mean(BS_Ent,axis=0)
    err_BS_Ent  = np.std(BS_Ent,axis=0,ddof=1)

    with open("BS_MaxBS%d.dat" % (max_BS), 'w') as f:
        for cnt in range(1,max_eigen-2):
            beta    = ave_InvTemp[cnt]
            Ene     = ave_BS_Ene[cnt]
            err_Ene = err_BS_Ene[cnt]
            Spc     = beta**2*ave_BS_Spc[cnt]
            err_Spc = beta**2*err_BS_Spc[cnt]
            Ent     = ave_BS_Ent[cnt]
            err_Ent = err_BS_Ent[cnt]
            #print(err_Ene,err_Spc)
            
            print(" %.16f  " % (1.0/ave_InvTemp[cnt]), end="", file=f)#1
            print(" %.16f  " % (err_InvTemp[cnt]), end="", file=f)#2
            print(" %.16f  " % (Ene), end="", file=f) #3
            print(" %.16f  " % (err_Ene), end="", file=f) #4
            print(" %.16f  " % (Spc), end="", file=f) #5
            print(" %.16f  " % (err_Spc), end="", file=f) #6
            print(" %.16f  " % (Ent), end="", file=f) #7
            print(" %.16f  " % (err_Ent), end="", file=f) #8
            print(" %.16f  " % (ave_BS_Z[cnt]), end="", file=f) #9
            print(" %.16f  " % (err_BS_Z[cnt]), end="", file=f) #10
            print(" ", file=f)

def get_maxeigen(in_file):
    with open("%s" % (in_file)) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
    return len(data)-1

if __name__ == "__main__":
    main()
