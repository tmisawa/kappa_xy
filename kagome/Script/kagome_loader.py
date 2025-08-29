# loader.py
from   typing import Dict, Any
import os
import toml  # keep using the same library as your current code
from   toml import TomlDecodeError

class ParamError(ValueError):
    """Raised when required parameters are missing or invalid."""
    pass

def _require_num(d: Dict[str, Any], section: str, key: str, typ: type) -> Any:
    """Fetch a numeric value and cast to the specified type with clear errors."""
    try:
        v = d[section][key]
    except KeyError:
        raise ParamError(f"Missing key: [{section}].{key}")
    try:
        return typ(v)
    except (TypeError, ValueError):
        raise ParamError(f"Invalid type for [{section}].{key}: expected {typ.__name__}, got {type(v).__name__} ({v!r})")

def _require_str(d: Dict[str, Any], section: str, key: str) -> str:
    """Fetch a string value (any non-empty string is allowed)."""
    try:
        v = d[section][key]
    except KeyError:
        raise ParamError(f"Missing key: [{section}].{key}")
    if not isinstance(v, str):
        raise ParamError(f"Invalid type for [{section}].{key}: expected str, got {type(v).__name__}")
    if v.strip() == "":
        raise ParamError(f"Invalid value for [{section}].{key}: must be non-empty string")
    return v

def _require_str_choice(d: Dict[str, Any], section: str, key: str, choices: list[str]) -> str:
    """Fetch a string value and check if it's in the allowed choices."""
    try:
        v = d[section][key]
    except KeyError:
        raise ParamError(f"Missing key: [{section}].{key}")
    if not isinstance(v, str):
        raise ParamError(f"Invalid type for [{section}].{key}: expected str, got {type(v).__name__}")
    if v not in choices:
        raise ParamError(f"Invalid value for [{section}].{key}: {v!r}, must be one of {choices}")
    return v


def load_params_from_toml(path: str) -> Dict[str, Any]:
    """
    Load and validate parameters from a TOML file.

    Returns a dict with:
      - J  : float
      - hz : float
      - Lx : int
      - Ly : int
      - boundary   : character "open" of "periodic"
      - method: character "cg" or "ed" or "tpq"
      - output_dir : arbitrary character string
    Raises ParamError (or TomlDecodeError) on problems.
    """
    # 1) basic checks
    if not os.path.isfile(path):
        raise ParamError(f"Input file not found: {path}")

    # 2) parse TOML
    try:
        data = toml.load(path)
    except TomlDecodeError as e:
        raise ParamError(f"TOML parse error in {path}: {e}") from e

    # 3) read required values with casting
    J            = _require_num(data, "ham", "J", float)
    hz           = _require_num(data, "ham", "hz", float)
    Lx           = _require_num(data, "ham", "Lx", int)
    Ly           = _require_num(data, "ham", "Ly", int)
    boundary     = _require_str_choice(data, "ham", "boundary", ["open", "periodic"])
    method       = _require_str_choice(data, "general", "method", ["cg", "ed", "tpq"])
    output_dir   = _require_str(data, "general", "output_dir")

    # 3) return normalized dict (keeps backward compatibility)
    return {"J": J,"hz": hz, "Lx": Lx, "Ly": Ly, "boundary": boundary,\
           "output_dir": output_dir,"method": method}

