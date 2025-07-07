mkdir -p dir_Norm
mkdir -p dir_Phys
bin=50
for ((j=1; j <= 2; j+=1)); do
  for ((i=0; i < $bin; i+=1)); do
    tot=$(perl -sle  'print ($var+$var3*($var2-1))' -- -var=$i -var2=$j -var3=$bin)
    echo "$i $j $tot"
    #
    cp ./No$j/dir_Norm/TPQ_$i\.dat ./dir_Norm/TPQ_$tot\.dat
    #
    cp ./No$j/dir_Phys/JE_tpq_set$i.dat   ./dir_Phys/JE_tpq_set$tot\.dat
    cp ./No$j/dir_Phys/Flux_tpq_set$i.dat ./dir_Phys/Flux_tpq_set$tot\.dat
    cp ./No$j/dir_Phys/Mag_tpq_set$i.dat  ./dir_Phys/Mag_tpq_set$tot\.dat
  done
done

