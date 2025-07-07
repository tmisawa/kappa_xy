#!/bin/sh
#------ pjsub option --------# 
#PJM -L rscgrp=regular
#PJM -L node=8
#PJM --omp thread=7
#PJM --mpi proc=64
#PJM -L elapse=47:30:00 
#PJM -g gq31
#PJM -j
#------- Program execution -------# 

#[s]obcx
module load python/3.7.3
#[e]obcx

MPI="mpiexec.hydra -n"
#VMC="./vmc.out"
#VMCDRY="./vmcdry.out"
HPhi="./HPhi -e"
python3="python3.7"

date
   ${MPI} ${PJM_MPI_PROC} ${HPhi} namelist_tpq.def
date
#python3 Aft_TPQ_Flux.py
#python3 Ave_TPQ_Flux.py
#python3 Aft_CG.py
#python3 Finite_CG.py
