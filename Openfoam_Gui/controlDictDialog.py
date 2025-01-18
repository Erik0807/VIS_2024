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

class controlDictDialog(ofDialog):
    # Konstruktor
    #============
    def __init__(self):
        # Mutterklassenkonstruktor
        super().__init__()

        # Titel des Fensters
        self.setWindowTitle("controlDict")
        self.name = self.windowTitle()

        # Erzeugen der Dropdown-Menüs für die Dictionary-Einträge
        #========================================================
        # Application
        #------------
        self.label_app = QLabel("application")
        self.layout().insertWidget(0, self.label_app)
        self.dropdown_app = QComboBox()
        self.dropdown_app.addItems(["icoFoam", "simpleFoam", "pimpleFoam"])
        self.layout().insertWidget(1, self.dropdown_app)
        #-----------------------------------------------------------------------------------

        # startFrom
        #----------
        self.label_startFrom = QLabel("startFrom")
        self.layout().insertWidget(2, self.label_startFrom)
        self.dropdown_startFrom = QComboBox()
        self.dropdown_startFrom.addItems(["latestTime", "startTime"])
        self.layout().insertWidget(3, self.dropdown_startFrom)
        #-----------------------------------------------------------------------------------

        # startTime
        #----------
        self.label_startTime = QLabel("startTime")
        self.layout().insertWidget(4, self.label_startTime)
        self.input_startTime = QLineEdit()
        self.input_startTime.setPlaceholderText("0")
        self.layout().insertWidget(5, self.input_startTime)
        #-----------------------------------------------------------------------------------

        # stopAt
        #-------
        self.label_stopAt = QLabel("stopAt")
        self.layout().insertWidget(6, self.label_stopAt)
        self.dropdown_stopAt = QComboBox()
        self.dropdown_stopAt.addItems(["stopAt"])
        self.layout().insertWidget(7, self.dropdown_stopAt)
        #-----------------------------------------------------------------------------------

        # endTime
        #--------
        self.label_endTime = QLabel("endTime")
        self.layout().insertWidget(8, self.label_endTime)
        self.input_endTime = QLineEdit()
        self.input_endTime.setPlaceholderText("1000")
        self.layout().insertWidget(9, self.input_endTime)
        #-----------------------------------------------------------------------------------

        # deltaT
        #-------
        self.label_deltaT = QLabel("endTime")
        self.layout().insertWidget(10, self.label_deltaT)
        self.input_deltaT = QLineEdit()
        self.input_deltaT.setPlaceholderText("1000")
        self.layout().insertWidget(11, self.input_deltaT)

        #-----------------------------------------------------------------------------------

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)

