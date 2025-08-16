# 🗺️ Projekt-Roadmap: openai-chat-splitter

> Status: ✅ Projekt gestartet, Core-Features fertig  
> Ziel: OpenAI-Exporte lokal analysieren, zerteilen und weiterverarbeiten  
> Fokus: Datenschutzfreundlich, CLI-basiert, lokal ausführbar

---

### ✅ Bereits erledigt

- [x] Projektstruktur mit `src/`, `input/`, `out_chats/`
- [x] Entpacken und Erkennen von OpenAI-Exporten (ZIP)
- [x] Analyse und Zählung von JSON-Dateien
- [x] Aufteilung von Chats in einzelne `.json` und `.md`
- [x] `.gitignore` für Output-Ordner
- [x] README mit zweisprachiger Schnellstart-Anleitung
- [x] Public Repo auf GitHub veröffentlicht
- [x] ZIP-Import und automatisches Entpacken im `input/`-Verzeichnis
- [x] Laden von `conversations.json` und Anzeige der enthaltenen Einträge
- [x] Splitten der Konversationen in einzelne `.json`- und `.md`-Dateien
- [x] Ausgabe im `out_chats/`-Verzeichnis mit sprechenden Ordnernamen
- [x] GitHub-Repository angelegt: [DockSeed/openai-chat-splitter](https://github.com/DockSeed/openai-chat-splitter)
- [x] Struktur mit `src/`, `main.py`, `requirements.txt`, `.gitignore`, `README.md`

### 🔜 Nächste Schritte (Geplant)

| Thema                       | Beschreibung                                                                 |
|----------------------------|------------------------------------------------------------------------------|
| 🧾 LICENSE-Datei           | Lizenz ergänzen (empfohlen: MIT oder Apache 2.0)                             |
| 🏷️ GitHub Topics setzen   | z. B. `openai`, `python`, `chat-export`, `cli-tool`, `json`, `markdown`     |
| 🧪 Beispiel-Export bereitstellen | Dummy-Account bei OpenAI anlegen, Mini-Chat erstellen, ZIP generieren und Beispiel bereitstellen |
| 📦 `requirements.txt` testen  | Verifizieren, dass `pip install -r requirements.txt` korrekt funktioniert    |
| 🆘 CLI-Hilfe integrieren    | Optional `--help` mit `argparse` oder `typer` hinzufügen                     |
| 🧪 Tests / Validation       | Grundlegende Tests für ZIP-Erkennung und Dateiausgabe                        |
| 🔖 Badges im README        | Python-Version, Lizenz-Badge, evtl. Link zu Docs                             |

### 🧠 Nice to Have (später)

- 🖼️ Web-GUI mit Drag-and-Drop ZIP → Anzeige der Chatliste
- 📝 Markdown-Vorlage anpassbar (z. B. mit Datum/Format)
- 🔍 Erweiterte Filter (z. B. nur User-Nachrichten extrahieren)
- 🧰 Tool als Python-Paket (`pip install openai-chat-splitter`)
- 📦 Dockerfile für einfaches Deployment
- 🧠 GPT-Modell für kontextuelle Tag-Zuweisung (optional lokal mit `ollama`)

---

## 🧩 Abhängigkeiten (Stand August 2025)

```txt
rich
markdownify
