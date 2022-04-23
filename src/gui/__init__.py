import logging
import datetime
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5 import QtGui
from src.core import Fish


def initLogging():
    logging.basicConfig(
        filename="C:/dergon-studios/pesquero/logs/gui-" + str(
            datetime.datetime.today().strftime('%Y%m%d%H%M%S')) + ".log",
        encoding="utf-8",
        level=logging.DEBUG
    )


class Window(QMainWindow):

    fish: Fish
    fish_key: str = "e"

    def __init__(self):
        super().__init__()
        self.initUI()
        self.fish = Fish()
        initLogging()

    def initUI(self):
        self.setGeometry(660, 340, 600, 400)
        self.setWindowTitle("DERGON Studios - Pesquero v2.0")
        self.setWindowIcon(QtGui.QIcon('assets/icon.png'))

        fishing_button = QPushButton("Start Fishing", self)
        fishing_button.setToolTip("Arranca a pescar")
        fishing_button.move(390, 360)
        fishing_button.clicked.connect(self.start)

        stop_fishing_button = QPushButton("Stop", self)
        stop_fishing_button.move(490, 360)
        stop_fishing_button.clicked.connect(self.stop)

        text_label = QLabel(self)
        text_label.move(10, 10)
        text_label.setText("Boton de pesca")

        textbox = QLineEdit(self)
        textbox.move(100, 10)
        textbox.setText(self.fish_key)
        textbox.textChanged[str].connect(self.change_fish_key)

        self.show()

    @pyqtSlot()
    def start(self):
        logging.debug("Start fishing")
        if self.fish_key and len(self.fish_key) == 1:
            self.fish.key = self.fish_key
            self.fish.start()
        else:
            logging.error("Invalid key. " + self.fish_key)
            QMessageBox.warning(self, "Weon...", "Selecciona una tecla para pescar")

    @pyqtSlot()
    def stop(self):
        self.fish.stop()

    def change_fish_key(self, text: str):
        logging.debug("Change key to '" + text + "'")
        self.fish_key = text.strip()

