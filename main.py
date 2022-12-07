import sys
from PyQt5.QtWidgets import QApplication, QWidget
from welcomemenu import Ui_WelcomeMenu
from controller import *

def main():
    app = QApplication(sys.argv)
    _ = MainController()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()