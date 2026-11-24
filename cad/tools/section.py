import sys, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from OCP.BRepTools import BRepTools
from OCP.BRep import BRep_Builder
from OCP.TopoDS import TopoDS_Shape, TopoDS
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE
from OCP.BRepAdaptor import BRepAdaptor_Curve
from OCP.GCPnts import GCPnts_UniformDeflection
d=sys.argv[1]; out=sys.argv[2]
idx=[l.split("\t") for l in open(f"{d}/index.txt").read().splitlines()]
def load(f):
    s=TopoDS_Shape(); BRepTools.Read_s(s,f,BRep_Builder()); return s
def group(p):
    n=p.split("/")[-1]; parts=p.split("/")+["",""]
    if n=="RAHMEN_GEHRUNG": return ("Rahmen (Gehrung)","black")
    if n=="BOTTOM_HOUSING": return ("Rückwand-Gehäuse","tab:blue")
    if n in("FRONT_PLATE","FCSP_FP"): return ("Frontplatte","tab:green")
    if n=="FABRIC": return ("Stoff (Lautsprecher)","tab:olive")
    if parts[2] in ("HSV",) and n=="HSV": return ("Logo-Einsatz (HSV als Beispiel)","tab:orange")
    if parts[2] in ("S04","BVB","BMG","FCB","SGE","FCSP"): return None
    if n=="BATTERY_COVER": return ("Batteriedeckel","tab:cyan")
    if "SCREW" in n or n=="EVA_10" or n=="STICKER": return ("Schrauben/Füße","gray")
    return ("Alte Elektronik (fliegt raus)","tab:red")
shapes=[(group(p),load(f)) for f,p in idx if group(p)]
def section(axis, val, title, fn, xlim, zlim):
    if axis=="y": pl=gp_Pln(gp_Pnt(0,val,0),gp_Dir(0,1,0)); h=0
    else: pl=gp_Pln(gp_Pnt(val,0,0),gp_Dir(1,0,0)); h=1
    fig,ax=plt.subplots(figsize=(14,6)); seen=set()
    for (lab,c),s in shapes:
        sec=BRepAlgoAPI_Section(s,pl,False); sec.ComputePCurveOn1(True); sec.Approximation(True); sec.Build()
        ex=TopExp_Explorer(sec.Shape(),TopAbs_EDGE)
        while ex.More():
            e=TopoDS.Edge(ex.Current()); cv=BRepAdaptor_Curve(e)
            ud=GCPnts_UniformDeflection(cv,0.05)
            if ud.IsDone():
                pts=[ud.Value(i) for i in range(1,ud.NbPoints()+1)]
                xs=[(p.X() if h==0 else p.Y()) for p in pts]; zs=[p.Z() for p in pts]
                ax.plot(xs,zs,color=c,lw=0.8,label=None if lab in seen else lab); seen.add(lab)
            ex.Next()
    ax.set_aspect("equal"); ax.set_xlim(*xlim); ax.set_ylim(*zlim); ax.grid(True,lw=0.3)
    ax.set_xlabel("X [mm]" if h==0 else "Y [mm]"); ax.set_ylabel("Z [mm]  (oben = Front/Betrachter)")
    ax.set_title(title); ax.legend(loc="upper left",fontsize=8,ncol=3)
    fig.tight_layout(); fig.savefig(f"{out}/{fn}",dpi=110); plt.close(fig)
os.makedirs(out,exist_ok=True)
for v in (0,-70,60):
    section("y",v,f"Schnitt bei Y = {v} mm (Blick von unten)",f"schnitt_y{v}.png",(-130,130),(-45,20))
for v in (0,110,-110):
    section("x",v,f"Schnitt bei X = {v} mm (Blick von der Seite)",f"schnitt_x{v}.png",(-130,130),(-45,20))
