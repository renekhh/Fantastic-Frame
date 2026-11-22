# Etappe 3 – MCP-Server & Cloud (Steuerung aus Claude)

> Voraussetzung: `00-kontext.md` + **Zusammenfassungen aus Etappe 1 und 2** davor einfügen.
> Empfehlung: mit **Claude Code** direkt in diesem Repository ausführen.

---

## Aufgabe dieser Etappe
Baue die Verbindung zwischen Fanbox und Claude – zuerst **lokal**, dann über die **Cloud**,
so dass Claude (Desktop, Web, Handy) die Kamera steuern kann.

## Schritt 3a – Lokaler MCP-Server (zuerst!)
- Läuft auf meinem PC im Heimnetz, spricht mit der lokalen API der Fanbox.
- **Einfach zu installieren** (ein Befehl, z. B. `npx …` oder `uvx …`), Konfiguration per
  `.env` oder Einrichtungs-Assistent, der die Fanbox im Netz automatisch findet (mDNS).
- Anleitung zum Eintragen in **Claude Desktop** (`claude_desktop_config.json`) und
  **Claude Code** (`claude mcp add …`) – mit exaktem Text zum Kopieren.

## Schritt 3b – Cloud / Remote-MCP-Server
- **Eine Codebasis** für lokal (stdio) und remote (Streamable HTTP + OAuth).
- Fanbox verbindet sich **ausgehend** mit der Cloud → keine Portfreigaben beim Kunden.
- Geräteverwaltung: Gerät per **Pairing-Code/QR** mit Benutzerkonto verknüpfen,
  mehrere Nutzer und mehrere Rahmen pro Nutzer.
- Bilder/Ereignisse speichern (EU-Hosting), automatische Löschung.
- Livestream über zeitlich begrenzte, geheime Links (Relay, da Claude Streams nicht ansehen kann).
- Hosting-Vorschlag (einfach zu betreiben, EU), Kosten pro Gerät und Monat,
  Deployment per **Docker Compose** mit Schritt-für-Schritt-Anleitung für Laien.
- Einbindung in Claude als **Custom Connector** (Anleitung).

## MCP-Tools
| Tool | Zweck |
|---|---|
| `list_devices()` | Meine Rahmen auflisten |
| `take_snapshot(device_id)` | Foto aufnehmen, als **Bild** an Claude zurückgeben |
| `get_stream_url(device_id, ttl_minutes)` | Zeitlich begrenzter Livestream-Link |
| `get_status(device_id)` | Strom/Akku, WLAN, scharf/unscharf, Speicher, Firmware |
| `list_events(device_id, since, until, limit)` | Bewegungs-Ereignisse |
| `get_event_image(event_id)` | Bild zu einem Ereignis |
| `arm(device_id)` / `disarm(device_id)` | Überwachung an/aus |
| `play_sound(device_id, sound)` | "alarm" \| "chime" \| "beep" |
| `set_config(device_id, …)` | Empfindlichkeit, Speicherdauer, Zeitpläne |

Klare Tool-Beschreibungen, damit Claude sie richtig nutzt; Fehlerbehandlung wenn das Gerät
offline ist oder schläft (Phase 2: letztes Bild aus Cache + Hinweis).

## Sicherheit & Datenschutz
- TLS überall, Token/Scopes pro Gerät, keine Default-Passwörter
- `play_sound`, `disarm` und `set_config` als "ändernde" Tools kennzeichnen
- Datenschutzhinweis-Vorlage für Endkunden, Löschkonzept

## Fertig, wenn …
- [ ] Ich kann in Claude Desktop sagen "Mach ein Foto" und sehe das Bild
- [ ] Alle Tools funktionieren lokal
- [ ] Cloud-Variante läuft, Fanbox lässt sich per Pairing-Code verknüpfen
- [ ] Claude (Web/Handy) erreicht die Fanbox über den Custom Connector
