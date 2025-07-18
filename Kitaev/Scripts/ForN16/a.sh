num_sample=50
#[s]For Phys
dir_Phys="dir_Phys"
for bs in 5 10 20
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
