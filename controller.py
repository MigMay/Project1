from PyQt5.QtWidgets import QApplication, QWidget

from welcomemenu import Ui_WelcomeMenu


class WelcomeMenuController(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_WelcomeMenu()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = WelcomeMenuController()
    sys.exit(app.exec_())
