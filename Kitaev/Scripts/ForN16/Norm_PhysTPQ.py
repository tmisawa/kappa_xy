import numpy as np
import os
import copy
import math
import cmath
import sys

def main():
    num_sample = int(sys.argv[1])
    dir_Norm   = sys.argv[2]
    dir_Phys   = sys.argv[3]
    tpq_type   = sys.argv[4]
    header     = sys.argv[5]
    IPL_InvTemp,IPL_Z=read_Norm(num_sample,dir_Norm)
    Phys        =  read_phys(num_sample,dir_Phys,header)
    num_step    = Phys.shape[1]
    num_phys    = Phys.shape[2]
    #print(Norm.shape[0],Norm.shape[1])
    #print(Phys)
    #print(Ene[0][9999])

    for cnt in range(num_sample):
        with open("%s/Norm_%s_set%d.dat" % (dir_Phys,header,cnt),'w') as f:
            print("# ",file=f )
    Norm_Phys  = CalcPhys(IPL_Z,IPL_InvTemp,Phys,tpq_type)
    #[s] numpy ave
    #[e] numpy ave
    for cnt in range(num_sample):
        print(cnt)
        with open("%s/Norm_%s_set%d.dat" % (dir_Phys,header,cnt),'a') as f2:
            for k in range(0,num_step-1):
                true_cnt  = int(Phys[cnt][k][0])
                print("%d     "% (true_cnt),end="",file=f2)
                print("%.12f  "% (IPL_Z[cnt][true_cnt]),end="",file=f2)
                for cnt_phys in range(1,num_phys):
                    print(" %.12f " % (Norm_Phys[cnt][k][cnt_phys]),end="",file=f2)
                print(" ",file=f2)

def read_phys(num_sample,dir_Phys,header):
    in_file = "%s/%s_set0.dat"  % (dir_Phys,header)
    print(in_file)

    with open("%s" % (in_file)) as f:
        data      = f.read()
        data      = data.split("\n")
    num_step    = int(len(data)-2)
    tmp         = data[1].split()
    num_phys    = len(tmp)
    print(num_step)
    print(num_phys)
    Phys        = np.zeros([num_sample,num_step,num_phys],dtype=np.float)

    for cnt_samp in range(num_sample):
        in_file = "%s/%s_set%d.dat" % (dir_Phys,header,cnt_samp)
        print(in_file)
        with open("%s" % (in_file)) as f:
            data      = f.read()
            data      = data.split("\n")
            #print(len(data))
        for i in range(0,num_step):
            cnt        = i
            tmp        = data[i].split()
            for cnt_phys in range(len(tmp)):
                Phys[cnt_samp][cnt][cnt_phys]  = float(tmp[cnt_phys])
    return  Phys


def read_Norm(num_sample,dir_Norm):
    in_file = "%s/TPQ_0.dat"%(dir_Norm)
    with open("%s" % (in_file)) as f:
        data      = f.read()
        data      = data.split("\n")
    num_step    = int(len(data)-2)
    print("num_step=",num_step)
    IPL_Z       = np.zeros([num_sample,num_step],dtype=np.float)
    IPL_InvTemp = np.zeros([num_sample,num_step],dtype=np.float)

    for cnt_samp in range(num_sample):
        in_file = "%s/TPQ_%d.dat" % (dir_Norm,cnt_samp)
        print(in_file)
        with open("%s" % (in_file)) as f:
            data      = f.read()
            data      = data.split("\n")
        for i in range(1,num_step+1):
            cnt       = i-1
            tmp       = data[i].split()
            IPL_InvTemp[cnt_samp][cnt] = float(tmp[1])
            IPL_Z[cnt_samp][cnt]       = float(tmp[2])

    return  IPL_InvTemp,IPL_Z


def CalcPhys(IPL_Z,IPL_InvTemp,Phys,tpq_type):
    num_sample  = Phys.shape[0]
    num_step    = Phys.shape[1]
    num_phys    = Phys.shape[2]
    print(num_sample,num_step,num_phys)
    Norm_Phys   = np.zeros([num_sample,num_step,num_phys],dtype=np.float)
    for k in range(0,num_step):
        for cnt_phys in range(0,num_phys):
            Norm_Phys[0][k][cnt_phys]  = Phys[0][k][cnt_phys]
 
    for cnt_samp in range(1,num_sample):
        for k in range(0,num_step-1):
            true_cnt                      = int(Phys[cnt_samp][k][0])
            Norm_Phys[cnt_samp][k][0]     = true_cnt
            #print(true_cnt)
            IPL_temp  = 1.0/IPL_InvTemp[cnt_samp][true_cnt]
            Norm_Phys[cnt_samp][k][1] = IPL_temp
            temp      = Phys[cnt_samp][k][0]
            if tpq_type=="mTPQ":
                if IPL_temp > temp: 
                    ext_k  = k-1
                elif IPL_temp < temp:
                    ext_k  = k+1
                else:
                    print("fatal")
                ratio_T   = (IPL_temp-Phys[cnt_samp][k][1])/(Phys[cnt_samp][ext_k][1]-Phys[cnt_samp][k][1])
                for cnt_phys in range(2,num_phys):
                    #Norm_Phys[cnt_samp][k][cnt_phys]=IPL_Z[cnt_samp][true_cnt]*Phys[cnt_samp][k][cnt_phys]
                    DPhys = Phys[cnt_samp][ext_k][cnt_phys]-Phys[cnt_samp][k][cnt_phys]
                    Norm_Phys[cnt_samp][k][cnt_phys]=IPL_Z[cnt_samp][true_cnt]*(DPhys*ratio_T+Phys[cnt_samp][k][cnt_phys])
            elif tpq_type=="cTPQ":
                for cnt_phys in range(2,num_phys):
                    Norm_Phys[cnt_samp][k][cnt_phys]=IPL_Z[cnt_samp][true_cnt]*Phys[cnt_samp][k][cnt_phys]
    return Norm_Phys

if __name__ == "__main__":
    main()
