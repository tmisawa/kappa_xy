#$ -S /bin/sh
#$ -pe openmpi 24
#$ -binding pe linear:24
#$ -v OMP_NUM_THREADS=1
#$ -cwd -m n
#$ -q all.q@bowmore02
. ~/.bashrc

cat $TMPDIR/machines | sort | uniq > $JOB_NAME.m$JOB_ID

export NUMBER_OF_PROCESS=1
export OMP_NUM_THREADS=24
export PROCESS_PER_NODE=1

./HPhi -e  namelist_tpq.def 
