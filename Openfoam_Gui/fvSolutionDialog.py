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



        # Layout für Gruppierung um p
        #----------------------------
        layout_p = QVBoxLayout()
        layout_p.addWidget(self.label_solver)
        layout_p.addWidget(self.dropdown_solver)
        layout_p.addWidget(self.label_preconditioner)
        layout_p.addWidget(self.dropdown_preconditioner)

        # Anlegen der p-Box
        #------------------
        p_box = QGroupBox("p")
        p_box.setLayout(layout_p)

        # Layout von p zu Gesamtlayout
        self.layout().insertWidget(1, p_box)

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)