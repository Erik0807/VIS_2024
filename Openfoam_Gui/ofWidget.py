from __future__ import annotations

from PySide6.QtCore import QDateTime, Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QWidget, QHeaderView, QHBoxLayout, QTableView,
                               QSizePolicy)
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis

#===================================================================================
#                               KLASSE - mbsWidget                                 #
#===================================================================================

class ofWidget(QWidget):
    # Konstruktor
    #============
    def __init__(self):
        # Mutterklassenkonstruktor
        #-------------------------
        QWidget.__init__(self)

        # Layout des Widgets
        #-------------------
        self.main_layout = QHBoxLayout()
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Layout auf das Widget anwenden
        #-------------------------------
        self.setLayout(self.main_layout)

        
