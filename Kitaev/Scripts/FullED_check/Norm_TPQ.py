import numpy as np
import os
import copy
import math
import cmath
import sys

def main():
    num_sample = int(sys.argv[1])
    dir_Norm = sys.argv[2]
    tpq_type = sys.argv[3]
    Norm,Temp,Ene,Ene2=read_file(num_sample)
    num_step    =  Norm.shape[1]
    #print(Norm.shape[0],Norm.shape[1])
    #print(Norm[0][9999])
    #print(Ene[0][9999])

    for cnt in range(num_sample):
        with open("%s/TPQ_%d.dat" % (dir_Norm,cnt),'w') as f:
            print("#  beta ene ene2",file=f )

        #alpha,b,c                  = make_weight(Norm,beta,Ns,large_value)
    phys_Z,phys_Ene,phys_Ene2,phys_Temp  = CalcPhys(Norm,Ene,Ene2,Temp,tpq_type)
    #[s] numpy ave
    #[e] numpy ave
    for cnt in range(num_sample):
        print(cnt)
        with open("%s/TPQ_%d.dat" % (dir_Norm,cnt),'a') as f2:
            for k in range(0,num_step-1):
                 print("%d %.12f %.12f %.12f %.12f " % (k,phys_Temp[cnt][k],phys_Z[cnt][k],phys_Ene[cnt][k],phys_Ene2[cnt][k]),file=f2)
        

def read_file(num_sample):
    in_file = "output/Norm_rand0.dat"
    print(in_file)

    with open("%s" % (in_file)) as f:
        data      = f.read()
        data      = data.split("\n")
    num_step    = int(len(data)-2)
    print(num_step)
    Norm        = np.zeros([num_sample,num_step],dtype=np.float)
    Temp        = np.zeros([num_sample,num_step],dtype=np.float)
    Ene         = np.zeros([num_sample,num_step],dtype=np.float)
    Ene2        = np.zeros([num_sample,num_step],dtype=np.float)

    for cnt_samp in range(num_sample):
        in_file = "output/Norm_rand%d.dat" % (cnt_samp)
        print(in_file)

        with open("%s" % (in_file)) as f:
            data      = f.read()
            data      = data.split("\n")
        for i in range(1,num_step+1):
            cnt       = i-1
            tmp       = data[i].split()
            Norm[cnt_samp][cnt] = float(tmp[1])**2
            #print(cnt,Norm[cnt])

        in_file = "output/SS_rand%d.dat" %(cnt_samp)
        print(in_file)

        with open("%s" % (in_file)) as f:
            data      = f.read()
            data      = data.split("\n")
            #print(len(data))
        for i in range(1,num_step+1):
            cnt        = i-1
            tmp        = data[i].split()
            Temp[cnt_samp][cnt]  = float(tmp[0])
            Ene[cnt_samp][cnt]   = float(tmp[1])
            Ene2[cnt_samp][cnt]  = float(tmp[2])
    return  Norm,Temp,Ene,Ene2


def CalcPhys(Norm,Ene,Ene2,Temp,tpq_type):
    num_sample  = Norm.shape[0]
    num_step    = Norm.shape[1]
    phys_Temp   = np.zeros([num_sample,num_step],dtype=np.float)
    phys_Z      = np.zeros([num_sample,num_step],dtype=np.float)
    phys_Ene    = np.zeros([num_sample,num_step],dtype=np.float)
    phys_Ene2   = np.zeros([num_sample,num_step],dtype=np.float)
    rescale     = np.zeros([num_step],dtype=np.int)
    for k in range(0,num_step):
        phys_Z[0][k]    = 1.0       
        phys_Ene[0][k]  = Ene[0][k]      
        phys_Ene2[0][k] = Ene2[0][k]
        phys_Temp[0][k] = Temp[0][k]
 
    for cnt_samp in range(1,num_sample):
        tot_Z    = 0
        tot_Ene  = 0
        tot_Ene2 = 0
        tmp_X    = 1.0
        tot_Z    = 1.0

        k = 0
        tot_Z      = tot_Z*Norm[cnt_samp][k]/Norm[0][k]
        tot_Ene    = Ene[cnt_samp][k]*tot_Z
        tot_Ene2   = Ene2[cnt_samp][k]*tot_Z
        phys_Z[cnt_samp][k]    = tot_Z        
        phys_Ene[cnt_samp][k]  = tot_Ene        
        phys_Ene2[cnt_samp][k] = tot_Ene2 
        phys_Temp[cnt_samp][k] = 0.0
 
        for k in range(1,num_step-1):
            if tpq_type == "mTPQ":
                if Temp[0][k] > Temp[cnt_samp][k]: 
                    ext_k  = k+1
                    if Temp[0][k] > Temp[cnt_samp][k+1]:
                        ext_k  = k+2
                        #print("A fatal error")
                elif Temp[0][k] < Temp[cnt_samp][k]:
                    ext_k  = k-1
                    if Temp[0][k] < Temp[cnt_samp][k-1]:
                        ext_k  = k-2
                        #print("B fatal error k=%d cnt_sampl=%d: %f %f %f" % (k,cnt_samp,Temp[0][k],Temp[cnt_samp][k],Temp[cnt_samp][k-1]))
                else:
                    print("fatal")
                ratio_beta = (Temp[0][k]-Temp[cnt_samp][k])/(Temp[cnt_samp][ext_k]-Temp[cnt_samp][k])
                IPL_Z      = (Norm[cnt_samp][ext_k]-Norm[cnt_samp][k])*ratio_beta+Norm[cnt_samp][k]
                IPL_Ene    = (Ene[cnt_samp][ext_k]-Ene[cnt_samp][k])*ratio_beta+Ene[cnt_samp][k]
                IPL_Ene2   = (Ene2[cnt_samp][ext_k]-Ene2[cnt_samp][k])*ratio_beta+Ene2[cnt_samp][k]
                IPL_Temp   = Temp[0][k]
            elif tpq_type == "cTPQ":
                IPL_Z    =  Norm[cnt_samp][k]
                IPL_Ene  =  Ene[cnt_samp][k]
                IPL_Ene2 =  Ene2[cnt_samp][k]
                IPL_Temp =  Temp[cnt_samp][k]
            tot_Z      = tot_Z*IPL_Z/Norm[0][k]
            tot_Ene    = IPL_Ene*tot_Z
            tot_Ene2   = IPL_Ene2*tot_Z
            phys_Z[cnt_samp][k]    = tot_Z        
            phys_Ene[cnt_samp][k]  = tot_Ene        
            phys_Ene2[cnt_samp][k] = tot_Ene2 
            phys_Temp[cnt_samp][k] = IPL_Temp
            #if flag == 0:  
            #    print("fatal cnt_sampl =%d : %d %d: min %d max %d:  %f %f %f" % (cnt_samp,k,l,l_min,l_max,Temp[0][l],Temp[cnt_samp][k],Temp[cnt_samp][k+1]))
            #    print(" %f: %f %f  %f" % (Temp[cnt_samp][k],Temp[0][k-1],Temp[0][k],Temp[0][k+1]))
              
    return phys_Z,phys_Ene,phys_Ene2,phys_Temp

if __name__ == "__main__":
    main()
