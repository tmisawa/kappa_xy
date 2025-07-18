import numpy as np
import os
import copy
import math
import cmath
import read    #using read.py#
import hphi_io #using hphi_io.py#
import toml
import sys

def main():
    #[s] tolm load
    input_file  = sys.argv[1]
    input_dict  = toml.load(input_file)
    #[e] tolm load
    #[s] set param.
    Kitaev       = float(input_dict["param"]["K"])  
    Gamma        = float(input_dict["param"]["G"])   
    GammaPR      = float(input_dict["param"]["GP"])  
    J            = float(input_dict["param"]["J"])  
    mag_h        = float(input_dict["param"]["h"])/math.sqrt(3.0)
    Lx           = int(input_dict["param"]["Lx"])  
    Ly           = int(input_dict["param"]["Ly"])  
    exct         = int(input_dict["param"]["exct"])
    All_N        = Lx*Ly
    #[e] set param.
    cnt_name = "test"
    output_dir = "dir_"+"{}".format(cnt_name)
    os.makedirs(output_dir,exist_ok=True)
    tmp_sdt  = "pair.txt"
    num      = read.func_count(tmp_sdt)
    #[s] interaction
    Ising     = np.zeros([All_N,All_N],dtype=np.float)
    Exchange  = np.zeros([All_N,All_N],dtype=np.float)
    PairLift  = np.zeros([All_N,All_N],dtype=np.float)
    InterAll  = np.zeros([All_N,2,All_N,2,All_N,2,All_N,2],dtype=np.complex)
    #[e] interaction
    siteI   = np.zeros([num],dtype=np.int)
    siteJ   = np.zeros([num],dtype=np.int)
    intT1   = np.zeros([num],dtype=np.unicode)
    intT2   = np.zeros([num],dtype=np.unicode)
    para    = np.zeros([num],dtype=np.double)
    print('num',num)
    read.func_readpair(tmp_sdt,siteI,siteJ,intT1,intT2,para)
    #
    tmp_sdt  = "green1.txt"
    tmp_num  = read.func_count(tmp_sdt)
    print('tmp_num=',tmp_num)
    G1siteI  = np.zeros([tmp_num],dtype=np.int)
    G1spinI  = np.zeros([tmp_num],dtype=np.unicode)
    G1Int0   = np.zeros([tmp_num],dtype=np.float)
    G1Int1   = np.zeros([tmp_num],dtype=np.float)
    G1sign   = np.zeros([tmp_num],dtype=np.float)
    read.func_green1(tmp_sdt,G1siteI,G1spinI,G1Int0,G1Int1,G1sign)
    hphi_io.func_g1("./{}/".format(output_dir)+"green1.def",G1siteI,G1spinI)
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
    tmp_sdt  = "green6.txt"
    tmp_num  = read.func_count(tmp_sdt)
    print('tmp_num=',tmp_num)
    G6site0  = np.zeros([tmp_num],dtype=np.int)
    G6spin0  = np.zeros([tmp_num],dtype=np.unicode)
    G6site1  = np.zeros([tmp_num],dtype=np.int)
    G6spin1  = np.zeros([tmp_num],dtype=np.unicode)
    G6site2  = np.zeros([tmp_num],dtype=np.int)
    G6spin2  = np.zeros([tmp_num],dtype=np.unicode)
    G6site3  = np.zeros([tmp_num],dtype=np.int)
    G6spin3  = np.zeros([tmp_num],dtype=np.unicode)
    G6site4  = np.zeros([tmp_num],dtype=np.int)
    G6spin4  = np.zeros([tmp_num],dtype=np.unicode)
    G6site5  = np.zeros([tmp_num],dtype=np.int)
    G6spin5  = np.zeros([tmp_num],dtype=np.unicode)
    G6Int0   = np.zeros([tmp_num],dtype=np.float)
    G6Int1   = np.zeros([tmp_num],dtype=np.float)
    G6sign   = np.zeros([tmp_num],dtype=np.float)
    read.func_green6(tmp_sdt,G6site0,G6spin0,G6site1,G6spin1,G6site2,G6spin2,G6site3,G6spin3,G6site4,G6spin4,G6site5,G6spin5,G6Int0,G6Int1,G6sign)
    hphi_io.func_g6("./{}/".format(output_dir)+"green6.def",G6site0,G6spin0,G6site1,G6spin1,G6site2,G6spin2,G6site3,G6spin3,G6site4,G6spin4,G6site5,G6spin5)

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
    hphi_io.func_mag("./{}/".format(output_dir)+"mag.def",All_N,mag_h)
    hphi_io.func_io_all("./{}/".format(output_dir)+"InterAll.def",All_N,InterAll)

    f        = open("./{}/".format(output_dir)+"calcmod_ed.def", 'wt')
    f.write("  #CalcType = 0:Lanczos, 1:TPQCalc, 2:FullDiag, 3:CG, 4:Time-evolution"+"\n")
    f.write("  #CalcModel = 0:Hubbard, 1:Spin, 2:Kondo, 3:HubbardGC, 4:SpinGC, 5:KondoGC"+"\n")
    f.write("  #Restart = 0:None, 1:Save, 2:Restart&Save, 3:Restart"+"\n")
    f.write("  #CalcSpec = 0:None, 1:Normal, 2:No H*Phi, 3:Save, 4:Restart, 5:Restart&Save"+"\n")
    f.write("  CalcType   2"+"\n")
    f.write("  CalcModel   4"+"\n")
    f.write("  ReStart   0"+"\n")
    f.write("  CalcSpec   0"+"\n")
    f.write("  CalcEigenVec   0"+"\n")
    f.write("  InitialVecType   0"+"\n")
    f.write("  InputEigenVec   0"+"\n")
    f.write("  OutputEigenVec   0"+"\n")
    f.write("  Scalapack 1"+"\n")
    f.close()

    
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
    f.write("  CalcType   5"+"\n")
    f.write("  CalcModel   4"+"\n")
    f.write("  ReStart   0"+"\n")
    f.write("  CalcSpec   0"+"\n")
    f.write("  CalcEigenVec   0"+"\n")
    f.write("  InitialVecType   -1"+"\n")
    f.write("  InputEigenVec   0"+"\n")
    f.write("  OutputEigenVec   0"+"\n")
    f.close()

    f        = open("./{}/".format(output_dir)+"namelist_ed.def", 'wt')
    f.write("  ModPara       modpara_ed.def"+"\n")
    f.write("  CalcMod       calcmod_ed.def"+"\n")
    f.write("  Trans         mag.def"+"\n")
    f.write("  LocSpin       locspn.def"+"\n")
    f.write("  Ising         Ising.def"+"\n")
    f.write("  Exchange      Exchange.def"+"\n")
    f.write("  Pairlift      PairLift.def"+"\n")
    f.write("  InterAll      InterAll.def"+"\n")
    f.write("  OneBodyG      green1.def"+"\n")
    f.write("  TwoBodyG      green2.def"+"\n")
    f.write("  ThreeBodyG    green3.def"+"\n")
    f.write("  SixBodyG      green6.def"+"\n")
    f.close()

    f        = open("./{}/".format(output_dir)+"namelist_cg.def", 'wt')
    f.write("  ModPara       modpara_cg.def"+"\n")
    f.write("  CalcMod       calcmod_cg.def"+"\n")
    f.write("  Trans         mag.def"+"\n")
    f.write("  LocSpin       locspn.def"+"\n")
    f.write("  Ising         Ising.def"+"\n")
    f.write("  Exchange      Exchange.def"+"\n")
    f.write("  Pairlift      PairLift.def"+"\n")
    f.write("  InterAll      InterAll.def"+"\n")
    f.write("  OneBodyG      green1.def"+"\n")
    f.write("  TwoBodyG      green2.def"+"\n")
    f.write("  ThreeBodyG    green3.def"+"\n")
    f.write("  SixBodyG      green6.def"+"\n")
    f.close()

    f        = open("./{}/".format(output_dir)+"namelist_tpq.def", 'wt')
    f.write("  ModPara       modpara_tpq.def"+"\n")
    f.write("  CalcMod       calcmod_tpq.def"+"\n")
    f.write("  Trans         mag.def"+"\n")
    f.write("  LocSpin       locspn.def"+"\n")
    f.write("  Ising         Ising.def"+"\n")
    f.write("  Exchange      Exchange.def"+"\n")
    f.write("  Pairlift      PairLift.def"+"\n")
    f.write("  InterAll      InterAll.def"+"\n")
    f.write("  OneBodyG      green1.def"+"\n")
    f.write("  TwoBodyG      green2.def"+"\n")
    f.write("  ThreeBodyG    green3.def"+"\n")
    f.write("  SixBodyG      green6.def"+"\n")
    f.close()

    f        = open("./{}/".format(output_dir)+"modpara_ed.def", 'wt')
    f.write("--------------------  "+"\n")
    f.write("Model_Parameters   0  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("HPhi_Cal_Parameters  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("CDataFileHead  zvo  "+"\n")
    f.write("CParaFileHead  zqp  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("Nsite          {}".format(All_N)+"\n")
    f.write("Ncond          {}".format(All_N)+"\n")
    f.write("Lanczos_max    2000   "+"\n")
    f.write("initial_iv     -1    "+"\n")
    f.write("exct           50   "+"\n")
    f.write("LanczosEps     14   "+"\n")
    f.write("LanczosTarget  2   "+"\n")
    f.write("LargeValue     30  "+"\n")
    f.write("NumAve         5   "+"\n")
    f.write("ExpecInterval  20  "+"\n")
    f.close()
    
    f        = open("./{}/".format(output_dir)+"modpara_cg.def", 'wt')
    f.write("--------------------  "+"\n")
    f.write("Model_Parameters   0  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("HPhi_Cal_Parameters  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("CDataFileHead  zvo  "+"\n")
    f.write("CParaFileHead  zqp  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("Nsite          {}".format(All_N)+"\n")
    f.write("Ncond          {}".format(All_N)+"\n")
    f.write("Lanczos_max    2000   "+"\n")
    f.write("initial_iv     -1    "+"\n")
    f.write("exct           {}".format(exct)+"\n")
    f.write("LanczosEps     14   "+"\n")
    f.write("LanczosTarget  2   "+"\n")
    f.write("LargeValue     30  "+"\n")
    f.write("NumAve         5   "+"\n")
    f.write("ExpecInterval  20  "+"\n")
    f.close()

    f        = open("./{}/".format(output_dir)+"modpara_tpq.def", 'wt')
    f.write("--------------------  "+"\n")
    f.write("Model_Parameters   0  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("HPhi_Cal_Parameters  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("CDataFileHead  zvo  "+"\n")
    f.write("CParaFileHead  zqp  "+"\n")
    f.write("--------------------  "+"\n")
    f.write("Nsite          {}".format(All_N)+"\n")
    f.write("Ncond          {}".format(All_N)+"\n")
    f.write("Lanczos_max    6001   "+"\n")
    f.write("initial_iv     122    "+"\n")
    f.write("exct           50   "+"\n")
    f.write("LanczosEps     14   "+"\n")
    f.write("LanczosTarget  2   "+"\n")
    f.write("LargeValue     50  "+"\n")
    f.write("NumAve         50   "+"\n")
    f.write("ExpecInterval  100  "+"\n")
    f.write("ExpandCoef     6  "+"\n")
    f.close()


    num_loc  = All_N
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

if __name__ == "__main__":
    main()
