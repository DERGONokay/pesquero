import sys
import os
from PyQt5.QtWidgets import QApplication
from gui import Window

if __name__ == '__main__':
    path = os.path.join("C:/dergon-studios", "pesquero", "logs")
    os.makedirs(path, exist_ok=True)
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
