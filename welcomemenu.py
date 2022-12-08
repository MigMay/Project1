from PyQt5 import QtCore, QtGui, QtWidgets
from candidatemenu import *

class Ui_WelcomeMenu(object):
    def setupUi(self, WelcomeMenu):
        WelcomeMenu.setObjectName("WelcomeMenu")
        WelcomeMenu.resize(500, 600)
        self.pushButton = QtWidgets.QPushButton(WelcomeMenu)
        self.pushButton.setGeometry(QtCore.QRect(140, 370, 200, 50))
        WelcomeMenu.setMinimumSize(QtCore.QSize(500, 600))
        WelcomeMenu.setMaximumSize(QtCore.QSize(500, 600))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(WelcomeMenu)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 430, 200, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(WelcomeMenu)
        self.label.setGeometry(QtCore.QRect(40, 30, 391, 141))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(WelcomeMenu)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 391, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.retranslateUi(WelcomeMenu)
        QtCore.QMetaObject.connectSlotsByName(WelcomeMenu)
        # self.pushButton.clicked.connect(self.openCandidateMenu)
        # self.pushButton_2.clicked.connect(self.closeProgram)

    def retranslateUi(self, WelcomeMenu):
        _translate = QtCore.QCoreApplication.translate
        WelcomeMenu.setWindowTitle(_translate("WelcomeMenu", "Dialog"))
        self.pushButton.setText(_translate("WelcomeMenu", "Vote"))
        self.pushButton_2.setText(_translate("WelcomeMenu", "See Results"))
        self.label.setText(_translate("WelcomeMenu", "Vote For Your Next Student Body President"))
        self.label_3.setText(_translate("WelcomeMenu", "Universtity of Nebraska at Omaha has begun elections for their student body president for 2023/2024"))

    ''' 
    def openCandidateMenu(self):
        self.window2 = QtWidgets.QWidget()
        self.ui = Ui_VoteMenu()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def closeProgram(self):
        Ui_WelcomeMenu.close()
    '''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeMenu = QtWidgets.QDialog()
    ui = Ui_WelcomeMenu()
    ui.setupUi(WelcomeMenu)
    WelcomeMenu.show()
    sys.exit(app.exec_())
