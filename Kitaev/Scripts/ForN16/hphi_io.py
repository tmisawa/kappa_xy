from __future__ import print_function
import numpy as np
import math
import cmath
import itertools
import lattice #using read.py#

def func_io_all(file_name,max_site,param):
    print(file_name)
    num_param = len(np.nonzero(param)[0])
    f        = open(file_name, 'wt')
    f.write("==================="+"\n")
    f.write("num "+"{0:8d}".format(num_param)+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    cnt = 0
    for all_i in range(0,max_site):
        for all_j in range(0,max_site):
            for spn_0,spn_1,spn_2,spn_3 in itertools.product([0,1],repeat=4):
                #print(spn_0,spn_1,spn_2,spn_3)
                tmp_param  = param[all_i][spn_0][all_i][spn_1][all_j][spn_2][all_j][spn_3]
                if abs(tmp_param) != 0:
                    cnt       += 1
                    #print(all_i,spn_0,all_i,spn_1,all_j,spn_2,all_j,spn_3,tmp_param.real,tmp_param.imag)
                    f.write(" {0:8d} ".format(all_i) \
                    +" {0:8d}   ".format(spn_0)     \
                    +" {0:8d}   ".format(all_i)     \
                    +" {0:8d}   ".format(spn_1)     \
                    +" {0:8d}   ".format(all_j)     \
                    +" {0:8d}   ".format(spn_2)     \
                    +" {0:8d}   ".format(all_j)     \
                    +" {0:8d}   ".format(spn_3)     \
                    +" {0:8f}   ".format(tmp_param.real) \
                    +" {0:8f}   ".format(tmp_param.imag) \
                    +"\n")
    f.close()



def func_io(file_name,param,out_type):
    print(file_name)
    num_param = len(np.nonzero(param)[0])
    f        = open(file_name, 'wt')
    f.write("==================="+"\n")
    f.write("num "+"{0:8d}".format(num_param)+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    cnt = 0
    for all_i in np.nonzero(param)[0]:
      all_j      = np.nonzero(param)[1][cnt]
      tmp_param  = param[all_i][all_j]
      cnt       += 1
      #print(all_i,all_j)
      if out_type == "two":
          f.write(" {0:8d} ".format(all_i) \
          +" {0:8d}   ".format(all_j)     \
          +" {0:8f}   ".format(tmp_param) \
          +"\n")
    f.close()

def func_mag(file_name,max_site,mag_h):
    print(file_name)
    num_param = 4*max_site
    f        = open(file_name, 'wt')
    f.write("==================="+"\n")
    f.write("num "+"{0:8d}".format(num_param)+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    for cnt in range(0,max_site):
      all_i     = cnt
      # 
      f.write(" {0:8d} ".format(all_i) \
      +" {0:8d}   ".format(0)          \
      +" {0:8d}   ".format(all_i)      \
      +" {0:8d}   ".format(1)          \
      +" {0:8f}   ".format(-0.5*mag_h)          \
      +" {0:8f}   ".format(0.5*mag_h)          \
      +"\n")
      # 
      f.write(" {0:8d} ".format(all_i) \
      +" {0:8d}   ".format(1)          \
      +" {0:8d}   ".format(all_i)      \
      +" {0:8d}   ".format(0)          \
      +" {0:8f}   ".format(-0.5*mag_h)          \
      +" {0:8f}   ".format(-0.5*mag_h)          \
      +"\n")
      #
      f.write(" {0:8d} ".format(all_i) \
      +" {0:8d}   ".format(0)          \
      +" {0:8d}   ".format(all_i)      \
      +" {0:8d}   ".format(0)          \
      +" {0:8f}   ".format(-0.5*mag_h)          \
      +" {0:8f}   ".format(0.0)          \
      +"\n")
      #
      f.write(" {0:8d} ".format(all_i) \
      +" {0:8d}   ".format(1)          \
      +" {0:8d}   ".format(all_i)      \
      +" {0:8d}   ".format(1)          \
      +" {0:8f}   ".format(0.5*mag_h)          \
      +" {0:8f}   ".format(0.0)          \
      +"\n")
      # 
    f.close()

def func_g1(file_name,siteI,spinI):
    spin_i0 = [0,0]
    spin_i1 = [0,0]
    print(file_name)
    num_param = len(siteI)
    f        = open(file_name, 'wt')
    f.write("==================="+"\n")
    f.write("num "+"{0:8d}".format(2*num_param)+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    for cnt in range(0,num_param):
      all_i     = siteI[cnt]
      if spinI[cnt] == 'x' or spinI[cnt] == 'y':
        spin_i0[0] = 0
        spin_i1[0] = 1
        spin_i0[1] = 1
        spin_i1[1] = 0
      elif spinI[cnt] == 'z':
        spin_i0[0] = 0
        spin_i1[0] = 0
        spin_i0[1] = 1
        spin_i1[1] = 1
      for ind0 in range(0,2):
        f.write(" {0:8d} ".format(all_i)       \
        +" {0:8d}   ".format(spin_i0[ind0])    \
        +" {0:8d}   ".format(all_i)            \
        +" {0:8d}   ".format(spin_i1[ind0])    \
        +"\n")
    f.close()




def func_g2(file_name,siteI,spinI,siteJ,spinJ):
    spin_i0 = [0,0]
    spin_i1 = [0,0]
    spin_j0 = [0,0]
    spin_j1 = [0,0]
    print(file_name)
    num_param = len(siteI)
    f        = open(file_name, 'wt')
    f.write("==================="+"\n")
    f.write("num "+"{0:8d}".format(4*num_param)+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    for cnt in range(0,num_param):
      all_i     = siteI[cnt]
      all_j     = siteJ[cnt]
      if spinI[cnt] == 'x' or spinI[cnt] == 'y':
        spin_i0[0] = 0
        spin_i1[0] = 1
        spin_i0[1] = 1
        spin_i1[1] = 0
      elif spinI[cnt] == 'z':
        spin_i0[0] = 0
        spin_i1[0] = 0
        spin_i0[1] = 1
        spin_i1[1] = 1
      if spinJ[cnt] == 'x' or spinJ[cnt] == 'y':
        spin_j0[0] = 0
        spin_j1[0] = 1
        spin_j0[1] = 1
        spin_j1[1] = 0
      elif spinJ[cnt] == 'z':
        spin_j0[0] = 0
        spin_j1[0] = 0
        spin_j0[1] = 1
        spin_j1[1] = 1
      for ind0 in range(0,2):
        for ind1 in range(0,2):
          f.write(" {0:8d} ".format(all_i)       \
          +" {0:8d}   ".format(spin_i0[ind0])    \
          +" {0:8d}   ".format(all_i)            \
          +" {0:8d}   ".format(spin_i1[ind0])    \
          +" {0:8d}   ".format(all_j)            \
          +" {0:8d}   ".format(spin_j0[ind1])    \
          +" {0:8d}   ".format(all_j)            \
          +" {0:8d}   ".format(spin_j1[ind1])    \
          +"\n")
    f.close()

def func_g3(file_name,siteI,spinI,siteJ,spinJ,siteK,spinK):
    spin_i0 = [0,0]
    spin_i1 = [0,0]
    spin_j0 = [0,0]
    spin_j1 = [0,0]
    spin_k0 = [0,0]
    spin_k1 = [0,0]
    print(file_name)
    num_param = len(siteI)
    f        = open(file_name, 'wt')
    f.write("==================="+"\n")
    f.write("num "+"{0:8d}".format(8*num_param)+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    for cnt in range(0,num_param):
      all_i     = siteI[cnt]
      all_j     = siteJ[cnt]
      all_k     = siteK[cnt]
      if spinI[cnt] == 'x' or spinI[cnt] == 'y':
        spin_i0[0] = 0
        spin_i1[0] = 1
        spin_i0[1] = 1
        spin_i1[1] = 0
      elif spinI[cnt] == 'z':
        spin_i0[0] = 0
        spin_i1[0] = 0
        spin_i0[1] = 1
        spin_i1[1] = 1
      #
      if spinJ[cnt] == 'x' or spinJ[cnt] == 'y':
        spin_j0[0] = 0
        spin_j1[0] = 1
        spin_j0[1] = 1
        spin_j1[1] = 0
      elif spinJ[cnt] == 'z':
        spin_j0[0] = 0
        spin_j1[0] = 0
        spin_j0[1] = 1
        spin_j1[1] = 1
      #
      if spinK[cnt] == 'x' or spinK[cnt] == 'y':
        spin_k0[0] = 0
        spin_k1[0] = 1
        spin_k0[1] = 1
        spin_k1[1] = 0
      elif spinK[cnt] == 'z':
        spin_k0[0] = 0
        spin_k1[0] = 0
        spin_k0[1] = 1
        spin_k1[1] = 1
      #
      for ind0 in range(0,2):
        for ind1 in range(0,2):
          for ind2 in range(0,2):
            f.write(" {0:8d} ".format(all_i)       \
            +" {0:8d}   ".format(spin_i0[ind0])    \
            +" {0:8d}   ".format(all_i)            \
            +" {0:8d}   ".format(spin_i1[ind0])    \
            +" {0:8d}   ".format(all_j)            \
            +" {0:8d}   ".format(spin_j0[ind1])    \
            +" {0:8d}   ".format(all_j)            \
            +" {0:8d}   ".format(spin_j1[ind1])    \
            +" {0:8d}   ".format(all_k)            \
            +" {0:8d}   ".format(spin_k0[ind2])    \
            +" {0:8d}   ".format(all_k)            \
            +" {0:8d}   ".format(spin_k1[ind2])    \
            +"\n")
    f.close()

def out_g3(file_name,cnt_max,in_siteI,in_spinI,in_siteJ,in_spinJ,in_siteK,in_spinK,val):
    f        = open(file_name, 'wt')
    for cnt in range(0,cnt_max):
        f.write(" {0:8d} ".format(in_siteI[cnt]) \
        +" {0:8s}   ".format(in_spinI[cnt])      \
        +" {0:8d}   ".format(in_siteJ[cnt])      \
        +" {0:8s}   ".format(in_spinJ[cnt])      \
        +" {0:8d}   ".format(in_siteK[cnt])      \
        +" {0:8s}   ".format(in_spinK[cnt])      \
        +" {0:8f}   ".format(val[cnt].real)      \
        +" {0:8f}   ".format(val[cnt].imag)      \
        +"\n")
    f.close()

def func_g6(file_name,site0,spin0,site1,spin1,site2,spin2,site3,spin3,site4,spin4,site5,spin5):
    spin_00 = [0,0]
    spin_01 = [0,0]
    spin_10 = [0,0]
    spin_11 = [0,0]
    spin_20 = [0,0]
    spin_21 = [0,0]
    spin_30 = [0,0]
    spin_31 = [0,0]
    spin_40 = [0,0]
    spin_41 = [0,0]
    spin_50 = [0,0]
    spin_51 = [0,0]
    print(file_name)
    num_param = len(site0)
    f        = open(file_name, 'wt')
    f.write("==================="+"\n")
    f.write("num "+"{0:8d}".format(64*num_param)+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    f.write("==================="+"\n")
    for cnt in range(0,num_param):
        #print(cnt,num_param)
        all_0     = site0[cnt]
        all_1     = site1[cnt]
        all_2     = site2[cnt]
        all_3     = site3[cnt]
        all_4     = site4[cnt]
        all_5     = site5[cnt]

        return_spin(spin0[cnt],spin_00,spin_01)
        return_spin(spin1[cnt],spin_10,spin_11)
        return_spin(spin2[cnt],spin_20,spin_21)
        return_spin(spin3[cnt],spin_30,spin_31)
        return_spin(spin4[cnt],spin_40,spin_41)
        return_spin(spin5[cnt],spin_50,spin_51)
        l1       = [0,1]
        tot_list = itertools.product(l1,l1,l1,l1,l1,l1)
        for ind0,ind1,ind2,ind3,ind4,ind5 in tot_list:
           # print(cnt,ind0,ind1,ind2,ind3,ind4,ind5 ,num_param)
            f.write("{0:4d} ".format(all_0)       \
            +"{0:4d} ".format(spin_00[ind0])    \
            +"{0:4d} ".format(all_0)            \
            +"{0:4d} ".format(spin_01[ind0])    \
            +"{0:4d} ".format(all_1)            \
            +"{0:4d} ".format(spin_10[ind1])    \
            +"{0:4d} ".format(all_1)            \
            +"{0:4d} ".format(spin_11[ind1])    \
            +"{0:4d} ".format(all_2)            \
            +"{0:4d} ".format(spin_20[ind2])    \
            +"{0:4d} ".format(all_2)            \
            +"{0:4d} ".format(spin_21[ind2])    \
            +"{0:4d} ".format(all_3)            \
            +"{0:4d} ".format(spin_30[ind3])    \
            +"{0:4d} ".format(all_3)            \
            +"{0:4d} ".format(spin_31[ind3])    \
            +"{0:4d} ".format(all_4)            \
            +"{0:4d} ".format(spin_40[ind4])    \
            +"{0:4d} ".format(all_4)            \
            +"{0:4d} ".format(spin_41[ind4])    \
            +"{0:4d} ".format(all_5)            \
            +"{0:4d} ".format(spin_50[ind5])    \
            +"{0:4d} ".format(all_5)            \
            +"{0:4d} ".format(spin_51[ind5])    \
            +"\n")
    f.close()

def out_g6(file_name,cnt_max,site0,spin0,site1,spin1,site2,spin2,site3,spin3,site4,spin4,site5,spin5,val):
    f        = open(file_name, 'wt')
    for cnt in range(0,cnt_max):
        f.write(" {0:8d} ".format(site0[cnt]) \
        +" {0:8s}   ".format(spin0[cnt])      \
        +" {0:8d}   ".format(site1[cnt])      \
        +" {0:8s}   ".format(spin1[cnt])      \
        +" {0:8d}   ".format(site2[cnt])      \
        +" {0:8s}   ".format(spin2[cnt])      \
        +" {0:8d}   ".format(site3[cnt])      \
        +" {0:8s}   ".format(spin3[cnt])      \
        +" {0:8d}   ".format(site4[cnt])      \
        +" {0:8s}   ".format(spin4[cnt])      \
        +" {0:8d}   ".format(site5[cnt])      \
        +" {0:8s}   ".format(spin5[cnt])      \
        +" {0:8f}   ".format(val[cnt].real)      \
        +" {0:8f}   ".format(val[cnt].imag)      \
        +"\n")
    f.close()


def return_spin(in_spin,out_spin_0,out_spin_1):
    if in_spin == 'x' or in_spin == 'y':
        out_spin_0[0] = 0
        out_spin_1[0] = 1
        out_spin_0[1] = 1
        out_spin_1[1] = 0
    elif in_spin == 'z':
        out_spin_0[0] = 0
        out_spin_1[0] = 0
        out_spin_0[1] = 1
        out_spin_1[1] = 1


