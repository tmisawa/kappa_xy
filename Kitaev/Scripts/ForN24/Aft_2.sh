num_sample=100
#[s]For SS
dir_Norm="dir_Norm"
dir_Phys="dir_Phys"
for bs in 10 20 30 40 50
do
  python3 BS_PhysTPQ_2.py  $num_sample $bs $dir_Phys JE_tpq
  python3 Ext.py           Norm_JE_tpq_MaxBS$bs.dat
  python3 Ext.py           Norm_Kappa_MaxBS$bs.dat
done
#[s]For Phys
