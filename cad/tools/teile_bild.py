"""Renders the printable parts as a 3D overview image (matplotlib)."""
import importlib.util, sys
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("t", root / "halterungen/src/fanbox_teile.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
names = ["kamera_sockel", "kamera_kopf", "pi_platte", "testteil"]
fig = plt.figure(figsize=(14, 10))
for i, n in enumerate(names):
    fn, _, flip = T.PARTS[n]
    sh = T._to_print(fn(), flip)
    vs, tris = sh.tessellate(0.05, 0.2)
    ax = fig.add_subplot(2, 2, i + 1, projection="3d")
    polys = [[(vs[a].x, vs[a].y, vs[a].z) for a in t] for t in tris]
    pc = Poly3DCollection(polys, facecolor="#f0a030", edgecolor="#704010", linewidths=0.05, alpha=1.0)
    pc.set_facecolor("#f0a030"); ax.add_collection3d(pc)
    bb = sh.BoundingBox(); m = max(bb.xlen, bb.ylen, bb.zlen) / 2
    cx, cy, cz = (bb.xmin + bb.xmax) / 2, (bb.ymin + bb.ymax) / 2, (bb.zmin + bb.zmax) / 2
    ax.set_xlim(cx - m, cx + m); ax.set_ylim(cy - m, cy + m); ax.set_zlim(cz - m, cz + m)
    ax.view_init(elev=35, azim=-60); ax.set_title(f"{n}  ({bb.xlen:.0f} × {bb.ylen:.0f} × {bb.zlen:.0f} mm, Druckausrichtung)")
    ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
fig.tight_layout(); fig.savefig(root / "halterungen/vorschau/teile_3d.png", dpi=90)
print("ok")
