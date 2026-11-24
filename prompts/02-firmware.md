# Etappe 2 – Firmware (Software auf dem Gerät)

> Voraussetzung: `00-kontext.md` + **Zusammenfassung aus Etappe 1** davor einfügen.
> Empfehlung: Diese Etappe mit **Claude Code** direkt in diesem Repository ausführen,
> damit der Code gleich als Dateien entsteht und getestet werden kann.

---

## Aufgabe dieser Etappe
Schreibe die komplette Firmware für die in Etappe 1 gewählte Hardware – so, dass ich
**ohne Programmier-Kenntnisse** das Gerät in Betrieb nehmen kann.

## Anforderungen an die Bedienung (für mich als Laien)
- **Kein Installieren von Entwicklungsumgebungen nötig**, wenn vermeidbar:
  - Firmware wird automatisch per **GitHub Actions** gebaut.
  - Aufspielen über den **Browser** (z. B. ESP Web Tools / "Web-Flasher"-Seite) bzw. per
    fertigem SD-Karten-Image (bei Raspberry Pi).
- **WLAN-Einrichtung ohne Code**: Gerät öffnet beim ersten Start ein eigenes WLAN
  (Captive Portal) oder per Bluetooth/App – ich wähle mein WLAN und gebe das Passwort ein.
- **Status-/Aufnahme-LED** zeigt, was das Gerät gerade tut (Tabelle: Farbe/Blinkmuster → Bedeutung).
  Die LED leuchtet bei jeder Aufnahme und jedem Stream; per Konfiguration abschalt- und dimmbar.
- Reset auf Werkseinstellungen per Taster.

## Funktionen
1. Foto auf Abruf (JPEG), Auflösung einstellbar
2. Videostream (MJPEG o. ä.) – nur bei Bedarf aktiv
3. Bewegungserkennung per PIR → Foto → auf microSD speichern (+ optional Upload, Etappe 3)
5. Scharf/unscharf, Zeitpläne, automatische Löschung alter Bilder nach X Tagen
6. Statuswerte: Stromquelle/Akku, WLAN-Signal, freier Speicher, Firmware-Version, Laufzeit
7. **Lokale API** (REST, mit Token-Schutz):
   `/snapshot`, `/stream`, `/status`, `/events`, `/events/{id}/image`,
   `/arm`, `/disarm`, `/led`, `/config`
8. **Vorbereitet für die Cloud** (Etappe 3): ausgehende verschlüsselte Verbindung
   (MQTT über TLS oder WebSocket) bzw. Fernzugriff gemäß Etappe 3
9. **Sichere Updates (OTA)** mit Rollback
10. Energiesparmodus für Phase 2 (Akku), per Konfiguration zuschaltbar

## Lieferumfang
- Projektstruktur als Baum, danach **alle Dateien vollständig**
- Begründung der Technik (ESP-IDF / Arduino / PlatformIO / ESPHome / Linux+Python)
  mit Blick auf **Einfachheit für mich** und gute Wartbarkeit
- GitHub-Actions-Workflow zum automatischen Bauen
- Web-Flasher-Seite (bzw. Image-Anleitung)
- **Inbetriebnahme-Anleitung für Laien**: flashen → WLAN einrichten → erstes Foto im Browser
- **Testanleitung**: Jede Funktion einzeln ausprobieren (Browser-Adresse eingeben, was
  sollte ich sehen?)
- Fehlerbehebung: die 10 häufigsten Probleme und ihre Lösung

## Fertig, wenn …
- [ ] Firmware baut automatisch fehlerfrei
- [ ] Ich kann das Gerät über den Browser flashen und ins WLAN bringen
- [ ] Foto, Stream, Bewegung, LED und Status funktionieren über die lokale API
- [ ] Zusammenfassung "API-Beschreibung für Etappe 3" (Endpunkte, Datenformate, Auth)
