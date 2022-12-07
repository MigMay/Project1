from PyQt5.QtWidgets import QApplication, QWidget
import candidatemenu
from welcomemenu import Ui_WelcomeMenu
from candidatemenu import Ui_VoteMenu
from votesubmitted import Ui_VoteSubmitted
from candidatedetails import Ui_viewdetails
from results import Ui_Results
from helper import *

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
        #welcome menu buttons
        self.welcome_menu.ui.pushButton_2.clicked.connect(self.results.show)
        self.welcome_menu.ui.pushButton_2.clicked.connect(self.welcome_menu.close)
        self.welcome_menu.ui.pushButton_2.clicked.connect(lambda: self.results.updateResults(*readVotes()))
        self.welcome_menu.ui.pushButton.clicked.connect(lambda: self.candidate_menu.ui.pushButton_9.setEnabled(False))
        self.welcome_menu.ui.pushButton.clicked.connect(self.candidate_menu.show)
        self.welcome_menu.ui.pushButton.clicked.connect(self.welcome_menu.close)

        #candidate menu buttons
        #self.candidate_menu.ui.pushButton_9.clicked.connect(self.vote_submitted.show)
        # detail buttons
        self.candidate_menu.ui.pushButton_5.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.pushButton_6.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.pushButton_8.clicked.connect(self.candidate_details.show)
        self.candidate_menu.ui.radioButton.clicked.connect(self.candidate_menu.ui.pushButton_9.setEnabled)
        self.candidate_menu.ui.radioButton_2.clicked.connect(self.candidate_menu.ui.pushButton_9.setEnabled)
        self.candidate_menu.ui.radioButton_3.clicked.connect(self.candidate_menu.ui.pushButton_9.setEnabled)

        self.candidate_menu.ui.pushButton_5.clicked.connect(
            lambda: self.candidate_details.updateDetails('Jeanne Haden', 'candidate1.jpg' )
        )
        self.candidate_menu.ui.pushButton_6.clicked.connect(
            lambda: self.candidate_details.updateDetails('Edwin O. Ramirez', 'candidate3.jpg' )
        )
        self.candidate_menu.ui.pushButton_8.clicked.connect(
            lambda: self.candidate_details.updateDetails('Patricia A. Spiegel', 'candidate2.jpg' )
        )
        #submit vote button
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.candidate_menu.submitVote)
        self.candidate_menu.ui.pushButton_9.clicked.connect(lambda: self.candidate_menu.submitVote())
        self.candidate_menu.ui.pushButton_9.clicked.connect(lambda: self.candidate_menu.submitVote())
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.candidate_menu.close)
        self.candidate_menu.ui.pushButton_9.clicked.connect(self.welcome_menu.show)

        self.vote_submitted.ui.pushButton_3.clicked.connect(self.candidate_menu.show)
        #self.vote_submitted.ui.pushButton_3.clicked.connect(self.vote_submitted.close)
        #self.vote_submitted.ui.pushButton_4.clicked.connect(self.results.show)
        #self.vote_submitted.ui.pushButton_4.clicked.connect(self.vote_submitted.close)

        #results page buttons
        self.results.ui.pushButton_8.clicked.connect(self.welcome_menu.show)
        self.results.ui.pushButton_8.clicked.connect(self.results.close)
        self.results.ui.pushButton_9.clicked.connect(self.results.close)

class WelcomeMenu(QWidget):

    def __init__(self, *args, **kwargs):
        """
         Initialize Welcome Menu

         :param amount:
         """
        super().__init__(*args, **kwargs)
        self.ui = Ui_WelcomeMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

    def setUpSignalsAndSlots(self):
        """
        set up signals and slots for welcome menu
        :param amount:
        """
        pass


class CandidateMenu(QWidget):
    def __init__(self, *args, **kwargs):
        """
        initial candidate menu
        :param amount:
        """
        super().__init__(*args, **kwargs)
        self.ui = Ui_VoteMenu()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()

    def setUpSignalsAndSlots(self):
        """
        set up signals and slots for welcome menu
        :param amount:
        """
        pass

    def submitVote(self):
        CA_vote = 0
        CB_vote = 0
        CC_vote = 0

        if self.ui.radioButton.isChecked():
            CA_vote += 1
            self.ui.radioButton.setAutoExclusive(False)
            self.ui.radioButton.setChecked(False)
            self.ui.radioButton.setAutoExclusive(True)

        if self.ui.radioButton_2.isChecked():
            CB_vote += 1
            self.ui.radioButton_2.setAutoExclusive(False)
            self.ui.radioButton_2.setChecked(False)
            self.ui.radioButton_2.setAutoExclusive(True)


        if self.ui.radioButton_3.isChecked():
            CC_vote += 1
            self.ui.radioButton_3.setAutoExclusive(False)
            self.ui.radioButton_3.setChecked(False)
            self.ui.radioButton_3.setAutoExclusive(True)

        vote_list = [CA_vote, CB_vote, CC_vote]
        print(f'votes{CA_vote}{CB_vote}{CC_vote}')
        logVote(vote_list)
        #self.candidate_menu.close
        #self.vote_submitted.show

        return CA_vote, CB_vote, CC_vote


class CandidateDetails(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_viewdetails()
        self.ui.setupUi(self)
        self.setUpSignalsAndSlots()
        self.candidate_menu = CandidateMenu()

    def setUpSignalsAndSlots(self):
        pass

    def updateDetails(self, candidate_name, candidate_image):
        self.ui.label_26.setText(candidate_name)
        self.ui.label_23.setPixmap(QtGui.QPixmap(candidate_image))


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

    def updateResults(self, CA_vote, CB_vote, CC_vote):

        self.ui.label_18.setText(str(CA_vote))
        self.ui.label_19.setText(str(CB_vote))
        self.ui.label_20.setText(str(CC_vote))

        if CA_vote > CB_vote and CA_vote > CC_vote:
            winner_name = 'Jeanne Haden'
            self.ui.label_21.setPixmap(QtGui.QPixmap("candidate1.jpg"))
        if CB_vote > CA_vote and CB_vote > CC_vote:
            winner_name = 'Edwin O. Ramirez'
            self.ui.label_21.setPixmap(QtGui.QPixmap("candidate3.jpg"))
        if CC_vote > CA_vote and CC_vote > CB_vote:
            winner_name = 'Patricia A. Spiegel'
            self.ui.label_21.setPixmap(QtGui.QPixmap("candidate2.jpg"))
        self.ui.label_22.setText(winner_name)

    def clearVotes(self):
        with open('votingrecords.csv', 'w', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec_())
