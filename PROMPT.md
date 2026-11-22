# Prompt: Fantastic Frame Fanbox → Smarte Überwachungskamera mit MCP-Steuerung

> Version 2 · Status: Entwurf. Offene Punkte sind mit `[OFFEN]` markiert.

---

## Rolle
Du bist ein erfahrener Produktentwickler für vernetzte Consumer-Hardware: Embedded-Hardware
(ESP32 / Raspberry Pi, Kameramodule, Power-Management), Mechanik/CAD (3D-Druck-Halterungen)
sowie Cloud- und Software-Architektur inklusive Model Context Protocol (MCP).
Du arbeitest gründlich, benennst Zielkonflikte offen und erfindest keine Bauteile, Maße oder
Datenblattwerte. Was du nicht sicher weißt, kennzeichnest du als **Annahme**.

## Kontext
- Das Produkt heißt "Fantastic Frame Fanbox". Es ist ein Bilderrahmen-Gehäuse, in dem bisher
  ein Lautsprecher und ein Batteriefach mit 4 Batterien stecken.
- **Die gesamte bisherige Elektronik fliegt raus.** Alles wird von Grund auf neu aufgebaut.
  Wiederverwendet werden nur das Gehäuse und, falls sinnvoll, das Batteriefach bzw. der
  Platz dafür.
- Als Anhang bekommst du eine **STEP-Datei (.stp) des Gehäuses**: `[OFFEN: Dateiname/Pfad]`.
- Das Gerät soll **später an Dritte weitergegeben bzw. verkauft werden können**. Das ist
  ein Produkt, kein Bastelprojekt für ein einzelnes Gerät.

## Ziel
Die Fanbox wird zu einer unauffälligen Kamera (Foto und Videostream). Gesteuert und abgefragt
wird sie über **MCP direkt aus Claude**. Beispiele für die Nutzung:
- "Mach jetzt ein Foto und zeig es mir."
- "Gab es heute Bewegungen? Zeig mir die Bilder dazu."
- "Schalte die Überwachung scharf / unscharf."
- "Gib mir den Link zum Livestream."
- "Spiel über den Lautsprecher einen Warnton ab."
- "Wie ist der Status (Strom/Akku, WLAN, Speicher)?"

## Anforderungen

### Funktional
1. **Foto auf Abruf** (Pflicht). Claude muss das Bild als Image-Content direkt sehen können.
2. **Videostream** (Pflicht). Live-Ansicht im Browser bzw. in der App über einen Link, den
   Claude liefert. Hinweis: Claude selbst kann keinen Stream "anschauen". Über MCP gibt es
   Einzelbilder oder eine kurze Bildfolge.
3. **Bewegungserkennung** per PIR-Sensor (stromsparend, wichtig für den späteren
   Akkubetrieb). Optional zusätzlich per Bildvergleich.
4. **Ereignisse** (Zeitstempel und Bild) speichern: lokal auf microSD und optional in der Cloud.
5. **Neuer Lautsprecher bzw. Verstärker** für Warn- und Bestätigungstöne (z. B. I2S-Verstärker).
6. Nachtsicht wird **jetzt nicht** gebraucht. Die Wahl des Kameramoduls soll aber eine
   spätere Nachrüstung (IR-LEDs, NoIR-Variante) nicht verbauen.

### Stromversorgung (zweistufig)
- **Phase 1:** Dauerstrom über **USB-C**.
- **Phase 2:** Akkubetrieb. Die Schaltung ist **von Anfang an** dafür ausgelegt:
  Lade-IC, Akku-Messung, Power-Path. Der Wechsel darf also nur ein "Umstecken" sein,
  kein Neuentwurf.
- Prüfe, ob 4 × AA (wie bisher) sinnvoll sind oder ob ein Li-Ion/LiPo-Akku mit USB-C-Laden
  besser ist. Empfiehl eine Lösung und belege sie mit einer **Energiebilanz**: Ruhestrom,
  Foto, Stream, WLAN. Sag ehrlich, welche Laufzeit im Akkubetrieb realistisch ist und welche
  Funktionen dann eingeschränkt sind (z. B. Stream nur auf Anfrage).

### Mechanik
- Werte die STEP-Datei aus: **nutzbaren Innenraum bestimmen** (Maße, Hindernisse,
  Wandstärken, vorhandene Dome/Schraubpunkte).
- Schlage die **Platzierung** aller Komponenten vor: Platine, Kamera, PIR, Lautsprecher,
  Akku, USB-C-Buchse, SD-Slot, Taster/Status-LED.
- **Kamera und PIR unauffällig** in der Front (Passepartout/Rahmen): Lochdurchmesser,
  Position, Bildwinkel.
- Liefere **Befestigungsdaten**: Maße und Bohrbilder der Bauteile sowie Konstruktionsvorschläge
  für 3D-druckbare Halterungen/Adapter. Idealerweise als parametrischer CAD-Code
  (z. B. CadQuery/Python oder OpenSCAD), der STEP und STL exportiert.
- Wärmeabfuhr, Antennenposition (kein Metall vor der WLAN-Antenne), Zugang zu USB-C,
  Akku und SD-Karte.

### Plattform & Steuerung (produkttauglich)
Das Gerät muss **auf zwei Wegen** steuerbar sein:
- **A) Lokal:** im Heimnetz ohne Internet bzw. Cloud, z. B. ein MCP-Server auf dem PC oder
  ein lokaler Endpunkt.
- **B) Cloud:** über einen **Remote-MCP-Server** (Streamable HTTP + OAuth), sodass Claude
  (Desktop, Web, Handy) auch von unterwegs zugreift, **ohne Portfreigaben** beim Kunden.
  Das Gerät baut dafür eine ausgehende, verschlüsselte Verbindung auf (z. B. MQTT über TLS
  oder WebSocket).

Dazu gehören:
- **Provisioning für Endkunden:** WLAN-Einrichtung ohne Programmieren (Captive Portal oder
  BLE-Provisioning), Gerät mit einem Benutzerkonto verknüpfen (Pairing-Code/QR).
- **Mandantenfähigkeit:** mehrere Nutzer und mehrere Rahmen pro Nutzer, jedes Gerät mit
  eigener Identität bzw. eigenem Zertifikat.
- **Sichere OTA-Updates** (signiert) mit Rollback.
- **Sicherheit:** keine Default-Passwörter, TLS überall, Tokens/Scopes pro Gerät, Stream-Links
  zeitlich begrenzt.

### Datenschutz & Produktkonformität
- Keine Tonaufnahme (§ 201 StGB).
- DSGVO: Speicherdauer konfigurierbar, automatisches Löschen, Datenspeicherung in der EU,
  Datenschutzhinweise für Endkunden.
- Ein Produkt, das in der EU verkauft wird, braucht **CE (RED, EMV, Niederspannung),
  RoHS, WEEE und Batterieverordnung**. Bevorzuge **vorzertifizierte Funkmodule**, um den
  Aufwand zu senken, und liste auf, was trotzdem zu prüfen ist.
- Hinweis auf Kennzeichnungs- und Hinweispflichten bei Kameras.

## Architektur (Vorschlag, bitte kritisch prüfen)

```
[Fanbox: MCU/SoC + Kamera + PIR + Lautsprecher]
      │  ausgehend: MQTT/WebSocket über TLS        │  lokal: HTTP/REST im LAN
      ▼                                            ▼
[Cloud-Backend: Geräteverwaltung, Speicher,     [Lokaler MCP-Server (stdio)]
 Stream-Relay, Remote-MCP-Server + OAuth]                  │
      │                                                    │
      └──────────────► Claude (Desktop / Web / Mobile) ◄───┘
```

Vergleiche mindestens diese Hardware-Varianten und empfiehl eine (für Prototyp **und** Serie):
- **A) ESP32-S3** (z. B. ESP32-S3-WROOM-1 mit PSRAM, für den Prototyp Seeed XIAO ESP32S3 Sense)
  mit OV2640/OV3660/OV5640: stromsparend, günstig, Stream nur MJPEG in niedriger Auflösung.
- **B) Raspberry Pi Zero 2 W** (bzw. CM-Variante) mit Camera Module 3: bessere Bilder,
  H.264/WebRTC, aber höherer Verbrauch, schlecht für den Akkubetrieb.
- Gern weitere Optionen (z. B. Kamera-SoCs mit H.264-Encoder), wenn sie besser passen.

## Deliverables (in dieser Reihenfolge, bei Bedarf in mehreren Antworten)
1. **Rückfragen:** maximal 5, falls etwas Wesentliches fehlt.
2. **Auswertung der STEP-Datei:** nutzbarer Bauraum mit Maßen.
3. **Variantenvergleich** als Tabelle (Bildqualität, Stream, Stromverbrauch, Akkutauglichkeit,
   Bauraum, Kosten Prototyp/Serie, Entwicklungsaufwand, Zertifizierung) und eine klare Empfehlung.
4. **Stückliste (BOM)** für den Prototyp: Bauteil, genaue Bezeichnung/Teilenummer, Menge,
   Preis ca. in €, Bezugsquelle in DE (Reichelt, Berrybase, Eckstein, Mouser, …), Zweck.
   Kleinteile eingeschlossen. Danach eine Abschätzung der Serienkosten.
5. **Schaltung:** Blockschaltbild, Pin-Belegung als Tabelle, Verdrahtung (Mermaid/ASCII),
   Power-Path USB-C ↔ Akku. Ausblick auf eine eigene Platine (PCB) für die Serie.
6. **Energiebilanz** mit Rechenweg für Phase 1 und Phase 2.
7. **Mechanik:** Platzierung der Komponenten, Front-Öffnungen, Halterungen als
   parametrischer CAD-Code mit STEP/STL-Export.
8. **Firmware** (vollständig, kompilierbar; Framework begründen: ESP-IDF/Arduino/PlatformIO
   oder Linux/Python):
   - Provisioning (WLAN und Pairing), sichere Geräteidentität
   - lokale REST-API: `/snapshot`, `/stream`, `/status`, `/events`, `/events/{id}/image`,
     `/arm`, `/disarm`, `/sound`, `/config`, alle mit Authentifizierung
   - Cloud-Anbindung (ausgehend, TLS), Wiederverbindung, Offline-Puffer
   - PIR-Ereignis → Foto → Speichern/Upload; Energiesparmodi für Phase 2
   - signiertes OTA mit Rollback
9. **MCP-Server** (vollständiger Code, bevorzugt TypeScript oder Python mit dem offiziellen
   MCP SDK). **Eine Codebasis**, die lokal (stdio) und als Remote-Server
   (Streamable HTTP + OAuth) läuft. Tools:
   - `list_devices()`
   - `take_snapshot(device_id)`: liefert ein Bild (Image-Content)
   - `get_stream_url(device_id, ttl_minutes)`: liefert einen zeitlich begrenzten Link
   - `get_status(device_id)`: Stromquelle/Akku, WLAN-RSSI, scharf/unscharf, Speicher, Firmware
   - `list_events(device_id, since, until, limit)`
   - `get_event_image(event_id)`
   - `arm(device_id)` / `disarm(device_id)`
   - `play_sound(device_id, sound: "alarm" | "chime" | "beep")`
   - `set_config(device_id, …)`: Empfindlichkeit, Speicherdauer, Zeitpläne
   Dazu: Fehlerbehandlung (Gerät offline oder im Schlafmodus), Logging, Konfiguration per `.env`.
10. **Cloud-Backend (MVP):** Komponenten, Hosting-Vorschlag in der EU, Datenmodell, Kosten pro
    Gerät und Monat, Deployment (z. B. Docker Compose).
11. **Einrichtung:** Schritt-für-Schritt-Anleitung für Entwickler (flashen, Server starten,
    Eintrag in Claude Desktop/Code bzw. als Custom Connector) **und** für Endkunden
    (Auspacken → WLAN → Claude verbinden).
12. **Testplan:** Komponententests, Integrationstests, Dauertest (Stabilität, Wärme, Akku).
13. **Roadmap:** Prototyp → Kleinserie → Serie, inklusive Zertifizierung.
    Mögliche Erweiterungen (Nachtsicht, Push-Benachrichtigungen, App) nur als Liste.

## Format
- Antworte auf Deutsch, Code-Kommentare auf Englisch.
- Code immer vollständig, ohne "…"-Auslassungen. Jede Datei mit Dateipfad, die
  Projektstruktur als Baum vorneweg.
- Annahmen klar markieren. Bei Unsicherheit lieber nachfragen als raten.
