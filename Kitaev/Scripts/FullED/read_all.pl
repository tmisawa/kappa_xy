#!/usr/local/bin/perl
    $max_term = 50000;
    $max_char = 500000;
    &input; 
    #$GP =  0.0;
    #$K  = -1.0;
    #$G  =  0.01;
    #$J  = -0.0;
    $h  =  $h/sqrt(3.0); #normalized
    $file=sprintf("all_16sites.txt");
    print "$file  \n";
    open(INPUTFILE,$file);
    while($name=<INPUTFILE>){
      chomp $name;
      @foo = split /(\+)|(\-)/, $name; # spit by + or -
      $cnt=0;
      for($tmp_cnt=0;$tmp_cnt< $max_term;$tmp_cnt++){
        if(defined($foo[$tmp_cnt]) && length($foo[$tmp_cnt])>1){
          $term[$cnt] = $foo[$tmp_cnt];
          $cnt+=1;  
        }
      }
      @foo = split //, $name; # spit all
      $cnt_2=0;
      for($tmp_cnt=0;$tmp_cnt< $max_char;$tmp_cnt++){ # detect + and -
        if(defined($foo[$tmp_cnt]) ){
          if($foo[$tmp_cnt] eq "+"){
            $sign[$cnt_2]  =  1.0;
            $cnt_2        +=  1;
          }elsif($foo[$tmp_cnt] eq "-"){
            $sign[$cnt_2]  = -1.0;
            $cnt_2        +=  1;
          }
        }else{
          last;
        }
      }
    }
    if($cnt != $cnt_2){
      print("FATAL ERROR !!!! \n");
    }else{
      print("$cnt $cnt_2 \n");
    }
    $cnt_max = $cnt;
    $Th_cnt  = 0;
    $Tw_cnt  = 0;
    close(INPUTFILE);
    for($cnt = 0;$cnt<$cnt_max;$cnt++){
      #print(" $term[$cnt]  \n");
      @tmp = split(/,/,$term[$cnt]);
      if(defined($tmp[3])){ # for two body
          $Th_sign[$Th_cnt] = $sign[$cnt]; 
          #
          @tmp_2           = split(/\[/,$tmp[0]);
          $Th_site_i[$Th_cnt] = $tmp_2[1]; 
          @tmp_2           = split(/\]/,$tmp[1]);
          $Th_spin_i[$Th_cnt] = $tmp_2[0]; 
          #
          @tmp_2              = split(/\[/,$tmp[1]);
          $Th_site_j[$Th_cnt] = $tmp_2[1]; 
          @tmp_2              = split(/\]/,$tmp[2]);
          $Th_spin_j[$Th_cnt] = $tmp_2[0]; 
          #
          @tmp_2              = split(/\[/,$tmp[2]);
          $Th_site_k[$Th_cnt] = $tmp_2[1]; 
          @tmp_2              = split(/\]/,$tmp[3]);
          $Th_spin_k[$Th_cnt] = $tmp_2[0]; 
          #
          @tmp_2       = split(/\(/,$term[$cnt]);
          @tmp_3       = split(/\)/,$tmp_2[1]);
          @tmp_4       = split(/\*/,$tmp_3[0]);
          print(" $term[$cnt]: $tmp_4[0] $tmp_4[1]: $Th_sign[$Th_cnt]  \n");
          #
          if($tmp_4[0] eq "GP0" || $tmp_4[0] eq "GP1" ){
            $Th_Int_0[$Th_cnt] = $GP;
          }elsif($tmp_4[0] eq "G0" || $tmp_4[0] eq "G1"){
            $Th_Int_0[$Th_cnt] = $G;
          }elsif($tmp_4[0] eq "h0" || $tmp_4[0] eq "h1"){
            $Th_Int_0[$Th_cnt] = $h;
          }elsif($tmp_4[0] eq "J0" || $tmp_4[0] eq "J1"){
            $Th_Int_0[$Th_cnt] = $J;
          }elsif($tmp_4[0] eq "K0" || $tmp_4[0] eq "K1"){
            $Th_Int_0[$Th_cnt] = $K;
          }else{
            printf("FATAL error in three body\n");
          } 
          #
          if($tmp_4[1] eq "GP0" || $tmp_4[1] eq "GP1" ){
            $Th_Int_1[$Th_cnt] = $GP;
          }elsif($tmp_4[1] eq "G0" || $tmp_4[1] eq "G1"){
            $Th_Int_1[$Th_cnt] = $G;
          }elsif($tmp_4[1] eq "h0" || $tmp_4[1] eq "h1"){
            $Th_Int_1[$Th_cnt] = $h;
          }elsif($tmp_4[1] eq "J0" || $tmp_4[1] eq "J1"){
            $Th_Int_1[$Th_cnt] = $J;
          }elsif($tmp_4[1] eq "K0" || $tmp_4[1] eq "K1"){
            $Th_Int_1[$Th_cnt] = $K;
          }else{
            print("FATAL error in three body\n");
          } 
          #
          $Th_cnt            += 1;

      }elsif(defined($tmp[2])){ # for two body
          $Tw_sign[$Tw_cnt] = $sign[$cnt]; 
          #
          @tmp_2             = split(/\[/,$tmp[0]);
          $Tw_site_i[$Tw_cnt] = $tmp_2[1]; 
          @tmp_2              = split(/\]/,$tmp[1]);
          $Tw_spin_i[$Tw_cnt] = $tmp_2[0]; 
          #
          @tmp_2              = split(/\[/,$tmp[1]);
          $Tw_site_j[$Tw_cnt] = $tmp_2[1]; 
          @tmp_2              = split(/\]/,$tmp[2]);
          $Tw_spin_j[$Tw_cnt] = $tmp_2[0]; 

          @tmp_2       = split(/\(/,$term[$cnt]);
          @tmp_3       = split(/\)/,$tmp_2[1]);
          @tmp_4       = split(/\*/,$tmp_3[0]);
          print(" $term[$cnt]: $tmp_4[0] $tmp_4[1]: $Tw_sign[$Tw_cnt]  \n");
          if($tmp_4[0] eq "GP0" || $tmp_4[0] eq "GP1" ){
            $Tw_Int_0[$Tw_cnt] = $GP;
          }elsif($tmp_4[0] eq "G0" || $tmp_4[0] eq "G1"){
            $Tw_Int_0[$Tw_cnt] = $G;
          }elsif($tmp_4[0] eq "h0" || $tmp_4[0] eq "h1"){
            $Tw_Int_0[$Tw_cnt] = $h;
          }elsif($tmp_4[0] eq "J0" || $tmp_4[0] eq "J1"){
            $Tw_Int_0[$Tw_cnt] = $J;
          }elsif($tmp_4[0] eq "K0" || $tmp_4[0] eq "K1"){
            $Tw_Int_0[$Tw_cnt] = $K;
          }else{
            print("FATAL error in two body\n");
          } 
          #
          if($tmp_4[1] eq "GP0"    || $tmp_4[1] eq "GP1" ){
            $Tw_Int_1[$Tw_cnt] = $GP;
          }elsif($tmp_4[1] eq "G0" || $tmp_4[1] eq "G1"){
            $Tw_Int_1[$Tw_cnt] = $G;
          }elsif($tmp_4[1] eq "h0" || $tmp_4[1] eq "h1"){
            $Tw_Int_1[$Tw_cnt] = $h;
          }elsif($tmp_4[1] eq "J0" || $tmp_4[1] eq "J1"){
            $Tw_Int_1[$Tw_cnt] = $J;
          }elsif($tmp_4[1] eq "K0" || $tmp_4[1] eq "K1"){
            $Tw_Int_1[$Tw_cnt] = $K;
          }else{
            print("FATAL error in two body\n");
          } 
          $Tw_cnt            += 1;
      } 
     }
     print("$cnt_max $Th_cnt $Tw_cnt \n");
     #
     $fname="green2.txt";
     open(FILE,">$fname");
     for($cnt = 0;$cnt<$Tw_cnt;$cnt++){
       print FILE ("$Tw_site_i[$cnt] $Tw_spin_i[$cnt] $Tw_site_j[$cnt] $Tw_spin_j[$cnt] $Tw_Int_0[$cnt] $Tw_Int_1[$cnt]  $Tw_sign[$cnt]\n");
     } 
     close(FILE);
     #
     $fname="green3.txt";
     open(FILE,">$fname");
     for($cnt = 0;$cnt<$Th_cnt;$cnt++){
       print FILE ("$Th_site_i[$cnt] $Th_spin_i[$cnt] $Th_site_j[$cnt] $Th_spin_j[$cnt] $Th_site_k[$cnt] $Th_spin_k[$cnt] $Th_Int_0[$cnt] $Th_Int_1[$cnt] $Th_sign[$cnt]\n");
     } 
     close(FILE);
     #

 sub input{
  #input START 
  $file=sprintf("param");
  open(INPUTFILE,$file);
  while($name=<INPUTFILE>){
    chomp $name;
    #DELETE EMPTY
    $_=$name; 
    s/^\s+//;
    $name=$_; 
    @tmp = split /\s+/, $name;
    if($tmp[0] eq 'K'){
      $K = $tmp[1];
    } 
    if($tmp[0] eq 'J'){
      $J = $tmp[1];
    } 
    if($tmp[0] eq 'G'){
      $G = $tmp[1];
    } 
    if($tmp[0] eq 'GP'){
      $GP = $tmp[1];
    } 
    if($tmp[0] eq 'h'){
      $h = $tmp[1];
    } 
  }
  #input FINISH
  close(INPUTFILE);
 }
