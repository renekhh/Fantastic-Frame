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
- Die Kamera sitzt **in der Mitte des Rahmens**. Das Objektiv wird **Teil des Motivs**,
  z. B. das **Auge eines Zyklopen**, die Pupille eines Auges, ein Planet/Mond, das Objektiv
  einer gezeichneten Kamera, ein Bullauge, ein Roboter-Auge …
- Das Motiv kann sein:
  - ein **bedrucktes Bild** auf der Frontplatte mit Loch für das Objektiv, und/oder
  - ein **3D-gedrucktes Relief-Motiv** (wie die vorhandenen Vereinslogo-Einsätze), in dem das
    Objektiv als Auge sitzt – gern **mehrfarbig** druckbar.
- **Favorit / Stilreferenz: "mystisches Ornament-Auge"** – ein einzelnes, realistisches Auge
  mit **leuchtend türkis-blauer Iris**, umrahmt von **goldener, symmetrischer Ornamentik**
  (spitz zulaufende Mandel-/Rautenform, Strahlen, Filigran) auf **schwarzem Hintergrund**.
  Die **schwarze Pupille ist das Kameraobjektiv** – die dunkle Linse fällt dort nicht auf.
  → Wir gestalten ein **eigenes Motiv in diesem Stil**, keine Kopie eines fremden Kunstwerks
  (Urheberrecht, v. a. falls die Fanbox später weitergegeben wird).
  Ideen zur Integration: **LED-Ring um die Pupille** als "leuchtende Iris" = Aufnahme-Anzeige;
  PIR-Sensor im oberen Ornament-Juwel; Status-LED in der unteren Spitze.
- **Variante 2 / Stilreferenz: "fotorealistisches Makro-Auge"** – ein Auge in Nahaufnahme füllt
  das Bild (Wimpern, Lid, detailreiche bernstein-/grünbraune Iris, **große schwarze Pupille**).
  Die Pupille ist viel größer als das Objektiv → das Objektiv sitzt **unsichtbar mitten in der
  schwarzen Pupille**. Idee: Der **weiße Lichtreflex** im Auge ist die **Aufnahme-LED**.
  Umsetzung als **hochaufgelöster Fotodruck** auf der Frontplatte (3D-Druck kann das nicht
  fotorealistisch). Bildquelle: eigenes Foto, lizenziertes Stockfoto oder KI-generiert –
  keine fremden Bilder ohne Lizenz.
- Für beide Varianten gilt: **Objektiv = Pupille, Position immer gleich (Bildmitte)**.
- **Wechselbare Motive**: Kamera bleibt fest montiert, nur der Motiv-Einsatz wird getauscht
  (gleiches Befestigungsprinzip wie die Logo-Einsätze, Objektivposition bei allen Motiven gleich).
- Bewegungssensor (PIR) und Aufnahme-LED möglichst **ebenfalls ins Motiv integrieren**
  (z. B. LED als zweites Auge/Nase/Stern, PIR als Detail) oder dezent in der Rahmenkante.

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
