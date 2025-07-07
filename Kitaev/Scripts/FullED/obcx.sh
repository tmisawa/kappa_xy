#!/bin/sh
#------ pjsub option --------# 
#PJM -L rscgrp=regular
#PJM -L node=32
#PJM --omp thread=56
#PJM --mpi proc=32
#PJM -L elapse=23:50:00 
#PJM -g gp29
#PJM -j
#------- Program execution -------# 

#[s]obcx
module load python/3.7.3
#[e]obcx

MPI="mpiexec.hydra -n"
#VMC="./vmc.out"
#VMCDRY="./vmcdry.out"
HPhi="./HPhi -e"
python="python3.7"

date
   ${MPI} ${PJM_MPI_PROC} ${HPhi} namelist_ed.def
date
