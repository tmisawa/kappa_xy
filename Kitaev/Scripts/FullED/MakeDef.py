import numpy as np
import os
import copy
import math
import cmath
import read    #using read.py#
import hphi_io #using hphi_io.py#

cnt_name = "test"
output_dir = "dir_"+"{}".format(cnt_name)
os.makedirs(output_dir,exist_ok=True)
tmp_sdt  = "pair.txt"
num      = read.func_count(tmp_sdt)
#[s] set param.
list_param =['K','J','G','GP','h'] # list for int. parameters
dict_param = read.func_param(list_param)     # read param.txt
print(dict_param['K'])
print(dict_param['G'])
print(dict_param['GP'])
print(dict_param['J'])
print(dict_param['h'])
mag_h    =  float(dict_param['h'])/math.sqrt(3.0)
max_site = 16
#[e] set param.
All_N    = max_site
#[s] interaction
Ising     = np.zeros([max_site,max_site],dtype=np.float)
Exchange  = np.zeros([max_site,max_site],dtype=np.float)
PairLift  = np.zeros([max_site,max_site],dtype=np.float)
InterAll  = np.zeros([max_site,2,max_site,2,max_site,2,max_site,2],dtype=np.complex)
#[e] interaction
siteI   = np.zeros([num],dtype=np.int)
siteJ   = np.zeros([num],dtype=np.int)
intT1   = np.zeros([num],dtype=np.unicode)
intT2   = np.zeros([num],dtype=np.unicode)
para    = np.zeros([num],dtype=np.double)
print('num',num)
read.func_readpair(tmp_sdt,siteI,siteJ,intT1,intT2,para)
#
tmp_sdt  = "green2.txt"
tmp_num  = read.func_count(tmp_sdt)
print('tmp_num=',tmp_num)
G2siteI  = np.zeros([tmp_num],dtype=np.int)
G2spinI  = np.zeros([tmp_num],dtype=np.unicode)
G2siteJ  = np.zeros([tmp_num],dtype=np.int)
G2spinJ  = np.zeros([tmp_num],dtype=np.unicode)
G2Int0   = np.zeros([tmp_num],dtype=np.float)
G2Int1   = np.zeros([tmp_num],dtype=np.float)
G2sign   = np.zeros([tmp_num],dtype=np.float)
read.func_green2(tmp_sdt,G2siteI,G2spinI,G2siteJ,G2spinJ,G2Int0,G2Int1,G2sign)
hphi_io.func_g2("./{}/".format(output_dir)+"green2.def",G2siteI,G2spinI,G2siteJ,G2spinJ)
#print(G2siteI)
#print(G2spinI)
#print(G2siteJ)
#print(G2spinJ)
#
tmp_sdt  = "green3.txt"
tmp_num  = read.func_count(tmp_sdt)
print('tmp_num=',tmp_num)
G3siteI  = np.zeros([tmp_num],dtype=np.int)
G3spinI  = np.zeros([tmp_num],dtype=np.unicode)
G3siteJ  = np.zeros([tmp_num],dtype=np.int)
G3spinJ  = np.zeros([tmp_num],dtype=np.unicode)
G3siteK  = np.zeros([tmp_num],dtype=np.int)
G3spinK  = np.zeros([tmp_num],dtype=np.unicode)
G3Int0   = np.zeros([tmp_num],dtype=np.float)
G3Int1   = np.zeros([tmp_num],dtype=np.float)
G3sign   = np.zeros([tmp_num],dtype=np.float)
read.func_green3(tmp_sdt,G3siteI,G3spinI,G3siteJ,G3spinJ,G3siteK,G3spinK,G3Int0,G3Int1,G3sign)
hphi_io.func_g3("./{}/".format(output_dir)+"green3.def",G3siteI,G3spinI,G3siteJ,G3spinJ,G3siteK,G3spinK)
#print(G3siteI)
#print(G3spinI)
#print(G3siteJ)
#print(G3spinJ)
#print(G3siteK)
#print(G3spinK)
#


for cnt in range(num):
    #print(intT[cnt])
    #[s] for diagonal part
    if intT1[cnt] == 'x' and intT2[cnt] == 'x':
        #print('x',siteI[cnt],siteJ[cnt],intT[cnt],para[cnt])
        PairLift[siteI[cnt]][siteJ[cnt]] += 0.25*para[cnt]
        Exchange[siteI[cnt]][siteJ[cnt]] += 0.25*para[cnt]
    if intT1[cnt] == 'y' and intT2[cnt] == 'y':
        #print('y',siteI[cnt],siteJ[cnt],intT[cnt],para[cnt])
        PairLift[siteI[cnt]][siteJ[cnt]] += -0.25*para[cnt]
        Exchange[siteI[cnt]][siteJ[cnt]] += 0.25*para[cnt]
    if intT1[cnt] == 'z' and intT2[cnt] == 'z':
        #print('z',siteI[cnt],siteJ[cnt],intT[cnt],para[cnt])
        Ising[siteI[cnt]][siteJ[cnt]] += para[cnt]
    #[e] for diagonal part
    #[s] for non-diagonal part
    if intT1[cnt] == 'x' and intT2[cnt] == 'y':
        I = siteI[cnt]
        J = siteJ[cnt]
        # xy
        InterAll[I][0][I][1][J][0][J][1] += complex(0,-0.25*para[cnt])
        InterAll[I][0][I][1][J][1][J][0] += complex(0,0.25*para[cnt])
        InterAll[I][1][I][0][J][0][J][1] += complex(0,-0.25*para[cnt])
        InterAll[I][1][I][0][J][1][J][0] += complex(0,0.25*para[cnt])
        # yx
        InterAll[I][0][I][1][J][0][J][1] += complex(0,-0.25*para[cnt])
        InterAll[I][0][I][1][J][1][J][0] += complex(0,-0.25*para[cnt])
        InterAll[I][1][I][0][J][0][J][1] += complex(0,0.25*para[cnt])
        InterAll[I][1][I][0][J][1][J][0] += complex(0,0.25*para[cnt])
    if intT1[cnt] == 'x' and intT2[cnt] == 'z':
        I = siteI[cnt]
        J = siteJ[cnt]
        # xz
        InterAll[I][0][I][1][J][0][J][0] +=  0.25*para[cnt]
        InterAll[I][0][I][1][J][1][J][1] += -0.25*para[cnt]
        InterAll[I][1][I][0][J][0][J][0] +=  0.25*para[cnt]
        InterAll[I][1][I][0][J][1][J][1] += -0.25*para[cnt]
        # zx
        InterAll[I][0][I][0][J][0][J][1] +=  0.25*para[cnt]
        InterAll[I][0][I][0][J][1][J][0] +=  0.25*para[cnt]
        InterAll[I][1][I][1][J][0][J][1] += -0.25*para[cnt]
        InterAll[I][1][I][1][J][1][J][0] += -0.25*para[cnt]
    if intT1[cnt] == 'y' and intT2[cnt] == 'z':
        I = siteI[cnt]
        J = siteJ[cnt]
        # yz
        InterAll[I][0][I][1][J][0][J][0] += complex(0,-0.25*para[cnt])
        InterAll[I][0][I][1][J][1][J][1] += complex(0,0.25*para[cnt])
        InterAll[I][1][I][0][J][0][J][0] += complex(0,0.25*para[cnt])
        InterAll[I][1][I][0][J][1][J][1] += complex(0,-0.25*para[cnt])
        # zy
        InterAll[I][0][I][0][J][0][J][1] += complex(0,-0.25*para[cnt])
        InterAll[I][0][I][0][J][1][J][0] += complex(0,0.25*para[cnt])
        InterAll[I][1][I][1][J][0][J][1] += complex(0,0.25*para[cnt])
        InterAll[I][1][I][1][J][1][J][0] += complex(0,-0.25*para[cnt])
    if intT1[cnt] == 'y' and intT2[cnt] == 'x':
        print('should be xy')
    if intT1[cnt] == 'z' and intT2[cnt] == 'x':
        print('should be xz')
    if intT1[cnt] == 'z' and intT2[cnt] == 'y':
        print('should be yz')
    #[e] for non-diagonal part
#print(np.nonzero(Exchange))
#print(np.nonzero(Exchange)[0])
#print(np.nonzero(Exchange)[0][5])
hphi_io.func_io("./{}/".format(output_dir)+"Ising.def",Ising,"two")
hphi_io.func_io("./{}/".format(output_dir)+"Exchange.def",Exchange,"two")
hphi_io.func_io("./{}/".format(output_dir)+"PairLift.def",PairLift,"two")
hphi_io.func_mag("./{}/".format(output_dir)+"mag.def",max_site,mag_h)
hphi_io.func_io_all("./{}/".format(output_dir)+"InterAll.def",max_site,InterAll)
 
f        = open("./{}/".format(output_dir)+"calcmod_cg.def", 'wt')
f.write("  #CalcType = 0:Lanczos, 1:TPQCalc, 2:FullDiag, 3:CG, 4:Time-evolution"+"\n")
f.write("  #CalcModel = 0:Hubbard, 1:Spin, 2:Kondo, 3:HubbardGC, 4:SpinGC, 5:KondoGC"+"\n")
f.write("  #Restart = 0:None, 1:Save, 2:Restart&Save, 3:Restart"+"\n")
f.write("  #CalcSpec = 0:None, 1:Normal, 2:No H*Phi, 3:Save, 4:Restart, 5:Restart&Save"+"\n")
f.write("  CalcType   3"+"\n")
f.write("  CalcModel   4"+"\n")
f.write("  ReStart   0"+"\n")
f.write("  CalcSpec   0"+"\n")
f.write("  CalcEigenVec   0"+"\n")
f.write("  InitialVecType   0"+"\n")
f.write("  InputEigenVec   0"+"\n")
f.write("  OutputEigenVec   0"+"\n")
f.close()

f        = open("./{}/".format(output_dir)+"calcmod_tpq.def", 'wt')
f.write("  #CalcType = 0:Lanczos, 1:TPQCalc, 2:FullDiag, 3:CG, 4:Time-evolution"+"\n")
f.write("  #CalcModel = 0:Hubbard, 1:Spin, 2:Kondo, 3:HubbardGC, 4:SpinGC, 5:KondoGC"+"\n")
f.write("  #Restart = 0:None, 1:Save, 2:Restart&Save, 3:Restart"+"\n")
f.write("  #CalcSpec = 0:None, 1:Normal, 2:No H*Phi, 3:Save, 4:Restart, 5:Restart&Save"+"\n")
f.write("  CalcType   1"+"\n")
f.write("  CalcModel   4"+"\n")
f.write("  ReStart   0"+"\n")
f.write("  CalcSpec   0"+"\n")
f.write("  CalcEigenVec   0"+"\n")
f.write("  InitialVecType   0"+"\n")
f.write("  InputEigenVec   0"+"\n")
f.write("  OutputEigenVec   0"+"\n")
f.close()


f        = open("./{}/".format(output_dir)+"namelist_cg.def", 'wt')
f.write("  ModPara       modpara.def"+"\n")
f.write("  CalcMod       calcmod_cg.def"+"\n")
f.write("  Trans         mag.def"+"\n")
f.write("  LocSpin       locspn.def"+"\n")
f.write("  Ising         Ising.def"+"\n")
f.write("  Exchange      Exchange.def"+"\n")
f.write("  Pairlift      PairLift.def"+"\n")
f.write("  InterAll      InterAll.def"+"\n")
f.write("  OneBodyG      greenone.def"+"\n")
f.write("  TwoBodyG      green2.def"+"\n")
f.write("  ThreeBodyG    green3.def"+"\n")
f.close()

f        = open("./{}/".format(output_dir)+"namelist_tpq.def", 'wt')
f.write("  ModPara       modpara.def"+"\n")
f.write("  CalcMod       calcmod_tpq.def"+"\n")
f.write("  Trans         mag.def"+"\n")
f.write("  LocSpin       locspn.def"+"\n")
f.write("  Ising         Ising.def"+"\n")
f.write("  Exchange      Exchange.def"+"\n")
f.write("  Pairlift      PairLift.def"+"\n")
f.write("  InterAll      InterAll.def"+"\n")
f.write("  TwoBodyG      green2.def"+"\n")
f.write("  ThreeBodyG    green3.def"+"\n")
f.close()
 

f        = open("./{}/".format(output_dir)+"modpara.def", 'wt')
f.write("--------------------  "+"\n")
f.write("Model_Parameters   0  "+"\n")
f.write("--------------------  "+"\n")
f.write("HPhi_Cal_Parameters  "+"\n")
f.write("--------------------  "+"\n")
f.write("CDataFileHead  zvo  "+"\n")
f.write("CParaFileHead  zqp  "+"\n")
f.write("--------------------  "+"\n")
f.write("Nsite          {}".format(max_site)+"\n")
f.write("Ncond          {}".format(max_site)+"\n")
f.write("Lanczos_max    2000   "+"\n")
f.write("initial_iv     -1    "+"\n")
f.write("exct           50   "+"\n")
f.write("LanczosEps     14   "+"\n")
f.write("LanczosTarget  2   "+"\n")
f.write("LargeValue     30  "+"\n")
f.write("NumAve         5   "+"\n")
f.write("ExpecInterval  20  "+"\n")
f.close()

num_loc  = max_site
f        = open("./{}/".format(output_dir)+"locspn.def", 'wt')
f.write("==================="+"\n")
f.write("loc "+"{0:8d}".format(num_loc)+"\n")
f.write("==================="+"\n")
f.write("==================="+"\n")
f.write("==================="+"\n")
for all_i in range(0,All_N):
     f.write(" {0:8d} ".format(all_i)+" 1 " \
     +"\n")
f.close()

num_green  = 0
f        = open("./{}/".format(output_dir)+"greenone.def", 'wt')
f.write("==================="+"\n")
f.write("loc "+"{0:8d}".format(num_green)+"\n")
f.write("==================="+"\n")
f.write("==================="+"\n")
f.write("==================="+"\n")
f.close()

num_green  = 6*All_N*All_N
f        = open("./{}/".format(output_dir)+"greentwo_full.def", 'wt')
f.write("==================="+"\n")
f.write("loc "+"{0:8d}".format(num_green)+"\n")
f.write("==================="+"\n")
f.write("==================="+"\n")
f.write("==================="+"\n")
#[s] z and orb
list_trans = [0,0,0,0] # for z
#[e] z and orb
for all_i in range(0,All_N):
    for all_j in range(0,All_N):
        f.write(" {0:8d} ".format(all_i)+" 0 " \
           +" {0:8d} ".format(all_i)+" 0 "     \
           +" {0:8d} ".format(all_j)+" 0 "     \
           +" {0:8d}   ".format(all_j)+" 0 "   \
           +"\n")
        f.write(" {0:8d} ".format(all_i)+" 0 " \
           +" {0:8d} ".format(all_i)+" 0 "     \
           +" {0:8d} ".format(all_j)+" 1 "     \
           +" {0:8d}   ".format(all_j)+" 1 "   \
           +"\n")
        f.write(" {0:8d} ".format(all_i)+" 1 " \
           +" {0:8d} ".format(all_i)+" 1 "     \
           +" {0:8d} ".format(all_j)+" 0 "     \
           +" {0:8d}   ".format(all_j)+" 0 "   \
           +"\n")
        f.write(" {0:8d} ".format(all_i)+" 1 " \
           +" {0:8d} ".format(all_i)+" 1 "     \
           +" {0:8d} ".format(all_j)+" 1 "     \
           +" {0:8d}   ".format(all_j)+" 1 "   \
           +"\n")
        f.write(" {0:8d} ".format(all_i)+" 0 " \
           +" {0:8d} ".format(all_j)+" 0 "     \
           +" {0:8d} ".format(all_j)+" 1 "     \
           +" {0:8d}   ".format(all_i)+" 1 "   \
           +"\n")
        f.write(" {0:8d} ".format(all_i)+" 1 " \
           +" {0:8d} ".format(all_j)+" 1 "     \
           +" {0:8d} ".format(all_j)+" 0 "     \
           +" {0:8d}   ".format(all_i)+" 0 "   \
           +"\n")
f.close()
