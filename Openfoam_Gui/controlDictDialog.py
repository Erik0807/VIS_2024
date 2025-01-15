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

        # Dropdown-Menü (QComboBox)
        self.dropdown = QComboBox()
        self.dropdown.addItems(["icoFoam", "simpleFoam", "pimpleFoam"])  # Menüeinträge hinzufügen
        self.layout().insertWidget(1, self.dropdown)

