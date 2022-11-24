from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt


class VoteMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.candidate_window = PickCandidate()
        self.setUpWidgets()

    def setUpWidgets(self):
        """Set up widgets in window."""
        intro_label = QLabel("VOTE MENU")
        vote_button = QPushButton("vote")
        vote_button.clicked.connect(self.candidate_window.show)
        exit_button = QPushButton("exit")
        exit_button.clicked.connect(self.close)
        exit_button.clicked.connect(lambda: QMessageBox.information(self, "Results", f'John = {self.candidate_window.john_votes}, Jane = {self.candidate_window.jane_votes}, Total = {self.candidate_window.total_votes}'))
        main_layout = QVBoxLayout()
        main_layout.addWidget(intro_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(vote_button)
        main_layout.addWidget(exit_button)
        self.setLayout(main_layout)


class PickCandidate(QWidget):
    def __init__(self):
        super().__init__()
        self.john_votes = 0
        self.jane_votes = 0
        self.setUpWidgets()

    def setUpWidgets(self):
        """Set up widgets in window."""
        candidates_label = QLabel("CANDIDATES")
        john_button = QPushButton("John")
        john_button.clicked.connect(self.addOneVoteToJohns)
        jane_button = QPushButton("Jane")
        jane_button.clicked.connect(self.addOneVoteToJane)
        main_layout = QVBoxLayout()
        main_layout.addWidget(candidates_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(john_button)
        main_layout.addWidget(jane_button)
        self.setLayout(main_layout)

    def addOneVoteToJohns(self):
        self.john_votes += 1
        print(self.john_votes)
        self.close()

    def addOneVoteToJane(self):
        self.jane_votes += 1
        print(self.jane_votes)
        self.close()

    @property
    def total_votes(self):
        return self.john_votes + self.jane_votes



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = VoteMenu()
    menu.show()
    sys.exit(app.exec_())
