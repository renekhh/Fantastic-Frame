# Etappe 0 – Gemeinsamer Kontext

> Version 3 · Diesen Block **an den Anfang jeder Etappe** kopieren (oder in Claude als
> Projekt-Anweisung / CLAUDE.md hinterlegen). Offene Punkte sind mit `[OFFEN]` markiert.

---

## Wer ich bin – bitte unbedingt berücksichtigen
- Ich habe **keinerlei Elektronik-Kenntnisse** und **nur sehr wenig Programmiererfahrung**.
- Erkläre jeden Schritt so, dass ein Laie ihn nachmachen kann: Was nehme ich in die Hand,
  wo stecke ich es ein, woran erkenne ich, dass es geklappt hat?
- Verwende Fachbegriffe nur mit kurzer Erklärung in Klammern.
- Wenn ich etwas am Computer eingeben muss: exakte Befehle zum Kopieren, und sag mir,
  was ich als Ergebnis sehen sollte.
- Lieber eine etwas teurere, aber **einfachere** Lösung als eine billige, komplizierte.

## Montage-Regeln (harte Anforderungen)
1. **Stecken statt Löten.** Bevorzuge fertige Module mit Steckverbindern
   (z. B. Seeed **Grove**, Adafruit **STEMMA QT** / SparkFun **Qwiic**, JST-PH-Stecker,
   vorkonfektionierte Kabel, Schraubklemmen).
2. Wenn Löten unvermeidbar ist: **so wenige Lötstellen wie möglich** (Ziel: unter 10),
   jede Lötstelle einzeln mit Foto-ähnlicher Beschreibung erklären und angeben,
   welches Einsteiger-Lötset ich brauche. Alternativ eine lötfreie Ausweichlösung nennen.
3. Keine Steckbretter (Breadboards) im fertigen Gerät – alles muss im Rahmen fest und
   erschütterungssicher sitzen (Halterungen, Schrauben, Klett, Kabelbinder).
4. Keine Bauteile, die man nur in Asien mit wochenlanger Lieferzeit bekommt, sofern es
   eine in Deutschland lieferbare Alternative gibt.

## Das Projekt
- Produkt: **"Fantastic Frame Fanbox"** – ein Bilderrahmen-Gehäuse. Bisher drin:
  ein Lautsprecher und ein Batteriefach mit 4 Batterien.
- **Die komplette alte Elektronik fliegt raus.** Nur das Gehäuse bleibt.
- Ich habe eine **STEP-Datei (.stp)** des Gehäuses: `[OFFEN: Dateiname/Pfad]`.
- Ziel: Die Fanbox wird zu einer unauffälligen **Kamera (Foto + Videostream)** mit
  Bewegungserkennung und Lautsprecher, die ich **über MCP direkt aus Claude** steuere:
  - "Mach ein Foto und zeig es mir."
  - "Gab es heute Bewegungen? Zeig mir die Bilder."
  - "Schalte die Überwachung scharf / unscharf."
  - "Gib mir den Link zum Livestream."
  - "Spiel einen Warnton ab."
  - "Wie ist der Status (Strom, WLAN, Speicher)?"
- **Nur für den privaten Einsatz in meinem Haushalt** – kein Verkauf, keine Weitergabe.
  → Keine Zertifizierung, keine Mehrbenutzer-/Kundenverwaltung, keine Datenschutz-Texte nötig.
  Lieber **einfach und robust** als "produktreif".
- Steuerung **lokal (Heimnetz)** und **von unterwegs** (z. B. Claude auf dem Handy).

## Vorhandene Ausstattung
- **3D-Drucker** ist vorhanden: `[OFFEN: Modell, Bauraum in mm, Düse]`, Material: `[OFFEN: PLA / PETG]`.
  Alle Halterungen und Befestigungen im Rahmen sollen damit **selbst gedruckt** werden.
- Werkzeug vorhanden: **Schraubendreher (ausreichend)**.
- Kann ich **bei Bedarf ausleihen oder kaufen**: **Heißklebepistole** und **Lötkolben**.
  → Plane so, dass beides **möglichst nicht** nötig ist. Wenn doch, sag mir klar,
  **ab welchem Schritt** ich es brauche, und empfiehl ein günstiges Einsteiger-Modell
  (inkl. Zubehör wie Lötzinn, Ablage) mit Bezugsquelle.

## Aufnahme-Kontrollleuchte (LED)
- Eine **sichtbare LED in der Front** zeigt an, ob die Kamera gerade **aufnimmt oder streamt**.
- Bevorzugt **eine RGB-LED** (z. B. steckbares Grove-/WS2812-Modul), die auch den Gerätestatus
  anzeigt (startet, WLAN-Problem, scharf geschaltet …). Farbschema als Tabelle.
- **Später entfernbar:** per **Stecker** abziehbar (kein Löten) **und** per Software/MCP
  abschaltbar bzw. dimmbar. Für das Frontloch eine **druckbare Blindkappe** vorsehen.
- Nicht direkt neben das Kameraobjektiv setzen (Lichtreflexe im Bild).

## Eckdaten
- **Strom:** Phase 1 über USB-C-Kabel. Phase 2 Akku. Die Teileauswahl muss Phase 2 schon
  berücksichtigen (Umstieg ohne Neuaufbau, idealerweise nur Akku anstecken).
- **Nachtsicht:** jetzt nicht, darf aber später nicht verbaut sein.
- **Ton:** nur Ausgabe (Lautsprecher), **keine Tonaufnahme** (§ 201 StGB).
- **Netzwerk:** WLAN 2,4 GHz; Zugriff von unterwegs **ohne offene Ports am Router**.
- **Sicherheit (Basis):** Passwort/Token-Schutz, damit niemand Fremdes auf die Kamera
  zugreifen kann. Speicherdauer der Bilder einstellbar.

## Arbeitsweise
- Wir arbeiten in **Etappen**. Bearbeite nur die aktuelle Etappe.
- Stelle vor dem Start **maximal 5 Rückfragen**, falls etwas Wesentliches fehlt.
- Erfinde keine Teilenummern, Maße oder Preise. Unsichere Angaben als **Annahme** markieren.
  Preise als "ca."-Werte mit Stand-Datum.
- Antworte auf Deutsch; Code-Kommentare auf Englisch.
- Code immer vollständig (keine "…"-Auslassungen), jede Datei mit Pfad.
- Am Ende jeder Etappe: **Checkliste "Fertig, wenn …"** und eine kurze Zusammenfassung der
  Entscheidungen, die ich in die nächste Etappe mitnehme.
