# Importieren benötigter Bibliotheken
#====================================
import sys
from ofWindow import ofWindow
from ofWidget import ofWidget
from PySide6.QtWidgets import QApplication
from pathlib import Path

#================================================================================
#                                  MAIN-FILE                                    #
#================================================================================

if __name__ == "__OpenFoam__":

    # Qt-Anwendung
    #=============
    app = QApplication()

    # Widget anlegen
    widget = ofWidget()

    # Anlegen und zeigen des Hauptfensters
    window = ofWindow(widget)
    window.show()

    # Ausführen der Anwendung
    sys.exit(app.exec())



