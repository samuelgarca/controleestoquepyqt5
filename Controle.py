from PyQt5 import uic,QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from datetime import date
import time

data = ""
dados = ""
idproduto = ""
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="samuelgarcia",
    database="cadastro_estoques"
)
banco2 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="samuelgarcia",
    database="sensor_temp"
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
        comando_SQL = "INSERT INTO estoque2 (descricao, quantidade, data, local) VALUES (%s, %s, %s, %s)"
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
    tela_freezer_1.close()
    tela_freezer_2.close()
    tela_freezer_3.close()
    ver_estoque.show()

def freezer_1():
    tela_freezer_1.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 1' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_1.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_1.tableWidget.setColumnCount(5)
    print(dados_lidos)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_freezer_1.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

            

def freezer_2():
    tela_freezer_2.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 2' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_2.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_2.tableWidget.setColumnCount(5)
    print(dados_lidos)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_freezer_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def freezer_3():
    print("freezer3")
    tela_freezer_3.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 3' "
    cursor.execute(comando_SQL, dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_3.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_3.tableWidget.setColumnCount(5)
    comando_SQL = "SELECT  FROM estoque WHERE local = 'Frezer 3' "
    print(dados_lidos)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_freezer_3.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))




def excluir_dados():
    linha = tela_saida.tableWidget.currentRow()
    coluna = tela_saida.tableWidget.currentColumn()
    veredit = tela_saida.comboBox.currentText()
    #print(linha,coluna)
    cursor = banco.cursor()
    #print(veredit)
    if veredit == "Freezer 1" and coluna==2:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 1'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        local = dados_lidos[linha][coluna]
        tela_editar_qt.show()
        tela_editar_qt.lineEdit.setText(str(local))
        idproduto = str(dados_lidos[linha][0])
        quantidade = cadastro.lineEdit.text()
        tela_editar_qt.label_6.setText(dados_lidos[linha][1])
        tela_editar_qt.label_7.setText(dados_lidos[linha][3])
        tela_editar_qt.label_9.setText(idproduto)
        tela_editar_qt.radioButton.setChecked(True)
        banco.commit()

    if veredit == "Freezer 2" and coluna==2:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 2'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        local = dados_lidos[linha][coluna]
        print(str(local))
        tela_editar_qt.show()
        tela_editar_qt.lineEdit.setText(str(local))
        print(dados_lidos)
        local = dados_lidos[linha]
        print(local)
        quantidade = cadastro.lineEdit.text()
        banco.commit()

    if veredit == "Freezer 3" and coluna==2:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 3'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        local = dados_lidos[linha][coluna]
        print(str(local))
        tela_editar_qt.show()
        tela_editar_qt.lineEdit.setText(str(local))
        print(dados_lidos)
        local = dados_lidos[linha]
        print(local)
        quantidade = cadastro.lineEdit.text()
        banco.commit()

def editar_qt():
        descricao = tela_editar_qt.label_6.text()
        novaquantidade = int(tela_editar_qt.lineEdit.text())
        veredit = tela_saida.comboBox.currentText()
        data = tela_editar_qt.label_7.text()
        idproduto = tela_editar_qt.label_9.text()
        #print (data)
        cursor = banco.cursor()
        if tela_editar_qt.radioButton.isChecked():
            print("Frezer 1 selecionado")
            local ="Frezer 1"
            comando_SQL ="""UPDATE estoque2 
                             SET descricao = %s, 
                             quantidade = %s, 
                             data = %s,
                             local = %s 
                             WHERE id = %s """
            #comando_SQL = "UPDATE estoque SET (descricao, quantidade, data, local) WHERE local VALUES (%s, %s, %s, %s, %s)"
            dados = (descricao, novaquantidade, data, local, idproduto)
            print(dados)
            cursor.execute(comando_SQL, dados)
            banco.commit()


        elif tela_editar_qt.radioButton_2.isChecked():
            print("Frezer 2 selecionado")
            local ="Frezer 2"
            comando_SQL ="""UPDATE estoque2 
                             SET descricao = %s, 
                             quantidade = %s, 
                             data = %s,
                             local = %s 
                             WHERE id = %s """
            #comando_SQL = "UPDATE estoque SET (descricao, quantidade, data, local) WHERE local VALUES (%s, %s, %s, %s, %s)"
            dados = (descricao, novaquantidade, data, local, idproduto)
            print(dados)
            cursor.execute(comando_SQL, dados)
            banco.commit()
        elif tela_editar_qt.radioButton_3.isChecked():
            print("Frezer 3 foi selecionado")
            local ="Frezer 3"
            comando_SQL ="""UPDATE estoque2 
                             SET descricao = %s, 
                             quantidade = %s, 
                             data = %s,
                             local = %s 
                             WHERE id = %s """
            #comando_SQL = "UPDATE estoque SET (descricao, quantidade, data, local) WHERE local VALUES (%s, %s, %s, %s, %s)"
            dados = (descricao, novaquantidade, data, local, idproduto)
            print(dados)
            cursor.execute(comando_SQL, dados)
            banco.commit()
        tela_editar_qt.close()
        
        





def tela_editar():
    tela_saida.show()
    veredit = tela_saida.comboBox.currentText()
    #print(veredit)
    #tela_saida.pushButton_5.clicked.connect(editar)
    if veredit == "Freezer 1":
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 1' "
        cursor.execute(comando_SQL,dados)
        dados_lidos = cursor.fetchall()
        tela_saida.tableWidget.setRowCount(len(dados_lidos))
        tela_saida.tableWidget.setColumnCount(5)
        #print(dados_lidos)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 5):
                tela_saida.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    if veredit == "Freezer 2":
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 2' "
        cursor.execute(comando_SQL,dados)
        dados_lidos = cursor.fetchall()
        tela_saida.tableWidget.setRowCount(len(dados_lidos))
        tela_saida.tableWidget.setColumnCount(4)
        linha = tela_saida.tableWidget.currentRow() 
        coluna = tela_saida.tableWidget.currentColumn() 
        print(str(dados_lidos[linha][coluna]))
        
        for i in range(0, len(dados_lidos)):
            for j in range(0, 5):
                tela_saida.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        
        linha = tela_saida.tableWidget.currentRow() 
        coluna = tela_saida.tableWidget.currentColumn() 
        test4 = tela_saida.tableWidget.cellWidget(linha, coluna)
        test6 = tela_saida.tableWidget.currentIndex()
        #print(str(dados_lidos[linha][coluna]))
        #print(test6)
    
    
    if veredit == "Freezer 3":
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 3' "
        cursor.execute(comando_SQL,dados)
        dados_lidos = cursor.fetchall()
        tela_saida.tableWidget.setRowCount(len(dados_lidos))
        tela_saida.tableWidget.setColumnCount(5)
        #print(dados_lidos)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 5):
                tela_saida.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



def monitor_():
    tela_monitor.show()
    cursor = banco2.cursor()
    comando_SQL = "SELECT wea_temp FROM temp ORDER BY wea_id DESC LIMIT 1"
    cursor.execute(comando_SQL,dados)
    dados_lidos = str(cursor.fetchall())
    print(dados_lidos)
    tela_monitor.label_3.setText(dados_lidos[2:6])





    



app=QtWidgets.QApplication([])
### Carregar janelas ###
cadastro=uic.loadUi("cadastro2.ui")
menu=uic.loadUi("menu.ui")
ver_estoque=uic.loadUi("telaview.ui")
tela_freezer_1=uic.loadUi("freezer_1.ui")
tela_freezer_2=uic.loadUi("freezer_2.ui")
tela_freezer_3=uic.loadUi("freezer_3.ui")
tela_saida=uic.loadUi("saida.ui")
tela_monitor=uic.loadUi("monitor.ui")
tela_editar_qt=uic.loadUi("editar.ui")

### Verifica qual botão é apertado ###
tela_freezer_1.pushButton_4.clicked.connect(tela_estoque_)
tela_freezer_2.pushButton_4.clicked.connect(tela_estoque_)
tela_freezer_3.pushButton_4.clicked.connect(tela_estoque_)
menu.pushButton_2.clicked.connect(tela_estoque_)
menu.pushButton.clicked.connect(tela_estoque)
menu.pushButton_3.clicked.connect(tela_editar)
menu.pushButton_4.clicked.connect(monitor_)
cadastro.pushButton.clicked.connect(funcao_princip)
cadastro.pushButton_2.clicked.connect(menu_)
ver_estoque.pushButton_4.clicked.connect(menu_)
ver_estoque.pushButton.clicked.connect(freezer_1)
ver_estoque.pushButton_2.clicked.connect(freezer_2)
ver_estoque.pushButton_3.clicked.connect(freezer_3)
tela_saida.pushButton_5.clicked.connect(tela_editar)
#tela_saida.pushButton_5.clicked.connect(excluir_dados)
tela_saida.pushButton_6.clicked.connect(excluir_dados)
tela_editar_qt.pushButton.clicked.connect(editar_qt)



#estoque.show()
menu.show()
app.exec_()


""" create table estoque3 (
id INT NOT NULL AUTO_INCREMENT,
codigo INT,
descricao TEXT,  
quantidade INTE(11),
local VARCHAR(20),
PRIMARY KEY (id)
);  """