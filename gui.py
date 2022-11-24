from PyQt5.QtWidgets import QApplication, QWidget
from votemenu import Ui_VoteMenu


class VoteMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VoteMenu()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = VoteMenu()
    menu.show()
    sys.exit(app.exec_())
