from PyQt5 import uic,QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import time

data = ""
dados = ""
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="samuelgarcia",
    database="cadastro_estoques"
)


def funcao_princip():
    descricao = cadastro.comboBox.currentText()
    quantidade = cadastro.lineEdit.text()
    dia = cadastro.comboBox_2.currentText()
    mes = cadastro.comboBox_3.currentText()
    ano = cadastro.comboBox_4.currentText()
    dataconvert = [dia, mes, ano]
    data = '-'.join(map(str, dataconvert)) 
    local = ""

## Verifica qual campo foi selecionado ##
    if cadastro.radioButton.isChecked():
        print("Frezer 1 selecionado")
        local ="Frezer 1"
    elif cadastro.radioButton_2.isChecked():
        print("Frezer 2 selecionado")
        local ="Frezer 2"
    elif cadastro.radioButton_3.isChecked():
        print("Frezer 3 foi selecionado")
        local ="Frezer 3"


    if quantidade !="":
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO estoque (descricao, quantidade, data, local) VALUES (%s, %s, %s, %s)"
        dados = (str(descricao), quantidade, data, local)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        QMessageBox.about(cadastro, "Alerta", "Salvo")
        print("gravado", descricao, quantidade, data, local)
        time.sleep(1)
    else:
        QMessageBox.about(cadastro, "Alerta", "Insira a Quantidade")
    


        
    ## Limpa Campos ##
    cadastro.lineEdit.setText("")



        

def tela_estoque():
    menu.close()
    cadastro.show()

def menu_():
    cadastro.close()
    ver_estoque.close()
    menu.show()

def tela_estoque_():
    cadastro.close()
    menu.close()
    ver_estoque.show()

def freezer_1():
    tela_freezer_1.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque WHERE local = 'Frezer 1' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_1.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_1.tableWidget.setColumnCount(4)
    print(dados_lidos)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_freezer_1.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

            

def freezer_2():
    tela_freezer_2.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque WHERE local = 'Frezer 2' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_2.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_2.tableWidget.setColumnCount(4)
    print(dados_lidos)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_freezer_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def freezer_3():
    print("freezer3")
    tela_freezer_3.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque WHERE local = 'Frezer 3' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_3.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_3.tableWidget.setColumnCount(4)
    print(dados_lidos)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            tela_freezer_3.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


    


    



app=QtWidgets.QApplication([])
### Carregar janelas ###
cadastro=uic.loadUi("cadastro.ui")
menu=uic.loadUi("menu.ui")
ver_estoque=uic.loadUi("telaview.ui")
tela_freezer_1=uic.loadUi("freezer_1.ui")
tela_freezer_2=uic.loadUi("freezer_2.ui")
tela_freezer_3=uic.loadUi("freezer_3.ui")

### Verifica qual botão é apertado ###
menu.pushButton_2.clicked.connect(tela_estoque_)
menu.pushButton.clicked.connect(tela_estoque)
cadastro.pushButton.clicked.connect(funcao_princip)
cadastro.pushButton_2.clicked.connect(menu_)
ver_estoque.pushButton_4.clicked.connect(menu_)
ver_estoque.pushButton.clicked.connect(freezer_1)
ver_estoque.pushButton_2.clicked.connect(freezer_2)
ver_estoque.pushButton_3.clicked.connect(freezer_3)


#estoque.show()
menu.show()
app.exec()


""" create table estoque (id INT NOT NULL AUTO_INCREMENT,
codigo INT,
descricao VARCHAR(50),  
quantidade DOUBLE,
local VARCHAR(20),
PRIMARY KEY (id)
);  """