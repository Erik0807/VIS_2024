# Einlesen benötigte Bibliotheken
#================================
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QDialog, QHBoxLayout,
                               QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox)
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Slot
from pathlib import Path

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

    # Fkt. - getSavePath
    #===================
    def getSavePath(self):
        '''
        Fkt.-Beschreibung:
        \t getSavePath liefert den Pfad, an dem die Dictionaries abgespeichert werden sollen
        \n
        Output:
        \t savePath...Pfad zum Speicherort des Dictionaries
        '''
        # Name des Dictionaries auf Namen des geöffneten Dropdown-Widgets festlegen
        dicName = self.name + ".txt"

        # Je nach Dictionary -> anderer Speicherort
        #------------------------------------------
        if self.name == "controlDict" or "fvSchemes" or "fvSolution":
            savePath = Path(self.file_path) / "case/system" / Path(dicName)
            savePath.resolve()

        elif self.name == "thermophysicalProperties" or "turbulenceProperties":
            savePath = Path(self.file_path) / "case/constant" / Path(dicName)
            savePath.resolve()

        elif self.name == "p" or "U" or "T":
            savePath = Path(self.file_path) / "case/0" / Path(dicName)
            savePath.resolve()

        else:
            # Fehlermeldung + anlegen eines unknown-Ordners
            print("Unbekanntes Dictionary -> wird in Ordner unknown abgelegt")
            unknown = Path(self.file_path) / "case"
            unknown.mkdir(parents = True, exist_ok = True)
            
            # Setzen des Speicherpfads
            savePath = Path(self.file_path) / "case/unknown" / Path(dicName)
            savePath.resolve()

        return savePath
    #=======================================================================================

    # Fkt. - writeDic
    #================
    def writeDic(self):
        '''
        Fkt.-Beschreibung:
        \t writeDic schreibt das im Dropdown-Menü erstellte Dictionary als txt-File in den
        \t gewünschten Ordner
        '''
        # Anlegen des Dictionaries, je nach Name des Widgets -> Rausschreiben
        #--------------------------------------------------------------------
        if self.name == "controlDict":
            dic = self.generateControlDict()
            self.writeSimpleDic(dic)

        elif self.name == "fvSchemes":
            dic = self.generateFvSchemes()
            self.writeComplexDic(dic)
     

        
    #=======================================================================================

    # Fkt. - writeSimpleDic
    #======================
    def writeSimpleDic(self, dic):
        '''
        Fkt.-Beschreibung:
            writeSimpleDic erledigt das Öffnen und zeilenweise Schreiben von Dictionaries bei
            einfacher Dictionary-Struktur (keine Subdictionaries)
        \n
        Input:
            dic...Dictionary (ohne Subdictionaries)
        '''
        # Bestimmen des Speicherorts
        #---------------------------
        savePath = self.getSavePath()

        # Überschreiben / Erstellen eines txt-Files
        #------------------------------------------
        with open(savePath, "w") as file:
            # Anlegen einer Liste von Zeilen
            lines = []

            # Schreiben des Headers
            self.writeOFHeader(lines)

            for key in dic:
                # Schreiben der aktuellen Zeile
                line = f"{key}\t\t\t{dic[key]};\n\n"

                # Hinzufügen der Zeile zur Liste
                lines.append(line)

            # Schreiben aller Zeilen
            file.writelines(lines)
    #=======================================================================================

    # Fkt. - writeComplexDic
    #=======================
    def writeComplexDic(self, dic):
        '''
        Fkt.-Beschreibung:
            writeComplexDic erledigt das Öffnen und zeilenweise Schreiben von Dictionaries bei
            komplexer Dictionary-Struktur (Subdictionaries)
        \n
        Input:
            dic...Dictionary (mit Subdictionaries) 
        '''
        # Bestimmen des Speicherorts
        #---------------------------
        savePath = self.getSavePath()

        # Überschreiben / Erstellen eines txt-Files
        #------------------------------------------
        with open(savePath, "w") as file:
            # Anlegen einer Liste von Zeilen
            lines = []

            # Schreiben des Headers
            self.writeOFHeader(lines)

            for key in dic:
                for subkey in dic[key]:
                    # Schreiben der aktuellen Zeile
                    line = f"{key}\n{{\n\t{subkey}\t\t{dic[key].get(subkey)};\n}}\n\n"

                    # Hinzufügen der Zeile zur Liste
                    lines.append(line)

            # Schreiben aller Zeilen
            file.writelines(lines)
    #=======================================================================================

    # Fkt. - writeOFHeader
    #=====================
    def writeOFHeader(self, lines):
        '''
        Fkt.-Beschreibung
        \t writeOFHeader schreibt den Header eines Openfoam-Textfiles zeilenweise in eine Liste
        '''
        line = "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // \n"
        lines.append(line)

        line = "FoamFile \n"
        lines.append(line)

        line = "{ \n"
        lines.append(line)

        line = "\t version \t 2.0; \n"
        lines.append(line)

        line = "\t format \t ascii; \n"
        lines.append(line)

        line = "\t class \t\t dictionary; \n"
        lines.append(line)

        line = "\t object \t" + self.name + ";\n"
        lines.append(line)

        line = "} \n"
        lines.append(line)

        line = "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // \n\n"
        lines.append(line)
    #=======================================================================================

    # Fkt. - generateControlDict
    #===========================
    def generateControlDict(self):
        '''
        Fkt.-Beschreibung
        \t generateControlDict legt ein controlDict-Dictionary basierend auf dem Dropdown-Widget an
        '''
        # Anlegen eines Dictionaries
        dic = {
            self.label_app.text():                  self.dropdown_app.currentText(),
            self.label_startFrom.text():            self.dropdown_startFrom.currentText(),
            self.label_startTime.text():            self.input_startTime.text(),
            self.label_stopAt.text():               self.dropdown_stopAt.currentText(),
            self.label_endTime.text():              self.input_endTime.text(),
            self.label_deltaT.text():               self.input_deltaT.text(),
            self.label_writeControl.text():         self.dropdown_writeControl.currentText(),
            self.label_writeInterval.text():        self.input_writeInterval.text(),
            self.label_purgeWrite.text():           self.input_purgeWrite.text(),
            self.label_writeFormat.text():          self.dropdown_writeFormat.currentText(),
            self.label_writePrecision.text():       self.dropdown_writePrecision.currentText(),
            self.label_writeCompression.text():     self.dropdown_writeCompression.currentText(),
            self.label_timeFormat.text():           self.dropdown_timeFormat.currentText(),
            self.label_timePrecision.text():        self.dropdown_timePrecision.currentText(),
            self.label_runTimeModifiable.text():    self.dropdown_runTimeModifiable.currentText(),
        }

        # Rückgabe des Dictionaries
        return dic
    #=======================================================================================

    # Fkt. - generateFvSchemes
    #=========================
    def generateFvSchemes(self):
        '''
        Fkt.-Beschreibung
        \t generateFvSchemes legt ein fvSchemes-Dictionary basierend auf dem Dropdown-Widget an
        '''
        # Anlegen eines Dictionaries
        dic = {
            self.label_ddtSchemes.text():   {"default": self.dropdown_ddtSchemes.currentText()},
        }

        # Rückgabe des Dictionaries
        return dic