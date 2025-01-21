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
        #==================================================================================

        # Erzeugen der Dropdown-Menüs für die Dictionary-Einträge von U-Solvern
        #======================================================================
        # solver
        #-------
        self.label_solver_U = QLabel("solver")
        self.dropdown_solver_U = QComboBox()
        self.dropdown_solver_U.addItems(["PCG", "PBiCGStab"])
        #----------------------------------------------------------------------------------

        # preconditioner
        #---------------
        self.label_preconditioner_U = QLabel("preconditioner")
        self.dropdown_preconditioner_U = QComboBox()
        self.dropdown_preconditioner_U.addItems(["DIC", "DILU"])
        #----------------------------------------------------------------------------------

        # tolerance
        #----------
        self.label_tolerance_U = QLabel("tolerance")
        self.input_tolerance_U = QLineEdit()
        self.input_tolerance_U.setPlaceholderText("1e-06")
        #----------------------------------------------------------------------------------

        # relTol
        #-------
        self.label_relTol_U = QLabel("relTol")
        self.input_relTol_U = QLineEdit()
        self.input_relTol_U.setPlaceholderText("0.05")
        #----------------------------------------------------------------------------------

        # Layout für Gruppierung um U
        #----------------------------
        layout_U = QVBoxLayout()

        layout_U.addWidget(self.label_solver_U)
        layout_U.addWidget(self.dropdown_solver_U)

        layout_U.addWidget(self.label_preconditioner_U)
        layout_U.addWidget(self.dropdown_preconditioner_U)

        layout_U.addWidget(self.label_tolerance_U)
        layout_U.addWidget(self.input_tolerance_U)

        layout_U.addWidget(self.label_relTol_U)
        layout_U.addWidget(self.input_relTol_U)

        # Anlegen der p-Box
        #------------------
        self.U_box = QGroupBox("U")
        self.U_box.setLayout(layout_U)
        #==================================================================================

        # Layout der Gruppen zu Gesamtlayout
        self.layout().insertWidget(1, self.p_box)
        self.layout().insertWidget(2, self.pFinal_box)
        self.layout().insertWidget(3, self.U_box)

        # Label als Überschrift für Application-Menü
        #===========================================
        self.label_vU_coupling = QLabel("velocity-pressure coupling")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_vU_coupling.setFont(font)
        self.layout().insertWidget(4, self.label_vU_coupling)

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)