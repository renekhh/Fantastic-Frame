import sys, pickle
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.TDF import TDF_Label
from OCP.OCP.collections import Sequence_TDF_Label as Seq
from OCP.TDataStd import TDataStd_Name
from OCP.TopLoc import TopLoc_Location
from OCP.BRepTools import BRepTools
from OCP.BRep import BRep_Builder
from OCP.TopoDS import TopoDS_Compound
import os
src, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
doc = TDocStd_Document(TCollection_ExtendedString("doc"))
r = STEPCAFControl_Reader(); r.SetNameMode(True); r.ReadFile(src); r.Transfer(doc)
st = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
def name(l):
    n = TDataStd_Name()
    return n.Get().ToExtString() if l.FindAttribute(TDataStd_Name.GetID_s(), n) else "?"
# leaf parts with path
leaves=[]
def walk(label, loc, path):
    if st.IsReference_s(label):
        ref=TDF_Label(); st.GetReferredShape_s(label, ref)
        loc = loc.Multiplied(st.GetLocation_s(label)); label=ref
    nm=name(label); p=path+[nm]
    if st.IsAssembly_s(label):
        seq=Seq(); st.GetComponents_s(label, seq)
        for i in range(1,seq.Length()+1): walk(seq.Value(i), loc, p)
    else:
        leaves.append(("/".join(p), st.GetShape_s(label).Moved(loc)))
roots=Seq(); st.GetFreeShapes(roots)
for i in range(1,roots.Length()+1): walk(roots.Value(i), TopLoc_Location(), [])
idx=[]
for k,(p,s) in enumerate(leaves):
    f=f"{outdir}/{k:03d}.brep"; BRepTools.Write_s(s, f); idx.append((p,f))
open(f"{outdir}/index.txt","w").write("\n".join(f"{f}\t{p}" for p,f in idx))
print(len(idx))
