"""
KatalogFactory by U.L.

Datei:
main_window.py

Version:
0.8.0d

Beschreibung:
Hauptfenster der KatalogFactory.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from config.app_config import (
    APP_NAME,
    APP_VERSION,
    STATUS_READY,
    WINDOW_HEIGHT,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_WIDTH,
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(APP_NAME)

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

        self.setMinimumSize(
            WINDOW_MIN_WIDTH,
            WINDOW_MIN_HEIGHT,
        )

        self.create_ui()

    # --------------------------------------------------
    # Oberfläche
    # --------------------------------------------------

    def create_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget,
        )

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignTop)

        central_widget.setLayout(
            layout,
        )

        title = QLabel(APP_NAME)

        title.setAlignment(
            Qt.AlignCenter,
        )

        title.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            padding-top: 25px;
            """
        )

        layout.addWidget(
            title,
        )

        version = QLabel(
            f"Version {APP_VERSION}",
        )

        version.setAlignment(
            Qt.AlignCenter,
        )

        version.setStyleSheet(
            """
            font-size: 12px;
            color: gray;
            padding-bottom: 20px;
            """
        )

        layout.addWidget(
            version,
        )

        status_bar = QStatusBar()

        status_bar.showMessage(
            STATUS_READY,
        )

        self.setStatusBar(
            status_bar,
        )


def run():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(
        app.exec(),
    )