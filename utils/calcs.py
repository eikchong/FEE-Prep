"""Pure engineering calculation functions (SI units, Eurocode notation).

Units are stated in every docstring. All functions are side-effect free so they can be
unit-tested (tests/test_calcs.py) and reused to verify question-bank answers.

Values marked NA_DEPENDENT are Nationally Determined Parameters. Defaults follow the
recommended EN values / common UK-NA practice — verify against the Singapore NA.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, asdict

G = 9.81          # m/s²
GAMMA_W = 9.81    # kN/m³
E_STEEL = 210_000  # N/mm² (EN 1993-1-1 3.2.6)
G_STEEL = 81_000   # N/mm²

NA_DEPENDENT = {
    "alpha_cc": "αcc (EC2 3.1.6) — recommended 1.0; UK NA 0.85. Verify against Singapore NA.",
    "gamma_M2": "γM2 (EC3-1-8 2.2) — recommended 1.25. Verify against Singapore NA.",
    "K_prime": "K′ = 0.167 assumes no moment redistribution (δ = 1) — depends on NA δ limits. Verify against Singapore NA.",
    "gamma_M0": "γM0 / γM1 — recommended 1.0. Verify against Singapore NA.",
    "lt_curve": "LTB method 6.3.2.3 (λLT,0 = 0.4, β = 0.75) — NA choice. Verify against Singapore NA.",
}


def _bisect(f, lo, hi, tol=1e-10, maxit=200):
    flo = f(lo)
    for _ in range(maxit):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if abs(fm) < tol or (hi - lo) < tol:
            return mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --------------------------------------------------------------------- soil phase
def soil_phase(Gs: float, e: float, w: float, gamma_w: float = GAMMA_W) -> dict:
    """Phase relations from specific gravity Gs, void ratio e and water content w (decimal).

    Returns S (decimal), n, γd, γ (bulk), γsat, γ′ in kN/m³.
    Se = wGs; γ = (Gs + Se)γw/(1+e).
    """
    if e <= 0 or Gs <= 0 or w < 0:
        raise ValueError("Gs, e must be > 0 and w ≥ 0")
    S = w * Gs / e
    if S > 1 + 1e-9:
        raise ValueError(f"Implied degree of saturation S = {S:.3f} > 1 — inconsistent inputs")
    return {
        "S": S,
        "n": e / (1 + e),
        "gamma_d": Gs * gamma_w / (1 + e),
        "gamma": (Gs + S * e) * gamma_w / (1 + e),
        "gamma_sat": (Gs + e) * gamma_w / (1 + e),
        "gamma_sub": (Gs - 1) * gamma_w / (1 + e),
    }


def effective_stress(layers: list[tuple[float, float]], z: float, z_w: float,
                     gamma_w: float = GAMMA_W) -> dict:
    """Vertical total/pore/effective stress at depth z (m).

    layers: [(thickness m, unit weight kN/m³), ...] from the surface down
    (use bulk γ above the water table and γsat below). z_w = depth to water table (m).
    """
    sigma, top = 0.0, 0.0
    for t, g in layers:
        dz = max(0.0, min(z, top + t) - top)
        sigma += dz * g
        top += t
        if top >= z:
            break
    u = max(0.0, z - z_w) * gamma_w
    return {"sigma_v": sigma, "u": u, "sigma_v_eff": sigma - u}


def consolidation_time(cv: float, H_dr: float, U: float) -> float:
    """Time (same time unit as cv) for average degree of consolidation U (decimal).

    Tv = (π/4)U² for U ≤ 0.6, else Tv = 1.781 − 0.933 log10(100(1−U)).  t = Tv·Hdr²/cv
    """
    if U <= 0.6:
        Tv = math.pi / 4 * U ** 2
    else:
        Tv = 1.781 - 0.933 * math.log10(100 * (1 - U))
    return Tv * H_dr ** 2 / cv


# --------------------------------------------------------------------- EC2 beam
def fctm(fck: float) -> float:
    """Mean tensile strength (EC2 Table 3.1), N/mm²."""
    if fck <= 50:
        return 0.30 * fck ** (2 / 3)
    return 2.12 * math.log(1 + (fck + 8) / 10)


def ec2_rect_beam(M_Ed_kNm: float, b: float, d: float, fck: float, fyk: float = 500,
                  d2: float = 50, K_prime: float = 0.167, gamma_s: float = 1.15) -> dict:
    """EC2 rectangular beam (simplified rectangular stress block, αcc = 0.85, γc = 1.5,
    fck ≤ 50). b, d, d2 in mm; M in kNm. Returns K, z, As (tension), As2 (compression), As,min.

    K = M/(b d² fck);  z = d[0.5 + √(0.25 − K/1.134)] ≤ 0.95d
    As = M/(fyd z)  with fyd = fyk/γs  (0.87 fyk)
    If K > K′: As2 = (K − K′) fck b d² / (fyd (d − d2)), As = K′ fck b d²/(fyd z′) + As2
    """
    M = M_Ed_kNm * 1e6
    fyd = fyk / gamma_s
    K = M / (b * d ** 2 * fck)
    as_min = max(0.26 * fctm(fck) / fyk * b * d, 0.0013 * b * d)
    if K <= K_prime:
        z = min(d * (0.5 + math.sqrt(0.25 - K / 1.134)), 0.95 * d)
        As = M / (fyd * z)
        As2 = 0.0
        doubly = False
    else:
        z = d * (0.5 + math.sqrt(0.25 - K_prime / 1.134))
        As2 = (K - K_prime) * fck * b * d ** 2 / (fyd * (d - d2))
        As = K_prime * fck * b * d ** 2 / (fyd * z) + As2
        doubly = True
    x = (d - z) / 0.4
    return {"K": K, "K_prime": K_prime, "z": z, "z_over_d": z / d, "x": x, "As": As,
            "As2": As2, "As_min": as_min, "As_req": max(As, as_min), "doubly": doubly,
            "fyd": fyd}


def ec2_short_column_axial(N_Ed_kN: float, b: float, h: float, fck: float,
                           fyk: float = 500, Es: float = 200_000, eps_c2: float = 0.002) -> dict:
    """Area of steel for a short column under pure axial load (EC2 3.1.7, 6.1(5)).

    N_Rd = 0.567 fck Ac + σs As, with σs = min(fyk/1.15, Es·εc2) = 400 N/mm² for B500.
    (Many UK texts use 0.87 fyk — slightly unconservative for pure compression.)
    """
    Ac = b * h
    sigma_s = min(fyk / 1.15, Es * eps_c2)
    N = N_Ed_kN * 1e3
    conc = 0.567 * fck * Ac
    As = max(0.0, (N - conc) / (sigma_s - 0.567 * fck))  # deduct concrete displaced by steel
    As_gross = max(0.0, (N - conc) / sigma_s)
    return {"Ac": Ac, "sigma_s": sigma_s, "N_conc_kN": conc / 1e3, "As": As, "As_simple": As_gross}


def ec2_min_eccentricity(h: float) -> float:
    """e0 = max(h/30, 20 mm) — EC2 6.1(4). h in mm, returns mm."""
    return max(h / 30, 20.0)


# --------------------------------------------------------------------- EC3
def ec3_epsilon(fy: float) -> float:
    return math.sqrt(235 / fy)


def ec3_Mc_Rd(W_mm3: float, fy: float, gamma_M0: float = 1.0) -> float:
    """Mc,Rd = W fy / γM0 (EC3 6.2.5) — use Wpl for Class 1/2, Wel for Class 3. Returns kNm."""
    return W_mm3 * fy / gamma_M0 / 1e6


def ec3_Av_rolled_I(A: float, b: float, tf: float, tw: float, r: float, hw: float,
                    eta: float = 1.0) -> float:
    """Shear area of rolled I/H section, load parallel to web (EC3 6.2.6(3)a), mm²."""
    return max(A - 2 * b * tf + (tw + 2 * r) * tf, eta * hw * tw)


def ec3_Vpl_Rd(Av: float, fy: float, gamma_M0: float = 1.0) -> float:
    """Vpl,Rd = Av (fy/√3)/γM0 (EC3 6.2.6), kN."""
    return Av * fy / math.sqrt(3) / gamma_M0 / 1e3


def euler_Ncr(E: float, I: float, L_cr: float) -> float:
    """Ncr = π² E I / Lcr². E in N/mm², I in mm⁴, Lcr in mm. Returns kN."""
    return math.pi ** 2 * E * I / L_cr ** 2 / 1e3


def ec3_flexural_buckling(A: float, fy: float, L_cr: float, i: float, alpha: float,
                          gamma_M1: float = 1.0) -> dict:
    """Flexural buckling resistance (EC3 6.3.1). L_cr, i in mm; A mm². Returns Nb,Rd kN."""
    lam1 = math.pi * math.sqrt(E_STEEL / fy)
    lam = L_cr / i / lam1
    phi = 0.5 * (1 + alpha * (lam - 0.2) + lam ** 2)
    chi = min(1.0, 1 / (phi + math.sqrt(phi ** 2 - lam ** 2)))
    return {"lambda1": lam1, "lambda_bar": lam, "Phi": phi, "chi": chi,
            "Nb_Rd": chi * A * fy / gamma_M1 / 1e3}


def ec3_Mcr(L: float, Iz: float, It: float, Iw: float, C1: float = 1.0,
            E: float = E_STEEL, Gm: float = G_STEEL, k: float = 1.0, kw: float = 1.0) -> float:
    """Elastic critical LTB moment, doubly-symmetric section, load at shear centre (kNm).

    Mcr = C1 π²EIz/(kL)² · √[(k/kw)² Iw/Iz + (kL)² G It/(π² E Iz)]
    L mm; Iz, It mm⁴; Iw mm⁶.
    """
    kL = k * L
    a = math.pi ** 2 * E * Iz / kL ** 2
    return C1 * a * math.sqrt((k / kw) ** 2 * Iw / Iz + kL ** 2 * Gm * It / (math.pi ** 2 * E * Iz)) / 1e6


def ec3_ltb_rolled(Wy: float, fy: float, Mcr_kNm: float, h_over_b: float,
                   gamma_M1: float = 1.0, lam_LT0: float = 0.4, beta: float = 0.75) -> dict:
    """LTB reduction for rolled sections (EC3 6.3.2.3, without f-modification).

    Curve b (α=0.34) if h/b ≤ 2, else curve c (α=0.49). Returns Mb,Rd (kNm).
    """
    alpha = 0.34 if h_over_b <= 2 else 0.49
    lam = math.sqrt(Wy * fy / (Mcr_kNm * 1e6))
    phi = 0.5 * (1 + alpha * (lam - lam_LT0) + beta * lam ** 2)
    chi = 1 / (phi + math.sqrt(phi ** 2 - beta * lam ** 2))
    chi = min(chi, 1.0, 1 / lam ** 2)
    return {"alpha_LT": alpha, "lambda_LT": lam, "Phi_LT": phi, "chi_LT": chi,
            "Mb_Rd": chi * Wy * fy / gamma_M1 / 1e6}


def ec3_bolt_shear(fub: float, As: float, alpha_v: float = 0.6, gamma_M2: float = 1.25,
                   n_planes: int = 1) -> float:
    """Fv,Rd = αv fub A / γM2 per shear plane (EC3-1-8 Table 3.4), kN.

    αv = 0.6 for 4.6, 5.6, 8.8 (threads in plane); 0.5 for 4.8, 5.8, 6.8, 10.9.
    """
    return n_planes * alpha_v * fub * As / gamma_M2 / 1e3


# --------------------------------------------------------------------- EC7
def ec7_bearing_factors(phi_deg: float) -> dict:
    """EC7 Annex D (D.4) drained bearing capacity factors.

    Nq = e^{π tanφ} tan²(45 + φ/2);  Nc = (Nq − 1) cotφ;  Nγ = 2(Nq − 1) tanφ (δ ≥ φ/2).
    """
    p = math.radians(phi_deg)
    Nq = math.exp(math.pi * math.tan(p)) * math.tan(math.pi / 4 + p / 2) ** 2
    Nc = (Nq - 1) / math.tan(p) if phi_deg > 0 else math.pi + 2
    Ng = 2 * (Nq - 1) * math.tan(p)
    return {"Nq": Nq, "Nc": Nc, "Ngamma": Ng}


def phi_design(phi_k_deg: float, gamma_phi: float) -> float:
    """φ′d = atan(tan φ′k / γφ′), degrees."""
    return math.degrees(math.atan(math.tan(math.radians(phi_k_deg)) / gamma_phi))


def strip_bearing_drained(B: float, D: float, gamma: float, phi_deg: float, c: float = 0.0,
                          gamma_eff_below: float | None = None) -> float:
    """Drained bearing resistance per unit area for a strip footing, vertical central load
    (EC7 D.4, s = i = b = 1). q′ = γD. Returns R/A′ in kPa."""
    f = ec7_bearing_factors(phi_deg)
    gb = gamma if gamma_eff_below is None else gamma_eff_below
    q = gamma * D
    return c * f["Nc"] + q * f["Nq"] + 0.5 * gb * B * f["Ngamma"]


def schmertmann_strip(dp: float, sigma_v0: float, sigma_vp: float, B: float,
                      sublayers: list[tuple[float, float, float]], C2: float = 1.0) -> dict:
    """Schmertmann (1978) settlement for a strip footing (L/B ≥ 10).

    dp = net applied pressure (kPa); sigma_v0 = effective overburden at founding level;
    sigma_vp = effective stress at depth of peak Iz (z = B below base).
    sublayers: [(z_top, z_bot, E kPa)] measured below founding level.
    Iz: 0.2 at z=0 → Iz,p at z=B → 0 at z=4B.  s = C1 C2 Δp Σ(Iz/E)Δz  (m).
    """
    Izp = 0.5 + 0.1 * math.sqrt(dp / sigma_vp)
    C1 = max(0.5, 1 - 0.5 * sigma_v0 / dp)

    def Iz(z):
        if z <= B:
            return 0.2 + (Izp - 0.2) * z / B
        if z <= 4 * B:
            return Izp * (4 * B - z) / (3 * B)
        return 0.0

    total, rows = 0.0, []
    for zt, zb, E in sublayers:
        zm = 0.5 * (zt + zb)
        contrib = Iz(zm) / E * (zb - zt)
        rows.append({"z_mid": zm, "Iz": Iz(zm), "E": E, "Iz_dz_over_E": contrib})
        total += contrib
    s = C1 * C2 * dp * total
    return {"Iz_p": Izp, "C1": C1, "C2": C2, "rows": rows, "s_m": s, "s_mm": s * 1000}


def rankine_Ka(phi_deg: float) -> float:
    s = math.sin(math.radians(phi_deg))
    return (1 - s) / (1 + s)


def rankine_Kp(phi_deg: float) -> float:
    return 1 / rankine_Ka(phi_deg)


# --------------------------------------------------------------------- open channels
def trapezoid(b: float, z: float, y: float) -> dict:
    """Trapezoidal section geometry: bottom width b, side slope z (H:1V), depth y (m)."""
    A = (b + z * y) * y
    P = b + 2 * y * math.sqrt(1 + z ** 2)
    T = b + 2 * z * y
    return {"A": A, "P": P, "R": A / P, "T": T, "D": A / T}


def manning_trapezoid(b: float, z: float, y: float, n: float, S0: float) -> dict:
    """Uniform flow by Manning: Q = (1/n) A R^{2/3} S0^{1/2}. Returns geometry + V, Q, Fr."""
    g = trapezoid(b, z, y)
    V = (1 / n) * g["R"] ** (2 / 3) * math.sqrt(S0)
    Q = V * g["A"]
    Fr = V / math.sqrt(G * g["D"])
    return {**g, "V": V, "Q": Q, "Fr": Fr}


def normal_depth_trapezoid(Q: float, b: float, z: float, n: float, S0: float) -> float:
    return _bisect(lambda y: manning_trapezoid(b, z, y, n, S0)["Q"] - Q, 1e-6, 100.0)


def critical_depth_trapezoid(Q: float, b: float, z: float) -> float:
    """Solve Q² T / (g A³) = 1."""
    def f(y):
        g = trapezoid(b, z, y)
        return Q ** 2 * g["T"] / (G * g["A"] ** 3) - 1
    return _bisect(f, 1e-6, 100.0)


def slope_class(yn: float, yc: float) -> str:
    if abs(yn - yc) / yc < 0.01:
        return "Critical (C)"
    return "Mild (M)" if yn > yc else "Steep (S)"


# --------------------------------------------------------------------- hydrology
def rational_Q(C: float, i_mm_h: float, A: float, area_unit: str = "ha") -> float:
    """Peak runoff Q (m³/s). A in ha → Q = CiA/360; A in km² → Q = CiA/3.6."""
    if area_unit == "ha":
        return C * i_mm_h * A / 360
    if area_unit == "km2":
        return C * i_mm_h * A / 3.6
    raise ValueError("area_unit must be 'ha' or 'km2'")


# --------------------------------------------------------------------- traffic
def greenshields(vf: float, kj: float) -> dict:
    """Greenshields linear speed–density. vf km/h, kj veh/km → qmax veh/h, kc, vc."""
    return {"q_max": vf * kj / 4, "k_c": kj / 2, "v_c": vf / 2}


def greenshields_density(q: float, vf: float, kj: float, congested: bool = False) -> float:
    """Density for a given flow q (veh/h) from q = vf k (1 − k/kj)."""
    disc = 1 - 4 * q / (vf * kj)
    if disc < -1e-12:
        raise ValueError("Flow exceeds capacity q_max")
    root = math.sqrt(max(0.0, disc))
    return kj / 2 * (1 + root) if congested else kj / 2 * (1 - root)


def shockwave_speed(q1: float, k1: float, q2: float, k2: float) -> float:
    """uw = (q2 − q1)/(k2 − k1) km/h (negative = moving upstream)."""
    return (q2 - q1) / (k2 - k1)


def aashto_ssd(V_kmh: float, t_s: float = 2.5, a: float = 3.4, grade: float = 0.0) -> dict:
    """AASHTO stopping sight distance (m). Level: 0.278Vt + 0.039V²/a.
    With grade G (decimal, + uphill): braking = V²/(254 (a/9.81 + G))."""
    d_r = 0.278 * V_kmh * t_s
    if grade == 0:
        d_b = 0.039 * V_kmh ** 2 / a
    else:
        d_b = V_kmh ** 2 / (254 * (a / 9.81 + grade))
    return {"reaction": d_r, "braking": d_b, "SSD": d_r + d_b}


# --------------------------------------------------------------------- environmental
def clarifier(Q_m3d: float, overflow_rate: float, detention_h: float) -> dict:
    """Circular primary clarifier sizing: A = Q/OR, D = √(4A/π), depth = Q·t/A."""
    A = Q_m3d / overflow_rate
    V = Q_m3d * detention_h / 24
    return {"A": A, "D": math.sqrt(4 * A / math.pi), "V": V, "depth": V / A}


def activated_sludge(Q_m3d: float, S0_mgL: float, FM: float, X_mgL: float,
                     Qw_m3d: float | None = None, Xr_mgL: float | None = None,
                     Qe_m3d: float = 0.0, Xe_mgL: float = 0.0) -> dict:
    """Aeration tank volume from F/M; HRT; SRT θc = VX/(Qw Xr + Qe Xe)."""
    V = Q_m3d * S0_mgL / (FM * X_mgL)
    out = {"V": V, "HRT_h": V / Q_m3d * 24}
    if Qw_m3d and Xr_mgL:
        out["SRT_d"] = V * X_mgL / (Qw_m3d * Xr_mgL + Qe_m3d * Xe_mgL)
    return out


@dataclass
class Result:
    """Convenience container for UI display."""
    label: str
    value: float
    unit: str = ""

    def as_dict(self):
        return asdict(self)
