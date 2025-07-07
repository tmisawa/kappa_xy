num_sample=100
#[s]For SS
dir_Norm="dir_Norm"
mkdir -p $dir_Norm
#python3 Norm_TPQ.py    $num_sample $dir_Norm cTPQ
for bs in 10 20 30 40 50
do
  python3 BS_TPQ.py    $num_sample $bs $dir_Norm 
  python3 Ext.py  BS_MaxBS$bs.dat
done
#[e]For SS

#[s]For Phys
dir_Phys="dir_Phys"
mkdir -p $dir_Phys
#
#python3 Aft_TPQ_Mag.py  $num_sample $dir_Phys
#python3 Aft_TPQ.py      $num_sample $dir_Phys input.toml
#python3 Aft_TPQ_Flux.py $num_sample $dir_Phys
#
#python3 Ave_TPQ_Mag.py  $num_sample $dir_Phys
#python3 Ave_TPQ.py      $num_sample $dir_Phys input.toml
#python3 Ave_TPQ_Flux.py $num_sample $dir_Phys
#
python3 Norm_PhysTPQ.py  $num_sample $dir_Norm $dir_Phys cTPQ Mag_tpq
python3 Norm_PhysTPQ.py  $num_sample $dir_Norm $dir_Phys cTPQ JE_tpq
python3 Norm_PhysTPQ.py  $num_sample $dir_Norm $dir_Phys cTPQ Flux_tpq
for bs in 10 20 30 40 50
do
  python3 BS_PhysTPQ.py  $num_sample $bs $dir_Phys Mag_tpq
  python3 BS_PhysTPQ.py  $num_sample $bs $dir_Phys JE_tpq
  python3 BS_PhysTPQ.py  $num_sample $bs $dir_Phys Flux_tpq
  python3 Ext.py         Norm_Mag_tpq_MaxBS$bs.dat
  python3 Ext.py         Norm_JE_tpq_MaxBS$bs.dat
  python3 Ext.py         Norm_Flux_tpq_MaxBS$bs.dat
  python3 Ext.py         Norm_Kappa_MaxBS$bs.dat
done
#[s]For Phys
