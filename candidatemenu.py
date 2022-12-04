from PyQt5 import QtCore, QtGui, QtWidgets
from votesubmitted import *

'''
when radio button selected and submit button pushed, count vote for candidate and go to window 3
when details button pushed, open window to show details
when only submit button pushed, prompt user to select candidate
how to store votes to later output
open and write into a csv file and store votes into list


'''


class Ui_VoteMenu(object):
    def __init__(self):
        self.voteForCandidateA = None
        self.voteForCandidateB = None
        self.voteForCandidateC = None
        self.gridLayout = None

    def setupUi(self, VoteMenu):
        VoteMenu.setObjectName("VoteMenu")
        VoteMenu.resize(940, 888)
        VoteMenu.setMinimumSize(QtCore.QSize(940, 888))
        VoteMenu.setMaximumSize(QtCore.QSize(940, 888))
        font = QtGui.QFont()
        font.setPointSize(12)
        VoteMenu.setFont(font)
        self.label_15 = QtWidgets.QLabel(VoteMenu)
        self.label_15.setGeometry(QtCore.QRect(60, 0, 391, 141))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(VoteMenu)
        self.label_16.setGeometry(QtCore.QRect(60, 50, 391, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.pushButton_9 = QtWidgets.QPushButton(VoteMenu)
        self.pushButton_9.setGeometry(QtCore.QRect(640, 790, 200, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.frame_4 = QtWidgets.QFrame(VoteMenu)
        self.frame_4.setGeometry(QtCore.QRect(30, 190, 791, 559))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setMinimumSize(QtCore.QSize(150, 150))
        self.label_23.setMaximumSize(QtCore.QSize(150, 150))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("candidate1.jpg"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 0, 5, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 2, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setMinimumSize(QtCore.QSize(150, 150))
        self.label_24.setMaximumSize(QtCore.QSize(150, 150))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("candidate3.jpg"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 0, 5, 1)
        self.label_28 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 1, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_32 = QtWidgets.QLabel(self.frame_3)
        self.label_32.setMinimumSize(QtCore.QSize(150, 150))
        self.label_32.setMaximumSize(QtCore.QSize(150, 150))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("candidate2.jpg"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 0, 0, 5, 1)
        self.label_34 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 3, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 0, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_3.addWidget(self.radioButton, 1, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 2, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 3, 1, 1, 1)
        self.frame_4.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.pushButton_9.raise_()

        self.retranslateUi(VoteMenu)
        QtCore.QMetaObject.connectSlotsByName(VoteMenu)
        #self.radioButton.toggled.connect(lambda: self.submitVote())
        #self.radioButton_2.toggled.connect(lambda: self.submitVote())
        #self.radioButton_3.toggled.connect(lambda: self.submitVote())



    def retranslateUi(self, VoteMenu):
        _translate = QtCore.QCoreApplication.translate
        VoteMenu.setWindowTitle(_translate("VoteMenu", "Form"))
        self.label_15.setText(_translate("VoteMenu", "Let\'s start voting..."))
        self.label_16.setText(_translate("VoteMenu", "You are apart of the College of IS&T voting pool. Please select your vote below. "))
        self.pushButton_9.setText(_translate("VoteMenu", "Submit Vote"))
        # self.pushButton_9.clicked.connect(self.selectCandidate)
        self.pushButton_5.setText(_translate("VoteMenu", "Details"))
        # self.pushButton_9.clicked.connect(self.viewCandidateDetails)
        self.label_27.setText(_translate("VoteMenu", ""))
        self.label_26.setText(_translate("VoteMenu", "Jeane Haden"))
        self.pushButton_6.setText(_translate("VoteMenu", "Details"))
        # self.pushButton_9.clicked.connect(self.viewCandidateDetails)
        self.label_28.setText(_translate("VoteMenu", "Edwin O. Ramirez"))
        self.label_29.setText(_translate("VoteMenu", ""))
        self.label_34.setText(_translate("VoteMenu", ""))
        self.pushButton_8.setText(_translate("VoteMenu", "Details"))
        # self.pushButton_9.clicked.connect(self.viewCandidateDetails)
        self.label_33.setText(_translate("VoteMenu", "Patricia A. Spiegel"))
        self.label_35.setText(_translate("VoteMenu", "Vote"))

    def submitVote(self):
        CA_vote = 0
        CB_vote = 0
        CC_vote = 0

        if self.radioButton.isChecked():
            CA_vote += 1
        if self.radioButton_2.isChecked():
            CB_vote += 1
        if self.radioButton_3.isChecked():
            CC_vote += 1

        print(f'votes{CA_vote}{CB_vote}{CC_vote}')
        self.welcomemenu.show()

        return CA_vote, CB_vote, CC_vote

    def selectCandidate(self):

        print(f' CA {self.voteForCandidateA}')
        print(f' CA {self.voteForCandidateB}')
        print(f' CA {self.voteForCandidateC}')
        '''
        self.window3 = QtWidgets.QDialog()
        self.ui = Ui_VoteSubmitted()
        self.ui.setupUi(self.window3)
        self.window3.show()
        '''

    def viewCandidateDetails(self):
        self.window5 = QtWidgets.QWidget()
        self.ui2 = Ui_viewdetails()
        self.ui2.setupUi(self.window5)
        self.window5.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VoteMenu = QtWidgets.QWidget()
    ui = Ui_VoteMenu()
    ui.setupUi(VoteMenu)
    VoteMenu.show()
    sys.exit(app.exec_())