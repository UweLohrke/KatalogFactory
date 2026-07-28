"""
KatalogFactory by U.L.

Datei:
init_database.py

Version:
1.0.0

Beschreibung:
Initialisiert die SQLite-Datenbank.
"""

import sqlite3
from pathlib import Path


DATABASE = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "database"
    / "katalogfactory.db"
)


def initialize_database():

    connection = sqlite3.connect(
        DATABASE
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS manufacturer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            website TEXT,
            logo TEXT,
            status TEXT DEFAULT 'Neu',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()

    print(
        "Datenbank erfolgreich initialisiert."
    )


if __name__ == "__main__":
    initialize_database()