import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from tela_inicial import Tela_inicial
from tela_cadastro import Tela_cadastro
from tela_busca import Tela_busca
from pessoa import Pessoa
from cadastro import Cadastro


class Ui_Main(QtWidgets.QWidget):
    def setupUI(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_busca()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUI(self)

        self.cad = Cadastro()
        self.tela_inicial.button_cadastrar.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.button_buscar.clicked.connect(self.abrirTelaBuscar)

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_busca.button_buscar.clicked.connect(self.botaoBusca)

    def botaoCadastra(self):
        nome = self.tela_cadastro.lineEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        endereco = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()
        if not (nome == '' or cpf == '' or endereco == '' or nascimento == ''):
            p = Pessoa(nome, cpf, endereco, nascimento)
            if (self.cad.cadastra(p)):
                QMessageBox.information(None, 'POO II', 'O seu cadastro foi realizado!')
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, 'POO II', 'O CPF informado já está cadastrado!')
        else:
            QMessageBox.information(None, 'POO II', 'É obrigatório preencher todos os campos!')
        self.QtStack.setCurrentIndex(0)

    def botaoBusca(self):
        cpf = self.tela_busca.line_cpf_busca.text()
        pessoa = self.cad.busca(cpf)
        if (pessoa != None):
            self.tela_busca.line_result_nome.setText(pessoa.nome)
            self.tela_busca.line_result_nome_3.setText(pessoa.endereco)
            self.tela_busca.line_result_nome_2.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None, 'POO II', 'O CPF informado não foi encontrado!')

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBuscar(self):
        self.QtStack.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
