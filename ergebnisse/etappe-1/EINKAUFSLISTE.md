# Einkaufsliste Fanbox-Kamera

> Auszug aus `ergebnisse/etappe-1/README.md` (Abschnitt 3). Preise sind grobe Schätzungen.

## Phase 1 (USB-Strom) – jetzt bestellen

Die Preise sind grobe Schätzungen (Stand Nov. 2026, nicht tagesaktuell geprüft).
**Suchbegriffe** funktionieren in jedem Shop.

| Nr. | Bauteil | Suchbegriff / Teilenummer | Menge | ca. € | Shops (DE) | Wofür? |
|---|---|---|---|---|---|---|
| 1 | Raspberry Pi Zero 2 **WH** (mit vorgelöteter Stiftleiste!) | „Raspberry Pi Zero 2 WH“ | 1 | 20–25 | Berrybase, Reichelt, Eckstein, Welectron | der kleine Computer: Kamera, Stream, MCP-Server |
| 2 | Raspberry Pi **Camera Module 3 Wide** (nicht NoIR) | „Camera Module 3 Wide“ | 1 | 35–40 | Berrybase, Reichelt, Eckstein, Elektor | die Kamera (120°, 25 × 24 × 12,4 mm) |
| 3 | Kamerakabel **Standard auf Mini, 200 mm** (für Pi Zero) | „Raspberry Pi Zero Kamerakabel 200 mm“ | 1 | 3–5 | wie oben | Kamera → Pi (die mitgelieferte Kamera-Leitung passt **nicht** an den Pi Zero) |
| 4 | Offizielles Raspberry-Pi-Netzteil **Micro-USB 5,1 V / 2,5 A**, 1,5 m | „Raspberry Pi Netzteil micro USB 2,5A“ | 1 | 8–10 | wie oben | Strom |
| 5 | microSD **32 GB „High Endurance“** | „SanDisk High Endurance 32GB“ | 1 | 10–12 | Amazon, MediaMarkt, Berrybase | Betriebssystem + Aufnahmen (für Dauerbetrieb gemacht) |
| 6 | **HLK-LD2410C** Radarsensor **mit Stiftleiste** („pre-soldered“) | „LD2410C Stiftleiste“ | 1 | 5–10 | Amazon, eBay, Berrybase, Pi Hut | Bewegung/Anwesenheit erkennen, durch das Bild hindurch |
| 7 | **LED-Ring 16 × WS2812B, Ø 44,5 mm** | „WS2812B 16 LED Ring“ / „NeoPixel Ring 16“ | 1 | 5–12 | Berrybase, Eckstein, AZ-Delivery | leuchtender Ring um die Pupille = Aufnahme-Anzeige |
| 8 | Jumper-Kabel **Buchse–Buchse, 30 cm** (40er-Pack) | „Jumper Kabel female female 30cm“ | 1 | 4–6 | überall | Radar + LED-Ring → Pi (stecken) |
| 9 | Kühlkörper für Pi Zero (selbstklebend) | „Kühlkörper Raspberry Pi Zero“ | 1 | 2–4 | Berrybase, Amazon | der Rahmen ist geschlossen, der Pi wird warm |
| 10 | Schrauben **M2 × 6** und **M2,5 × 8** (Zylinderkopf, Edelstahl), am einfachsten als Sortiment | „Schrauben Sortiment M2 M2,5“ | je 4 + 3 | 8–10 | Amazon, Baumarkt | Kamera (M2), Pi + Kamera-Kopf (M2,5); sie schneiden ihr Gewinde selbst in den Druck |
| 11 | **Moosgummi schwarz, selbstklebend, 2 mm** (A4) | „Moosgummi selbstklebend schwarz 2mm“ | 1 | 3–5 | Bastelladen, Amazon | Dichtring um das Objektiv (gegen Spiegelungen) |
| 12 | Locheisen-Set 3–12 mm | „Locheisen Set“ | 1 | 8–10 | Baumarkt | Dichtring sauber ausstanzen (alternativ Schere) |
| 13 | Kleine Kabelbinder (2,5 mm breit) | – | 10 | 2–3 | Baumarkt | Kabel ordentlich befestigen |
| 14 | Filament **PETG schwarz** (falls nicht vorhanden) | – | ca. 40 g | – | Bambu Store | Druckteile (schwarz = kein Streulicht) |
| 15 | Acrylplatte 2 mm, UV-Druck | über eure Druckerei | 1 | – | eure UV-Druckerei | das Motiv (Vorlage siehe Abschnitt 5b) |

**Summe Phase 1:** Kernteile 1–7 ca. **90–115 €**, mit Kleinteilen und Werkzeug ca. **120–150 €**.

### Werkzeug

| Werkzeug | Status |
|---|---|
| Kreuzschlitz-Schraubendreher PH0 + PH1 | vorhanden |
| Cuttermesser und kleine Feile (für die Kabel-Kerbe) | ca. 10 €, falls nicht da |
| microSD-Kartenleser für den PC | ca. 8 €, falls dein PC keinen hat |
| **Lötkolben** | **nur für den LED-Ring: 3 Lötstellen** (siehe unten) |

**Löten: nur 3 Lötstellen, und es gibt eine lötfreie Alternative.**
- **Mit Löten:** Der WS2812B-Ring (Nr. 7) hat Lötpunkte statt Steckern. Du lötest 3 Jumper-Kabel an: 5V, GND und DIN.
  - Einsteiger-Lötstation (z. B. „Lötstation 60 W mit Temperaturregelung“, ca. 25–35 €)
  - bleifreies Lötzinn 0,8 mm
  - kurze Anleitung in Schritt 4b
- **Ohne Löten:** **Seeed Grove RGB LED Ring 16 × WS2813 Mini** (104020171), mit Stecker.
  - Dazu brauchst du ein „Grove auf Buchse“-Adapterkabel.
  - Er ist aber **Ø 58 mm** groß und laut Händlern teils ausverkauft bzw. ausgelaufen.
  - Wenn du ihn nimmst, trägst du in `fanbox_teile.py` den Durchmesser ein und erzeugst die Teile neu (siehe Abschnitt 5).

### Phase 2 (Akku) – nicht jetzt kaufen

Ehrlich gesagt: Mit dem Pi ist **Akkubetrieb nur kurzzeitig sinnvoll**, nämlich ca. **1 Tag pro 10.000 mAh** (Rechnung siehe Abschnitt 6).
- **Vorübergehend** reicht eine Powerbank mit Pass-Through, die sich unauffällig hinter dem Rahmen platzieren lässt. Ein Umbau ist nicht nötig, du steckst nur das Kabel um.
- **Echter Akku über Wochen** geht nur mit der ESP32-Variante. Das klären wir in Etappe 4.

