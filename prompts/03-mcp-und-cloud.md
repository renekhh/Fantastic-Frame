# Etappe 3 – MCP-Server & Fernzugriff (Steuerung aus Claude)

> Voraussetzung: `00-kontext.md` + **Zusammenfassungen aus Etappe 1 und 2** davor einfügen.
> Empfehlung: mit **Claude Code** direkt in diesem Repository ausführen.

---

## Aufgabe dieser Etappe
Baue die Verbindung zwischen Fanbox und Claude – zuerst **lokal** im Heimnetz, dann
**von unterwegs** (Claude auf Handy/Web). Nur für mich bzw. meinen Haushalt – so
**einfach wie möglich** zu betreiben.

## Schritt 3a – Lokaler MCP-Server (zuerst!)
- Läuft auf meinem PC im Heimnetz, spricht mit der lokalen API der Fanbox.
- **Einfach zu installieren** (ein Befehl, z. B. `npx …` oder `uvx …`), Konfiguration per
  `.env`; die Fanbox wird im Netz automatisch gefunden (mDNS), sonst feste Adresse.
- Anleitung zum Eintragen in **Claude Desktop** (`claude_desktop_config.json`) und
  **Claude Code** (`claude mcp add …`) – mit exaktem Text zum Kopieren.

## Schritt 3b – Zugriff von unterwegs
- Ziel: Claude auf dem Handy/im Web kann die Fanbox steuern, **ohne Portfreigabe am Router**.
- Vergleiche 2–3 einfache Wege und empfiehl einen, z. B.:
  - **Tailscale** (privates VPN) + MCP-Server auf einem immer laufenden Gerät zu Hause
    (Raspberry Pi / NAS / PC),
  - **Cloudflare Tunnel** zu einem Remote-MCP-Server (Streamable HTTP) zu Hause,
  - kleiner **Cloud-Server** (günstiger VPS), mit dem sich die Fanbox ausgehend verbindet.
  Kriterien: Einrichtungsaufwand für Laien, laufende Kosten, Sicherheit, Zuverlässigkeit.
- **Eine Codebasis** für lokal (stdio) und remote (Streamable HTTP mit Login/Token).
- Einbindung in Claude als **Custom Connector** (Schritt-für-Schritt-Anleitung).
- Livestream von unterwegs über einen zeitlich begrenzten, geheimen Link
  (Claude selbst kann Streams nicht ansehen, nur Einzelbilder).
- Falls ein Server nötig ist: Deployment per **Docker Compose** mit Laien-Anleitung.

## MCP-Tools
| Tool | Zweck |
|---|---|
| `list_devices()` | Meine Rahmen auflisten (vorbereitet für mehr als einen) |
| `take_snapshot(device_id)` | Foto aufnehmen, als **Bild** an Claude zurückgeben |
| `get_stream_url(device_id, ttl_minutes)` | Zeitlich begrenzter Livestream-Link |
| `get_status(device_id)` | Strom/Akku, WLAN, scharf/unscharf, Speicher, Firmware |
| `list_events(device_id, since, until, limit)` | Bewegungs-Ereignisse |
| `get_event_image(event_id)` | Bild zu einem Ereignis |
| `arm(device_id)` / `disarm(device_id)` | Überwachung an/aus |
| `set_led(device_id, mode)` | LED-Effekte/Helligkeit (z. B. "Auge leuchten lassen") – Aufnahme-Anzeige kann **nicht** abgeschaltet werden |
| `set_config(device_id, …)` | Empfindlichkeit, Speicherdauer, Zeitpläne, Aufnahme-LED an/aus/Helligkeit |

Klare Tool-Beschreibungen, damit Claude sie richtig nutzt; Fehlerbehandlung, wenn das Gerät
offline ist oder schläft (Phase 2: letztes Bild aus Cache + Hinweis).

## Sicherheit (Basis)
- Verschlüsselte Verbindungen, Token/Passwort-Schutz, keine Standard-Passwörter.
- `set_led`, `disarm` und `set_config` als "ändernde" Tools kennzeichnen.

## Fertig, wenn …
- [ ] Ich kann in Claude Desktop sagen "Mach ein Foto" und sehe das Bild
- [ ] Alle Tools funktionieren lokal
- [ ] Von unterwegs (Handy) funktioniert "Mach ein Foto" ebenfalls
