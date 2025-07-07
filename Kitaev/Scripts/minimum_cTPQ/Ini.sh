#[s]obcx
#module load python/3.7.3
#python3=python3.7
#[e]obcx
python3 --version
python3  MakeGreen.py input.toml
python3  MakePair.py  input.toml
python3  MakeDef.py   input.toml
cp dir_test/* .
