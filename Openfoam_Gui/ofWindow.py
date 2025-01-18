# Einlesen benötigte Bibliotheken
#================================
import sys
import os
from pathlib import Path
from PySide6.QtCore import Slot
import vtk
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import ofDialog as ofDialog
import setCaseDialog as setCaseDialog
import controlDictDialog as controlDictDialog
import setWorkDirDialog as setWorkDirDialog

#===================================================================================
#                               KLASSE - ofWindow                                 #
#===================================================================================

class ofWindow(QMainWindow):
    # Konstruktor
    #============
    def __init__(self, widget):
        # Mutterklassenkonstruktor
        #-------------------------
        QMainWindow.__init__(self)

        # Initialisieren eines Dateipfads
        self.file_path = ""

        # Fenstertitel / zentrales Widget definieren
        #-------------------------------------------
        self.setWindowTitle("OpenFoam")
        self.setCentralWidget(widget)

        # Initialisiere Instanzvariable für das VTK-Widget
        self.vtkWidget = None
    
        # Menüleiste anlegen (File, system, constant, 0)
        #-----------------------------------------------
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.sys_menu = self.menu.addMenu("system")
        self.const_menu = self.menu.addMenu("constant")
        self.RB_menu = self.menu.addMenu("Randbedingungen")
        #--------------------------------------------------------------------------

        # Funktionen im File-Menü
        #------------------------
        # SetWorkDir-Aktion, um Arbeitsverzeichnis festzulegen
        setWorkDir_action = QAction("Set Working Directory", self)
        setWorkDir_action.triggered.connect(self.setWorkDir)

        # SetCase-Aktion, um Ordnerstruktur aufzusetzen
        setCase_action = QAction("Set Case", self)
        setCase_action.triggered.connect(self.setCase)

        # Exit-Aktion definieren
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        # Aktionen zu File-Menü hinzufügen
        self.file_menu.addAction(setWorkDir_action)
        self.file_menu.addAction(setCase_action)
        self.file_menu.addAction(exit_action)
        #--------------------------------------------------------------------------

        # Funktionen im system-Menü
        #--------------------------
        controlDict_action = QAction("controlDict", self)
        controlDict_action.triggered.connect(self.writeControlDict)

        fvSchemes_action = QAction("fvSchemes", self)
        fvSolution_action = QAction("fvSolution", self)

        # Aktionen zu system-Menü hinzufügen
        self.sys_menu.addAction(controlDict_action)
        self.sys_menu.addAction(fvSchemes_action)
        self.sys_menu.addAction(fvSolution_action)
        #--------------------------------------------------------------------------

        # Funktionen im constant-Menü
        #----------------------------
        thermo_action = QAction("thermophysicalProperties", self)
        turbulence_action = QAction("turbulenceProperties", self)

        # Aktionen zu system-Menü hinzufügen
        self.const_menu.addAction(thermo_action)
        self.const_menu.addAction(turbulence_action)
        #--------------------------------------------------------------------------

        # Funktionen im Randbedingungen-Menü
        #-----------------------------------
        p_action = QAction("p", self)
        U_action = QAction("U", self)
        T_action = QAction("T", self)

        # Aktionen zu system-Menü hinzufügen
        self.RB_menu.addAction(p_action)
        self.RB_menu.addAction(U_action)
        self.RB_menu.addAction(T_action)
        #--------------------------------------------------------------------------

        # Statusleiste
        #-------------
        self.status = self.statusBar()
        self.status.showMessage("OpenFoam startklar")

        # Interaktion mit VTK
        #--------------------
        self.loadVTKbackGround(widget)

        # Abmessungen des Main-Windows festlegen
        #---------------------------------------
        geometry = self.screen().availableGeometry()
        self.setFixedSize(geometry.width() * 0.6, geometry.height() * 0.7)
    #=======================================================================================

    # Fkt. - loadVTKbackGround
    #=========================
    def loadVTKbackGround(self, widget):
        # QVTKRenderWindowInteractor hinzufügen
        self.vtkWidget = QVTKRenderWindowInteractor(widget)
        widget.main_layout.addWidget(self.vtkWidget)

        # VTK Renderer einrichten
        self.renderer = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)

        # Interactor initialisieren
        self.interactor = self.vtkWidget.GetRenderWindow().GetInteractor()
        self.renderer.SetBackground(0.1, 0.2, 0.4)  # Hintergrundfarbe
        self.interactor.Initialize()
    #=======================================================================================

    # Fkt. - setWorkDir
    #==================
    def setWorkDir(self):
        '''
        Fkt.-Beschreibung:
            setWorkDir legt das gewünschte Arbeitsverzeichnis (Pfad zum bestehenden Case) \n
        Output:
            workDir...Pfad zum aktuellen Case
        '''
        # Aufrufen des Dialogs (für case-Pfad)
        self.dialog = setWorkDirDialog.setWorkDirDialog()
        self.dialog.exec()

        # Abspeichern des case-Pfads
        self.workDir = Path(self.dialog.getFilepath()).resolve()
    #=======================================================================================

    # Fkt. - setCase
    #===============
    def setCase(self):
        '''
        Fkt.-Beschreibung:
        \t setCase legt die benötigte Ordnerstruktur eines Openfoam-Cases an
           (system, constant, 0)
        '''
        # Aufrufen des Dialogs (für case-Pfad)
        self.dialog = setCaseDialog.setCaseDialog()
        self.dialog.exec()

        # Abspeichern des case-Pfads
        self.file_path = Path(self.dialog.getFilepath()).resolve()

        # Anlegen des Case-Ordners und der 3 Unterordner
        Case = Path(self.file_path) / "case"
        system = Path(self.file_path) / "case/system"
        constant = Path(self.file_path) / "case/constant"
        dir0 = Path(self.file_path) / "case/0"

        # Erstellen des Case-Ordners und der 3 Unterordner
        Case.mkdir(parents = True, exist_ok = True)
        system.mkdir(parents = True, exist_ok = True)
        constant.mkdir(parents = True, exist_ok = True)
        dir0.mkdir(parents = True, exist_ok = True)
    #=======================================================================================

    # Fkt. - writeControlDict
    #========================
    def writeControlDict(self):
        '''
        Fkt.-Beschreibung:
        \t writeControlDict öffnet einen Q-Dialog mit versch. Dropdown-Menüs zum 
        \t controlDict. Bei Klick auf ok wird ein Textfile in den system-Ordner gespeichert.
        '''
        # Aufrufen des Dialogs (für case-Pfad)
        self.dialog = controlDictDialog.controlDictDialog()
        self.dialog.exec()
    #=======================================================================================
