"""
Fanbox camera conversion – parametric 3D-printable parts (CadQuery).

Run:   pip install cadquery
       python cad/halterungen/src/fanbox_teile.py
Output: cad/halterungen/<part>.stl  (print orientation, flat side down)
        cad/halterungen/<part>.step (print orientation)
        cad/halterungen/baugruppe/<part>_eingebaut.step (positioned in frame coordinates,
        for collision checks against the housing STEP)

Frame coordinate system (same as cad/analyse/ANALYSE.md):
  origin = frame centre, X = left/right, Y+ = up, Z+ = towards the viewer.

All values in mm. Values marked ANNAHME come from datasheets/memory and must be
checked against the real parts (print 'testteil' first!).
"""
from pathlib import Path
import cadquery as cq

OUT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------- tolerances
FIT = 0.25            # general clearance for printed fits (Bambu X1C, PETG)

# ---------------------------------------------------------------- housing (from STEP)
Z_FRONT_TOP = 1.74          # top of the original 0.5 mm front plate
TAPE = 0.5                  # double-sided tape under the acrylic  (ANNAHME)
Z_ACRYL_BACK = Z_FRONT_TOP + TAPE   # back face of the 2 mm acrylic motif plate

SPK_BOSSES = [(0.0, 44.45), (0.0, -28.5)]   # old speaker bosses on back housing
Z_SPK_BOSS_TOP = -27.65                     # top face of those bosses
SPK_SCREW_HOLE = 3.0                        # clearance for original M2.6 x 10 screws

PCB_SCREW_BOSSES = [(106.3, -40.5), (106.3, -67.5)]  # flat bosses -> original 1.7 x 5 screws
PCB_PIN_BOSSES = [(74.0, -40.5), (74.0, -67.5)]      # bosses with a 2 mm locating pin on top
PIN_CLEAR = (7.0, 5.0)                                # window in the plate for those pins
Z_PCB_BOSS_TOP = -27.18
PCB_SCREW_HOLE = 2.1                        # clearance for original 1.7 x 5 screws

# ---------------------------------------------------------------- Camera Module 3 (Wide)
CAM_W, CAM_H = 25.0, 24.0                   # PCB size (ANNAHME: official drawing)
CAM_HOLES = [(-10.5, -12.5 + 2.0), (10.5, -12.5 + 2.0), (-10.5, 0.0), (10.5, 0.0)]
#   hole pattern 21 x 12.5 mm, given relative to the LENS centre; the two upper holes
#   are level with the lens centre, the lens sits 9.5 mm below the top edge (ANNAHME)
CAM_LENS_FROM_TOP = 9.5
CAM_HEIGHT = 12.4             # PCB underside -> lens front, Wide version (ANNAHME)
CAM_PILOT = 1.8               # pilot hole for M2 x 6 screws (self-tapping into PETG)
CAM_STANDOFF = 3.0            # room for the FPC connector on the back side
LENS_GAP = 1.5                # lens front -> acrylic back, bridged by a foam ring

# ---------------------------------------------------------------- LED ring (WS2812/WS2813, 16 LED)
RING_OD, RING_ID = 44.5, 31.75   # ANNAHME (Adafruit-size 16-LED ring) - measure yours!
RING_THK = 3.2                   # PCB + LEDs
RING_POST_R = (RING_OD + RING_ID) / 4      # posts sit under the ring PCB
RING_POST_ANGLES = (0, 60, 120, 180)       # deg; below the lens is kept free for the FPC
Z_RING_TOP = Z_ACRYL_BACK - 1.5            # LEDs 1.5 mm behind the acrylic

# ---------------------------------------------------------------- Radar HLK-LD2410C
RADAR_W, RADAR_H = 22.0, 16.0    # ANNAHME (datasheet) - measure yours!
RADAR_CENTER = (0.0, 34.0)       # inside the central tray opening, above the LED ring
Z_RADAR_FRONT = Z_ACRYL_BACK - 3.0
RADAR_PCB = 1.0

# ---------------------------------------------------------------- Raspberry Pi Zero 2 WH
PI_L, PI_W = 65.0, 30.0
PI_HOLE_DX, PI_HOLE_DY = 58.0, 23.0
PI_PILOT = 2.2                   # pilot for M2.5 x 8 screws into PETG
PI_STANDOFF = 4.0
PI_CENTER = (90.0, -48.0)        # long side along Y, ports facing -X (towards battery box)
                                 # (kept clear of the frame screw boss at (88, -88))

# =====================================================================================
def _z_levels():
    z_lens = Z_ACRYL_BACK - LENS_GAP
    z_cam_pcb = z_lens - CAM_HEIGHT
    z_head_top = z_cam_pcb - CAM_STANDOFF
    z_head_bot = z_head_top - HEAD_T
    return z_lens, z_cam_pcb, z_head_top, z_head_bot


HEAD_T = 3.0
HEAD_SCREWS = [(-6.0, -3.0), (6.0, -3.0), (0.0, 34.0)]   # M2.5 x 8, head -> base flange
HEAD_SCREW_CLEAR = 2.9
BASE_RIB_Y = (-12.0, 38.0)        # rib/flange stay clear of both boss screws (screwdriver access)


def kamera_sockel():
    """Base: bridge screwed onto the 2 old speaker bosses (original M2.6 x 10 screws),
    vertical rib and a chamfered flange on top. Printed as installed, no supports."""
    _, _, _, z_head_bot = _z_levels()
    bridge_t = 4.0
    z_bridge_top = Z_SPK_BOSS_TOP + bridge_t
    y0, y1 = SPK_BOSSES[1][1] - 5.0, SPK_BOSSES[0][1] + 5.0
    bridge = (cq.Workplane("XY").workplane(offset=Z_SPK_BOSS_TOP)
              .center(0, (y0 + y1) / 2).rect(12, y1 - y0).extrude(bridge_t))
    for (x, y) in SPK_BOSSES:
        bridge = bridge.cut(cq.Workplane("XY").workplane(offset=Z_SPK_BOSS_TOP - 1)
                            .center(x, y).circle(SPK_SCREW_HOLE / 2).extrude(bridge_t + 2))
    ry0, ry1 = BASE_RIB_Y
    flange_t = 3.0
    z_fl_bot = z_head_bot - flange_t
    rib = (cq.Workplane("XY").workplane(offset=z_bridge_top)
           .center(0, (ry0 + ry1) / 2).rect(8, ry1 - ry0).extrude(z_fl_bot - z_bridge_top))
    # flange 20 mm wide with 45 deg chamfers underneath (printable without supports)
    ch = 6.0
    flange = (cq.Workplane("YZ").workplane(offset=-10)
              .polyline([(ry0, z_fl_bot - ch), (ry1, z_fl_bot - ch), (ry1, z_head_bot), (ry0, z_head_bot)])
              .close().extrude(20))
    wedge_cut = None
    for sgn in (-1, 1):   # cut the lower outer corners at 45 deg
        w = (cq.Workplane("XZ").workplane(offset=-ry1 - 1)
             .polyline([(sgn * 4, z_fl_bot - ch - 0.01), (sgn * 10.01, z_fl_bot - ch - 0.01),
                        (sgn * 10.01, z_fl_bot + 0.01 - 0.0)]).close().extrude(ry1 - ry0 + 2))
        wedge_cut = w if wedge_cut is None else wedge_cut.union(w)
    flange = flange.cut(wedge_cut)
    part = bridge.union(rib).union(flange)
    part = part.cut(cq.Workplane("XY").workplane(offset=z_fl_bot - ch - 1)
                    .pushPoints(HEAD_SCREWS).circle(PI_PILOT / 2).extrude(ch + flange_t + 2))
    return part


def kamera_kopf():
    """Head plate: camera standoffs, LED-ring posts, radar holder.
    Printed with the plate on the bed (as installed), no supports."""
    import math
    _, z_cam_pcb, z_head_top, z_head_bot = _z_levels()
    hy0, hy1 = -24.0, RADAR_CENTER[1] + RADAR_H / 2 + 4
    head = (cq.Workplane("XY").workplane(offset=z_head_bot)
            .center(0, (hy0 + hy1) / 2).rect(54, hy1 - hy0).extrude(HEAD_T))
    # window under the camera's FPC connector so the flat cable can go down
    head = head.cut(cq.Workplane("XY").workplane(offset=z_head_bot - 1)
                    .center(0, -CAM_H + CAM_LENS_FROM_TOP + 2).rect(20, 10).extrude(HEAD_T + 2))
    # screw holes to the base (heads end up under the camera board / under the radar)
    head = head.cut(cq.Workplane("XY").workplane(offset=z_head_bot - 1)
                    .pushPoints(HEAD_SCREWS).circle(HEAD_SCREW_CLEAR / 2).extrude(HEAD_T + 2))
    # camera standoffs
    so = None
    for (x, y) in CAM_HOLES:
        c = (cq.Workplane("XY").workplane(offset=z_head_top)
             .center(x, y).circle(2.4).extrude(CAM_STANDOFF))
        so = c if so is None else so.union(c)
    so = so.cut(cq.Workplane("XY").workplane(offset=z_head_top - 2)
                .pushPoints(CAM_HOLES).circle(CAM_PILOT / 2).extrude(CAM_STANDOFF + 3))
    # LED-ring posts (ring is fixed with small pads of double-sided tape)
    posts = None
    z_ring_bot = Z_RING_TOP - RING_THK
    for a in RING_POST_ANGLES:
        x, y = RING_POST_R * math.cos(math.radians(a)), RING_POST_R * math.sin(math.radians(a))
        p = (cq.Workplane("XY").workplane(offset=z_head_top)
             .center(x, y).rect(5, 5).extrude(z_ring_bot - z_head_top))
        posts = p if posts is None else posts.union(p)
    # radar holder: open rim (module pins/parts on the back stay free)
    z_radar_back = Z_RADAR_FRONT - RADAR_PCB
    rx, ry = RADAR_CENTER
    ow, oh = RADAR_W + 2 * FIT + 4, RADAR_H + 2 * FIT + 4
    rim = (cq.Workplane("XY").workplane(offset=z_head_top).center(rx, ry)
           .rect(ow, oh).extrude(z_radar_back - z_head_top))
    rim = rim.cut(cq.Workplane("XY").workplane(offset=z_head_top).center(rx, ry)
                  .rect(RADAR_W - 3, RADAR_H - 3).extrude(50))
    lip = (cq.Workplane("XY").workplane(offset=z_radar_back).center(rx, ry)
           .rect(ow, oh).extrude(RADAR_PCB)
           .cut(cq.Workplane("XY").workplane(offset=z_radar_back - 1).center(rx, ry)
                .rect(RADAR_W + 2 * FIT, RADAR_H + 2 * FIT).extrude(5)))
    # gap in the rim for the 5-pin header cable (lower side, towards the lens)
    cablegap = (cq.Workplane("XY").workplane(offset=z_head_top + 3).center(rx, ry - oh / 2)
                .rect(14, 6).extrude(50))
    part = head.union(so).union(posts).union(rim).union(lip).cut(cablegap)
    return part


def pi_platte():
    """Plate for the Pi Zero 2 WH; screws onto the 4 old PCB bosses (original screws)."""
    t = 2.0       # plate thickness at the screws (original 1.7 x 5 screws!)
    rib_h = 3.0   # stiffening ribs on top
    px, py = PI_CENTER
    w, l = 40.0, 70.0
    plate = (cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP)
             .center(px, py).rect(w, l).extrude(t))
    # stiffening frame
    frame = (cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP + t)
             .center(px, py).rect(w, l).extrude(rib_h)
             .cut(cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP + t - 1)
                  .center(px, py).rect(w - 6, l - 6).extrude(rib_h + 2)))
    plate = plate.union(frame)
    # screw holes + head clearance in the frame
    for (x, y) in PCB_SCREW_BOSSES:
        plate = plate.cut(cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP - 1)
                          .center(x, y).circle(PCB_SCREW_HOLE / 2).extrude(t + 2))
        plate = plate.cut(cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP + t)
                          .center(x, y).circle(3.2).extrude(rib_h + 1))
    for (x, y) in PCB_PIN_BOSSES:   # locating pins pass through -> plate cannot shift
        plate = plate.cut(cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP - 1)
                          .center(x + 1.0, y).rect(*PIN_CLEAR).extrude(t + rib_h + 2))
    # Pi standoffs (Pi long side along Y)
    holes = [(px + sx * PI_HOLE_DY / 2, py + sy * PI_HOLE_DX / 2) for sx in (-1, 1) for sy in (-1, 1)]
    for (x, y) in holes:
        plate = plate.union(cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP + t)
                            .center(x, y).circle(3.0).extrude(PI_STANDOFF))
    plate = plate.cut(cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP + 0.6)
                      .pushPoints(holes).circle(PI_PILOT / 2).extrude(t + PI_STANDOFF + 1))
    # cable-tie slots for strain relief of the power cable (+X side, towards the side slot)
    plate = plate.cut(cq.Workplane("XY").workplane(offset=Z_PCB_BOSS_TOP - 1)
                      .pushPoints([(px + w / 2 - 4, py + 12), (px + w / 2 - 4, py + 4)])
                      .rect(4, 2.5).extrude(t + 2))
    return plate


def testteil():
    """Quick fit test (~15 min): camera + Pi hole patterns, screw holes, radar pocket."""
    base = cq.Workplane("XY").rect(80, 40).extrude(2)
    # camera standoffs (21 x 12.5)
    cam = [(x - 22, y + 6) for (x, y) in CAM_HOLES]
    base = base.union(cq.Workplane("XY").workplane(offset=2).pushPoints(cam).circle(2.4).extrude(3))
    base = base.cut(cq.Workplane("XY").workplane(offset=0.6).pushPoints(cam)
                    .circle(CAM_PILOT / 2).extrude(6))
    # two Pi standoffs (23 mm spacing)
    pi = [(12, -11.5 + 6), (12, 11.5 + 6)]
    base = base.union(cq.Workplane("XY").workplane(offset=2).pushPoints(pi).circle(3).extrude(4))
    base = base.cut(cq.Workplane("XY").workplane(offset=0.6).pushPoints(pi)
                    .circle(PI_PILOT / 2).extrude(7))
    # clearance holes: M2.6 speaker screw, 1.7 PCB screw
    base = base.cut(cq.Workplane("XY").pushPoints([(-34, -14)]).circle(SPK_SCREW_HOLE / 2).extrude(5))
    base = base.cut(cq.Workplane("XY").pushPoints([(-26, -14)]).circle(PCB_SCREW_HOLE / 2).extrude(5))
    base = base.cut(cq.Workplane("XY").center(-30, -5).rect(*PIN_CLEAR).extrude(5))
    # radar pocket
    rp = (24, -8)
    base = base.union(cq.Workplane("XY").workplane(offset=2).center(*rp)
                      .rect(RADAR_W + 2 * FIT + 4, RADAR_H + 2 * FIT + 4).extrude(2)
                      .cut(cq.Workplane("XY").workplane(offset=1).center(*rp)
                           .rect(RADAR_W + 2 * FIT, RADAR_H + 2 * FIT).extrude(5)))
    base = base.cut(cq.Workplane("XY").workplane(offset=-1).center(*rp)
                    .rect(RADAR_W - 3, RADAR_H - 3).extrude(5))
    return base


def zentrier_schablone():
    """Thin template 226 x 226 mm laid into the frame pocket: marks the exact centre
    (camera window) on the front/fabric and helps positioning the acrylic plate."""
    s = 226.4 - 2 * FIT
    t = 0.8
    outer = cq.Workplane("XY").rect(s, s).extrude(t)
    outer = outer.cut(cq.Workplane("XY").rect(s - 20, s - 20).extrude(t + 1))
    arms = (cq.Workplane("XY").rect(s - 2, 12).extrude(t)
            .union(cq.Workplane("XY").rect(12, s - 2).extrude(t)))
    hub = cq.Workplane("XY").circle(16).extrude(t)
    part = outer.union(arms).union(hub)
    part = part.cut(cq.Workplane("XY").circle(14.0 / 2).extrude(t + 1))   # hole to cut in fabric
    part = part.cut(cq.Workplane("XY").center(*RADAR_CENTER).rect(6, 6).extrude(t + 1))  # radar mark
    # "OBEN" marker notch on the top arm
    part = part.cut(cq.Workplane("XY").center(0, s / 2 - 5).polygon(3, 8).extrude(t + 1))
    return part


# ---------------------------------------------------------------- export
def _to_print(wp, flip=False):
    """Move part so its lowest face is on z=0 (optionally flipped upside down)."""
    shape = wp.val()
    if flip:
        shape = shape.rotate((0, 0, 0), (1, 0, 0), 180)
    bb = shape.BoundingBox()
    return shape.translate((-(bb.xmin + bb.xmax) / 2, -(bb.ymin + bb.ymax) / 2, -bb.zmin))


PARTS = {
    # name: (builder, positioned_in_frame, flip_for_print)
    "kamera_sockel": (kamera_sockel, True, False),
    "kamera_kopf": (kamera_kopf, True, False),
    "pi_platte": (pi_platte, True, False),
    "testteil": (testteil, False, False),
    "zentrier_schablone": (zentrier_schablone, False, False),
}

if __name__ == "__main__":
    (OUT / "baugruppe").mkdir(parents=True, exist_ok=True)
    for name, (fn, positioned, flip) in PARTS.items():
        wp = fn()
        if positioned:
            cq.exporters.export(wp, str(OUT / "baugruppe" / f"{name}_eingebaut.step"))
        pr = _to_print(wp, flip)
        cq.exporters.export(pr, str(OUT / f"{name}.stl"), tolerance=0.02, angularTolerance=0.1)
        cq.exporters.export(pr, str(OUT / f"{name}.step"))
        bb = pr.BoundingBox()
        print(f"{name:20s} {bb.xlen:6.1f} x {bb.ylen:6.1f} x {bb.zlen:5.1f} mm  vol {pr.Volume()/1000:5.1f} cm3")


def export_3mf():
    """Two build plates for Bambu Studio (256 x 256 mm): parts already arranged."""
    plate1 = [("kamera_sockel", (-90, -40)), ("kamera_kopf", (-30, -40)),
              ("pi_platte", (40, -40)), ("testteil", (10, 60))]
    shapes = []
    for name, (x, y) in plate1:
        fn = PARTS[name][0]
        shapes.append(_to_print(fn(), PARTS[name][2]).translate((x + 128, y + 128, 0)))
    cq.exporters.export(cq.Compound.makeCompound(shapes), str(OUT / "druckplatte_1_halterungen.3mf"))
    s = _to_print(zentrier_schablone()).translate((128, 128, 0))
    cq.exporters.export(s, str(OUT / "druckplatte_2_schablone.3mf"))


if __name__ == "__main__":
    export_3mf()
    print("3MF ok")
