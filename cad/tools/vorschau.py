"""Section/top views of housing + new parts + dummy electronics -> PNG.
Usage: python cad/tools/vorschau.py <brep_dir> <out_dir>"""
import sys, importlib.util
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cadquery as cq
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE
from OCP.TopoDS import TopoDS
from OCP.BRepAdaptor import BRepAdaptor_Curve
from OCP.GCPnts import GCPnts_UniformDeflection

d, out = sys.argv[1], Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
src = open(Path(sys.argv[0]).with_name("kollision.py")).read().split("ok = True")[0]
sys.argv = [str(Path(sys.argv[0]).with_name("kollision.py")), d]
__file__ = sys.argv[0]
exec(src)

col = {"RAHMEN_GEHRUNG": ("Rahmen", "black"), "BOTTOM_HOUSING": ("Rückwand", "tab:blue"),
       "FRONT_PLATE": ("alte Front", "tab:green"), "BATTERY_COVER": ("Batteriedeckel", "tab:cyan")}
layers = [(col[k][0], col[k][1], 0.8, v) for k, v in housing.items() if k in col]
layers += [("NEU: Kamera-Sockel", "tab:orange", 1.6, new["kamera_sockel"]),
           ("NEU: Kamera-Kopf", "gold", 1.6, new["kamera_kopf"]),
           ("NEU: Pi-Platte", "tab:purple", 1.6, new["pi_platte"])]
dcol = {"Kamera (Platine+Objektiv)": "red", "LED-Ring": "magenta", "Radar": "tab:brown",
        "Pi Zero (inkl. Bauteile)": "darkgreen", "Netzstecker am Pi (Micro-USB)": "gray"}
layers += [(k, dcol[k], 1.2, new[k]) for k in dcol]
# acrylic plate
acr = cq.Workplane("XY").workplane(offset=T.Z_ACRYL_BACK).rect(226.4, 226.4).extrude(2.0).val()
layers.append(("Acrylplatte 2 mm (Motiv)", "deepskyblue", 1.2, acr))

def plot(pl, hor, xlim, ylim, title, fn, figsize):
    fig, ax = plt.subplots(figsize=figsize); seen = set()
    for lab, c, lw, s in layers:
        sec = BRepAlgoAPI_Section(s.wrapped, pl, False); sec.Build()
        ex = TopExp_Explorer(sec.Shape(), TopAbs_EDGE)
        while ex.More():
            cv = BRepAdaptor_Curve(TopoDS.Edge(ex.Current()))
            ud = GCPnts_UniformDeflection(cv, 0.05)
            if ud.IsDone():
                pts = [ud.Value(i) for i in range(1, ud.NbPoints() + 1)]
                ax.plot([hor(p)[0] for p in pts], [hor(p)[1] for p in pts], color=c, lw=lw,
                        label=None if lab in seen else lab); seen.add(lab)
            ex.Next()
    ax.set_aspect("equal"); ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.grid(True, lw=0.3)
    ax.set_title(title); ax.legend(loc="lower left", fontsize=7, ncol=3)
    fig.tight_layout(); fig.savefig(out / fn, dpi=110); plt.close(fig)

plot(gp_Pln(gp_Pnt(0, 0, 0), gp_Dir(1, 0, 0)), lambda p: (p.Y(), p.Z()), (-60, 70), (-42, 8),
     "Seitenschnitt X = 0: Kamera, LED-Ring, Radar (oben = Front)", "neu_schnitt_x0.png", (13, 4.5))
plot(gp_Pln(gp_Pnt(0, 0, 0), gp_Dir(0, 1, 0)), lambda p: (p.X(), p.Z()), (-40, 125), (-42, 8),
     "Querschnitt Y = 0: Kamera und Pi-Bereich", "neu_schnitt_y0.png", (13, 4.5))
plot(gp_Pln(gp_Pnt(0, -48, 0), gp_Dir(0, 1, 0)), lambda p: (p.X(), p.Z()), (40, 125), (-42, 8),
     "Querschnitt Y = -48: Raspberry Pi auf Pi-Platte", "neu_schnitt_y-48.png", (10, 4.5))
plot(gp_Pln(gp_Pnt(0, 0, -20), gp_Dir(0, 0, 1)), lambda p: (p.X(), p.Y()), (-128, 128), (-128, 128),
     "Draufsicht (Schnitt Z = -20 mm, Blick von vorn)", "neu_draufsicht_z-20.png", (10, 10))
plot(gp_Pln(gp_Pnt(0, 0, -1.5), gp_Dir(0, 0, 1)), lambda p: (p.X(), p.Y()), (-60, 60), (-50, 60),
     "Detail Bildmitte (Schnitt Z = -1,5 mm): Kamera, LED-Ring, Radar", "neu_detail_mitte.png", (8, 7.5))
print("ok")
