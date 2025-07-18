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
