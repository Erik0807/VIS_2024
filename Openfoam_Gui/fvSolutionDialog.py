# Einlesen benötigte Bibliotheken
#================================
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QDialog, QHBoxLayout,
                               QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox,
                               QGroupBox)
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

        # Label als Überschrift für Solver-Menü
        #======================================
        self.label_solvers = QLabel("solvers")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_solvers.setFont(font)
        self.layout().insertWidget(0, self.label_solvers)

        # Erzeugen der Dropdown-Menüs für die Dictionary-Einträge von p-Solvern
        #======================================================================
        # solver
        #-------
        self.label_solver = QLabel("solver")
        self.dropdown_solver = QComboBox()
        self.dropdown_solver.addItems(["PCG", "PBiCGStab"])
        #----------------------------------------------------------------------------------

        # preconditioner
        #---------------
        self.label_preconditioner = QLabel("preconditioner")
        self.dropdown_preconditioner = QComboBox()
        self.dropdown_preconditioner.addItems(["DIC", "DILU"])
        #----------------------------------------------------------------------------------

        # tolerance
        #----------
        self.label_tolerance = QLabel("tolerance")
        self.input_tolerance = QLineEdit()
        self.input_tolerance.setPlaceholderText("1e-06")
        #----------------------------------------------------------------------------------

        # relTol
        #-------
        self.label_relTol = QLabel("relTol")
        self.input_relTol = QLineEdit()
        self.input_relTol.setPlaceholderText("0.05")
        #----------------------------------------------------------------------------------

        # Layout für Gruppierung um p
        #----------------------------
        layout_p = QVBoxLayout()

        layout_p.addWidget(self.label_solver)
        layout_p.addWidget(self.dropdown_solver)

        layout_p.addWidget(self.label_preconditioner)
        layout_p.addWidget(self.dropdown_preconditioner)

        layout_p.addWidget(self.label_tolerance)
        layout_p.addWidget(self.input_tolerance)

        layout_p.addWidget(self.label_relTol)
        layout_p.addWidget(self.input_relTol)

        # Anlegen der p-Box
        #------------------
        self.p_box = QGroupBox("p")
        self.p_box.setLayout(layout_p)
        #==================================================================================

        # Erzeugen der Dropdown-Menüs für die Dictionary-Einträge von pFinal-Solvern
        #===========================================================================
        # relTol
        #-------
        self.label_relTol_pFin = QLabel("relTol")
        self.input_relTol_pFin = QLineEdit()
        self.input_relTol_pFin.setPlaceholderText("0.05")
        #----------------------------------------------------------------------------------

        # Layout für Gruppierung um pFinal
        #---------------------------------
        layout_pFinal = QVBoxLayout()

        layout_pFinal.addWidget(self.label_relTol_pFin)
        layout_pFinal.addWidget(self.input_relTol_pFin)

        # Anlegen der pFinal-Box
        #-----------------------
        self.pFinal_box = QGroupBox("pFinal")
        self.pFinal_box.setLayout(layout_pFinal)




        # Layout der Gruppen zu Gesamtlayout
        self.layout().insertWidget(1, self.p_box)
        self.layout().insertWidget(2, self.pFinal_box)

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)