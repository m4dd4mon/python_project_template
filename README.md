# python-project-template

Ein Copier-Template fuer moderne Python-Projekte mit einer festen,
opinionierten Grundstruktur. Das Template erzeugt ein sofort lauffaehiges
Projekt nach dem src-Layout mit `uv` als Paketmanager, `ruff` fuer Linting
und Formatierung, `pytest` fuer Tests und `mypy` fuer statische Typpruefung.
Optional laesst sich Datenbank-Support mit SQLAlchemy, Alembic und einem
Dual-DB-Design (externe Datenbank und lokale Docker-Instanz parallel
nutzbar) aktivieren, dazu eine Web-Oberflaeche, eine Desktop-GUI und ein
CLI-Einstiegspunkt.

## Wofuer dieses Template gedacht ist

Es ist ein persoenliches Werkzeug, um in zwei Minuten Copier-Dialog statt
in fuenfzehn Minuten manuellem Kopieren und Umbenennen ein neues
Python-Projekt aufzusetzen, das bereits die Konventionen und
Werkzeug-Entscheidungen mitbringt, die sich in eigenen Projekten bewaehrt
haben. Die Werkzeug-Entscheidungen (uv, ruff, pytest, mypy) sind hart
verdrahtet und nicht abfragbar, weil jede zusaetzliche Frage im
Copier-Dialog Reibung erzeugt und die Auswahl in der Praxis ohnehin immer
dieselbe waere.

## Aufruf

```bash
copier copy gh:m4dd4mon/python-project-template mein-neues-projekt
```

Mit expliziter Versionsangabe (empfohlen fuer reproduzierbare
Generierung):

```bash
copier copy --vcs-ref v0.1.0 gh:m4dd4mon/python-project-template mein-neues-projekt
```

Beim ersten Aufruf fuehrt Copier durch den Fragenkatalog (Projektname,
Paket-Slug, Python-Version, Feature-Flags), rendert den Schablonenbaum in
den Zielordner und legt eine `.copier-answers.yml` ab, die spaetere
`copier update`-Laeufe zur Fortschreibung des Projekts nutzen koennen.

## Update eines bestehenden Projekts

In einem Projekt, das aus einer frueheren Template-Version generiert
wurde, reicht ein Aufruf, um Verbesserungen aus dem Template als
Drei-Wege-Merge zurueckzuspielen:

```bash
copier update
```

Projektspezifische Aenderungen bleiben erhalten, neue Template-Dateien
kommen dazu, geaenderte werden gemerged. Konflikte werden im
`.orig`/`.rej`-Format zum Aufloesen vorgelegt.

## Status

Dieses Repository ist ein Copier-Template, **kein** GitHub-Template. Der
"Use this template"-Button in den GitHub-Einstellungen ist bewusst
ausgeschaltet, weil er konzeptionell mit Copier konfligieren wuerde.
