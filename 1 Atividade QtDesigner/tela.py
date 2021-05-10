# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Joanny\Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cadastro import Cadastro
from pessoa import Pessoa


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 80, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 110, 251, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 140, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 140, 251, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 170, 251, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 220, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 280, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 340, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 340, 111, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 370, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 340, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 380, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(350, 420, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 340, 191, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(430, 380, 191, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(430, 420, 191, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
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

# ----------------------------------------------------------
        self.cad = Cadastro()
        self.pushButton.clicked.connect(self.botaoCadastra)
        self.pushButton_2.clicked.connect(self.botaoBusca)

    def botaoCadastra(self):
        nome = self.lineEdit.text()
        cpf = self.lineEdit_2.text()
        endereco = self.lineEdit_3.text()
        nascimento = self.lineEdit_4.text()
        if not (nome == '' or cpf == '' or endereco == '' or nascimento == ''):
            p = Pessoa(nome, cpf, endereco, nascimento)
            if (self.cad.cadastra(p)):
                QMessageBox.information(None, 'POO II', 'O seu cadastro foi realizado!')
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,'POO II', 'O CPF informado já está cadastrado!')
        else:
            QMessageBox.information(None,'POO II', 'É obrigatório preencher todos os campos!')

    def botaoBusca(self):
        cpf = self.lineEdit_5.text()
        pessoa = self.cad.busca(cpf)
        if (pessoa != None):
            self.lineEdit_6.setText(pessoa.nome)
            self.lineEdit_7.setText(pessoa.endereco)
            self.lineEdit_8.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None, 'POO II', 'O CPF informado não foi encontrado!')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastrar Cliente"))
        self.label_2.setText(_translate("MainWindow", "Nome:"))
        self.label_3.setText(_translate("MainWindow", "CPF:"))
        self.label_4.setText(_translate("MainWindow", "Endereço:"))
        self.label_5.setText(_translate("MainWindow", "Nascimento:"))
        self.pushButton.setText(_translate("MainWindow", "Finalizar cadastro!"))
        self.label_6.setText(_translate("MainWindow", "Buscar Cliente"))
        self.label_7.setText(_translate("MainWindow", "Informe o CPF:"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar CPF"))
        self.label_8.setText(_translate("MainWindow", "Nome:"))
        self.label_9.setText(_translate("MainWindow", "Endereço:"))
        self.label_10.setText(_translate("MainWindow", "Nascimento:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
