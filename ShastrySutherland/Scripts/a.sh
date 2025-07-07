num_sample=50
#[s]For SS
dir_Norm="dir_Norm"
mkdir -p $dir_Norm
python3 Norm_TPQ.py    $num_sample $dir_Norm cTPQ
for bs in 25
do
  python3 BS_TPQ.py    $num_sample $bs $dir_Norm 
  python3 Ext.py  BS_MaxBS$bs.dat
done
[e]For SS

#[s]For Phys
dir_Phys="dir_Phys"
mkdir -p $dir_Phys
#
python3 Aft_TPQ_Mag.py  $num_sample $dir_Phys
#
python3 Ave_TPQ_Mag.py  $num_sample $dir_Phys
#
python3 Norm_PhysTPQ.py  $num_sample $dir_Norm $dir_Phys cTPQ Mag_tpq
for bs in 25
do
  python3 BS_PhysTPQ.py  $num_sample $bs $dir_Phys Mag_tpq
done
#[s]For Phys
