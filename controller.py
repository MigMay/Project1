from PyQt5.QtWidgets import QApplication, QWidget

from welcomemenu import Ui_WelcomeMenu
from votemenu import Ui_VoteMenu


class MainController:
    def __init__(self):
        self.welcome_menu = WelcomeMenu()
        self.candidate_menu = CandidateMenu()
        self.set_up_signals_and_slots()
        self.welcome_menu.show()

    def set_up_signals_and_slots(self):
        self.welcome_menu.ui.pushButton.clicked.connect(self.candidate_menu.show)


class WelcomeMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_WelcomeMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

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
    controller = MainController()
    sys.exit(app.exec_())
