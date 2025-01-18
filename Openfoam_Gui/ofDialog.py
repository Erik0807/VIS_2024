# Einlesen benötigte Bibliotheken
#================================
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QDialog, QHBoxLayout,
                               QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox)
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

        # Initialisieren eines Objektnamens
        self.name = ""

        # Fenster anlegen
        self.setLayout(QVBoxLayout())

        # Anlegen eines generischen Dropdown-Menüs
        self.dropdown = QComboBox()

        # Erzeugen eines Ok- und Close-Buttons nebeneinander
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.close_button = QPushButton("Close")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.close_button)
        self.layout().addLayout(button_layout)
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
    #=======================================================================================

    # Fkt. - writeDic
    #================
    def writeDic(self):
        '''
        Fkt.-Beschreibung:
        \t writeDic schreibt das im Dropdown-Menü erstellre Dictionary als txt-File in den
        \t gewünschten Ordner
        '''
        # Anlegen eines Dictionaries
        dic = self.generateDic()

        # Name des Dictionaries auf Namen des geöffneten Dropdown-Widgets festlegen
        dicName = self.name + ".txt"
        

        for key in dic:
            print(key, "\t", dic[key], ";")

        # Überschreiben / Erstellen eines txt-Files
        with open(dicName, "w") as file:
             for key in dic:
                 file.write(f"{key}\t{dic[key]};\n")
    #=======================================================================================

    # Fkt. - generateDic
    #===================
    def generateDic(self):
        '''
        Fkt.-Beschreibung
        \t generateDic legt ein Dictionary basierend auf dem Dropdown-Widget an
        '''
        # Anlegen eines Dictionaries
        dic = {
            "application":  self.dropdown.currentText()
        }

        return dic
        

