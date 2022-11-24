from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class VoteMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpWidgets()

    def setUpWidgets(self):
        """Set up widgets in window."""
        intro_label = QLabel("VOTE MENU")
        vote_button = QPushButton("vote")
        exit_button = QPushButton("exit")
        exit_button.clicked.connect(self.close)
        main_layout = QVBoxLayout()
        main_layout.addWidget(intro_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(vote_button)
        main_layout.addWidget(exit_button)
        self.setLayout(main_layout)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = VoteMenu()
    menu.show()
    sys.exit(app.exec_())
