"""
Print template for the 2 mm acrylic motif plate (UV print shop).

Run:  python cad/druckvorlage/src/druckvorlage.py
Out:  cad/druckvorlage/fanbox_motivplatte_vorlage.svg   (layers, for Inkscape/Illustrator/Affinity)
      cad/druckvorlage/fanbox_motivplatte_vorlage.pdf   (overview to print 1:1 / send to the shop)
      cad/druckvorlage/fanbox_weissmaske.svg            (white layer only, black = white ink)

Geometry is taken from cad/halterungen/src/fanbox_teile.py so camera, LED ring and radar
always match the printed carrier.
"""
import importlib.util, math
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("t", HERE.parent / "halterungen/src/fanbox_teile.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)

SIZE = 226.4          # final plate size (pocket in the frame)
BLEED = 3.0           # bleed on each side
W = SIZE + 2 * BLEED
C = W / 2             # centre in SVG coordinates (y axis points down in SVG!)

WINDOW_D = 12.0       # clear, completely unprinted camera window
LED_R0 = T.RING_ID / 2 - 1.0     # LED zone: colour only, NO white -> glows when LED is on
LED_R1 = T.RING_OD / 2 + 1.0
PUPIL_D = 64.0        # recommended pupil size (black) - camera window sits in the middle
IRIS_D = 200.0        # recommended iris size
TAPE_BORDER = 12.0    # double-sided tape only in this border zone (old front plate exists there)

rx, ry = T.RADAR_CENTER


def svg_y(y):           # frame Y (up) -> SVG y (down)
    return C - y


def layer(id_, label, body, visible=True):
    style = "" if visible else ' style="display:none"'
    return (f'<g inkscape:groupmode="layer" id="{id_}" inkscape:label="{label}"{style}>\n'
            f'{body}\n</g>\n')


def ring_path(cx, cy, r0, r1):
    return (f'M {cx + r1} {cy} A {r1} {r1} 0 1 0 {cx - r1} {cy} A {r1} {r1} 0 1 0 {cx + r1} {cy} Z '
            f'M {cx + r0} {cy} A {r0} {r0} 0 1 1 {cx - r0} {cy} A {r0} {r0} 0 1 1 {cx + r0} {cy} Z')


def build_svg(white_only=False):
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
            f'width="{W}mm" height="{W}mm" viewBox="0 0 {W} {W}">\n')
    s0, s1 = BLEED, BLEED + SIZE
    # white mask = full bleed square minus camera window minus LED zone (evenodd)
    wr = WINDOW_D / 2
    white = (f'<path fill="#000000" fill-rule="evenodd" d="M 0 0 H {W} V {W} H 0 Z '
             f'M {C + wr} {C} A {wr} {wr} 0 1 0 {C - wr} {C} A {wr} {wr} 0 1 0 {C + wr} {C} Z '
             f'{ring_path(C, C, LED_R0, LED_R1).split(" Z ")[0]} Z '
             f'{ring_path(C, C, LED_R0, LED_R1).split(" Z ")[1]}"/>')
    if white_only:
        return head + layer("weiss", "WEISS (Spot-Farbe White) - schwarz = weiss drucken", white) + "</svg>\n"

    motiv = (f'<rect x="0" y="0" width="{W}" height="{W}" fill="#ffffff"/>\n'
             f'<circle cx="{C}" cy="{C}" r="{IRIS_D / 2}" fill="#6fa3b8" opacity="0.35"/>\n'
             f'<circle cx="{C}" cy="{C}" r="{PUPIL_D / 2}" fill="#000000" opacity="0.6"/>\n'
             f'<text x="{C}" y="{C - IRIS_D / 2 + 18}" font-size="7" text-anchor="middle" '
             f'font-family="sans-serif">PLATZHALTER - eigenes Motiv hier einsetzen</text>')
    hilfe = (f'<rect x="{s0}" y="{s0}" width="{SIZE}" height="{SIZE}" fill="none" stroke="#ff00ff" stroke-width="0.3"/>\n'
             f'<rect x="{s0 + TAPE_BORDER}" y="{s0 + TAPE_BORDER}" width="{SIZE - 2 * TAPE_BORDER}" '
             f'height="{SIZE - 2 * TAPE_BORDER}" fill="none" stroke="#ff9900" stroke-width="0.3" stroke-dasharray="3 2"/>\n'
             f'<circle cx="{C}" cy="{C}" r="{IRIS_D / 2}" fill="none" stroke="#0077ff" stroke-width="0.3" stroke-dasharray="2 2"/>\n'
             f'<circle cx="{C}" cy="{C}" r="{PUPIL_D / 2}" fill="none" stroke="#0077ff" stroke-width="0.3" stroke-dasharray="2 2"/>\n'
             f'<path d="M {C - 6} {C} H {C + 6} M {C} {C - 6} V {C + 6}" stroke="#ff0000" stroke-width="0.2"/>\n'
             f'<rect x="{C + rx - T.RADAR_W / 2}" y="{svg_y(ry) - T.RADAR_H / 2}" width="{T.RADAR_W}" '
             f'height="{T.RADAR_H}" fill="none" stroke="#996633" stroke-width="0.3" stroke-dasharray="1 1"/>\n'
             f'<text x="{C}" y="{svg_y(ry) - T.RADAR_H / 2 - 1.5}" font-size="3" text-anchor="middle" '
             f'font-family="sans-serif" fill="#996633">Radar dahinter: keine Metallic-Farben</text>\n'
             f'<text x="{s0 + 2}" y="{s0 + TAPE_BORDER - 3}" font-size="3.5" font-family="sans-serif" '
             f'fill="#ff9900">Klebeband nur im Randstreifen (12 mm)</text>\n'
             f'<text x="{C}" y="{C + PUPIL_D / 2 + 5}" font-size="3.5" text-anchor="middle" '
             f'font-family="sans-serif" fill="#0077ff">Pupille Ø {PUPIL_D:.0f} mm / Iris Ø {IRIS_D:.0f} mm (Empfehlung)</text>\n'
             f'<text x="{C}" y="{s0 + 6}" font-size="4" text-anchor="middle" font-family="sans-serif" '
             f'fill="#ff00ff">▲ OBEN</text>')
    # crop marks outside the trim box
    cm = ""
    for x in (s0, s1):
        cm += f'<path d="M {x} 0 V {BLEED - 0.5} M {x} {W} V {W - BLEED + 0.5}" stroke="#000" stroke-width="0.2"/>\n'
    for y in (s0, s1):
        cm += f'<path d="M 0 {y} H {BLEED - 0.5} M {W} {y} H {W - BLEED + 0.5}" stroke="#000" stroke-width="0.2"/>\n'
    zonen = (f'<circle cx="{C}" cy="{C}" r="{WINDOW_D / 2}" fill="none" stroke="#00aa00" stroke-width="0.4"/>\n'
             f'<path d="{ring_path(C, C, LED_R0, LED_R1)}" fill="#ff0000" fill-opacity="0.25" '
             f'fill-rule="evenodd" stroke="#ff0000" stroke-width="0.2"/>\n'
             f'<text x="{C}" y="{C - LED_R1 - 1.5}" font-size="3" text-anchor="middle" font-family="sans-serif" '
             f'fill="#cc0000">LED-Zone: Farbe ohne Weiß (leuchtet durch)</text>\n'
             f'<text x="{C}" y="{C + WINDOW_D / 2 + 3.5}" font-size="2.6" text-anchor="middle" '
             f'font-family="sans-serif" fill="#00aa00">Kamera-Fenster Ø {WINDOW_D:.0f}: KEINE Farbe</text>')
    return (head
            + layer("motiv", "MOTIV (Bild hier einfügen, bis Beschnitt)", motiv)
            + layer("weiss", "WEISS (Spot-Farbe White)", white.replace('#000000', '#d0d0d0'), visible=False)
            + layer("zonen", "ZONEN - nicht drucken", zonen)
            + layer("hilfe", "HILFSLINIEN - nicht drucken", hilfe + cm)
            + "</svg>\n")


def build_pdf(path):
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle, Rectangle, Wedge
    inch = 25.4
    fig = plt.figure(figsize=(W / inch, W / inch))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(-W / 2, W / 2); ax.set_ylim(-W / 2, W / 2); ax.axis("off")
    ax.add_patch(Rectangle((-SIZE / 2, -SIZE / 2), SIZE, SIZE, fill=False, ec="magenta", lw=0.6))
    ax.add_patch(Rectangle((-SIZE / 2 + TAPE_BORDER, -SIZE / 2 + TAPE_BORDER), SIZE - 2 * TAPE_BORDER,
                           SIZE - 2 * TAPE_BORDER, fill=False, ec="orange", lw=0.6, ls="--"))
    ax.add_patch(Circle((0, 0), IRIS_D / 2, fill=False, ec="tab:blue", ls="--", lw=0.6))
    ax.add_patch(Circle((0, 0), PUPIL_D / 2, color="black", alpha=0.15))
    ax.add_patch(Wedge((0, 0), LED_R1, 0, 360, width=LED_R1 - LED_R0, color="red", alpha=0.3))
    ax.add_patch(Circle((0, 0), WINDOW_D / 2, fill=True, fc="white", ec="green", lw=0.8))
    ax.add_patch(Rectangle((rx - T.RADAR_W / 2, ry - T.RADAR_H / 2), T.RADAR_W, T.RADAR_H,
                           fill=False, ec="brown", ls=":", lw=0.6))
    ax.plot([-6, 6], [0, 0], "r", lw=0.3); ax.plot([0, 0], [-6, 6], "r", lw=0.3)
    t = dict(ha="center", fontsize=6)
    ax.text(0, SIZE / 2 - 8, "▲ OBEN   –   Fanbox Motivplatte 226,4 × 226,4 mm (Maßstab 1:1)", **t, color="magenta")
    ax.text(0, -WINDOW_D / 2 - 4, f"Kamera-Fenster Ø {WINDOW_D:.0f} mm: keine Farbe", **t, color="green")
    ax.text(0, LED_R1 + 2, "LED-Zone: Farbe ohne Weiß", **t, color="red")
    ax.text(0, -PUPIL_D / 2 - 6, f"Pupille Ø {PUPIL_D:.0f} mm  /  Iris Ø {IRIS_D:.0f} mm (Empfehlung)", **t, color="tab:blue")
    ax.text(rx, ry + T.RADAR_H / 2 + 2, "Radar: keine Metallic-Farben", **t, color="brown")
    ax.text(-SIZE / 2 + 2, -SIZE / 2 + 4, "Klebeband nur im 12-mm-Randstreifen", fontsize=6, color="orange")
    ax.text(0, -SIZE / 2 + 4, "Kontrolle: Diese Linie muss 100 mm lang sein →", ha="right", fontsize=5)
    ax.plot([2, 102], [-SIZE / 2 + 5, -SIZE / 2 + 5], "k", lw=0.8)
    fig.savefig(path); plt.close(fig)


if __name__ == "__main__":
    (HERE / "fanbox_motivplatte_vorlage.svg").write_text(build_svg(), encoding="utf-8")
    (HERE / "fanbox_weissmaske.svg").write_text(build_svg(white_only=True), encoding="utf-8")
    build_pdf(HERE / "fanbox_motivplatte_vorlage.pdf")
    print("ok", W, "mm incl. bleed")
