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
        self.dropdown_stopAt.addItems(["endTime"])
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
        self.label_deltaT = QLabel("deltaT")
        self.layout().insertWidget(10, self.label_deltaT)
        self.input_deltaT = QLineEdit()
        self.input_deltaT.setPlaceholderText("0.001")
        self.layout().insertWidget(11, self.input_deltaT)
        #-----------------------------------------------------------------------------------

        # writeControl
        #-------------
        self.label_writeControl = QLabel("writeControl")
        self.layout().insertWidget(12, self.label_writeControl)
        self.dropdown_writeControl = QComboBox()
        self.dropdown_writeControl.addItems(["timeStep"])
        self.layout().insertWidget(13, self.dropdown_writeControl)
        #-----------------------------------------------------------------------------------

        # writeInterval
        #--------------
        self.label_writeInterval = QLabel("writeInterval")
        self.layout().insertWidget(14, self.label_writeInterval)
        self.input_writeInterval = QLineEdit()
        self.input_writeInterval.setPlaceholderText("10")
        self.layout().insertWidget(15, self.input_writeInterval)
        #-----------------------------------------------------------------------------------

        # purgeWrite
        #-----------
        self.label_purgeWrite = QLabel("purgeWrite")
        self.layout().insertWidget(16, self.label_purgeWrite)
        self.input_purgeWrite = QLineEdit()
        self.input_purgeWrite.setPlaceholderText("0")
        self.layout().insertWidget(17, self.input_purgeWrite)
        #-----------------------------------------------------------------------------------

        # writeFormat
        #------------
        self.label_writeFormat = QLabel("writeFormat")
        self.layout().insertWidget(18, self.label_writeFormat)
        self.dropdown_writeFormat = QComboBox()
        self.dropdown_writeFormat.addItems(["ascii", "binary"])
        self.layout().insertWidget(19, self.dropdown_writeFormat)
        #-----------------------------------------------------------------------------------

        # writePrecision
        #---------------
        self.label_writePrecision = QLabel("writePrecision")
        self.layout().insertWidget(20, self.label_writePrecision)
        self.dropdown_writePrecision = QComboBox()
        self.dropdown_writePrecision.addItems(["2", "3", "4", "5", "6"])
        self.layout().insertWidget(21, self.dropdown_writePrecision)
        #-----------------------------------------------------------------------------------

        # writeCompression
        #-----------------
        self.label_writeCompression = QLabel("writeCompression")
        self.layout().insertWidget(22, self.label_writeCompression)
        self.dropdown_writeCompression = QComboBox()
        self.dropdown_writeCompression.addItems(["on", "off"])
        self.layout().insertWidget(23, self.dropdown_writeCompression)
        #-----------------------------------------------------------------------------------

        # timeFormat
        #-----------
        self.label_timeFormat = QLabel("timeFormat")
        self.layout().insertWidget(24, self.label_timeFormat)
        self.dropdown_timeFormat = QComboBox()
        self.dropdown_timeFormat.addItems(["general"])
        self.layout().insertWidget(25, self.dropdown_timeFormat)
        #-----------------------------------------------------------------------------------

        # timePrecision
        #--------------
        self.label_timePrecision = QLabel("timePrecision")
        self.layout().insertWidget(26, self.label_timePrecision)
        self.dropdown_timePrecision = QComboBox()
        self.dropdown_timePrecision.addItems(["2", "3", "4", "5", "6"])
        self.layout().insertWidget(27, self.dropdown_timePrecision)
        #-----------------------------------------------------------------------------------

        # runTimeModifiable
        #------------------
        self.label_runTimeModifiable = QLabel("runTimeModifiable")
        self.layout().insertWidget(28, self.label_runTimeModifiable)
        self.dropdown_runTimeModifiable = QComboBox()
        self.dropdown_runTimeModifiable.addItems(["true", "false"])
        self.layout().insertWidget(29, self.dropdown_runTimeModifiable)
        #-----------------------------------------------------------------------------------

        # Buttonverbindungen
        self.ok_button.clicked.connect(self.writeDic)
        self.close_button.clicked.connect(self.reject)

