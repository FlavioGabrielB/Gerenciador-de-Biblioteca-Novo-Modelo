from doctest import NORMALIZE_WHITESPACE
import sys
import sqlite3
from datetime import date
from beautiful_date import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel
from PyQt6 import QtCore, QtGui, QtWidgets
from gui.gui import *

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = Ui_MainWindow()
        self.menu.setupUi(self)
        
        self.lb = QLabel(self.menu.frame_20)
        self.lb.hide()
        self.lb_2 = QLabel(self.menu.frame_20)
        self.lb.hide()
        self.lb_3 = QLabel(self.menu.frame_20)
        self.lb.hide()

        self.menu.pushButton_28.hide()
        self.menu.pushButton_28.clicked.connect(self.ed_u)
        self.menu.pushButton_29.hide()
        self.menu.pushButton_29.clicked.connect(self.ed_l)
        self.menu.pushButton_30.hide()
        self.menu.pushButton_30.clicked.connect(self.ed_a)
        self.menu.pushButton_13.clicked.connect(self.excluir_a)
        self.menu.pushButton_15.clicked.connect(self.excluir_l)
        self.menu.pushButton_17.clicked.connect(self.excluir_u)
        self.menu.pushButton_12.clicked.connect(self.editar_a)
        self.menu.pushButton_14.clicked.connect(self.editar_l)
        self.menu.pushButton_16.clicked.connect(self.editar_u)
        self.menu.pushButton_26.clicked.connect(self.limpar_p1)
        self.menu.pushButton_27.clicked.connect(self.limpar_p2)
        self.menu.pushButton_25.hide()
        self.menu.pushButton_24.hide()
        self.menu.pushButton_6.clicked.connect(self.pesquisar_a)
        self.menu.pushButton_7.clicked.connect(self.pesquisar_l)
        self.menu.pushButton_8.clicked.connect(self.pesquisar_u)
        self.menu.pushButton_24.clicked.connect(self.se_aluno)
        self.menu.pushButton_23.hide()
        self.menu.pushButton_23.clicked.connect(self.se_livro)
        self.menu.pushButton_11.clicked.connect(self.enviar_p)
        self.menu.pushButton_22.clicked.connect(self.p_tabela)
        self.menu.pushButton.clicked.connect(self.limpar)
        self.menu.pushButton_2.clicked.connect(self.diminuir)
        self.menu.pushButton_18.clicked.connect(self.s_aluno)
        self.menu.pushButton_19.clicked.connect(self.s_livro)
        self.menu.pushButton_21.clicked.connect(self.a_tabela)
        self.menu.pushButton_20.clicked.connect(self.l_tabela)
        self.menu.pushButton_3.clicked.connect(self.ps3)
        self.menu.pushButton_4.clicked.connect(self.ps4)
        self.menu.pushButton_5.clicked.connect(self.ps5)
        self.menu.pushButton_9.clicked.connect(self.aluno)
        self.menu.pushButton_10.clicked.connect(self.livro)
        
        self.banco_aluno = '''CREATE TABLE IF NOT EXISTS aluno (id integer not null primary key autoincrement, nome_aluno text, ano_serie text, cpf text)'''

        self.banco = sqlite3.connect('db/banco_aluno.db')
        self.csr = self.banco.cursor()
        self.csr.execute(self.banco_aluno)
        self.banco.commit()
        self.banco.close()

        self.banco_livro = '''CREATE TABLE IF NOT EXISTS livro (id integer not null primary key autoincrement, livro text, ISBN text, categoria text)'''

        self.banco = sqlite3.connect('db/banco_livro.db')
        self.csr = self.banco.cursor()
        self.csr.execute(self.banco_livro)
        self.banco.commit()
        self.banco.close()

        self.banco_aluguel = '''CREATE TABLE IF NOT EXISTS aluguel (id integer not null primary key autoincrement, aluno text, livro text, dias integer, entragar text)'''

        self.banco = sqlite3.connect('db/banco_aluguel.db')
        self.csr = self.banco.cursor()
        self.csr.execute(self.banco_aluguel)
        self.banco.commit()
        self.banco.close()
    

        self.diminuir()    
        self.a_tabela()
        self.l_tabela()
        self.p_tabela()

    def editar_a(self):

        self.linha = self.menu.tableWidget.currentRow()
        self.banco = sqlite3.connect('db/banco_aluno.db')
        self.csr = self.banco.cursor()
        self.csr.execute("SELECT id FROM aluno")
        self.dados_lidos = self.csr.fetchall()
        self.valor_id = self.dados_lidos[self.linha][0]

        self.csr.execute("SELECT * FROM aluno WHERE id=" + str(self.valor_id))
        self.produto = self.csr.fetchall()
        #print(self.produto)
        self.banco.commit()
        self.banco.close()

        self.lb.setText(str(self.produto[0][0]))
        self.menu.lineEdit_4.setText(self.produto[0][1])
        self.menu.lineEdit_5.setText(self.produto[0][3])
        self.menu.comboBox.setItemText(0,self.produto[0][2])

        self.menu.stackedWidget.setCurrentWidget(self.menu.page_4)
        self.menu.tabWidget_2.setCurrentWidget(self.menu.tab_4)
        self.menu.pushButton_9.hide()
        self.menu.pushButton_30.show()

    def ed_a(self):
        self.id_a = self.lb.text()
        self.nome_aluno = self.menu.lineEdit_4.text()
        self.serie = self.menu.comboBox.currentText()
        self.cpf = self.menu.lineEdit_5.text()

        self.banco = sqlite3.connect('db/banco_aluno.db')
        self.csr = self.banco.cursor()
        self.d = '''UPDATE dados SET nome_aluno = {}, ano_serie = {}, nome_livro = {}, genero = {}, dias = {}, devolver = {}'''
        self.csr.execute(f'''UPDATE aluno SET nome_aluno = "{self.nome_aluno}", ano_serie = "{self.serie}", cpf = "{self.cpf}"  WHERE id = "{self.id_a}"''')
        self.banco.commit()
        self.banco.close()
        
        self.a_tabela()

        self.menu.stackedWidget.setCurrentWidget(self.menu.page_3)
        self.menu.tabWidget.setCurrentWidget(self.menu.tab)

        self.menu.lineEdit_4.setText("")
        self.menu.lineEdit_5.setText("")

        self.menu.pushButton_9.show()
        self.menu.pushButton_30.hide()

    def editar_l(self):
        self.linha = self.menu.tableWidget_3.currentRow()
        self.banco = sqlite3.connect('db/banco_livro.db')
        self.csr = self.banco.cursor()
        self.csr.execute("SELECT id FROM livro")
        self.dados_lidos = self.csr.fetchall()
        self.valor_id = self.dados_lidos[self.linha][0]

        self.csr.execute("SELECT * FROM livro WHERE id=" + str(self.valor_id))
        self.produto = self.csr.fetchall()
        #print(self.produto)
        self.banco.commit()
        self.banco.close()

        self.lb_2.setText(str(self.produto[0][0]))
        self.menu.lineEdit_6.setText(self.produto[0][1])
        self.menu.lineEdit_7.setText(self.produto[0][2])
        self.menu.comboBox_2.setItemText(0,self.produto[0][3])

        self.menu.stackedWidget.setCurrentWidget(self.menu.page_4)
        self.menu.tabWidget_2.setCurrentWidget(self.menu.tab_5)
        self.menu.pushButton_10.hide()
        self.menu.pushButton_29.show()

    def ed_l (self):
        self.id_l = self.lb_2.text()
        self.nome_livro = self.menu.lineEdit_6.text()
        self.categoria = self.menu.comboBox_2.currentText()
        self.isbn = self.menu.lineEdit_7.text()

        self.banco = sqlite3.connect('db/banco_livro.db')
        self.csr = self.banco.cursor()
        self.d = '''UPDATE dados SET nome_aluno = {}, ano_serie = {}, nome_livro = {}, genero = {}, dias = {}, devolver = {}'''
        self.csr.execute(f'''UPDATE livro SET livro = "{self.nome_livro}", ISBN = "{self.isbn}", categoria = "{self.categoria}"  WHERE id = "{self.id_l}"''')
        self.banco.commit()
        self.banco.close()

        self.l_tabela()
        self.menu.tabWidget.setCurrentWidget(self.menu.tab_3)
        self.menu.stackedWidget.setCurrentWidget(self.menu.page_3)

        self.menu.lineEdit_6.setText("")
        self.menu.lineEdit_7.setText("")

        self.menu.pushButton_10.show()
        self.menu.pushButton_29.hide()

    def editar_u(self):
        self.linha = self.menu.tableWidget_2.currentRow()
        self.banco = sqlite3.connect('db/banco_aluguel.db')
        self.csr = self.banco.cursor()
        self.csr.execute("SELECT id FROM aluguel")
        self.dados_lidos = self.csr.fetchall()
        self.valor_id = self.dados_lidos[self.linha][0]

        self.csr.execute("SELECT * FROM aluguel WHERE id=" + str(self.valor_id))
        self.produto = self.csr.fetchall()
        #print(self.produto)
        self.banco.commit()
        self.banco.close()

        self.lb_3.setText(str(self.produto[0][0]))
        self.menu.label_14.setText(self.produto[0][1])
        self.menu.label_15.setText(self.produto[0][2])
        self.menu.spinBox.setValue(self.produto[0][3])

        self.menu.stackedWidget.setCurrentWidget(self.menu.page_4)
        self.menu.tabWidget_2.setCurrentWidget(self.menu.tab_6)
        self.menu.pushButton_11.hide()
        self.menu.pushButton_28.show()
    
    def ed_u (self):
        self.id_3 = self.lb_3.text()
        self.alun = self.menu.label_14.text()
        self.liv = self.menu.label_15.text()
        self.dias = self.menu.spinBox.text()

        self.dh = date.today()
        self.di = int(self.dias)
        self.dia_amanha = BeautifulDate(self.dh.year,self.dh.month,self.dh.day)
        self.df = str(self.dia_amanha + self.di*days)
        self.dfff = self.df[8]+self.df[9]+self.df[7]+self.df[5]+self.df[6]+self.df[4]+self.df[0]+self.df[1]+self.df[2]+self.df[3]
        self.banco = sqlite3.connect('db/banco_aluguel.db')
        self.csr = self.banco.cursor()
        self.d = '''UPDATE dados SET nome_aluno = {}, ano_serie = {}, nome_livro = {}, genero = {}, dias = {}, devolver = {}'''
        self.csr.execute(f'''UPDATE aluguel SET aluno = "{self.alun}", livro = "{self.liv}", dias = "{self.dias}", entragar = "{self.dfff}" WHERE id = "{self.id_3}"''')
        self.banco.commit()
        self.banco.close()

        self.p_tabela()

        self.menu.stackedWidget.setCurrentWidget(self.menu.page_3)
        self.menu.tabWidget.setCurrentWidget(self.menu.tab_2)
        self.menu.pushButton_11.show()
        self.menu.pushButton_28.hide()



    def excluir_u(self):
        try:
            self.linha = self.menu.tableWidget_2.currentRow()
            self.menu.tableWidget.removeRow(self.linha)
            self.banco = sqlite3.connect('db/banco_aluguel.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT id FROM aluguel")
            self.dados_lidos = self.csr.fetchall()
            self.valor_id = self.dados_lidos[self.linha][0]
            #print(self.valor_id)
            self.csr.execute("DELETE FROM aluguel WHERE id=" + str(self.valor_id))
            self.banco.commit()
            self.banco.close()
            self.p_tabela()
        except:
            self.menu.label.setText("Campo não encontrado!")

    def excluir_l(self):
        try:
            self.linha = self.menu.tableWidget_3.currentRow()
            self.menu.tableWidget.removeRow(self.linha)
            self.banco = sqlite3.connect('db/banco_livro.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT id FROM livro")
            self.dados_lidos = self.csr.fetchall()
            self.valor_id = self.dados_lidos[self.linha][0]
            #print(self.valor_id)
            self.csr.execute("DELETE FROM livro WHERE id=" + str(self.valor_id))
            self.banco.commit()
            self.banco.close()
            self.l_tabela()
        except:
            self.menu.label.setText("Campo não encontrado!")

    def excluir_a(self):
        try:
            self.linha = self.menu.tableWidget.currentRow()
            self.menu.tableWidget.removeRow(self.linha)
            self.banco = sqlite3.connect('db/banco_aluno.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT id FROM aluno")
            self.dados_lidos = self.csr.fetchall()
            self.valor_id = self.dados_lidos[self.linha][0]
            #print(self.valor_id)
            self.csr.execute("DELETE FROM aluno WHERE id=" + str(self.valor_id))
            self.banco.commit()
            self.banco.close()
        except:
            self.menu.label.setText("Campo não encontrado!")
            

    def pesquisar_u(self):
        self.texto = self.menu.lineEdit_3.text()
        #print(self.texto)
        self.banco = sqlite3.connect('db/banco_aluguel.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute(f'SELECT aluno, livro, dias, entragar FROM aluguel WHERE aluno LIKE "%{self.texto}%" OR livro LIKE "%{self.texto}%" OR dias LIKE "%{self.texto}%" OR entragar LIKE "%{self.texto}%"')
        self.dados_lidos = self.csr.fetchall()
        self.menu.tableWidget_2.setRowCount(len(self.dados_lidos))
        self.menu.tableWidget_2.setColumnCount(4)
        #print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,4):
                self.menu.tableWidget_2.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))             
        self.banco.close()
    def ps3(self):
        self.menu.stackedWidget.setCurrentWidget(self.menu.page_3)
        self.a_tabela()
        self.l_tabela()
        self.p_tabela()

    def pesquisar_l(self):
        self.texto = self.menu.lineEdit_2.text()
        #print(self.texto)
        self.banco = sqlite3.connect('db/banco_livro.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute(f'SELECT livro, ISBN, categoria FROM livro WHERE livro LIKE "%{self.texto}%" OR ISBN LIKE "%{self.texto}%" OR categoria LIKE "%{self.texto}%"')
        self.dados_lidos = self.csr.fetchall()
        self.menu.tableWidget_3.setRowCount(len(self.dados_lidos))
        self.menu.tableWidget_3.setColumnCount(3)
        #print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,3):
                self.menu.tableWidget_3.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))             
        self.banco.close()

    def pesquisar_a(self):
        self.texto = self.menu.lineEdit.text()
        #print(self.texto)
        self.banco = sqlite3.connect('db/banco_aluno.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute(f'SELECT nome_aluno, cpf, ano_serie FROM aluno WHERE nome_aluno LIKE "%{self.texto}%" OR ano_serie LIKE "%{self.texto}%" OR cpf LIKE "%{self.texto}%"')
        self.dados_lidos = self.csr.fetchall()
        self.menu.tableWidget.setRowCount(len(self.dados_lidos))
        self.menu.tableWidget.setColumnCount(3)
        #print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,3):
                self.menu.tableWidget.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))             
        self.banco.close()



    def p_tabela(self):
        self.banco = sqlite3.connect('db/banco_aluguel.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute('SELECT aluno, livro, dias, entragar FROM aluguel')
        self.dados_lidos = self.csr.fetchall()
        self.menu.tableWidget_2.setRowCount(len(self.dados_lidos))
        self.menu.tableWidget_2.setColumnCount(4)
        #print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,4):
                self.menu.tableWidget_2.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))
        self.banco.close()    


    def enviar_p(self):
        self.alun = self.menu.label_14.text()
        self.liv = self.menu.label_15.text()
        self.nu = self.menu.spinBox.text()
        
        try:
            self.dh = date.today()
            self.di = int(self.nu)
            self.dia_amanha = BeautifulDate(self.dh.year,self.dh.month,self.dh.day)
            self.df = str(self.dia_amanha + self.di*days)
            self.dfff = self.df[8]+self.df[9]+self.df[7]+self.df[5]+self.df[6]+self.df[4]+self.df[0]+self.df[1]+self.df[2]+self.df[3]

            self.b = f'''INSERT INTO aluguel(aluno, livro, dias, entragar)
                        VALUES('{self.alun}', '{self.liv}', '{self.nu}', '{self.dfff}')'''

            self.banco = sqlite3.connect('db/banco_aluguel.db')
            self.csr = self.banco.cursor()
            self.csr.execute(self.b)
            self.banco.commit()
            self.banco.close()
        except:
            self.menu.label("Error")
        self.menu.label_14.setText("")
        self.menu.label_15.setText("")
        self.menu.spinBox.setValue(0)

    def limpar_p1(self):
        self.menu.label_14.setText("")
    
    def limpar_p2(self):
        self.menu.label_15.setText("")

    def s_aluno(self):
        self.menu.tabWidget.setCurrentWidget(self.menu.tab)
        self.menu.stackedWidget.setCurrentWidget(self.menu.page_3)
        self.menu.pushButton_24.show()

    def se_aluno(self):

        try:
            self.linha = self.menu.tableWidget.currentRow()
            self.banco = sqlite3.connect('db/banco_aluno.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT id FROM aluno")
            self.dados_lidos = self.csr.fetchall()
            self.valor_id = self.dados_lidos[self.linha][0] 
            self.csr.execute("SELECT nome_aluno FROM aluno WHERE id=" + str(self.valor_id))
            self.nom = self.csr.fetchall()
            self.nom1 = self.nom[0][0]
            self.menu.label_14.setText(self.nom1)
            self.menu.pushButton_24.hide()
            self.menu.tabWidget.setCurrentWidget(self.menu.tab_5)
            self.menu.stackedWidget.setCurrentWidget(self.menu.page_4)
        except:
            self.menu.label.setText("Selecione o nome do Aluno...")
 
    def s_livro(self):
       self.menu.tabWidget.setCurrentWidget(self.menu.tab_3)
       self.menu.stackedWidget.setCurrentWidget(self.menu.page_3)
       self.menu.pushButton_23.show()

    def se_livro(self):

        try:
            self.linha = self.menu.tableWidget.currentRow()
            self.banco = sqlite3.connect('db/banco_livro.db')
            self.csr = self.banco.cursor()
            self.csr.execute("SELECT id FROM livro")
            self.dados_lidos = self.csr.fetchall()
            self.valor_id = self.dados_lidos[self.linha][0] 
            self.csr.execute("SELECT livro FROM livro WHERE id=" + str(self.valor_id))
            self.nom = self.csr.fetchall()
            self.nom1 = self.nom[0][0]
            self.menu.label_15.setText(self.nom1)
            self.menu.tabWidget.setCurrentWidget(self.menu.tab_5)
            self.menu.stackedWidget.setCurrentWidget(self.menu.page_4)
            self.menu.pushButton_23.hide()
        
        except:
            self.menu.label.setText("Selecione o nome do Livro...")


    def abrirlivro(self):
        self.uil.show()

    def abriraluno(self):
        self.uia.show()

    def ps4(self):
        self.menu.stackedWidget.setCurrentWidget(self.menu.page_4)
    
    def ps5(self):
        self.menu.stackedWidget.setCurrentWidget(self.menu.page)


    def a_tabela(self):
        self.banco = sqlite3.connect('db/banco_aluno.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute('SELECT nome_aluno, cpf, ano_serie FROM aluno')
        self.dados_lidos = self.csr.fetchall()
        self.menu.tableWidget.setRowCount(len(self.dados_lidos))
        self.menu.tableWidget.setColumnCount(3)
        #print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,3):
                self.menu.tableWidget.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))
        self.banco.close()

    def l_tabela(self):
        self.banco = sqlite3.connect('db/banco_livro.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute('SELECT livro, ISBN, categoria FROM livro')
        self.dados_lidos = self.csr.fetchall()
        self.menu.tableWidget_3.setRowCount(len(self.dados_lidos))
        self.menu.tableWidget_3.setColumnCount(3)
        #print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,3):
                self.menu.tableWidget_3.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))
        self.banco.close()    


    def aluno(self):
        
        self.nome_aluno = self.menu.lineEdit_4.text()
        self.cpf = self.menu.lineEdit_5.text()
        self.serie = self.menu.comboBox.currentText()
        self.enviar_a = f'''INSERT INTO aluno(nome_aluno, ano_serie, cpf)
                    VALUES('{self.nome_aluno}', '{self.serie}', '{self.cpf}')'''
        
        try:
            self.cpf= int(self.cpf)
            if len(str(self.cpf)) == 11:
                    
                self.banco = sqlite3.connect('db/banco_aluno.db')
                self.csr = self.banco.cursor()
                self.csr.execute(self.enviar_a)
                self.banco.commit()
                self.banco.close()
                self.menu.label.setText("Cadastro realizado com sucesso!")
                self.menu.lineEdit_4.setText("")
                self.menu.lineEdit_5.setText("")

            else:
                self.menu.label.setText("CPF Incorreto!")
        except:
            self.menu.label.setText("CPF Incorreto!")

    def livro(self):
        self.nome_livro = self.menu.lineEdit_6.text()
        self.isbn = self.menu.lineEdit_7.text()
        self.categoria = self.menu.comboBox_2.currentText()
        self.enviar_l = f'''INSERT INTO livro(livro, ISBN, categoria)
                    VALUES('{self.nome_livro}', '{self.isbn}', '{self.categoria}')'''
        

        try:
            self.isbn= int(self.isbn)
            if len(str(self.isbn)) == 13:
                    
                self.banco = sqlite3.connect('db/banco_livro.db')
                self.csr = self.banco.cursor()
                self.csr.execute(self.enviar_l)
                self.banco.commit()
                self.banco.close()
                self.menu.label.setText("Cadastro realizado com sucesso!")
                self.menu.lineEdit_6.setText("")
                self.menu.lineEdit_7.setText("")

            else:
                self.menu.label.setText("ISBN Incorreto!")
        except:
            self.menu.label.setText("ISBN Incorreto!")


    def diminuir(self):
        self.ms = self.menu.frame.maximumSize()
        self.mis = self.menu.frame.minimumSize()
        self.win= self.mis.width()
        self.wim = self.ms.width()

        if self.win == 200:
            self.icon_ = QtGui.QIcon()
            self.icon_.addPixmap(QtGui.QPixmap("../../../../Downloads/angle-right-free-icon-font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.menu.pushButton_2.setIcon(self.icon_)
            self.menu.frame.setMinimumWidth(50)
            self.menu.frame.setMaximumWidth(50)
            self.menu.pushButton_3.setText("")
            self.menu.pushButton_4.setText("")
            self.menu.pushButton_5.setText("")
            
        else:
            self.icon_z = QtGui.QIcon()
            self.icon_z.addPixmap(QtGui.QPixmap("../../../../Downloads/angle-left-free-icon-font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.menu.pushButton_2.setIcon(self.icon_z)
            self.menu.frame.setMinimumWidth(200)
            self.menu.frame.setMaximumWidth(300)
            self.menu.pushButton_3.setText(" Gerenciar")
            self.menu.pushButton_4.setText(" Cadastrar")
            self.menu.pushButton_5.setText(" Sobre      ")


        
        
    def limpar(self):
        self.menu.label.setText('')
  


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = Menu()
    view.show()
    qt.exec()
