import sys

from PyQt5.QtWidgets import QApplication, QWidget

from welcomemenu import Ui_WelcomeMenu


if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcomemenu = QWidget()
    ui_welcomemenu = Ui_WelcomeMenu()
    ui_welcomemenu.setupUi(welcomemenu)
    welcomemenu.show()
    sys.exit(app.exec_())
