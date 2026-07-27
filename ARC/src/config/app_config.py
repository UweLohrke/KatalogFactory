"""
KatalogFactory by U.L.

Datei:
app_config.py

Version:
1.0.2

Beschreibung:
Zentrale Konfiguration der Anwendung.
"""

from pathlib import Path

# --------------------------------------------------
# Programm
# --------------------------------------------------

APP_NAME = "KatalogFactory"

APP_SIGNATURE = "by U.L."

APP_VERSION = "1.0.2"

# --------------------------------------------------
# Hauptfenster
# --------------------------------------------------

WINDOW_WIDTH = 920
WINDOW_HEIGHT = 650

WINDOW_MIN_WIDTH = 900
WINDOW_MIN_HEIGHT = 650

# --------------------------------------------------
# Statusleiste
# --------------------------------------------------

STATUS_READY = "Bereit"
STATUS_LOADING = "Katalog wird erstellt..."
STATUS_SUCCESS = "Katalog erfolgreich erstellt."
STATUS_ERROR = "Fehler bei der Katalogerstellung."

# --------------------------------------------------
# Datenordner
# --------------------------------------------------

DATA_ROOT = Path.home() / "KatalogFactory"

DATA_ROOT.mkdir(
    parents=True,
    exist_ok=True,
)

IMAGE_FOLDER = DATA_ROOT / "bilder"
EXCEL_FOLDER = DATA_ROOT / "excel"
CATALOG_FOLDER = DATA_ROOT / "kataloge"
DATABASE_FOLDER = DATA_ROOT / "database"
LOG_FOLDER = DATA_ROOT / "logs"

for folder in (
    IMAGE_FOLDER,
    EXCEL_FOLDER,
    CATALOG_FOLDER,
    DATABASE_FOLDER,
    LOG_FOLDER,
):
    folder.mkdir(
        parents=True,
        exist_ok=True,
    )