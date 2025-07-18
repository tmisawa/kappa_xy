#!/bin/sh
#------ pjsub option --------# 
#PJM -L rscgrp=short
#PJM -L node=1
#PJM --omp thread=56
#PJM --mpi proc=1
#PJM -L elapse=05:30:00 
#PJM -g gq31
#PJM -j
#------- Program execution -------# 

#[s]obcx
module load python/3.7.3
export PYTHONUSERBASE=/work/gq31/o00016/.local
#e[]obcx
#sh ./Aft.sh
date
python3 Aft_Thermal.py
date
