# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Joanny\Desktop\tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_cadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 130, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 130, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 190, 251, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 240, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 240, 251, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 300, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 300, 251, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 380, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastrar Cliente"))
        self.label_2.setText(_translate("MainWindow", "Nome:"))
        self.label_3.setText(_translate("MainWindow", "CPF:"))
        self.label_4.setText(_translate("MainWindow", "Endereço:"))
        self.label_5.setText(_translate("MainWindow", "Nascimento:"))
        self.pushButton.setText(_translate("MainWindow", "Finalizar cadastro!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

