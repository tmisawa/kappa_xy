num_sample=100
#[s]For SS
dir_Norm="dir_Norm"
#[e]For SS

#[s]For Phys
dir_Phys="dir_Phys"
#
python3 Aft_TPQ_Mag.py  $num_sample $dir_Phys
#
python3 Ave_TPQ_Mag.py  $num_sample $dir_Phys
#
python3 Norm_PhysTPQ.py  $num_sample $dir_Norm $dir_Phys cTPQ Mag_tpq
for bs in 5 10 20 50
do
  python3 BS_PhysTPQ.py  $num_sample $bs $dir_Phys Mag_tpq
  python3 Ext.py         Norm_Mag_tpq_MaxBS$bs.dat
done
#[s]For Phys
