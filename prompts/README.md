# Prompts: Fanbox → Kamera mit Claude-Steuerung

So benutzt du die Prompts:

| Etappe | Datei | Womit ausführen? | Was kommt raus? |
|---|---|---|---|
| 0 | `00-kontext.md` | – (wird jeder Etappe vorangestellt) | – |
| 1 | `01-hardware-und-mechanik.md` | Claude (Chat) + **STEP-Datei anhängen** | Einkaufsliste, Bauanleitung, 3D-Halterungen |
| 2 | `02-firmware.md` | **Claude Code** in diesem Repo | Software für das Gerät, Web-Flasher |
| 3 | `03-mcp-und-cloud.md` | **Claude Code** in diesem Repo | MCP-Server lokal + Cloud |
| 4 | `04-produkt.md` | Claude (Chat) | Weg zum verkaufsfähigen Produkt |

**Ablauf:**
1. Inhalt von `00-kontext.md` kopieren, darunter den Inhalt der aktuellen Etappe einfügen.
2. Rückfragen von Claude beantworten.
3. Am Ende jeder Etappe die **Zusammenfassung** speichern (z. B. als `ergebnisse/etappe-1.md`)
   und in die nächste Etappe mitnehmen.
4. Erst weitermachen, wenn die Checkliste "Fertig, wenn …" erfüllt ist.
