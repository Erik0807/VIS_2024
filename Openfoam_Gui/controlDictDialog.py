# Einlesen benötigte Bibliotheken
#================================
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QDialog, QHBoxLayout,
                               QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox)
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Slot
from ofDialog import ofDialog


#===================================================================================
#                               KLASSE - controlDictDialog                         #
#===================================================================================

class controlDictDialog(ofDialog):
    # Konstruktor
    #============
    def __init__(self):
        # Mutterklassenkonstruktor
        super().__init__()

        # Titel des Fensters
        self.setWindowTitle("controlDict")

        # Application
        self.label = QLabel("apllication")
        self.layout().insertWidget(0, self.label)

        # Dropdown-Menü (QComboBox) befüllen
        self.dropdown.addItems(["icoFoam", "simpleFoam", "pimpleFoam"])
        self.layout().insertWidget(1, self.dropdown)

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)

