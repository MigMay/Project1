from PyQt5.QtWidgets import QApplication, QWidget

from welcomemenu import Ui_WelcomeMenu


class MainController:
    def __init__(self):
        self.welcome_menu = QWidget()
        self.setupUiForAllWindows()
        self.welcome_menu.show()

    def setupUiForAllWindows(self):
        ui = Ui_WelcomeMenu()
        ui.setupUi(self.welcome_menu)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec_())
