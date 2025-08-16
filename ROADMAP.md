# Projekt-Roadmap: AI Chat Export Analyzer

**Scope:** Offline-Analyse historischer Chat-Exporte (OpenAI/Claude/…), ohne Live-Integration oder Community-Backend. Ziel: ZIP rein → Reports/Ordner raus (CLI & optional GUI).

---

## Struktur der Roadmap
1. Core-Tool Features (Kern) — P0/P1
2. Erweiterte Analyse (Optional) — P1/P2
3. Langzeit- & Community-Features → ausgelagert in `futureideas.md`
4. Moonshot & Spaßideen → ausgelagert in `futureideas.md`

> Prioritäten: P0 = Now, P1 = Next, P2 = Later (Impact × Effort).

---

## 1) Core-Tool Features (Kern)

### M0 — Fundament (P0)
- Provider-System & Normalisierung (openai/anthropic/generic) → einheitliches normalized schema.
- CLI (`--provider`, `--formats`, `--out`, `--analyze`, `--report`, `--encrypt`).
- Exporte: Markdown (linear/branched), JSON (normalized), HTML (lokal, mit Suche).  
- Multimedia-Support: Bilder/Audio/Anhänge extrahieren & in HTML/MD einbetten.
- Smart Search: Volltext & Feldfilter (Zeit, Rolle, Tags).
- Convo-Bookmarks: Sprungmarken & Inhaltsverzeichnisse in langen Chats.
- Verschlüsselung (optional): AES-GCM für Exportordner/ZIP.

### M1 — Reports & GUI (P0–P1)
- HTML-Report mit Statistiken (Aktivität, Häufigkeiten, Top-Wörter).
- PDF-Buch (P1): Kapitel/TOC, eingebettete Medien.
- EPUB (P2): später; gleiche Struktur wie PDF.
- GUI lokal (optional, P1): ZIP wählen → Zielordner/Report generieren.

### M2 — Analyse Core (P1)
- Wort-/Token-Stats pro Rolle/Zeitraum (CSV + Charts).
- Aktivitäts-Timeline (Heatmap/Tageszeiten/Monate).
- Themenanalyse (Topic-Cluster/Top-Begriffe).  
- Retry-/Fehler-Muster (wiederholte Fragen, Error-Patterns).
- Fragment-Glue: Fäden über Monate verknüpfen.
- Knowledge-Graph (leichtgewichtig): Entitäten/Themen-Beziehungen.

> Aus dem Kern entfernt (verschoben): Sentiment Journey, Learning Velocity, Chat-DNA, Provider-Vergleich (KI-Battle) → siehe `futureideas.md` (nur eingeschränkt sinnvoll ohne Live-Daten).

---

## 2) Erweiterte Analyse (Optional – P1/P2)
- Evolution-Timeline: Entwicklung von Themen über Zeit (P1).
- Cluster-Visualisierungen (Mindmap/Graph) im HTML-Report (P1).
- Auto-Tags (offline-first): Regelsatz + NLP; optional `--llm-tags` (P2).

---

## Akzeptanzkriterien
- Normalized Schema per JSON-Schema validiert (id, created_at ISO, role, content[], attachments[], meta…).
- HTML offline: lokale Medien, Suche < 150 ms bei 10k Messages.
- CLI/Report Konsistenz: identische Suchergebnisse in CLI & HTML.
- PDF/EPUB: TOC, Paginierung, Bilder eingebettet; Größenlimits dokumentiert.
- Crypto: `--encrypt` erzeugt entschlüsselbares ZIP (Passphrase-Flow).

---

## Backlog nach Nutzen
**High (P0/P1)**  
Provider/Schema, CLI, MD/HTML/JSON, Multimedia, Smart Search, Bookmarks, HTML-Report, PDF, Wort-/Aktivitäts-Stats, Fragment-Glue, Retry-/Error-Patterns, Knowledge-Graph light.

**Medium (P1/P2)**  
GUI lokal, Evolution-Timeline, Cluster-Visuals, Auto-Tags (offline-first), EPUB.

**Low (P2)**  
Fancy-Visuals Feinschliff, zusätzliche Export-Layouts.

---

## Nicht-Ziele in diesem Projekt
Alle Features, die Langzeitnutzung, Live-Daten, Community oder Marketing/Entertainment benötigen → ausgelagert in `futureideas.md` (Abschnitte „Langzeit- & Community-Features“ und „Moonshot & Spaßideen“).
