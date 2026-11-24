# Analyse der STEP-Datei `00_fantastic_frame-20260423.stp`

Quelle: `cad/00_fantastic_frame-20260423.zip` (Creo-Baugruppe, 23.04.2026, 80 MB entpackt).
Alle Maße in mm. Ausgewertet per Skript (`cad/tools/`), Werte auf ca. 0,5 mm genau.

## Koordinatensystem
- Ursprung = Mitte des Rahmens.
- **X** = links/rechts, **Y** = unten/oben, **Z+** = Richtung Betrachter (Front).
- Annahme: **Y+ ist oben** (Aufhängung bei Y ≈ +73, Batteriefach unten bei Y ≈ −70).

## Außenmaße
| | Wert |
|---|---|
| Rahmen außen | **250,7 × 250,7 mm** |
| Bildfläche (Frontplatte) | **226,4 × 226,4 mm** |
| Rahmenbreite sichtbar (Front) | ca. 12 mm je Seite |
| Tiefe Rahmen-Vorderkante (Z +6,7) bis Rückseite (Z −42,0) | **ca. 49 mm** |
| Logo-Einsätze ragen nach vorn bis | Z +11 … +15 (S04: bis +43) |

## Aufbau (von vorn nach hinten)
| Teil | Name in STEP | Z-Bereich | Bemerkung |
|---|---|---|---|
| Logo-Relief (wechselbar) | HSV, S04, BVB, BMG, FCB, SGE, FCSP | ca. −6,6 … +15 | 7 Varianten, je eine verbaut |
| Frontplatte (Bild) | FRONT_PLATE / FCSP_FP | +1,24 … +1,74 | 0,5 mm dünn |
| Lautsprecher-Stoff | FABRIC | +0,7 … +1,2 | 98 × 98 mm, Mitte (X −49…49, Y −39…59) |
| Rahmen inkl. Trägerplatte | RAHMEN_GEHRUNG | −28,6 … +7,1 | Trägerplatte Z −0,56 … +1,14 (1,7 mm), Rippen nach hinten bis Z ≈ −5,5 |
| Rückwand-Gehäuse | BOTTOM_HOUSING | −42,0 … −15,0 | Boden innen Z −38,2, Wandstärke 2 mm |

## Freier Innenraum (nach Ausbau der alten Elektronik)
| | Wert |
|---|---|
| Fläche (flacher Boden) | ca. **220 × 220 mm** (X/Y ±110), zum Rand hin gerundet |
| Lichte Höhe zwischen Trägerplatte und Boden | **37,6 mm** (Z −0,56 … −38,2) |
| **Sicher nutzbare Höhe** (unter Rippen, über Schraubdomen) | **ca. 27 mm** (Z −5,5 … −33) |
| Seitenwand Rahmen | 2,3 mm (X ±122,6 … ±124,9) |

→ **Sehr viel Platz.** Ein ESP32-S3-Board (21 × 18 mm), Kamera, PIR, Verstärker und
später ein LiPo-Akku passen problemlos.

## Vorhandene Befestigungspunkte
| Zweck | Position (X, Y) | Schraube |
|---|---|---|
| Rahmen ↔ Rückwand (8 Dome) | (±88, ±88), (±88, 0), (0, +76), (0, −72) | M2,6 × 10 |
| Alter Lautsprecher (2 Dome) | (0, +44,5), (0, −28,5) | M2,6 × 10 |
| Alte Platine (4 Dome) | (74, −40), (74, −67), (106, −40), (106, −67) | Blechschraube 1,7 × 5 |
| Batterie-Platine | (19,5/−72), (42,5/−75,5), (56/−70) | Blechschraube 1,7 × 5 |
| Aufhängung (Wand) | (0, ≈ +73) | – |

**Tipp:** Die 4 alten Platinen-Dome und die 2 Lautsprecher-Dome eignen sich ideal, um eine
gedruckte **Montageplatte** anzuschrauben – ohne das Gehäuse zu verändern.

## Wiederverwendbare Öffnungen
- **Lautsprecheröffnung + Stoff** in der Mitte (ca. 98 × 98 mm) → neuer Lautsprecher kann dahinter.
- **Seitliche Öffnung rechts** (alter Lautstärkeregler, X ≈ +119, Y ≈ −52, Z ≈ −30)
  → Durchführung für **USB-C-Kabel/-Buchse** und ggf. Reset-Taster per gedrucktem Einsatz.
- **Batteriefach** (4 × AA, Deckel von hinten, ca. 105 × 30 mm, X −53…55, Y −88…−56)
  → Phase 2: für Akku (4 × AA NiMH oder gedruckter LiPo-Halter) weiter nutzbar.

## Mögliche Positionen für Kamera, Bewegungssensor & LED
| Option | Wo | Vorteil | Nachteil |
|---|---|---|---|
| A | **Bildfläche** (Frontplatte + Trägerplatte, zusammen ca. 2,3 mm), Loch Ø 4–7 mm | einfach, viel Platz dahinter | Loch im Motiv sichtbar, wenn nicht im dunklen Bildbereich |
| B | **Im Logo-Relief** (z. B. in einem dunklen Detail) | sehr unauffällig | Logo-Einsatz muss angepasst/neu gedruckt werden |
| C | **Rahmen-Vorderkante** (Lippe 2 mm dick, ca. 12 mm breit; darunter nur ca. 8,5 mm Kanal) | sehr unauffällig | eng – nur sehr kleine Kameramodule |

PIR-Sensor braucht freie Sicht (funktioniert **nicht** durch Kunststoff, schlecht durch Stoff)
→ eigenes Loch Ø ca. 10 mm (Mini-PIR) nötig.

## Bilder
- `schnitt_x0.png` – Seitenschnitt durch die Mitte (Lautsprecher, Batteriefach)
- `schnitt_y60.png` – Querschnitt oben (freier Raum)
- `schnitt_y-70.png` – Querschnitt durch Batteriefach
- `schnitt_x110.png`, `schnitt_x-110.png` – Seitenschnitte am Rand
- `draufsicht_z-10.png`, `draufsicht_z-30.png` – Draufsichten mit Domen und Rippen
- `bauteile_mit_massen.txt` – alle Bauteile mit Positionen
