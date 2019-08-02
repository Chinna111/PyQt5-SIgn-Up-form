# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1098, 844)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 270, 251, 251))
        self.label.setStyleSheet("background-image: url(:/newPrefix/User.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(410, 40, 611, 751))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 160, 421, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 250, 421, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 350, 421, 51))
        self.lineEdit_3.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 440, 421, 51))
        self.lineEdit_4.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(100, 530, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 630, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Create an account"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Retype Password"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Email"))
        self.radioButton.setText(_translate("Dialog", "I Agree with Terms and Conditions"))
        self.pushButton.setText(_translate("Dialog", "Sign Up"))


import resourcefile

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

