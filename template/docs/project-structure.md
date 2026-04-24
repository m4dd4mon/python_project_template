# Projektstruktur

Platzhalter. Die ausfuehrliche Strukturbeschreibung wird im Zuge des
Jinjafizierungs-Schritts aus der Template-Vorlage generiert.

Kurzuebersicht:

- `src/projekt/` — der eigentliche Paketcode (src-Layout).
  - `core/` — Geschaeftslogik, UI-unabhaengig.
  - `data/` — Repository-Schicht, ORM-Modelle, Engine-Factories.
  - `common/` — Querschnittsfunktionen (Config, Logging).
  - `web/`, `gui/`, `cli/` — Praesentationsschichten.
  - `resources/` — paketinterne Konfiguration und Schemas.
- `tests/` — pytest-Tests, ausserhalb von `src/`.
- `scripts/` — einmalige Helfer (Seeding, Migrations-Skripte).
- `assets/` — Nicht-Python-Ressourcen (Icons, Beispieldaten).
- `docs/` — Projektdokumentation.
- `data/` — Laufzeitdaten, nicht in Git.
- `logs/` — Laufzeit-Protokolle, nicht in Git.
