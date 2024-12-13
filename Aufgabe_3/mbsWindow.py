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
import mbsModel as mbsModel
import mbsObject as mbsObject
import mbsDialog as mbsDialog

#===================================================================================
#                               KLASSE - mbsWindow                                 #
#===================================================================================

class mbsWindow(QMainWindow):
    # Konstruktor
    #============
    def __init__(self, widget):
        # Mutterklassenkonstruktor
        #-------------------------
        QMainWindow.__init__(self)

        # Initialisieren eines mbsModells
        self.mbsModel = None

        # Fenstertitel / zentrales Widget definieren
        #-------------------------------------------
        self.setWindowTitle("pyFreedyn")
        self.setCentralWidget(widget)

        # Initialisiere Instanzvariable für das VTK-Widget
        self.vtkWidget = None
    
        # File-Menü anlegen
        #------------------
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Load-Aktion definieren
        #-----------------------
        load_action = QAction("Load", self)
        load_action.triggered.connect(lambda: self.load(widget))

        # Speicher-Aktion definieren
        #--------------------------
        save_action = QAction("Save", self)
        save_action.triggered.connect(lambda: self.save())

        # Import-Aktion definieren (Achtung: lambda für callable Aktion, sonst wird
        # diese sofort ausgeführt)
        #-------------------------
        importFdd_action = QAction("importFdd", self)
        importFdd_action.triggered.connect(lambda: self.importFdd(widget))

        # Exit-Aktion definieren
        #-----------------------
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        # Aktionen zu File-Menü hinzufügen
        #---------------------------------
        self.file_menu.addAction(load_action)
        self.file_menu.addAction(save_action)
        self.file_menu.addAction(importFdd_action)
        self.file_menu.addAction(exit_action)

        # Statusleiste
        #-------------
        self.status = self.statusBar()
        self.status.showMessage("Freedyn startklar")

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
            # Speicherpfad bestimmen (am selben Ort wie Pfadeingabe, nur mit .json)
            fdd_path = Path(sys.argv[1])
            path = fdd_path.with_suffix(".json")
            
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
        self.dialog = mbsDialog.mbsDialog()
        self.dialog.exec()

        # Abspeichern des .fdd-Pfades
        file_path = self.dialog.getFilepath()

        # Abspeichern der Dateiendung
        file_name, file_extension = os.path.splitext(file_path)

        # Import eines fdd-Files bei Endung .fdd
        if file_extension == ".fdd":
            # .fdd-File einlesen und anzeigen
            self.mbsModel.importFddFile(file_path)
            self.mbsModel.showModel(self.renderer)
        
        # Import eines json-Files bei Endung .json
        elif file_extension == ".json":
            self.mbsModel.loadDatabase(file_path)
            self.mbsModel.showModel(self.renderer)

        # Fehlermeldung bei anderer Endung
        else:
            print("Wrong file type: " + file_extension)
            return False
