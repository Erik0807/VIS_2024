# Einlesen benötigte Bibliotheken
#================================
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QDialog, QHBoxLayout,
                               QVBoxLayout, QLabel, QPushButton, QLineEdit)
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Slot
from ofDialog import ofDialog


#===================================================================================
#                               KLASSE - setCaseDialog                             #
#===================================================================================

class setCaseDialog(ofDialog):
    # Konstruktor
    #============
    def __init__(self):
        # Mutterklassenkonstruktor
        super().__init__()

        # Titel des Fensters
        self.setWindowTitle("Set Case-Structure")

        # Aufforderung an User
        self.label = QLabel("Bitte geben Sie den Pfad zu Ihrem case ein:")
        self.layout().insertWidget(0, self.label)

        # Eingabefeld
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Pfad/zu/meinem/case")
        self.layout().insertWidget(1, self.input_field)

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.getInput)
        self.close_button.clicked.connect(self.reject)