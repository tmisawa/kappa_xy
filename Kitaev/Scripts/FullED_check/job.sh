#!/bin/sh
#QSUB -queue F144cpu
#QSUB -node  4
#QSUB -mpi   512
#QSUB -omp   3
#QSUB -place pack
#QSUB -over false
#PBS -l walltime=00:30:00
#PBS -N HPhi
cd ${PBS_O_WORKDIR}
 #. /etc/profile.d/modules.sh
#module list > a
#module list

#source /home/issp/materiapps/HPhi/HPhivars.sh 
date
 mpijob ./HPhi -e namelist_cg.def
date
