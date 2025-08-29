# TEST_kagome.py
# Tests for MakeKagomePair
# - Write small, precise snapshot tests for tiny lattices
# - Add property-style tests (dtype, bounds, no self-loops, label domain, etc.)

import numpy as np
import pytest

# If your function lives in another module, change the import path accordingly.
# from yourmodule import MakeKagomePair
from makekagome import MakeKagomePair, heisenberg_pairs

# ---------- Property-style tests (general invariants) ----------

@pytest.mark.parametrize("Lx,Ly,boundary", [
    (1, 1, "periodic"),
    (2, 1, "open"),
    (2, 2, "periodic"),
    (3, 2, "open"),
])
def test_basic_shape_and_dtype(Lx, Ly, boundary):
    # Should return (All_N, IntType) with proper shape and dtype=object
    All_N, IntType = MakeKagomePair(Lx, Ly, boundary)
    assert isinstance(All_N, int)
    assert isinstance(IntType, np.ndarray)
    assert IntType.shape == (All_N, All_N)
    assert IntType.dtype == object  # object dtype is required by caller code


@pytest.mark.parametrize("Lx,Ly,boundary", [
    (1, 1, "periodic"),
    (2, 1, "open"),
    (2, 2, "periodic"),
    (3, 2, "open"),
])
def test_value_domain_and_no_self_loops(Lx, Ly, boundary):
    # Only 'heisenberg' or falsy (0/None/empty). No self loops (i,i) should be labeled.
    All_N, IntType = MakeKagomePair(Lx, Ly, boundary)
    for i in range(All_N):
        assert not IntType[i, i], "No self-loop should be labeled"
        for j in range(All_N):
            v = IntType[i, j]
            assert (not v) or (v == "heisenberg"), f"Unexpected label: {v}"


@pytest.mark.parametrize("Lx,Ly", [
    (1, 1),
    (2, 2),
    (3, 2),
    (4, 3),
])
def test_periodic_edge_count(Lx, Ly):
    # For periodic boundary:
    # The code writes exactly 6 directed edges per unit cell.
    # Expected number of 'heisenberg' entries = 6 * Lx * Ly
    All_N, IntType = MakeKagomePair(Lx, Ly, "periodic")
    pairs = heisenberg_pairs(IntType)
    assert len(pairs) == 6 * Lx * Ly # Hand-derived formula for periodic edges


@pytest.mark.parametrize("Lx,Ly", [
    (2, 1),
    (3, 2),
    (4, 3),
])
def test_open_edges_reasonable(Lx, Ly):
    # For open boundary:
    # - there should be some edges
    # - edges must be fewer than or equal to the periodic case
    All_N_open, IntType_open = MakeKagomePair(Lx, Ly, "open")
    pairs_open               = heisenberg_pairs(IntType_open)

    assert All_N_open      == 3*(Lx-1)*Ly+2*Ly
    if Lx>=2:
        tmp_num = 5*Ly+6*(Lx-2)*Ly+3*Ly 
        print(Lx,Ly,len(pairs_open),tmp_num)
        assert len(pairs_open) ==  tmp_num  # Hand-derived formula for open edges


# ---------- Snapshot tests (tiny lattices; exact edge set) ----------
def dump_nonzero(IntType):
    # Print only nonzero entries like: (i,j) = heisenberg
    n = IntType.shape[0]
    for i in range(n):
        for j in range(n):
            if IntType[i, j]:
                print(f"({i},{j}) = {IntType[i, j]}")


def test_periodic_L1x1_snapshot():
    # Lx=Ly=1, periodic:
    # From the code, we get the following directed edges inside the single cell:
    # (0->1), (0->2), (1->2), (1->0), (2->0), (2->1)
    All_N, IntType = MakeKagomePair(1, 1, "periodic")
    assert All_N == 3
    print("All_N:", All_N)
    dump_nonzero(IntType)
    expected = {(0,1), (0,2), (1,2), (1,0), (2,0), (2,1)}
    assert heisenberg_pairs(IntType) == expected


def test_open_L2x2_snapshot():
    # Hand-checked with the current open-boundary code:
    # Lx=2, Ly=2 => All_N =  3*(Lx-1)*Ly + 2*Ly = 10
    #
    Lx = 2
    Ly = 2
    All_N, IntType = MakeKagomePair(Lx, Ly, "open")
    pairs_open     = heisenberg_pairs(IntType)
    #dump_nonzero(IntType)
    assert All_N == 10
    if Lx>=2:
        tmp_num = 5*Ly+6*(Lx-2)*Ly+3*Ly 
        print(Lx,Ly,len(pairs_open),tmp_num)
        assert len(pairs_open) ==  tmp_num  # Hand-derived formula for open edges
    expected = {(0,1),(0,2),(1,2),(1,3),(2,5),(3,4), (4,6),(4,8),(5,6),(5,7),(6,7),(6,8),(7,0),(8,9),(9,1),(9,3)}
    assert heisenberg_pairs(IntType) == expected

