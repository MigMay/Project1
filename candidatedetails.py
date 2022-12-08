from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewdetails(object):
    def setupUi(self, viewdetails):
        viewdetails.setObjectName("viewdetails")
        viewdetails.resize(708, 847)
        font = QtGui.QFont()
        font.setPointSize(12)
        viewdetails.setFont(font)
        self.label_23 = QtWidgets.QLabel(viewdetails)
        self.label_23.setGeometry(QtCore.QRect(180, 140, 300, 300))
        self.label_23.setMinimumSize(QtCore.QSize(300, 300))
        self.label_23.setMaximumSize(QtCore.QSize(300, 300))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("candidate1.jpg"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_26 = QtWidgets.QLabel(viewdetails)
        self.label_26.setGeometry(QtCore.QRect(230, 450, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(viewdetails)
        self.label_27.setGeometry(QtCore.QRect(70, 460, 561, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.retranslateUi(viewdetails)
        QtCore.QMetaObject.connectSlotsByName(viewdetails)

    def retranslateUi(self, viewdetails):
        _translate = QtCore.QCoreApplication.translate
        viewdetails.setWindowTitle(_translate("viewdetails", "Voting Machine"))
        self.label_26.setText(_translate("viewdetails", "Patricia A. Spiegel"))
        self.label_27.setText(_translate("viewdetails", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Risus feugiat in ante metus. Et netus et malesuada fames. Aliquam sem et tortor consequat. Placerat in egestas erat imperdiet. Platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim. Nam aliquam sem et tortor consequat id. Nibh venenatis cras sed felis eget velit. Scelerisque felis imperdiet proin fermentum leo vel orci porta non. Diam maecenas sed enim ut. Semper viverra nam libero justo."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewdetails = QtWidgets.QWidget()
    ui = Ui_viewdetails()
    ui.setupUi(viewdetails)
    viewdetails.show()
    sys.exit(app.exec_())