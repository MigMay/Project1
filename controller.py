from PyQt5.QtWidgets import QApplication, QWidget

from welcomemenu import Ui_WelcomeMenu
from votemenu import Ui_VoteMenu
from votesubmitted import Ui_VoteSubmitted
from candidatedetails import Ui_viewdetails
from results import Ui_Results


class MainController:
    def __init__(self):
        self.welcome_menu = WelcomeMenu()
        self.candidate_menu = CandidateMenu()
        self.vote_submitted = VoteSubmitted()
        self.candidate_details = CandidateDetails()
        self.results = Results()
        self.set_up_signals_and_slots()
        self.welcome_menu.show()

    def set_up_signals_and_slots(self):
        self.welcome_menu.ui.pushButton_2.clicked.connect(self.welcome_menu.close)
        self.welcome_menu.ui.pushButton.clicked.connect(self.candidate_menu.show)
        self.welcome_menu.ui.pushButton.clicked.connect(self.welcome_menu.close)
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.vote_submitted.show)
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.candidate_menu.close)
        self.candidate_menu.ui.pushButton_5.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.pushButton_6.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.pushButton_8.clicked.connect(self.candidate_details.show)
        self.vote_submitted.ui.pushButton_3.clicked.connect(self.candidate_menu.show)
        self.vote_submitted.ui.pushButton_4.clicked.connect(self.results.show)

class WelcomeMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_WelcomeMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

    def setUpSignalsAndSlots(self):
        pass


class CandidateMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_VoteMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

    def setUpSignalsAndSlots(self):
        pass

class CandidateDetails(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_viewdetails()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

    def setUpSignalsAndSlots(self):
        pass


class VoteSubmitted(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_VoteSubmitted()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

    def setUpSignalsAndSlots(self):
        pass

class Results(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Results()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

    def setUpSignalsAndSlots(self):
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec_())
