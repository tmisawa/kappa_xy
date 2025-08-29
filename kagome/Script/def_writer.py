# def_writer.py
from typing import Iterable, Tuple, Callable, Union, List, Dict, Any,Optional

PairIterable = Iterable[Tuple[int, int]]
Weight = Union[float, Callable[[int, int], float]]

class DefWriter:
    """Unified writer for .def files used in your workflow."""

    def __init__(self, float_prec: int = 12, sort_pairs: bool = True):
        # float_prec controls printed precision; sort_pairs makes output stable.
        self.float_prec = float_prec
        self.sort_pairs = sort_pairs

    # ---------- low-level helpers ----------
    def _write_header(self, f, N: int) -> None:
        print("---", file=f)
        print(f"N {N}", file=f)
        print("---", file=f)
        print("---", file=f)
        print("---", file=f)

    def _fmt_pair(self, i: int, j: int, val: float) -> str:
        # Keep exact spacing and a trailing space for full compatibility
        return f"  {i:8d} {j:8d} {val:.{self.float_prec}f} "

    # ---------- generic writers ----------
    def write_pairs_def(
        self,
        filename: str,
        pairs: PairIterable,
        N: int | None = None,
        weight: Weight = 0.0,
    ) -> None:
        """
        Write a generic pair-wise .def file.

        - pairs: iterable of (i, j)
        - N: header count (if None, uses len(pairs))
        - weight:
            * float  -> constant value for all pairs
            * callable (i,j)->float -> per-pair value
        """
        pairs_list = list(pairs)
        if self.sort_pairs:
            pairs_list = sorted(pairs_list)
        if N is None:
            N = len(pairs_list)

        # Precompute numeric values to avoid surprises in printing
        if callable(weight):
            vals = [float(weight(i, j)) for (i, j) in pairs_list]
        else:
            w = float(weight)
            vals = [w] * len(pairs_list)

        with open(filename, "w") as f:
            self._write_header(f, N)
            for (i, j), v in zip(pairs_list, vals):
                print(self._fmt_pair(i, j, v), file=f)

    def write_site_field_def(
        self,
        filename: str,
        n_sites: int,
        hz: float,
        scale: float = 0.5,
    ) -> None:
        """
        Write a two-line-per-site field .def (mag.def / kagome_namelist.def alike).

        For each site i:
          "  {i:8d} 0  {i:8d} 0 {+scale*hz:.12f} 0.0 "
          "  {i:8d} 1  {i:8d} 1 {-scale*hz:.12f} 0.0 "
        """
        with open(filename, "w") as f:
            self._write_header(f, 2 * n_sites)
            plus  = +scale * float(hz)
            minus = -scale * float(hz)
            for i in range(n_sites):
                print(f"  {i:8d} 0  {i:8d} 0 { plus:.{self.float_prec}f} 0.0 ", file=f)
                print(f"  {i:8d} 1  {i:8d} 1 {minus:.{self.float_prec}f} 0.0 ", file=f)

    # ---------- presets (for readability) ----------
    def write_spin_exchange_def(self, filename: str, pairs: PairIterable, J: float, N: int | None = None, scale: float = 0.5):
        """Alias preset for spin_exchange.def (value = scale*J for all pairs)."""
        self.write_pairs_def(filename, pairs, N=N, weight=scale * float(J))

    def write_ising_def(self, filename: str, pairs: PairIterable, J: float, N: int | None = None, scale: float = 0.5):
        """Alias preset for ising.def (same shape as spin_exchange.def)."""
        self.write_pairs_def(filename, pairs, N=N, weight=scale * float(J))

    def write_mag_def(self, filename: str, n_sites: int, hz: float, scale: float = 0.5):
        """Alias preset for mag.def."""
        self.write_site_field_def(filename, n_sites, hz, scale=scale)

    # -------------------------------------------------------------------------
    # calcmod
    # -------------------------------------------------------------------------
    def write_calcmod_def(
        self,
        filename: str,
        calc_type: int,
        calc_model: int = 4,
        restart: int = 0,
        calc_spec: int = 0,
        calc_eigenvec: int = 0,
        initial_vec_type: int = 0,
        input_eigenvec: int = 0,
        output_eigenvec: int = 0,
        scalapack: int = 1,
    ) -> None:
        """Write calcmod_*.def with standard header and chosen parameters."""
        with open(filename, "w") as f:
            f.write("  #CalcType = 0:Lanczos, 1:TPQCalc, 2:FullDiag, 3:CG, 4:Time-evolution\n")
            f.write("  #CalcModel = 0:Hubbard, 1:Spin, 2:Kondo, 3:HubbardGC, 4:SpinGC, 5:KondoGC\n")
            f.write("  #Restart = 0:None, 1:Save, 2:Restart&Save, 3:Restart\n")
            f.write("  #CalcSpec = 0:None, 1:Normal, 2:No H*Phi, 3:Save, 4:Restart, 5:Restart&Save\n")
            f.write(f"  CalcType   {calc_type}\n")
            f.write(f"  CalcModel   {calc_model}\n")
            f.write(f"  ReStart   {restart}\n")
            f.write(f"  CalcSpec   {calc_spec}\n")
            f.write(f"  CalcEigenVec   {calc_eigenvec}\n")
            f.write(f"  InitialVecType   {initial_vec_type}\n")
            f.write(f"  InputEigenVec   {input_eigenvec}\n")
            f.write(f"  OutputEigenVec   {output_eigenvec}\n")
            if scalapack is not None:
                f.write(f"  Scalapack {scalapack}\n")

    # -------------------------------------------------------------------------
    # namelist
    # -------------------------------------------------------------------------
    def write_namelist_def(
        self,
        filename: str,
        modpara: str,
        calcmod: str,
        *,
        # Optional entries. Pass a string (filename) to include, or None/False to omit.
        locspin: str | None = "locspn.def",
        trans: str | None = None,
        ising: str | None = None,
        exchange: str | None = None,
        pairlift: str | None = None,
        interall: str | None = None,
        onebodyg: str | None = None,
        twobodyg: str | None = None,
        threebodyg: str | None = None,
        sixbodyg: str | None = None,
        # Ex: {"Foo": "foo.def", "Bar": None}
        extras: dict[str, str | None] | None = None,
    ) -> None:
        """Write namelist_*.def with required entries and optional ones.
        - Always writes ModPara, CalcMod
        - LocSpin is included by default
        - Other entries default to None (not written)
        - extras: appended at the end, preserves your given order
        """
        items: list[tuple[str, str | None]] = [
            ("ModPara", modpara),
            ("CalcMod", calcmod),
            ("LocSpin", locspin),
            ("Trans", trans),
            ("Ising", ising),
            ("Exchange", exchange),
            ("Pairlift", pairlift),
            ("InterAll", interall),
            ("OneBodyG", onebodyg),
            ("TwoBodyG", twobodyg),
            ("ThreeBodyG", threebodyg),
            ("SixBodyG", sixbodyg),
        ]

        if extras:
            items += list(extras.items())

        with open(filename, "w") as f:
            for key, val in items:
                if not val:
                    continue
                f.write(f"  {key:<12s} {val}\n")

    # -------------------------------------------------------------------------
    # modpara
    # -------------------------------------------------------------------------
    def write_modpara_def(
        self,
        filename: str,
        All_N: int,
        Ncond: int | None = None,
        Lanczos_max: int = 2000,
        initial_iv: int = -1,
        exct: int = 1,
        LanczosEps: int = 14,
        LanczosTarget: int = 2,
        LargeValue: int = 50,
        NumAve: int = 5,
        ExpecInterval: int = 20,
        ExpandCoef: int | None = None,
    ) -> None:
        """Write modpara_*.def with header and parameters."""
        if Ncond is None:
            Ncond = All_N
        with open(filename, "w") as f:
            f.write("--------------------  \n")
            f.write("Model_Parameters   0  \n")
            f.write("--------------------  \n")
            f.write("HPhi_Cal_Parameters  \n")
            f.write("--------------------  \n")
            f.write("CDataFileHead  zvo  \n")
            f.write("CParaFileHead  zqp  \n")
            f.write("--------------------  \n")
            f.write(f"Nsite          {All_N}\n")
            f.write(f"Ncond          {Ncond}\n")
            f.write(f"Lanczos_max    {Lanczos_max}   \n")
            f.write(f"initial_iv     {initial_iv}    \n")
            f.write(f"exct           {exct}   \n")
            f.write(f"LanczosEps     {LanczosEps}   \n")
            f.write(f"LanczosTarget  {LanczosTarget}   \n")
            f.write(f"LargeValue     {LargeValue}  \n")
            f.write(f"NumAve         {NumAve}   \n")
            f.write(f"ExpecInterval  {ExpecInterval}  \n")
            if ExpandCoef is not None:
                f.write(f"ExpandCoef     {ExpandCoef}  \n")

    # -------------------------------------------------------------------------
    # locspn
    # -------------------------------------------------------------------------
    def write_locspn_def(self, filename: str, All_N: int) -> None:
        """Write locspn.def listing all sites."""
        with open(filename, "w") as f:
            f.write("===================\n")
            f.write(f"loc {All_N:8d}\n")
            f.write("===================\n")
            f.write("===================\n")
            f.write("===================\n")
            for i in range(All_N):
                f.write(f" {i:8d}  1 \n")

    # =========================
    # Presets: CALCMOD
    # =========================
    def write_calcmod_ed(self, filename: str) -> None:
        """Preset: ED (FullDiag) -> CalcType=2, CalcModel=4, Scalapack=1."""
        self.write_calcmod_def(
            filename=filename,
            calc_type=2,      # FullDiag
            calc_model=4,     # SpinGC (keep identical to your snippet)
            restart=0,
            calc_spec=0,
            calc_eigenvec=0,
            initial_vec_type=0,
            input_eigenvec=0,
            output_eigenvec=0,
            scalapack=1,
        )

    def write_calcmod_cg(self, filename: str) -> None:
        """Preset: CG -> CalcType=3, CalcModel=4."""
        self.write_calcmod_def(
            filename=filename,
            calc_type=3,      # CG
            calc_model=4,
            restart=0,
            calc_spec=0,
            calc_eigenvec=0,
            initial_vec_type=0,
            input_eigenvec=0,
            output_eigenvec=0,
            scalapack=1,
        )

    def write_calcmod_tpq(self, filename: str) -> None:
        """Preset: TPQ (your snippet uses CalcType=5)"""
        self.write_calcmod_def(
            filename=filename,
            calc_type=5,      # <- keep exactly as in your snippet
            calc_model=4,
            restart=0,
            calc_spec=0,
            calc_eigenvec=0,
            initial_vec_type=-1,
            input_eigenvec=0,
            output_eigenvec=0,
            scalapack=None,   # not printed in your snippet
        )

    # =========================
    # Presets: MODPARA
    # =========================
    def write_modpara_ed(self, filename: str, All_N: int) -> None:
        """Preset: ED modpara (exactly matches your snippet)."""
        self.write_modpara_def(
            filename=filename,
            All_N=All_N,
            Ncond=All_N,
            Lanczos_max=2000,
            initial_iv=-1,
            exct=50,
            LanczosEps=14,
            LanczosTarget=2,
            LargeValue=30,
            NumAve=5,
            ExpecInterval=20,
            ExpandCoef=None,
        )

    def write_modpara_cg(self, filename: str, All_N: int, exct: int) -> None:
        """Preset: CG modpara (exct only differs; keep others same as ED)."""
        self.write_modpara_def(
            filename=filename,
            All_N=All_N,
            Ncond=All_N,
            Lanczos_max=2000,
            initial_iv=-1,
            exct=exct,
            LanczosEps=14,
            LanczosTarget=2,
            LargeValue=30,
            NumAve=5,
            ExpecInterval=20,
            ExpandCoef=None,
        )
    def write_modpara_tpq(
        self,
        filename: str,
        All_N: int,
        *,
        Ncond: int | None = None,
        Lanczos_max: int = 6000,
        initial_iv: int = 122,
        exct: int = 50,
        LanczosEps: int = 14,
        LanczosTarget: int = 2,
        LargeValue: int = 50,
        NumAve: int = 50,
        ExpecInterval: int = 100,
        ExpandCoef: int = 6,
    ) -> None:
        """Preset: TPQ modpara (all params overridable, defaults match your snippet)."""
        if Ncond is None:
            Ncond = All_N
        self.write_modpara_def(
            filename=filename,
            All_N=All_N,
            Ncond=Ncond,
            Lanczos_max=Lanczos_max,
            initial_iv=initial_iv,
            exct=exct,
            LanczosEps=LanczosEps,
            LanczosTarget=LanczosTarget,
            LargeValue=LargeValue,
            NumAve=NumAve,
            ExpecInterval=ExpecInterval,
            ExpandCoef=ExpandCoef,
        )

    # =========================
    # Optional: one-shot bundles
    # =========================
    def write_bundle(
        self,
        outdir: str,
        All_N: int,
        variant: str,  # "ed" | "cg" | "tpq"
        *,
        # ---- namelist optional entries (default None means skipped) ----
        locspin: str | None = "locspn.def",
        trans: str | None = None,
        ising: str | None = None,
        exchange: str | None = None,
        pairlift: str | None = None,
        interall: str | None = None,
        onebodyg: str | None = None,
        twobodyg: str | None = None,
        threebodyg: str | None = None,
        sixbodyg: str | None = None,
        extras: dict[str, str | None] | None = None,

        # ---- override file names (if you want custom names) ----
        modpara_filename: Optional[str] = None,
        calcmod_filename: Optional[str] = None,
        namelist_filename: Optional[str] = None,

        # ---- overrides for parameters (if you don’t want presets) ----
        modpara_overrides: dict | None = None,
        calcmod_overrides: dict | None = None,
    ) -> None:
        """
        Write calcmod_<variant>.def / modpara_<variant>.def / namelist_<variant>.def.
        The suffix (variant) is the only difference among ed/cg/tpq presets.
        """
        v = variant.lower()
        if v not in {"ed", "cg", "tpq"}:
            raise ValueError(f"variant must be 'ed', 'cg', or 'tpq' (got {variant!r})")

        # --- determine default file names (can be overridden) ---
        modpara_file  = modpara_filename  or f"{outdir}/modpara_{v}.def"
        calcmod_file  = calcmod_filename  or f"{outdir}/calcmod_{v}.def"
        namelist_file = namelist_filename or f"{outdir}/namelist_{v}.def"

        # --- write calcmod ---
        if calcmod_overrides:
            # user-provided overrides go directly to write_calcmod_def
            self.write_calcmod_def(filename=calcmod_file, **calcmod_overrides)
        else:
            # fallback to presets
            if v == "ed":
                self.write_calcmod_ed(calcmod_file)
            elif v == "cg":
                self.write_calcmod_cg(calcmod_file)
            else:  # "tpq"
                self.write_calcmod_tpq(calcmod_file)

        # --- write modpara ---
        if modpara_overrides:
            # user-provided overrides go directly to write_modpara_def
            overrides = {"All_N": All_N, **modpara_overrides}
            overrides.setdefault("Ncond", All_N)
            self.write_modpara_def(filename=modpara_file, **overrides)
        else:
            # fallback to presets
            if v == "ed":
                self.write_modpara_ed(modpara_file, All_N)
            elif v == "cg":
                self.write_modpara_cg(modpara_file, All_N, exct=50)
            else:  # "tpq"
                self.write_modpara_tpq(modpara_file, All_N)

        # --- write namelist ---
        self.write_namelist_def(
            filename=namelist_file,
            modpara=modpara_file.split("/")[-1],  # relative name
            calcmod=calcmod_file.split("/")[-1],
            locspin=locspin,
            trans=trans,
            ising=ising,
            exchange=exchange,
            pairlift=pairlift,
            interall=interall,
            onebodyg=onebodyg,
            twobodyg=twobodyg,
            threebodyg=threebodyg,
            sixbodyg=sixbodyg,
            extras=extras,
        )
