import sys
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.TDF import TDF_Label
from OCP.OCP.collections import Sequence_TDF_Label as TDF_LabelSequence
from OCP.TDataStd import TDataStd_Name
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.TopLoc import TopLoc_Location
import pickle

doc = TDocStd_Document(TCollection_ExtendedString("doc"))
r = STEPCAFControl_Reader(); r.SetNameMode(True)
assert r.ReadFile(sys.argv[1]) == 1
r.Transfer(doc)
st = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
def name(l):
    n = TDataStd_Name()
    if l.FindAttribute(TDataStd_Name.GetID_s(), n): return n.Get().ToExtString()
    return "?"
out=[]
def walk(label, loc, depth):
    ref = TDF_Label()
    if st.IsReference_s(label):
        st.GetReferredShape_s(label, ref)
        loc = loc.Multiplied(st.GetLocation_s(label))
        nm = name(label)+" -> "+name(ref)
        label2 = ref
    else:
        nm = name(label); label2 = label
    shape = st.GetShape_s(label2).Moved(loc)
    b = Bnd_Box(); BRepBndLib.Add_s(shape, b, True)
    mn=b.CornerMin(); mx=b.CornerMax(); x0,y0,z0,x1,y1,z1 = mn.X(),mn.Y(),mn.Z(),mx.X(),mx.Y(),mx.Z()
    out.append((depth, nm, (x0,y0,z0,x1,y1,z1)))
    print("  "*depth + f"{nm:45s} X[{x0:8.2f},{x1:8.2f}] Y[{y0:8.2f},{y1:8.2f}] Z[{z0:8.2f},{z1:8.2f}]  size {x1-x0:6.2f}x{y1-y0:6.2f}x{z1-z0:6.2f}")
    if st.IsAssembly_s(label2):
        seq = TDF_LabelSequence(); st.GetComponents_s(label2, seq)
        for i in range(1, seq.Length()+1):
            walk(seq.Value(i), loc, depth+1)
roots = TDF_LabelSequence(); st.GetFreeShapes(roots)
for i in range(1, roots.Length()+1):
    walk(roots.Value(i), TopLoc_Location(), 0)
