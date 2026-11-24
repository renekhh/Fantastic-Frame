import sys
from OCP.BRepTools import BRepTools
from OCP.BRep import BRep_Builder
from OCP.TopoDS import TopoDS_Shape
from OCP.IntCurvesFace import IntCurvesFace_ShapeIntersector
from OCP.gp import gp_Lin, gp_Pnt, gp_Dir
d=sys.argv[1]
idx=dict((p,f) for f,p in (l.split("\t") for l in open(f"{d}/index.txt").read().splitlines()))
def load(name):
    f=[v for k,v in idx.items() if k.endswith(name)][0]
    s=TopoDS_Shape(); BRepTools.Read_s(s,f,BRep_Builder()); return s
parts={n:load(n) for n in ["RAHMEN_GEHRUNG","BOTTOM_HOUSING","HSV/FRONT_PLATE"]}
def ray(p,dirv):
    res={}
    for n,s in parts.items():
        it=IntCurvesFace_ShapeIntersector(); it.Load(s,1e-4)
        it.Perform(gp_Lin(gp_Pnt(*p),gp_Dir(*dirv)),-1e4,1e4)
        res[n]=sorted(round(it.Pnt(i).Coord(dirv.index(1)+1 if 1 in dirv else 1),2) for i in range(1,it.NbPnt()+1))
    return res
for xy in [(60,60),(-60,-30),(100,100),(117,0),(-117,50),(0,-110)]:
    print("Z-ray at",xy, ray((xy[0],xy[1],100),(0,0,1)))
for y,z in [(-52,-30),(-52,-20),(0,-20),(0,-10)]:
    print("X-ray at y,z",(y,z), ray((-200,y,z),(1,0,0)))
