from PyQt5 import QtCore, QtGui, QtWidgets
from results import *
from candidatemenu import *

'''
start another vote, open candidate selection window
show results pushed, open results window and take data with flow

remove this gui file entirely and modify and use welcome menu file
'''
class Ui_VoteSubmitted(object):
    def setupUi(self, VoteSubmitted):
        VoteSubmitted.setObjectName("VoteSubmitted")
        VoteSubmitted.resize(497, 399)
        VoteSubmitted.setMinimumSize(QtCore.QSize(497, 399))
        VoteSubmitted.setMaximumSize(QtCore.QSize(497, 399))
        self.label_13 = QtWidgets.QLabel(VoteSubmitted)
        self.label_13.setGeometry(QtCore.QRect(40, 50, 391, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(VoteSubmitted)
        self.label_14.setGeometry(QtCore.QRect(40, 0, 391, 141))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_14.setFont(font)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(VoteSubmitted)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 240, 200, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(VoteSubmitted)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 300, 200, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(VoteSubmitted)
        QtCore.QMetaObject.connectSlotsByName(VoteSubmitted)

        #self.pushButton_3.clicked.connect(self.voteAgain)
        #self.pushButton_4.clicked.connect(self.seeResults)

    def retranslateUi(self, VoteSubmitted):
        _translate = QtCore.QCoreApplication.translate
        VoteSubmitted.setWindowTitle(_translate("VoteSubmitted", "Dialog"))
        self.label_13.setText(_translate("VoteSubmitted", "Voter ID voted for Candidate"))
        self.label_14.setText(_translate("VoteSubmitted", "Your vote was submitted!"))
        self.pushButton_3.setText(_translate("VoteSubmitted", "Start Another Vote"))
        self.pushButton_4.setText(_translate("VoteSubmitted", "See Results"))

    def seeResults(self):
        # open next window
        self.window4 = QtWidgets.QDialog()
        self.ui = Ui_Results()
        self.ui.setupUi(self.window4)
        self.window4.show()

    def voteAgain(self):
        self.window2 = QtWidgets.QWidget()
        self.ui = Ui_VoteMenu()
        self.ui.setupUi(self.window2)
        self.window2.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VoteSubmitted = QtWidgets.QDialog()
    ui = Ui_VoteSubmitted()
    ui.setupUi(VoteSubmitted)
    VoteSubmitted.show()
    sys.exit(app.exec_())