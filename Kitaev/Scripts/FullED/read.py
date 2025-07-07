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
  print('check input',data)
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
