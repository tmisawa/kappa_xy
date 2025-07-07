#!/bin/sh
#------ pjsub option --------# 
#PJM -L rscgrp=debug
#PJM -L node=1
#PJM --omp thread=56
#PJM --mpi proc=1
#PJM -L elapse=00:30:00 
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

#[s]obcx
module load python/3.7.3
python3=python3.7
#[e]obcx
python3 --version
date
python3 Aft_Thermal.py
date
python3 Finite.py
