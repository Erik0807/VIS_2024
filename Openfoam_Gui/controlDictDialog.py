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
        self.name = self.windowTitle()

        # Erzeugen der Dropdown-Menüs für die Dictionary-Einträge
        #--------------------------------------------------------
        # Application
        self.label_app = QLabel("application")
        self.layout().insertWidget(0, self.label_app)
        self.dropdown_app = QComboBox()
        self.dropdown_app.addItems(["icoFoam", "simpleFoam", "pimpleFoam"])
        self.layout().insertWidget(1, self.dropdown_app)

        # startFrom
        self.label_start = QLabel("startFrom")
        self.layout().insertWidget(2, self.label_start)
        self.dropdown_start = QComboBox()
        self.dropdown_start.addItems(["latestTime", "0"])
        self.layout().insertWidget(3, self.dropdown_start)

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)

