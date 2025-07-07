import numpy as np
import copy
import math
import cmath
import sys

with open("all_1.dat" , 'w') as out_f:
    print(" # ",file=out_f)
  #  for cnt in range(0,65536):
    for cnt in range(0,2**16):
        file_name  = "output/zvo_cisajs_eigen%d.dat" % (cnt)
        #print(file_name)
        with open(file_name) as f:
            data      = f.read()
            data      = data.split("\n")
            #[s] count not empty elements
        Sx  = 0.0
        Sy  = 0.0
        Sz  = 0.0
        for i in range(0,len(data)):
            if data[i]: # if data[i] is not empty
                tmp        = data[i].split()
                if tmp[0] == tmp[2]: #and tmp[0] == '0':  
                    if tmp[1] == '0' and tmp[3] == '1':  
                        Sx+=float(tmp[4])
                        Sy+=float(tmp[5])
                    if tmp[1] == '1' and tmp[3] == '0':  
                        Sx+=float(tmp[4])
                        Sy+=-1.0*float(tmp[5])
                    if tmp[1] == '0' and tmp[3] == '0':  
                        Sz+=float(tmp[4])
                    if tmp[1] == '1' and tmp[3] == '1':  
                        Sz+=-1.0*float(tmp[4])
        Sx=0.5*Sx/4.0
        Sy=0.5*Sy/4.0
        Sz=0.5*Sz/2.0
        tot_mag = math.sqrt((Sx)**2+(Sy)**2+(Sz)**2)
        #print(tot_mag,Sx,Sy,Sz)
        print(" %d %16.8f %16.8f %16.8f %16.8f " % (cnt,tot_mag,Sx,Sy,Sz),file=out_f)
