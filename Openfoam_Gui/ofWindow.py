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
        self.RB_menu = self.menu.addMenu("0")
        #--------------------------------------------------------------------------

        # Funktionen im File-Menü
        #------------------------
        # Load-Aktion definieren
        load_action = QAction("Load", self)
        load_action.triggered.connect(lambda: self.load(widget))

        # Speicher-Aktion definieren
        save_action = QAction("Save", self)
        save_action.triggered.connect(lambda: self.save())

        # Exit-Aktion definieren
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        # Aktionen zu File-Menü hinzufügen
        self.file_menu.addAction(load_action)
        self.file_menu.addAction(save_action)
        self.file_menu.addAction(exit_action)
        #--------------------------------------------------------------------------

        # Funktionen im system-Menü
        #--------------------------
        controlDict_action = QAction("controlDict", self)
        fvSchemes_action = QAction("fvSchemes", self)
        fvSolution_action = QAction("fvSolution", self)

        # Aktionen zu system-Menü hinzufügen
        self.sys_menu.addAction(controlDict_action)
        self.sys_menu.addAction(fvSchemes_action)
        self.sys_menu.addAction(fvSolution_action)

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

    # Fkt. - importFdd
    #=================
    def importFdd(self, widget):
        '''
        Fkt.-Beschreibung:
        \t importFdd liest ein fdd-File ein und visualisiert dieses
        \n
        Input-Variablen:
        \t widget...Objekt vom Typ QWidget oder einer abgeleiteten Klasse
        '''
        # Überprüfen, ob schon ein vtk-Widget existiert (wenn nicht -> Widget erstellen)
        if not self.vtkWidget:
            self.loadVTKbackGround(widget)

        # Funktion zum Dialog-Aufruf und Modell-Import aufrufen
        self.importModel()

        # Nachricht in Statusleiste
        self.status.showMessage("Fdd-File eingelesen")
    #=======================================================================================

    # Fkt. - load
    #============
    def load(self, widget):
        '''
        Fkt.-Beschreibung:
        \t load lädt ein json-File und visualisiert dieses
        \n
        Input-Variablen:
        \t widget...Objekt vom Typ QWidget oder einer abgeleiteten Klasse
        '''
         # Überprüfen, ob schon ein vtk-Widget existiert (wenn nicht -> Widget erstellen)
        if not self.vtkWidget:
            self.loadVTKbackGround(widget)

        self.importModel()

        # Nachricht in Statusleiste
        self.status.showMessage("Freedyn-Modell geladen")
    #=======================================================================================

    # Fkt. - save
    #============
    def save(self):
        '''
        Fkt.-Beschreibung:
        \t save speichert das aktuell, geöffnete Modell als json-File
        '''
        # Freedyn-Modell fehlt -> Fehlernachricht
        #----------------------------------------
        if self.mbsModel is None:
            self.status.showMessage("Kein Modell zum Speichern geladen!")

        # Freedyn-Modell ist vorhanden
        #-----------------------------
        else:
            # Abspeichern der Dateiendung
            file_name, file_extension = os.path.splitext(self.file_path)

            # Wenn fdd-File eingelesen -> Endung auf .json ändern zum Speichern
            if file_extension == ".fdd":
                path = self.file_path.with_suffix(".json")

            # Wenn Endung schon .json -> keine Änderung notwendig
            elif file_extension == ".json":
                path = self.file_path
            
            # Aufruf der Speicherfkt. von mbsModel
            self.mbsModel.saveDatabase(path)

            # Nachricht in Statusleiste
            self.status.showMessage("Freedyn-Modell gespeichert")
    #=======================================================================================

    # Fkt. - importModel
    #===================
    def importModel(self):
        '''
        Fkt.-Beschreibung:
        \t importModel lädt die gewählte Datei und visualiesiert diese im vtk-Widget. Es wird
           dabei zwischen fdd-Files und json-Files unterschieden
        '''
       # Objekt vom Typ mbsModel anlegen
        self.mbsModel = mbsModel.mbsModel()

        # Aufrufen des Dialogs
        self.dialog = ofDialog.mbsDialog()
        self.dialog.exec()

        # Abspeichern des .fdd-Pfades
        self.file_path = self.dialog.getFilepath()

        # Abspeichern der Dateiendung
        file_name, file_extension = os.path.splitext(self.file_path)

        # Import eines fdd-Files bei Endung .fdd
        if file_extension == ".fdd":
            # .fdd-File einlesen und anzeigen
            self.mbsModel.importFddFile(self.file_path)
            self.mbsModel.showModel(self.renderer)
        
        # Import eines json-Files bei Endung .json
        elif file_extension == ".json":
            self.mbsModel.loadDatabase(self.file_path)
            self.mbsModel.showModel(self.renderer)

        # Fehlermeldung bei anderer Endung
        else:
            print("Wrong file type: " + file_extension)
            return False
