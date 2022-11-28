from PyQt5.QtWidgets import QApplication, QWidget

from welcomemenu import Ui_WelcomeMenu


class WelcomeMenuController(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_WelcomeMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()
        self.show()

    def setUpSignalsAndSlots(self):
        self.ui.pushButton_2.clicked.connect(self.close)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = WelcomeMenuController()
    sys.exit(app.exec_())
