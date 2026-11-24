import sys
sys.argv=[sys.argv[0],sys.argv[1],sys.argv[2]]
exec(open(sys.argv[0].replace("topview.py","section.py")).read().split("def section(")[0])
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
def zsec(z, fn, title):
    pl=gp_Pln(gp_Pnt(0,0,z),gp_Dir(0,0,1))
    fig,ax=plt.subplots(figsize=(10,10)); seen=set()
    for (lab,c),s in shapes:
        sec=BRepAlgoAPI_Section(s,pl,False); sec.Build()
        ex=TopExp_Explorer(sec.Shape(),TopAbs_EDGE)
        while ex.More():
            e=TopoDS.Edge(ex.Current()); cv=BRepAdaptor_Curve(e)
            ud=GCPnts_UniformDeflection(cv,0.05)
            if ud.IsDone():
                pts=[ud.Value(i) for i in range(1,ud.NbPoints()+1)]
                ax.plot([p.X() for p in pts],[p.Y() for p in pts],color=c,lw=0.8,label=None if lab in seen else lab); seen.add(lab)
            ex.Next()
    ax.set_aspect("equal"); ax.set_xlim(-130,130); ax.set_ylim(-130,130); ax.grid(True,lw=0.3)
    ax.set_xlabel("X [mm]"); ax.set_ylabel("Y [mm]"); ax.set_title(title); ax.legend(loc="upper left",fontsize=8)
    fig.tight_layout(); fig.savefig(f"{out}/{fn}",dpi=110); plt.close(fig)
zsec(-30,"draufsicht_z-30.png","Draufsicht: Schnitt bei Z = -30 mm (nahe Rückwand, Blick von vorn)")
zsec(-10,"draufsicht_z-10.png","Draufsicht: Schnitt bei Z = -10 mm (hinter der Frontplatte, Blick von vorn)")
