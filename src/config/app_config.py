"""
KatalogFactory by U.L.

Datei:
app_config.py

Version:
1.1.0

Beschreibung:
Zentrale Konfiguration der Anwendung.

Alle Datenordner werden zentral
verwaltet.

Bevorzugt wird der gemeinsame
iCloud-Datenordner. Existiert dieser
nicht, wird automatisch auf den
lokalen Projektordner zurückgegriffen.
"""

from pathlib import Path

# --------------------------------------------------
# Programm
# --------------------------------------------------

APP_NAME = "KatalogFactory"

APP_SIGNATURE = "by U.L."

APP_VERSION = "1.1.0"

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

ICLOUD_ROOT = (
    Path.home()
    / "Library"
    / "Mobile Documents"
    / "com~apple~CloudDocs"
    / "KatalogFactory"
)

LOCAL_ROOT = (
    Path.home()
    / "KatalogFactory"
)

if ICLOUD_ROOT.exists():

    DATA_ROOT = ICLOUD_ROOT

else:

    DATA_ROOT = LOCAL_ROOT

IMAGE_FOLDER = DATA_ROOT / "Bilder"
EXCEL_FOLDER = DATA_ROOT / "Excel"
CATALOG_FOLDER = DATA_ROOT / "Kataloge"
DATABASE_FOLDER = DATA_ROOT / "Datenbank"
LOG_FOLDER = DATA_ROOT / "Logs"

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