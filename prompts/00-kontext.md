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
- **STEP-Datei** des Gehäuses: `cad/00_fantastic_frame-20260423.zip` (Creo-Baugruppe).
  **Bereits ausgewertet:** `cad/analyse/ANALYSE.md` (Maße, Dome, Öffnungen, Schnittbilder) – lies sie zuerst.
  Kurzfassung: Rahmen 250,7 × 250,7 × ca. 49 mm, Bildfläche 226,4 mm², freier Innenraum ca.
  220 × 220 mm bei ca. 27 mm sicher nutzbarer Höhe; große Öffnung (ca. 70 × 70 mm) in der Trägerplatte
  in der Mitte (früher Lautsprecher, X ±35, Y −25…+45) – ideal für die zentrale Kamera,
  seitliche Öffnung rechts (alter Lautstärkeregler), Batteriefach 4 × AA unten, vorhandene
  Schraubdome für Montageplatte nutzbar. 7 wechselbare Vereins-Logo-Einsätze vorn.
- Ziel: Die Fanbox wird zu einer **dezent gestalteten, aber als Kamera erkennbaren**
  **Kamera (Foto + Videostream)** mit
  Bewegungserkennung, die ich **über MCP direkt aus Claude** steuere:
  - "Mach ein Foto und zeig es mir."
  - "Gab es heute Bewegungen? Zeig mir die Bilder."
  - "Schalte die Überwachung scharf / unscharf."
  - "Gib mir den Link zum Livestream."
  - "Wie ist der Status (Strom, WLAN, Speicher)?"
- **Jetzt: privater Einsatz in meinem Haushalt** – keine Zertifizierung, keine
  Kundenverwaltung. Lieber **einfach und robust** als "produktreif".
- **Gestaltungsziel:** Die Kamera soll **wohnlich aussehen** (Bild statt klobiger
  Überwachungskamera), aber **nicht heimlich** filmen. Alle Personen im Haushalt wissen
  Bescheid; Gäste werden informiert.

## Rechtlicher Rahmen (harte Anforderung – Konstruktion muss das einhalten)
- **§ 8 TDDDG** (früher § 90 TKG): Funk-Kameras, die als Alltagsgegenstand getarnt und dazu
  bestimmt sind, Personen **unbemerkt** aufzunehmen, sind in Deutschland schon im **Besitz**
  verboten (Bundesnetzagentur geht dagegen vor). → Das Gerät muss als Kamera **erkennbar**
  bleiben und Aufnahmen **sichtbar anzeigen**. Prüfe die Konstruktion gezielt darauf und
  nenne, was ggf. noch nötig ist (z. B. Hinweis-Aufkleber, Rückfrage bei der Bundesnetzagentur).
- **§ 201a StGB:** keine Aufnahmen in Bad, Schlafzimmer o. ä. geschützten Räumen;
  **§ 201 StGB:** keine Tonaufnahme.
- Aufnahmen anderer Erwachsener im Haushalt nur mit deren Wissen.
- **Später:** evtl. ein paar Exemplare für **Freunde**, langfristig Fertigung durch einen
  **Hersteller in großer Stückzahl** (eigene Etappe 4).
  → Triff Entscheidungen so, dass dieser Weg **nicht verbaut** wird (z. B. gängige, langfristig
  lieferbare Bauteile, deren Chip es auch als einzelnes Modul für eine eigene Platine gibt;
  nachbaubare Anleitung; mehrere Geräte im Code vorgesehen). Kurz begründen, wo das relevant ist.
- Steuerung **lokal (Heimnetz)** und **von unterwegs** (z. B. Claude auf dem Handy).

## Vorhandene Ausstattung
- **3D-Drucker:** **Bambu Lab X1 Carbon** (geschlossener Bauraum 256 × 256 × 256 mm,
  Standarddüse 0,4 mm, Slicer: Bambu Studio). Kann PLA, PETG, ABS/ASA, TPU.
  Material: **PLA bevorzugt**; wo nötig ein anderes (z. B. **PETG** an warmen Stellen wie
  Kamera/Platine, da PLA ab ca. 55 °C weich wird; **TPU** für Dämpfer/Kabeldurchführungen) –
  jeweils begründen.
  Alle Halterungen und Befestigungen im Rahmen sollen damit **selbst gedruckt** werden.
- Werkzeug vorhanden: **Schraubendreher (ausreichend)**.
- Kann ich **bei Bedarf ausleihen oder kaufen**: **Heißklebepistole** und **Lötkolben**.
  → Plane so, dass beides **möglichst nicht** nötig ist. Wenn doch, sag mir klar,
  **ab welchem Schritt** ich es brauche, und empfiehl ein günstiges Einsteiger-Modell
  (inkl. Zubehör wie Lötzinn, Ablage) mit Bezugsquelle.

## Kamera zentral im Motiv (Gestaltungsidee)
- Die Kamera sitzt **in der Mitte des Rahmens**. Das Objektiv wird **Teil des Motivs** –
  typischerweise die **Pupille eines Auges** (weitere Ideen: Zyklop, Planet/Mond, Bullauge,
  Roboter-Auge …). **Objektivposition ist bei allen Motiven gleich (Bildmitte).**
- **Motive werden ausschließlich auf eine transparente Platte gedruckt** – damit haben wir
  bereits Erfahrung. **Kein 3D-gedrucktes Relief-Motiv.** Unser bisheriges Verfahren:
  `[OFFEN: Plattenmaterial, Dicke, Druckverfahren/Dienstleister]`.
  **Befestigung bisher:** Platte mit **doppelseitigem Klebeband auf die Front geklebt**
  (bewährt, einfach). Klebeband-Dicke zählt zur Gesamthöhe; im Bereich von Objektiv-, LED- und
  PIR-Fenster darf kein Klebeband sitzen.
- Platz laut STEP: Tasche **226,4 × 226,4 mm**, Plattenauflage bei Z +1,14, Rahmen-Innenwand
  bis ca. Z +4,7 → Platten bis ca. **3 mm** Dicke liegen innerhalb der Rahmenkante
  (Annahme, am Bauteil prüfen).
- **Stilreferenzen** (eigene Motive in diesem Stil, keine Kopie fremder Werke):
  1. **Mystisches Ornament-Auge:** türkis-blaue Iris, goldene symmetrische Ornamentik
     (Mandel-/Rautenform, Strahlen, Filigran) auf schwarzem Hintergrund.
  2. **Fotorealistisches Makro-Auge:** Nahaufnahme mit Wimpern, Lid, detailreicher Iris und
     **großer schwarzer Pupille**; der **weiße Lichtreflex** im Auge könnte die Aufnahme-LED sein.
  3. **Iris-Fotografie (aktueller Favorit):** frontale Makroaufnahme nur der Iris, kreisrund,
     zentriert, auf **weißem Hintergrund**; blau-grüne Iris mit goldenen Sprenkeln und feinen
     Fasern, **große schwarze Pupille genau in der Mitte** (ca. ⅓ des Iris-Durchmessers).
     Passt ideal: Bei ca. 200 mm Iris-Durchmesser ist die Pupille ca. 65 mm groß – das Objektiv
     verschwindet darin. Weißer Hintergrund → weiße Grundierung; die Iris eignet sich zum
     **Hinterleuchten** als Aufnahme-Anzeige.
     Idee: ein **Foto der eigenen Iris** (Iris-Fotostudio oder Makro-Aufnahme) – persönlich und
     ohne Urheberrechtsfragen.
  Bildquelle: eigenes Foto, lizenziertes Stockfoto oder KI-generiert.
- Wichtig für die Kamera hinter der Platte:
  - **Klares, unbedrucktes Fenster** (oder Bohrung) genau vor dem Objektiv.
  - Objektiv mit **schwarzer Schaumstoff-Dichtung** direkt an der Platte – keine Spiegelungen
    oder Streulicht (auch von der LED) im Kamerabild.
  - **Weiße Grundierung** hinter dem Motiv, damit das Innere nicht durchscheint – außer an
    Stellen, die **hinterleuchtet** werden sollen (z. B. Iris leuchtet als Aufnahme-Anzeige).
- **Wechselbare Motive:** Kamera bleibt fest montiert, nur die Platte wird getauscht.
  Vergleiche dafür: (a) wie bisher **Klebeband** (ggf. wieder ablösbares Klebeband),
  (b) **Magnete** (in Platte/Front eingeklebt), (c) gedruckte **Klemm-/Clipleisten** am Rand.
  Kriterien: einfach, kein sichtbarer Halter, Platte sitzt plan, Objektiv-Fenster immer exakt
  mittig. Bevorzugt die einfachste Lösung, die nah am bewährten Klebeband-Prinzip bleibt.
- Bewegungssensor (PIR) und Aufnahme-LED möglichst **ins Motiv integrieren** (eigenes Fenster in
  der Platte) oder dezent in der Rahmenkante.

## Aufnahme-Kontrollleuchte (LED)
- Eine **sichtbare LED in der Front** zeigt an, ob die Kamera gerade **aufnimmt oder streamt**.
- Bevorzugt **eine RGB-LED** (z. B. steckbares Grove-/WS2812-Modul), die auch den Gerätestatus
  anzeigt (startet, WLAN-Problem, scharf geschaltet …). Farbschema als Tabelle.
- **Pflicht, fest verbaut:** Die LED leuchtet bei **jeder** Aufnahme und jedem Stream gut
  sichtbar. Sie ist **dimmbar, aber nicht abschaltbar** (weder per Software/MCP noch durch
  einfaches Abziehen) – sie ist Teil der rechtlichen Absicherung (siehe oben).
- Steckbar angeschlossen ist sie trotzdem (einfache Montage, kein Löten).
- Nicht direkt neben das Kameraobjektiv setzen (Lichtreflexe im Bild).

## Eckdaten
- **Strom:** Phase 1 über USB-C-Kabel. Phase 2 Akku. Die Teileauswahl muss Phase 2 schon
  berücksichtigen (Umstieg ohne Neuaufbau, idealerweise nur Akku anstecken).
- **Nachtsicht:** jetzt nicht, darf aber später nicht verbaut sein.
- **Kein Lautsprecher** (wird nicht gebraucht) und **keine Tonaufnahme** (§ 201 StGB, kein Mikrofon nutzen).
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
