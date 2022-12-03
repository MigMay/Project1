from PyQt5.QtWidgets import QApplication, QWidget

import votemenu
from welcomemenu import Ui_WelcomeMenu
from votemenu import Ui_VoteMenu
from votesubmitted import Ui_VoteSubmitted
from candidatedetails import Ui_viewdetails
from results import Ui_Results


class MainController:
    def __init__(self):
        """
         Initialize Maincontroller

         :param amount: just maincontroller
         """
        self.welcome_menu = WelcomeMenu()
        self.candidate_menu = CandidateMenu()
        self.vote_submitted = VoteSubmitted()
        self.candidate_details = CandidateDetails()
        self.results = Results()
        self.set_up_signals_and_slots()
        self.welcome_menu.show()

    def set_up_signals_and_slots(self):
        """
         sets up signals and slots

         :param amount: self
         """
        self.welcome_menu.ui.pushButton_2.clicked.connect(self.welcome_menu.close)
        self.welcome_menu.ui.pushButton.clicked.connect(self.candidate_menu.show)
        self.welcome_menu.ui.pushButton.clicked.connect(self.welcome_menu.close)
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.vote_submitted.show)
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.candidate_menu.submitVote)
        self.candidate_menu.ui.pushButton_5.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.pushButton_6.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.pushButton_8.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.candidate_menu.close)
        self.vote_submitted.ui.pushButton_3.clicked.connect(self.candidate_menu.show)
        self.vote_submitted.ui.pushButton_3.clicked.connect(self.vote_submitted.close)
        self.vote_submitted.ui.pushButton_4.clicked.connect(self.results.show)
        self.vote_submitted.ui.pushButton_4.clicked.connect(self.vote_submitted.close)
        self.results.ui.pushButton_8.clicked.connect(self.welcome_menu.show)
        self.results.ui.pushButton_8.clicked.connect(self.results.close)

class WelcomeMenu(QWidget):
     """
     Initialize Maincontroller

     :param amount: just maincontroller
     :return: True if deposit was successful, otherwise false
     """
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

    def submitVote(self):
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


class Voter():
    def voter(self):
        self.pushButton_9.setText("submitted")
        self.voteForCandidateA = 0
        self.voteForCandidateB = 0
        self.voteForCandidateC = 0

        if self.radioButton.isChecked():
            self.voteForCandidateA += 1
        if self.radioButton_2.isChecked():
            self.voteForCandidateB += 1
        if self.radioButton_3.isChecked():
            self.voteForCandidateC += 1


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec_())
