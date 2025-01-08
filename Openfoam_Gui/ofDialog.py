# Einlesen benötigte Bibliotheken
#================================
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QDialog, QHBoxLayout,
                               QVBoxLayout, QLabel, QPushButton, QLineEdit)
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Slot


#===================================================================================
#                               KLASSE - ofDialog                                 #
#===================================================================================

class ofDialog(QDialog):
    # Konstruktor
    #============
    def __init__(self):
        # Mutterklassenkonstruktor
        super().__init__()

        # Initialisieren des Dateipfads
        self.file_path = ""

        # Fenster anlegen
        self.setWindowTitle("Import Freedyn-File")
        self.setLayout(QVBoxLayout())
        
        # Aufforderung an User
        self.label = QLabel("Bitte geben Sie den Pfad zu ihrem Freedyn-File ein:")
        self.layout().addWidget(self.label)

        # Eingabefeld
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Pfad/zu/meinem/File.xyz")
        self.layout().addWidget(self.input_field)

        # Erzeugen eines Ok- und Close-Buttons nebeneinander
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.close_button = QPushButton("Close")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.close_button)
        self.layout().addLayout(button_layout)

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.getInput)
        self.close_button.clicked.connect(self.reject)
    #=======================================================================================

    # Fkt. - getInput
    #================
    def getInput(self):
        '''
        Fkt.-Beschreibung:
        \t getInput gibt den Text aus dem Eingabefeld zurück
        '''
        self.file_path = self.input_field.text()
        self.accept()
    #=======================================================================================

    # Fkt. - getFilepath
    #===================
    def getFilepath(self):
        '''
        Fkt.-Beschreibung:
        \t getFilepath gibt den Dateipfad zum fdd-File zurück
        '''
        return self.file_path
