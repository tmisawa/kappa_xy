import numpy as np
import os
import copy
import math
import cmath
import sys


in_file=sys.argv[1]
print(in_file)
with open(in_file) as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     cnt_max=len(data)

temp   = np.zeros([cnt_max],dtype=np.float)
#
JL1    = np.zeros([cnt_max],dtype=np.float)
JL2    = np.zeros([cnt_max],dtype=np.float)
JM     = np.zeros([cnt_max],dtype=np.float)
Jtot   = np.zeros([cnt_max],dtype=np.float)
#
d_JL1  = np.zeros([cnt_max],dtype=np.float)
d_JL2  = np.zeros([cnt_max],dtype=np.float)
d_JM   = np.zeros([cnt_max],dtype=np.float)
d_Jtot = np.zeros([cnt_max],dtype=np.float)

with open(in_file) as f:
     data      = f.read()
     data      = data.split("\n")
     print(len(data))
     cnt_max=len(data)
     #[s] count not empty elements
     cnt = 0
     for i in range(0,len(data)):
         tmp        = data[i].split()
         #print(len(tmp))
         if len(tmp)>1: # if data[i] is not empty
             cnt        += 1
print(cnt)
