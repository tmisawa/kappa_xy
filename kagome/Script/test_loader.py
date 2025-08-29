# TEST_loader.py
import os
import pytest
from kagome_loader import load_params_from_toml, ParamError

def _write_tmp_toml_local(content: str, filename: str = "test.toml") -> str:
    """Write a TOML file into the current working directory and return its path."""
    path = os.path.join(os.getcwd(), filename)
    with open(path, "w") as f:
        f.write(content)
    return path

def test_load_params_ok():
    path = _write_tmp_toml_local("""
[ham]
J  = 1.5
hz = 0.5
Lx = 4
Ly = 3
boundary = "open"
[general]
output_dir = "output"
method = "tpq"
""",filename="params_test.toml")
    print("Testing with file:", path)
    p = load_params_from_toml(path)
    assert p == {"J": 1.5, "hz": 0.5,"Lx": 4, "Ly": 3, "boundary": "open",\
        "output_dir": "output", "method": "tpq"}

@pytest.mark.parametrize("bad_toml", [
    """[param]\nLx=4\nLy=3\n""",                 # missing J
    """[param]\nJ="x"\nLx=4\nLy=3\n""",          # J type error
    """[param]\nJ=1.0\nLx=0\nLy=3\n""",          # Lx <= 0
])
def test_load_params_error(bad_toml):
    path = _write_tmp_toml_local(bad_toml,filename="bad_params.toml")
    with pytest.raises(ParamError):
        load_params_from_toml(path)

