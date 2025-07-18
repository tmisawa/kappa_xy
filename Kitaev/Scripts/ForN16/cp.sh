for ((i=0; i < 50; i+=1)); do
  j=$(perl -sle  'print ($var+50)' -- -var=$i)
  echo "$j"
  #
  cp ../No1/dir_Norm/TPQ_$i\.dat ./dir_Norm/TPQ_$i\.dat
  cp ../No2/dir_Norm/TPQ_$i\.dat ./dir_Norm/TPQ_$j\.dat
  #
  cp ../No1/dir_Phys/JE_tpq_set$i.dat   ./dir_Phys/JE_tpq_set$i\.dat
  cp ../No1/dir_Phys/Flux_tpq_set$i.dat ./dir_Phys/Flux_tpq_set$i\.dat
  cp ../No1/dir_Phys/Mag_tpq_set$i.dat  ./dir_Phys/Mag_tpq_set$i\.dat
  #
  cp ../No2/dir_Phys/JE_tpq_set$i.dat   ./dir_Phys/JE_tpq_set$j\.dat
  cp ../No2/dir_Phys/Flux_tpq_set$i.dat ./dir_Phys/Flux_tpq_set$j\.dat
  cp ../No2/dir_Phys/Mag_tpq_set$i.dat  ./dir_Phys/Mag_tpq_set$j\.dat
done

