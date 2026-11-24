"""Collision check: new parts (+ dummy electronics) vs. housing parts from the STEP.
Usage: python cad/tools/kollision.py <brep_dir from load.py>"""
import sys, importlib.util, math
from pathlib import Path
import cadquery as cq
from OCP.BRepTools import BRepTools
from OCP.BRep import BRep_Builder
from OCP.TopoDS import TopoDS_Shape

d = sys.argv[1]
spec = importlib.util.spec_from_file_location("t", Path(__file__).parents[1] / "halterungen/src/fanbox_teile.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)

idx = [l.split("\t") for l in open(f"{d}/index.txt").read().splitlines()]
def load(f):
    s = TopoDS_Shape(); BRepTools.Read_s(s, f, BRep_Builder()); return cq.Shape.cast(s)
keep = ("RAHMEN_GEHRUNG", "BOTTOM_HOUSING", "HSV/FRONT_PLATE", "BATTERY_COVER/BATTERY_COVER")
housing = {p.split("/")[-1]: load(f) for f, p in idx if p.endswith(keep)}
# frame-to-back screws stay in place
# frame-to-back screws stay; the 2 old speaker screws are re-used through the camera carrier
screws = [sc for sc in (load(f) for f, p in idx if p == "00_FANTASTIC_FRAME/SCREW_M2D6X10")
          if not (abs(sc.Center().x) < 1 and (abs(sc.Center().y - 44.45) < 1 or abs(sc.Center().y + 28.5) < 1))]

z_lens = T.Z_ACRYL_BACK - T.LENS_GAP
z_pcb = z_lens - T.CAM_HEIGHT
cam_cy = -(T.CAM_H / 2 - T.CAM_LENS_FROM_TOP)
dummies = {
    "Kamera (Platine+Objektiv)": cq.Workplane("XY").workplane(offset=z_pcb).center(0, cam_cy)
        .rect(T.CAM_W, T.CAM_H).extrude(1.0).union(
        cq.Workplane("XY").workplane(offset=z_pcb).rect(9, 9).extrude(T.CAM_HEIGHT)),
    "LED-Ring": cq.Workplane("XY").workplane(offset=T.Z_RING_TOP - T.RING_THK)
        .circle(T.RING_OD / 2).circle(T.RING_ID / 2).extrude(T.RING_THK),
    "Radar": cq.Workplane("XY").workplane(offset=T.Z_RADAR_FRONT - T.RADAR_PCB).center(*T.RADAR_CENTER)
        .rect(T.RADAR_W, T.RADAR_H).extrude(T.RADAR_PCB).union(
        cq.Workplane("XY").workplane(offset=T.Z_RADAR_FRONT - T.RADAR_PCB - 4).center(*T.RADAR_CENTER)
        .rect(T.RADAR_W - 4, T.RADAR_H - 4).extrude(4)),
    "Pi Zero (inkl. Bauteile)": cq.Workplane("XY").workplane(offset=T.Z_PCB_BOSS_TOP + 2 + T.PI_STANDOFF)
        .center(*T.PI_CENTER).rect(T.PI_W, T.PI_L).extrude(6),
    "Netzstecker am Pi (Micro-USB)": cq.Workplane("XY").workplane(offset=T.Z_PCB_BOSS_TOP + 2 + T.PI_STANDOFF + 1)
        .center(T.PI_CENTER[0] - T.PI_W / 2 - 10, T.PI_CENTER[1] - T.PI_L / 2 + 54).rect(20, 11).extrude(7.5),
}
new = {"kamera_sockel": T.kamera_sockel().val(), "kamera_kopf": T.kamera_kopf().val(), "pi_platte": T.pi_platte().val()}
new.update({k: v.val() for k, v in dummies.items()})

ok = True
for n, s in new.items():
    for hn, h in list(housing.items()) + [(f"Schraube{i}", sc) for i, sc in enumerate(screws)]:
        try:
            v = s.intersect(h).Volume()
        except Exception as e:
            v = float("nan")
        if v > 0.5 or v != v:   # < 0.5 mm3 = touching faces (part sits on a boss)
            ok = False
            print(f"KOLLISION  {n:32s} <-> {hn:22s} {v:8.2f} mm3")
            for so in s.intersect(h).Solids():
                bb = so.BoundingBox()
                print(f"      bei X[{bb.xmin:.1f},{bb.xmax:.1f}] Y[{bb.ymin:.1f},{bb.ymax:.1f}] Z[{bb.zmin:.2f},{bb.zmax:.2f}]")
for a in new:
    for b in new:
        if a < b and {a, b} not in ({"kamera_kopf", "Radar"},):
            v = new[a].intersect(new[b]).Volume()
            if v > 0.01:
                ok = False; print(f"KOLLISION  {a} <-> {b}: {v:.2f} mm3")
print("OK - keine Kollisionen" if ok else "Kollisionen gefunden")
