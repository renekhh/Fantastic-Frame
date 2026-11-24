# Etappe 1 – Bauteile, Einkaufsliste & Einbau

> Voraussetzung: Inhalt von `00-kontext.md` davor einfügen. Die **STEP-Datei** liegt unter `cad/`.
> Empfehlung: mit **Claude Code** in diesem Repository ausführen, damit echte 3D-Dateien entstehen.

---

## Aufgabe dieser Etappe
Finde die **einfachste zuverlässige Hardware-Lösung** für die Fanbox, erstelle eine
**Einkaufsliste**, mit der ich sofort bestellen kann, und eine **Bauanleitung für Laien**.

## 1. Bauraum aus der STEP-Datei
(Grundauswertung liegt in `cad/analyse/ANALYSE.md` – prüfen, ergänzen, Kamera-/PIR-Position festlegen.)
- Nutzbarer Innenraum (B × H × T in mm), Hindernisse, Wandstärken, vorhandene
  Schraubdome/Befestigungspunkte, Position des alten Batteriefachs und der zentralen Öffnung (früher Lautsprecher).
- Wo können Kamera und Bewegungssensor (PIR) dezent, aber erkennbar durch die Front schauen?
  (Lochdurchmesser, Position, Bildwinkel)

## 2. Variantenvergleich
Vergleiche mindestens:
- **A)** Seeed **XIAO ESP32S3 Sense** (Kamera steckbar, microSD an Bord) + Grove-Erweiterung
- **B)** **Raspberry Pi Zero 2 W** + Camera Module 3 (Flachbandkabel, steckbar)
- gern weitere Fertig-Lösungen, falls einfacher

Bewertungskriterien als Tabelle: **Montage-Einfachheit (Lötstellen!)**, Bildqualität,
Videostream, Stromverbrauch, Akku-Tauglichkeit (Phase 2), Platzbedarf, Kosten,
Software-Aufwand. Danach **eine klare Empfehlung**.

## 3. Einkaufsliste (das Wichtigste dieser Etappe)
Tabelle mit:
| Nr. | Bauteil (genaue Bezeichnung) | Hersteller-Teilenummer | Menge | Preis ca. € | Shop in DE (+ Alternative) | Wofür? (1 Satz, laienverständlich) |

- Shops bevorzugt: Berrybase, Reichelt, Eckstein, Botland, Mouser, Amazon.de.
- Shop-Links nur angeben, wenn du dir sicher bist – sonst exakten Suchbegriff nennen.
- **Alles** aufführen: Kabel (Länge + Steckertyp), USB-C-Netzteil, microSD-Karte,
  Schrauben/Abstandshalter (Größe), Klett/Kabelbinder, Werkzeug.
- Teile für **Phase 2 (Akku)** in einer **separaten** Liste – nicht jetzt kaufen,
  aber jetzt schon kompatibel auswählen.
- Summe Phase 1 und Phase 2.
- Ein **Starter-Werkzeug-Set** für Laien (und ob ein Lötkolben nötig ist).

## 4. Verbindungsplan für Laien
- Bild/Diagramm (Mermaid oder ASCII): welches Kabel steckt **von welcher Buchse zu welcher Buchse**.
- Tabelle "Kabel Nr. → von → nach → Steckertyp → Farbe/Orientierung beachten?".
- Falls Löten nötig: jede Lötstelle einzeln beschreiben + lötfreie Alternative.
- Typische Fehler und wie ich sie vermeide (z. B. Stecker verdreht, falsches Netzteil).

## 5. Einbau in den Rahmen – 3D-Druckteile
Ich habe einen eigenen 3D-Drucker (siehe Kontext). Alle Teile werden **im Rahmen mit
gedruckten Halterungen** befestigt.

**Platzierung**
- Platzierungsplan aller Teile (Draufsicht-Skizze mit Maßen, bezogen auf die STEP-Datei).
- Hinweise: Wärme, WLAN-Antenne nicht hinter Metall, Zugang zu USB-C, microSD und Reset-Taster.

**Konstruktion der Druckteile**
- Halterungen für: Hauptplatine, Kamera (exakt hinter dem Frontloch ausgerichtet),
  Bewegungssensor (PIR), Aufnahme-LED (gut sichtbar, fest verbaut), Kabelführung/Zugentlastung, USB-C-Buchse,
  später Akku. Gern als **eine Grundplatte (Montageplatte)**, auf der alles sitzt und die
  als Ganzes in den Rahmen geschraubt/geklemmt wird – wenn der Bauraum das erlaubt.
- Befestigung der Elektronik in den Halterungen **ohne Spezialwerkzeug**:
  Clips/Schnappverbindungen oder kleine selbstschneidende Schrauben (Größe angeben).
  **Keine Gewindeeinsätze, die eingeschmolzen werden müssen.**
- Befestigung der Halterungen im Rahmen: vorhandene Schraubdome aus der STEP-Datei nutzen;
  sonst Klemmen/Kleben (welcher Kleber für welches Gehäusematerial?).
- Druckgerecht konstruieren: **ohne Stützmaterial** druckbar, flache Seite aufs Druckbett,
  passend zum Bauraum meines Druckers, Toleranzen für Passungen (z. B. +0,2–0,3 mm) als
  einstellbarer Parameter.
- Maße der Bauteile aus Datenblättern; unsichere Maße als **Annahme** markieren und
  vorher ein kleines **Test-/Passungsteil** zum Ausprobieren mitliefern.

**Lieferung der Dateien**
- **Druckfertige STL-Dateien** (eine Datei pro Teil, sinnvoll benannt, z. B. `kamera-halter.stl`)
  **plus STEP** für spätere Änderungen.
- Den **parametrischen Quellcode** (CadQuery/Python) dazu, damit Maße später leicht
  angepasst werden können – mit einer Anleitung, wie ich die Dateien neu erzeuge.
- Eine **Baugruppen-Ansicht** (alle Teile im Gehäuse aus der STEP-Datei), um Kollisionen
  vor dem Druck auszuschließen.
- Zusätzlich eine **Bambu-Studio-Projektdatei (.3mf)** mit allen Teilen fertig angeordnet
  (falls technisch möglich; sonst Anleitung zum Anordnen).
- **Druckeinstellungen pro Teil** als Tabelle: Material, Schichthöhe, Wandlinien, Infill,
  Ausrichtung auf dem Druckbett, Stützen ja/nein, ungefähre Druckzeit.
- Reihenfolge: zuerst Testteil drucken → Passung prüfen → Toleranz ggf. anpassen → Rest drucken.

## 5b. Motiv mit integriertem Kamera-Auge
- Kamera **zentral** (Objektivmitte bei X = 0, Y = 0 bzw. in der zentralen Öffnung – begründen).
- Wähle ein Kameramodul/Objektiv, das gut als "Auge" wirkt (Durchmesser, Farbe der Linse),
  und einen passenden **Bildwinkel** für einen Raum, wenn der Rahmen an der Wand hängt
  (Weitwinkel ja/nein, Verzerrung).
- Schlage **3–5 Motiv-Ideen** vor (Favorit: **Ornament-Auge**, siehe Kontext; weitere z. B. Zyklop, Eule, Roboter, Weltraum), jeweils mit:
  wo sitzen Objektiv, PIR und LED im Motiv?
- Vergleiche die beiden Favoriten **Ornament-Auge** (stilisiert, als Relief druckbar) und
  **fotorealistisches Makro-Auge** (Fotodruck) hinsichtlich Tarnung des Objektivs, Aufwand, Wirkung.
- Für das Makro-Auge: Druckverfahren/Material für die Frontplatte (226,4 × 226,4 mm, ca. 0,5 mm),
  Bildauflösung, wo drucken lassen; Loch/Fenster für das Objektiv in der Pupille; Lichtreflex-LED.
- **Proportionen** für das Ornament-Auge: Pupille = Objektiv-Durchmesser, Iris-Durchmesser,
  Gesamtgröße des Auges auf der Bildfläche (226 × 226 mm) – mit Skizze.
- Prüfe, ob ein **kleiner RGB-LED-Ring** (z. B. WS2812, steckbar) um das Objektiv passt
  (leuchtende Iris als Aufnahme-Anzeige), ohne Reflexe ins Kamerabild zu werfen.
- Umsetzung vergleichen: (a) **Bilddruck** auf der Frontplatte, (b) **3D-Relief** mehrfarbig,
  (c) **Kombination** (gedruckter Hintergrund + gedrucktes Relief-Auge). Empfehlung geben.
- Liefere für **das Ornament-Auge** einen **druckfertigen Relief-Einsatz** (STL/STEP/3MF,
  mehrfarbig falls mein Drucker ein AMS hat: `[OFFEN: AMS ja/nein]`) plus eine **Vorlage**
  (Maße, Loch-Positionen), mit der ich eigene Motive gestalten oder als Bild drucken kann.
- Befestigung des Motiv-Einsatzes so, dass er **ohne Werkzeug tauschbar** ist und die Kamera
  dabei nicht verstellt wird.

## 6. Energiebilanz
- Phase 1 (USB-C): welches Netzteil (Watt/Ampere)?
- Phase 2 (Akku): erwartete Laufzeit mit Rechenweg, welche Funktionen dann eingeschränkt sind
  (z. B. Stream nur auf Abruf), welcher Akku passt in den Bauraum.

## 7. Schritt-für-Schritt-Bauanleitung
Nummerierte Schritte vom Auspacken bis "Gerät ist im Rahmen verschraubt und leuchtet",
jeweils mit **"So prüfst du, dass es geklappt hat"**.

## Fertig, wenn …
- [ ] Empfohlene Variante steht fest und ist begründet
- [ ] Einkaufsliste Phase 1 ist bestellfertig (inkl. Werkzeug), Phase 2 separat
- [ ] Verbindungsplan und Bauanleitung sind für einen Laien nachvollziehbar
- [ ] Ornament-Auge-Motiv-Einsatz + Motiv-Vorlage liegen druckfertig vor
- [ ] Druckfertige STL- und STEP-Dateien für alle Halterungen liegen vor, inkl. Testteil,
      Druckeinstellungen und Baugruppen-Ansicht ohne Kollisionen
- [ ] Zusammenfassung "Hardware-Entscheidungen für Etappe 2" (Board, Pins, Sensoren, Kamera)
