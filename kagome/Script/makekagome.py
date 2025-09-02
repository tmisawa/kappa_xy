import numpy as np
import os
import copy
import math
import cmath
import toml
import sys
import itertools
from kagome_loader import load_params_from_toml, ParamError
from def_writer import DefWriter

def main():
    # Keep argv compatibility
    if len(sys.argv) < 2:
        print("Usage: python main.py input.toml")
        sys.exit(2)
    input_file = sys.argv[1]

    try:
        params = load_params_from_toml(input_file)
    except ParamError as e:
        # print user-friendly message and exit with non-zero
        print(f"[ERROR] {e}")
        sys.exit(1)
    #[s] parameters for Hamiltonian
    J            = params["J"]
    Dz           = 0.1
    hz           = params["hz"]
    Lx           = params["Lx"]
    Ly           = params["Ly"]
    boundary     = params["boundary"]
    output_dir   = params["output_dir"]
    method       = params["method"]
    print(f"Loaded[hamg]:    J={J}, hz={hz}, Lx={Lx}, Ly={Ly}")
    print(f"Loaded[general]: boundary={boundary}, output_dir={output_dir}, method={params['method']}   ")
    #[e] parameters for Hamiltonian
    os.makedirs(output_dir, exist_ok=True)
    All_N,IntType, DMType    = MakeKagomePair(Lx,Ly,boundary)
    #print(DMType)
    print("kagome lattice: boundary:%s All_N:%d" % (boundary, All_N))
    heisenberg_int   =  heisenberg_pairs(IntType)
    DM_int           =  DM_pairs(DMType)
    num_ising        =  num_ex    = len(heisenberg_int)
    num_DM           =  len(DM_int)
    # --- Decide whether DM is effectively present ---
    dm_scale = 0.25  # keep in one place to avoid mismatch
    # Policy: DM is "present" only if there are DM bonds AND the scaled amplitude is non-zero
    has_dm   = (num_DM > 0) and (abs(Dz * dm_scale) > 0.0)
    print(f"Number of pairs: heisenberg={num_ex}, DM={num_DM} (DM active: {has_dm})")
                        

    StandardGreenDef(output_dir, All_N)
    writer = DefWriter(float_prec=8, sort_pairs=True)
    # exisiting parameters: heisenberg_int, num_ex, num_ising, J, hz, All_N
    writer.write_spin_exchange_def(f"{output_dir}/spin_exchange.def", heisenberg_int, J, N=num_ex, scale=0.5)
    writer.write_ising_def(f"{output_dir}/ising.def",heisenberg_int, J, N=num_ising, scale=1.0)
    if has_dm:
        writer.write_dm_def(f"{output_dir}/interall.def",DM_int, Dz, N=2*num_DM, scale=0.25)
    writer.write_mag_def(f"{output_dir}/mag.def",All_N, hz, scale=0.5)
    writer.write_locspn_def(f"{output_dir}/locspn.def", All_N)


    # --- Build common bundle kwargs and add interall only if DM exists ---
    bundle_kwargs = dict(
        ising="ising.def",
        exchange="spin_exchange.def",
        trans="mag.def",
        onebodyg="green1.def",
        twobodyg="green2.def",
    )
    if has_dm:
        bundle_kwargs["interall"] = "interall.def"
    writer.write_bundle(output_dir, All_N,method,**bundle_kwargs)
    #NB: **bundle_kwargs: unpacks dict into keyword arguments
    print(f"Wrote all .def files into {output_dir}/")

def MakeKagomePair(Lx,Ly,boundary):
    assert boundary in ("periodic", "open")
    orb_num = 3
    if boundary == "periodic":
        All_N   = Lx*Ly*orb_num
    elif boundary == "open":
        All_N   = (Lx-1)*Ly*orb_num + 1*Ly*2
    IntType   = np.zeros([All_N,All_N],dtype=object)
    IntDM     = np.zeros([All_N,All_N],dtype=object)
    if boundary == "periodic":
        for Rx in range(Lx):
            for Ry in range(Ly):
                    #[s] orb_i = 0
                    all_i = 0 + (Rx+Ry*Lx)*orb_num
                    all_j = 1 + (Rx+Ry*Lx)*orb_num
                    IntType[all_i][all_j] = "heisenberg"
                    IntDM[all_i][all_j]   = "minus"

                    all_i = 0 + (Rx+Ry*Lx)*orb_num
                    all_j = 2 + (Rx+Ry*Lx)*orb_num
                    IntType[all_i][all_j] = "heisenberg"
                    IntDM[all_i][all_j]   = "plus"
                    #[e] orb_i = 0

                    #[s] orb_i = 1
                    all_i = 1 + (Rx+Ry*Lx)*orb_num
                    all_j = 2 + (Rx+Ry*Lx)*orb_num
                    IntType[all_i][all_j] = "heisenberg"
                    IntDM[all_i][all_j]   = "minus"

                    all_i = 1 + (Rx+Ry*Lx)*orb_num
                    all_j = 0 + ((Rx+1)%Lx+Ry*Lx)*orb_num
                    IntType[all_i][all_j] = "heisenberg"
                    IntDM[all_i][all_j]   = "plus"
                    #[e] orb_i = 1

                    #[s] orb_i = 2
                    all_i = 2 + (Rx+Ry*Lx)*orb_num
                    all_j = 0 + (Rx+((Ry+1)%Ly)*Lx)*orb_num
                    IntType[all_i][all_j] = "heisenberg"
                    IntDM[all_i][all_j]   = "minus"

                    all_i = 2 + (Rx+Ry*Lx)*orb_num
                    all_j = 1 + (((Rx-1+Lx)%Lx)+((Ry+1)%Ly)*Lx)*orb_num
                    IntType[all_i][all_j] = "heisenberg"
                    IntDM[all_i][all_j]   = "plus"
                    #[e] orb_i = 2
    elif boundary == "open":
        for Rx in range(Lx):
            for Ry in range(Ly):
                    #[s] orb_i = 0
                    if Rx != Lx-1:
                        all_i = 0 + (Rx+Ry*Lx)*orb_num-Ry
                        all_j = 1 + (Rx+Ry*Lx)*orb_num-Ry
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "minus"

                    if Rx != Lx-1:
                        all_i = 0 + (Rx+Ry*Lx)*orb_num-Ry
                        all_j = 2 + (Rx+Ry*Lx)*orb_num-Ry
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "plus"
                    elif Rx == Lx-1:
                        all_i = 0 + (Rx+Ry*Lx)*orb_num-Ry
                        all_j = 2 + (Rx+Ry*Lx)*orb_num-Ry-1
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "plus"
                    #[e] orb_i = 0

                    if Rx != Lx-1:
                        #[s] orb_i = 1
                        all_i = 1 + (Rx+Ry*Lx)*orb_num-Ry
                        all_j = 2 + (Rx+Ry*Lx)*orb_num-Ry
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "minus"

                        all_i = 1 + (Rx+Ry*Lx)*orb_num-Ry
                        all_j = 0 + ((Rx+1)+Ry*Lx)*orb_num-Ry
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "plus"
                        #[e] orb_i = 1

                    #[s] orb_i = 2
                    if Rx != Lx-1:
                        all_i = 2 + (Rx+Ry*Lx)*orb_num-Ry
                        all_j = 0 + (Rx+((Ry+1)%Ly)*Lx)*orb_num-(Ry+1)%Ly
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "minus"
                    elif Rx == Lx-1:
                        all_i = 2 + (Rx+Ry*Lx)*orb_num-Ry-1
                        all_j = 0 + (Rx+((Ry+1)%Ly)*Lx)*orb_num-(Ry+1)%Ly
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "minus"

                    if Rx != 0 and Rx != Lx-1:
                        all_i = 2 + (Rx+Ry*Lx)*orb_num-Ry
                        all_j = 1 + (((Rx-1+Lx)%Lx)+((Ry+1)%Ly)*Lx)*orb_num-(Ry+1)%Ly
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "plus"
                    elif Rx == Lx-1:
                        all_i = 2 + (Rx+Ry*Lx)*orb_num-Ry -1
                        all_j = 1 + (((Rx-1+Lx)%Lx)+((Ry+1)%Ly)*Lx)*orb_num-(Ry+1)%Ly
                        IntType[all_i][all_j] = "heisenberg"
                        IntDM[all_i][all_j]   = "plus"
                    #[e] orb_i = 2
    return All_N,IntType,IntDM

def heisenberg_pairs(IntType):
    """Return set of (i, j) where IntType[i, j] == 'heisenberg'."""
    n = IntType.shape[0]
    pairs = set()
    for i in range(n):
        for j in range(n):
            if IntType[i, j] == "heisenberg":
                pairs.add((i, j))
    return pairs

def DM_pairs(IntType):
    """Return set of (i, j) where IntType[i, j] == 'plus' or minus."""
    n = IntType.shape[0]
    pairs = set()
    for i in range(n):
        for j in range(n):
            if IntType[i, j] == "plus":
                pairs.add((i, j))
            elif IntType[i, j] == "minus":
                pairs.add((j, i))
    return pairs


def StandardGreenDef(output_dir, All_N):
    with open("%s/green1.def"%(output_dir) , 'w') as f:
        print("===",file=f)
        print("N %d"%(4*All_N),file=f)
        print("===",file=f)
        print("===",file=f)
        print("===",file=f)
        for all_i in range(0,All_N):
            print(" %d %d %d %d" % (all_i,0,all_i,0), file=f)
            print(" %d %d %d %d" % (all_i,1,all_i,1), file=f)
            print(" %d %d %d %d" % (all_i,0,all_i,1), file=f)
            print(" %d %d %d %d" % (all_i,1,all_i,0), file=f)

    with open("%s/green2.def"%(output_dir) , 'w') as f:
        print("===",file=f)
        print("N %d"%(6*All_N*All_N),file=f)
        print("===",file=f)
        print("===",file=f)
        print("===",file=f)
        for all_i in range(0,All_N):
            for all_j in range(0,All_N):
                print(" %d %d %d %d %d %d %d %d " % (all_i,0,all_i,0,all_j,0,all_j,0), file=f)
                print(" %d %d %d %d %d %d %d %d " % (all_i,0,all_i,0,all_j,1,all_j,1), file=f)
                print(" %d %d %d %d %d %d %d %d " % (all_i,1,all_i,1,all_j,0,all_j,0), file=f)
                print(" %d %d %d %d %d %d %d %d " % (all_i,1,all_i,1,all_j,1,all_j,1), file=f)
                #
                print(" %d %d %d %d %d %d %d %d " % (all_i,0,all_i,1,all_j,1,all_j,0), file=f)
                print(" %d %d %d %d %d %d %d %d " % (all_i,1,all_i,0,all_j,0,all_j,1), file=f)




if __name__ == "__main__":
    main()
