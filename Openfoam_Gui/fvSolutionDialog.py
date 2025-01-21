# Einlesen benötigte Bibliotheken
#================================
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QDialog, QHBoxLayout,
                               QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox)
from PySide6.QtGui import QAction, QKeySequence, QFont
from PySide6.QtCore import Slot
from ofDialog import ofDialog


#===================================================================================
#                               KLASSE - fvSolutionDialog                         #
#===================================================================================

class fvSolutionDialog(ofDialog):
    # Konstruktor
    #============
    def __init__(self):
        # Mutterklassenkonstruktor
        super().__init__()

        # Titel des Fensters
        self.setWindowTitle("fvSolution")
        self.name = self.windowTitle()

        # Buttons für Solver-Submenü
        self.label_solvers = QLabel("solvers")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_solvers.setFont(font)
        self.layout().insertWidget(0, self.label_solvers)

        # Erzeugen der Dropdown-Menüs für die Dictionary-Einträge
        #========================================================
        # ddtSchemes
        #-----------


        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)