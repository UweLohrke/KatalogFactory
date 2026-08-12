#!/bin/bash

# ==========================================================
# KatalogFactory
#
# Datei:
# import_ecoinform.sh
#
# Version:
# 1.0.0
#
# Beschreibung:
#
# Importiert alle Bildarchive von Ecoinform.
#
# Die ZIP-Dateien bleiben unverändert im Archiv.
#
# Ziel:
#
# Ecoinform/
#     ARC/
#         Bilder_01.zip
#         Bilder_02.zip
#         ...
#
#                ↓
#
# Ecoinform/
#     Bilder/
#         4001234567890.jpg
#         4012345678901.jpg
#
# ==========================================================

clear

echo "=========================================================="
echo "        KatalogFactory - Ecoinform Import"
echo "=========================================================="
echo

cd ~/KatalogFactory || exit 1

ARC="Ecoinform/ARC"
TARGET="Ecoinform/Bilder"

mkdir -p "$TARGET"

echo "Archiv : $ARC"
echo "Ziel   : $TARGET"
echo

ZIP_COUNT=$(find "$ARC" -maxdepth 1 -name "*.zip" | wc -l | tr -d ' ')

echo "ZIP-Dateien gefunden : $ZIP_COUNT"
echo

if [ "$ZIP_COUNT" -eq 0 ]; then

    echo "Keine ZIP-Dateien gefunden."

    exit 0

fi

echo "Starte Import..."
echo

for ZIPFILE in "$ARC"/*.zip
do

    echo "----------------------------------------"
    echo "Entpacke:"
    echo "$(basename "$ZIPFILE")"
    echo

    unzip -n "$ZIPFILE" -d "$TARGET"

    echo

done

echo
echo "----------------------------------------"

IMAGE_COUNT=$(find "$TARGET" -type f | wc -l | tr -d ' ')

echo
echo "Import abgeschlossen."
echo
echo "Bilder insgesamt : $IMAGE_COUNT"
echo
echo "=========================================================="