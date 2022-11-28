from PyQt5.QtWidgets import QApplication, QWidget

from welcomemenu import Ui_WelcomeMenu
from votemenu import Ui_VoteMenu


class MainController:
    pass


class WelcomeMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_WelcomeMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()
        self.show()

    def setUpSignalsAndSlots(self):
        self.ui.pushButton.clicked.connect(self.openCandidateMenu)
        self.ui.pushButton_2.clicked.connect(self.close)

    def openCandidateMenu(self):
        pass


class CandidateMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_VoteMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()
        self.show()

    def setUpSignalsAndSlots(self):
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = WelcomeMenu()
    sys.exit(app.exec_())
