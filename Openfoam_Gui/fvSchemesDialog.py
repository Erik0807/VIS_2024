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

class fvSchemesDialog(ofDialog):
    # Konstruktor
    #============
    def __init__(self):
        # Mutterklassenkonstruktor
        super().__init__()

        # Titel des Fensters
        self.setWindowTitle("fvSchemes")
        self.name = self.windowTitle()

        # Erzeugen der Dropdown-Menüs für die Dictionary-Einträge
        #========================================================
        # ddtSchemes
        #-----------
        self.label_ddtSchemes = QLabel("ddtSchemes")
        self.layout().insertWidget(0, self.label_ddtSchemes)
        self.dropdown_ddtSchemes = QComboBox()
        self.dropdown_ddtSchemes.addItems(["steady", "Euler", "backward", "CrankNicolson"])
        self.layout().insertWidget(1, self.dropdown_ddtSchemes)
        #----------------------------------------------------------------------------------




        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)