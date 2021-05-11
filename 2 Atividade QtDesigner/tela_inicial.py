# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Joanny\Desktop\tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(210, 80, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_main.setFont(font)
        self.label_main.setObjectName("label_main")
        self.button_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.button_cadastrar.setGeometry(QtCore.QRect(280, 200, 89, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cadastrar.sizePolicy().hasHeightForWidth())
        self.button_cadastrar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(13)
        self.button_cadastrar.setFont(font)
        self.button_cadastrar.setObjectName("button_cadastrar")
        self.button_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.button_buscar.setGeometry(QtCore.QRect(280, 280, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(13)
        self.button_buscar.setFont(font)
        self.button_buscar.setObjectName("button_buscar")
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
        self.label_main.setText(_translate("MainWindow", "Controle de Estoque"))
        self.button_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.button_buscar.setText(_translate("MainWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_inicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

