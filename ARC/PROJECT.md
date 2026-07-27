# KatalogFactory

## Projekt

Automatische Erstellung von Produktkatalogen für die Rhein-Main-Bio GmbH.

Die KatalogFactory importiert Artikeldaten aus einer Excel-Datei,
gruppiert diese nach Herstellern und erzeugt daraus einen professionellen PDF-Katalog.

---

# Aktuelle Version

0.5.0

---

# Projektstatus

✅ Excel-Import

✅ Regionsauswahl

✅ Herstellergruppierung

✅ PDF-Erzeugung

✅ PDF-Kopf

🔄 Erste echte Artikeldaten

⬜ Produktbilder

⬜ Barcode

⬜ Vollständiger Katalog

⬜ GUI

---

# Projektstruktur

KatalogFactory/

assets/
bilder/
config/
database/
excel/
kataloge/
logs/
src/
tests/

CHANGELOG.md

PROJECT.md

VERSION

---

# Datenquelle

Excel-Datei

Listungsanalyse nach Region 25.05.2026.xlsx

---

# PDF-Aufbau

Seitenkopf

Logo

Rhein-Main-Bio GmbH

Region

Datum

Seitenzahl

Hersteller

Artikel

Produktbild

Artikelname

Mengentext

EH GTIN

Listenpreis

UVP

Barcode

---

# Wichtige Entscheidungen

Die EH GTIN ist der eindeutige Schlüssel eines Artikels.

Produktbilder werden anhand der EH GTIN gefunden.

Barcodes werden aus der EH GTIN erzeugt.

Hersteller werden gruppiert dargestellt.

Der PDFGenerator kennt keine Excel-Datei.

Der CatalogBuilder liefert die Daten für den PDFGenerator.

---

# Entwicklungsregeln

Es wird immer nur eine Datei gleichzeitig geändert.

Nach jeder Änderung wird getestet.

Nach jedem erfolgreichen Test erfolgt ein Git-Commit.

Es werden immer komplette Dateien ersetzt.

Keine Teilstücke.

Keine halbfertigen Funktionen.

---

# Roadmap

Version 0.5.0

Erste echte Artikeldaten

Version 0.6.0

Alle Artikel eines Herstellers

Version 0.7.0

Seitenumbruch

Version 0.8.0

Produktbilder

Version 0.9.0

Barcode

Version 1.0.0

Produktive Version