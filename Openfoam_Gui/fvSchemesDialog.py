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

        # gradSchemes
        #------------
        self.label_gradSchemes = QLabel("gradSchemes")
        self.layout().insertWidget(2, self.label_gradSchemes)
        self.dropdown_gradSchemes = QComboBox()
        self.dropdown_gradSchemes.addItems(["Gauss linear", "leastSquares"])
        self.layout().insertWidget(3, self.dropdown_gradSchemes)
        #----------------------------------------------------------------------------------

        # divSchemes
        #-----------
        self.label_divSchemes = QLabel("divSchemes")
        self.layout().insertWidget(4, self.label_divSchemes)
        self.dropdown_divSchemes = QComboBox()
        self.dropdown_divSchemes.addItems(["Gauss upwind", "Gauss linearUpwind", "Gauss linear", "Gauss vanLeer", "Gauss limitedLinear", "leastSquares"])
        self.layout().insertWidget(5, self.dropdown_divSchemes)
        #----------------------------------------------------------------------------------

        # laplacianSchemes
        #-----------------
        self.label_laplacianSchemes = QLabel("laplacianSchemes")
        self.layout().insertWidget(6, self.label_laplacianSchemes)
        self.dropdown_laplacianSchemes = QComboBox()
        self.dropdown_laplacianSchemes.addItems(["Gauss linear orthogonal", "Gauss linear corrected", "Gauss linear limited", "Gauss linear uncorrected"])
        self.layout().insertWidget(7, self.dropdown_laplacianSchemes)
        #----------------------------------------------------------------------------------

        # interpolationSchemes
        #---------------------
        self.label_interpolationSchemes = QLabel("interpolationSchemes")
        self.layout().insertWidget(8, self.label_interpolationSchemes)
        self.dropdown_interpolationSchemes = QComboBox()
        self.dropdown_interpolationSchemes.addItems(["linear"])
        self.layout().insertWidget(9, self.dropdown_interpolationSchemes)
        #----------------------------------------------------------------------------------

        # snGradSchemes
        #--------------
        self.label_snGradSchemes = QLabel("snGradSchemes")
        self.layout().insertWidget(10, self.label_snGradSchemes)
        self.dropdown_snGradSchemes = QComboBox()
        self.dropdown_snGradSchemes.addItems(["limited 1", "orthogonal"])
        self.layout().insertWidget(11, self.dropdown_snGradSchemes)
        #----------------------------------------------------------------------------------

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)