import itertools
import numpy as np

def func_input(list_lat):
  with open('input.txt') as f:
    data = f.read()
  data = data.split("\n")
  #print('check input',data)
  #print(len(data))
  dict_lat = {}
  for i in data:
    tmp = i.split()
    if len(tmp)>0:
      for i in list_lat:
        if i == tmp[0]:
          dict_lat[i] = tmp[1]
  return dict_lat

def func_param(list_param):
  with open('param') as f:
    data = f.read()
  data = data.split("\n")
  #print('check input',data)
  print(len(data))
  dict_param = {}
  for i in data:
    tmp = i.split()
    if len(tmp)>0:
      for i in list_param:
        if i == tmp[0]:
          dict_param[i] = tmp[1]
  return dict_param

def func_mod(in_file,list_param):
  with open(in_file) as f:
    data = f.read()
  data = data.split("\n")
  #print('check input',data)
  print(len(data))
  dict_param = {}
  for i in data:
    tmp = i.split()
    if len(tmp)>0:
      for i in list_param:
        if i == tmp[0]:
          dict_param[i] = tmp[1]
  return dict_param


def func_readdef(name):
  with open(name) as f:
    data = f.read()
  data = data.split("\n")
  tmp = data[1].split()
  print(tmp[0],tmp[1])
  return int(tmp[1])


def func_count(file_name):
    #[s] file name
    print(file_name)
    #[e] file name
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        #print(len(data))
        #[s] count not empty elements
    cnt = 0
    for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           cnt += 1
        #print(cnt)
    return cnt

def func_readSS(file_name,inv_temp,cnt_max):
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
    max_i = min(len(data),cnt_max)
    for i in range(1,max_i):
        if data[i]: # if data[i] is not empty
           tmp            = data[i].split()
           cnt            = int(tmp[5])
           inv_temp[cnt]  = float(tmp[0])


def func_readpair(file_name,siteI,siteJ,intT1,intT2,para):
    #[s] file name
    #[e] file name
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    cnt   = 0
    for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           tmp        = data[i].split()
           siteI[cnt] = int(tmp[0])
           siteJ[cnt] = int(tmp[1])
           intT1[cnt]  =     tmp[2]
           intT2[cnt]  =     tmp[3]
           para[cnt]  = float(tmp[4])
           cnt       += 1
        #print(cnt)

def func_green1(file_name,siteI,spinI,Int0,Int1,sign):
    #[s] file name
    #[e] file name
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    cnt = 0
    for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           tmp        = data[i].split()
           siteI[cnt] = int(tmp[0])
           spinI[cnt] =     tmp[1]
           Int0[cnt]  = float(tmp[2])
           Int1[cnt]  = float(tmp[3])
           sign[cnt]  = float(tmp[4])
           cnt       += 1
        #print(cnt)

def func_green2(file_name,siteI,spinI,siteJ,spinJ,Int0,Int1,sign):
    #[s] file name
    #[e] file name
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    cnt = 0
    for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           tmp        = data[i].split()
           siteI[cnt] = int(tmp[0])
           spinI[cnt] =     tmp[1]
           siteJ[cnt] = int(tmp[2])
           spinJ[cnt] =     tmp[3]
           Int0[cnt]  = float(tmp[4])
           Int1[cnt]  = float(tmp[5])
           sign[cnt]  = float(tmp[6])
           cnt       += 1
        #print(cnt)

def func_green3(file_name,siteI,spinI,siteJ,spinJ,siteK,spinK,Int0,Int1,sign):
    #[s] file name
    #[e] file name
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    cnt = 0
    for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           tmp        = data[i].split()
           #print(tmp)
           siteI[cnt] = int(tmp[0])
           spinI[cnt] =     tmp[1]
           siteJ[cnt] = int(tmp[2])
           spinJ[cnt] =     tmp[3]
           siteK[cnt] = int(tmp[4])
           spinK[cnt] =     tmp[5]
           Int0[cnt]  = float(tmp[6])
           Int1[cnt]  = float(tmp[7])
           sign[cnt]  = float(tmp[8])
           cnt       += 1
        #print(cnt)

def mod_val_green1(file_name,in_spinI,val_x,val_y,val_z):
    tot_sgn  = [0,0]
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    for i in range(0,len(data)-1): # fck -1
        if i%2 == 0 : # 2 is a unit for 1body int
            org_i   = i
            cnt     = int(i/2)
            pre     = 1.0
            #print("i=",i,"cnt=",cnt)
            if in_spinI[cnt] == 'x':
                pre      = pre*0.5
                sgn_I    = 1.0
                tmp         = data[org_i+0].split()
                site        = int(tmp[0])
                val_x[site] = float(tmp[4])
                val_y[site] = float(tmp[5])
            elif in_spinI[cnt] == 'y':
                pre = -0.5*pre*complex(0.0,1.0)
                sgn_I    = -1.0
            elif in_spinI[cnt] == 'z':
                val_x[site] = float(tmp[4])
                tmp        = data[org_i+0].split()
                site       = int(tmp[0])
                tmp_val    = 0.5*float(tmp[4])
                tmp        = data[org_i+1].split()
                tmp_val   += -0.5*float(tmp[4])
                val_z[site] = tmp_val
        #print(cnt)

def val_green1(file_name,in_spinI,val):
    tot_sgn  = [0,0]
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    for i in range(0,len(data)-1): # fck -1
        if i%2 == 0 : # 2 is a unit for 1body int
            org_i   = i
            cnt     = int(i/2)
            pre     = 1.0
            #print("i=",i,"cnt=",cnt)
            if in_spinI[cnt] == 'x':
                pre      = pre*0.5
                sgn_I    = 1.0
            elif in_spinI[cnt] == 'y':
                pre = -0.5*pre*complex(0.0,1.0)
                sgn_I    = -1.0
            elif in_spinI[cnt] == 'z':
                pre = pre*0.5
                sgn_I    = -1.0
            #
            tot_sgn[0]  = 1
            tot_sgn[1]  = sgn_I
            #
            tmp_val = 0.0
            for loc_cnt in range(0,2):
               tmp        = data[org_i+loc_cnt].split()
               tmp_val   += tot_sgn[loc_cnt]*complex(float(tmp[4]),float(tmp[5]))
            val[cnt] = pre*tmp_val
        #print(cnt)





def val_green2(file_name,in_spinI,in_spinJ,val):
    tot_sgn  = [0,0,0,0]
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    for i in range(0,len(data)-1): # fck -1
        if i%4 == 0 : # 4 is a unit for 2body int
            org_i   = i
            cnt     = int(i/4)
            pre     = 1.0
            #print("i=",i,"cnt=",cnt)
            if in_spinI[cnt] == 'x':
                pre      = pre*0.5
                sgn_I    = 1.0
            elif in_spinI[cnt] == 'y':
                pre = -0.5*pre*complex(0.0,1.0)
                sgn_I    = -1.0
            elif in_spinI[cnt] == 'z':
                pre = pre*0.5
                sgn_I    = -1.0
            #
            if in_spinJ[cnt] == 'x':
                pre      = pre*0.5
                sgn_J    =  1.0
            elif in_spinJ[cnt] == 'y':
                pre = -0.5*pre*complex(0.0,1.0)
                sgn_J    =  -1.0
            elif in_spinJ[cnt] == 'z':
                pre = pre*0.5
                sgn_J    =  -1.0
            # 
            tot_sgn[0]  = 1
            tot_sgn[1]  = sgn_J
            tot_sgn[2]  = sgn_I
            tot_sgn[3]  = sgn_I*sgn_J
            #
            tmp_val = 0.0
            for loc_cnt in range(0,4):
               tmp        = data[org_i+loc_cnt].split()
               tmp_val   += tot_sgn[loc_cnt]*complex(float(tmp[8]),float(tmp[9]))
            val[cnt] = pre*tmp_val
        #print(cnt)

def val_green3(file_name,in_spinI,in_spinJ,in_spinK,val):
    tot_sgn  = [0,0,0,0,0,0,0,0]
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    for i in range(0,len(data)-1): # fck -1
        if i%8 == 0 : # 8 is a unit for 3body int
            org_i   = i
            cnt     = int(i/8)
            pre     = 1.0
            #print("i=",i,"cnt=",cnt)
            if in_spinI[cnt] == 'x':
                pre      = pre*0.5
                sgn_I    = 1.0
            elif in_spinI[cnt] == 'y':
                pre = -0.5*pre*complex(0.0,1.0)
                sgn_I    = -1.0
            elif in_spinI[cnt] == 'z':
                pre = pre*0.5
                sgn_I    = -1.0
            #
            if in_spinJ[cnt] == 'x':
                pre      = pre*0.5
                sgn_J    =  1.0
            elif in_spinJ[cnt] == 'y':
                pre = -0.5*pre*complex(0.0,1.0)
                sgn_J    =  -1.0
            elif in_spinJ[cnt] == 'z':
                pre = pre*0.5
                sgn_J    =  -1.0
            # 
            if in_spinK[cnt] == 'x':
                pre      = pre*0.5
                sgn_K    = 1.0
            elif in_spinK[cnt] == 'y':
                pre      = -0.5*pre*complex(0.0,1.0)
                sgn_K    = -1.0
            elif in_spinK[cnt] == 'z':
                pre      = pre*0.5
                sgn_K    = -1.0
            #
            tot_sgn[0]  = 1
            tot_sgn[1]  = sgn_K
            tot_sgn[2]  = sgn_J
            tot_sgn[3]  = sgn_J*sgn_K
            tot_sgn[4]  = sgn_I
            tot_sgn[5]  = sgn_I*sgn_K
            tot_sgn[6]  = sgn_I*sgn_J
            tot_sgn[7]  = sgn_I*sgn_J*sgn_K
            #
            tmp_val = 0.0
            for loc_cnt in range(0,8):
               tmp        = data[org_i+loc_cnt].split()
               tmp_val   += tot_sgn[loc_cnt]*complex(float(tmp[12]),float(tmp[13]))
            val[cnt] = pre*tmp_val
        #print(cnt)

def val_green6(file_name,in_spin0,in_spin1,in_spin2,in_spin3,in_spin4,in_spin5,val):
    tot_sgn  = np.zeros([64],dtype=np.complex)
    tot_cnt  = 0

    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    for i in range(0,len(data)-1): # fck -1
        if i%64 == 0 : # 64 is a unit for 6body int
            org_i   = i
            cnt     = int(i/64)
            pre     = 1.0
            #print("i=",i,"cnt=",cnt)
            out_sgn0 = [1,1]
            out_sgn1 = [1,1]
            out_sgn2 = [1,1]
            out_sgn3 = [1,1]
            out_sgn4 = [1,1]
            out_sgn5 = [1,1]
            out_sgn0 = val_spin(in_spin0[cnt])
            out_sgn1 = val_spin(in_spin1[cnt])
            out_sgn2 = val_spin(in_spin2[cnt])
            out_sgn3 = val_spin(in_spin3[cnt])
            out_sgn4 = val_spin(in_spin4[cnt])
            out_sgn5 = val_spin(in_spin5[cnt])
            #print(pre)
            #print(in_spin0[cnt],out_sgn0)
            #print(in_spin1[cnt],out_sgn1)
            #print(in_spin2[cnt],out_sgn2)
            #print(in_spin3[cnt],out_sgn3)
            #print(in_spin4[cnt],out_sgn4)
            #print(in_spin5[cnt],out_sgn5)
            #
            tot_cnt  = 0
            l1       = [0,1]
            tot_list = itertools.product(l1,l1,l1,l1,l1,l1)
            for ind0,ind1,ind2,ind3,ind4,ind5 in tot_list:
                tmp              = out_sgn0[ind0]*out_sgn1[ind1]*out_sgn2[ind2]
                tmp              = tmp*out_sgn3[ind3]*out_sgn4[ind4]*out_sgn5[ind5]
                tot_sgn[tot_cnt] = tmp
                #print(tmp,tot_cnt,ind0,ind1,ind2,ind3,ind4,ind5)
                tot_cnt +=1
            #
            tmp_val = 0.0
            for loc_cnt in range(0,64):
               tmp        = data[org_i+loc_cnt].split()
               tmp_val   += tot_sgn[loc_cnt]*complex(float(tmp[24]),float(tmp[25]))
               #print(float(tmp[24]),float(tmp[25]))
            val[cnt] = pre*tmp_val
        #print(cnt)

def func_green6(file_name,site0,spin0,site1,spin1,site2,spin2,site3,spin3,site4,spin4,site5,spin5,Int0,Int1,sign):
    #[s] file name
    #[e] file name
    print(file_name)
    with open(file_name) as f:
        data      = f.read()
        data      = data.split("\n")
        print(len(data))
        #[s] count not empty elements
    cnt = 0
    for i in range(0,len(data)):
        if data[i]: # if data[i] is not empty
           tmp        = data[i].split()
           site0[cnt] = int(tmp[0])
           spin0[cnt] =     tmp[1]
           site1[cnt] = int(tmp[2])
           spin1[cnt] =     tmp[3]
           site2[cnt] = int(tmp[4])
           spin2[cnt] =     tmp[5]
           site3[cnt] = int(tmp[6])
           spin3[cnt] =     tmp[7]
           site4[cnt] = int(tmp[8])
           spin4[cnt] =     tmp[9]
           site5[cnt] = int(tmp[10])
           spin5[cnt] =     tmp[11]
           Int0[cnt]  = float(tmp[12])
           Int1[cnt]  = float(tmp[13])
           sign[cnt]  = float(tmp[14])
           cnt       += 1
        #print(cnt)


def val_spin(in_spin):
    out_sgn = [1,1]
    if in_spin == 'x':
        out_sgn[0]    = 1.0
        out_sgn[1]    = 1.0
    elif in_spin == 'y':
        out_sgn[0]    = complex(0.0,-1.0)
        out_sgn[1]    = complex(0.0,1.0)
    elif in_spin == 'z':
        out_sgn[0]    = 1.0
        out_sgn[1]    = -1.0
    return out_sgn
 

