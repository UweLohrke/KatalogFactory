"""
KatalogFactory by U.L.

Datei:
main_window.py

Version:
0.8.0a

Beschreibung:
Erzeugt das Hauptfenster der KatalogFactory.
"""

import tkinter as tk


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("KatalogFactory by U.L.")

        self.root.geometry("900x600")

        self.root.minsize(800, 550)

        self.create_widgets()

    # --------------------------------------------------
    # Oberfläche erstellen
    # --------------------------------------------------

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="KatalogFactory by U.L.",
            font=("Helvetica", 22, "bold"),
        )

        title.pack(pady=(30, 10))

        version = tk.Label(
            self.root,
            text="Version 0.8.0a",
            font=("Helvetica", 11),
        )

        version.pack()

        status = tk.Label(
            self.root,
            text="Status: Bereit",
            font=("Helvetica", 10),
        )

        status.pack(side="bottom", pady=15)

    # --------------------------------------------------
    # Fenster starten
    # --------------------------------------------------

    def run(self):

        self.root.mainloop()