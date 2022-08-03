from PyQt5 import uic,QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from datetime import date
import time
import os

data = ""
dados = ""
idproduto = ""
banco = mysql.connector.connect(
    host="192.168.1.50",
    user="root2",
    passwd="abacate3114481",
    database="cadastro_estoques"
)

banco2 = mysql.connector.connect(
    host="192.168.1.50",
    user="root2",
    passwd="abacate3114481",
    database="Sensor_temp"
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
    elif cadastro.radioButton_4.isChecked():
        print("Frezer 4 foi selecionado")
        local ="Frezer 4"


    if quantidade !="" and local !="":
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO estoque2 (descricao, quantidade, data, local) VALUES (%s, %s, %s, %s)"
        dados = (str(descricao), quantidade, data, local)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        #cursor.clsoe()
        QMessageBox.about(cadastro, "Alerta", "Salvo")
        print("gravado", descricao, quantidade, data, local)
        time.sleep(1)
    else:
        QMessageBox.about(cadastro, "Alerta", "Insira a quantidade e o local de armazenamento")
    


        
    ## Limpa Campos ##
    cadastro.lineEdit.setText("")

def incrementa_10():
    print("ola")
    quantidade = cadastro.lineEdit.text()
    if quantidade == "":
        quantidade = 0
        nova_qt = quantidade+10
        nova_qt = str(nova_qt)
        cadastro.lineEdit.setText(nova_qt)
        print(nova_qt)
    else:
        nova_qt = int(quantidade)+10
        cadastro.lineEdit.setText(str(nova_qt))
        print(nova_qt)
        
def incrementa_1():
    quantidade = cadastro.lineEdit.text()
    if quantidade == "":
        quantidade = 0
        nova_qt = quantidade+1
        nova_qt = str(nova_qt)
        cadastro.lineEdit.setText(nova_qt)
        print(nova_qt)
    else:
        nova_qt = int(quantidade)+1
        cadastro.lineEdit.setText(str(nova_qt))
        print(nova_qt)

def decrementa_10():
    quantidade = cadastro.lineEdit.text()
    nova_qt = int(quantidade)
    if nova_qt >=10:   
        if quantidade == "":
                quantidade = 0
                nova_qt = quantidade-10
                nova_qt = str(nova_qt)
                cadastro.lineEdit.setText(nova_qt)
                print(nova_qt)
        else:
                nova_qt = int(quantidade)-10
                cadastro.lineEdit.setText(str(nova_qt))
                print(nova_qt)
    else:
        print("Voce atingiu o número minimo")

def decrementa_1():
    quantidade = cadastro.lineEdit.text()
    nova_qt = int(quantidade)
    if nova_qt >=1:   
        if quantidade == "":
                quantidade = 0
                nova_qt = quantidade-1
                nova_qt = str(nova_qt)
                cadastro.lineEdit.setText(nova_qt)
                print(nova_qt)
        else:
                nova_qt = int(quantidade)-1
                cadastro.lineEdit.setText(str(nova_qt))
                print(nova_qt)
    else:
        print("Voce atingiu o número minimo")

        
def incrementa_10_saida():
    quantidade = tela_editar_qt.lineEdit.text()
    if quantidade == "":
        quantidade = 0
        nova_qt = quantidade+10
        nova_qt = str(nova_qt)
        tela_editar_qt.lineEdit.setText(nova_qt)
        print(nova_qt)
    else:
        nova_qt = int(quantidade)+10
        tela_editar_qt.lineEdit.setText(str(nova_qt))
        print(nova_qt)
        
def incrementa_1_saida():
    quantidade = tela_editar_qt.lineEdit.text()
    if quantidade == "":
        quantidade = 0
        nova_qt = quantidade+1
        nova_qt = str(nova_qt)
        tela_editar_qt.lineEdit.setText(nova_qt)
        print(nova_qt)
    else:
        nova_qt = int(quantidade)+1
        tela_editar_qt.lineEdit.setText(str(nova_qt))
        print(nova_qt)

def decrementa_10_saida():
    quantidade = tela_editar_qt.lineEdit.text()
    nova_qt = int(quantidade)
    if nova_qt >=10:   
        if quantidade == "":
                quantidade = 0
                nova_qt = quantidade-10
                nova_qt = str(nova_qt)
                tela_editar_qt.lineEdit.setText(nova_qt)
                print(nova_qt)
        else:
                nova_qt = int(quantidade)-10
                tela_editar_qt.lineEdit.setText(str(nova_qt))
                print(nova_qt)
    else:
        print("Voce atingiu o número minimo")

def decrementa_1_saida():
    quantidade = tela_editar_qt.lineEdit.text()
    nova_qt = int(quantidade)
    if nova_qt >=1:   
        if quantidade == "":
                quantidade = 0
                nova_qt = quantidade-1
                nova_qt = str(nova_qt)
                tela_editar_qt.lineEdit.setText(nova_qt)
                print(nova_qt)
        else:
                nova_qt = int(quantidade)-1
                tela_editar_qt.lineEdit.setText(str(nova_qt))
                print(nova_qt)
    else:
        print("Voce atingiu o número minimo")
    

def tela_estoque():
    menu.close()
    cadastro.show()

def menu_():
    cadastro.close()
    ver_estoque.close()
    tela_saida.close()
    menu.show()

def tela_estoque_():
    cadastro.close()
    menu.close()
    tela_freezer_1.close()
    tela_freezer_2.close()
    tela_freezer_3.close()
    tela_freezer_4.close()
    ver_estoque.show()

def freezer_1():
    #banco.close()
    tela_freezer_1.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 1' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_1.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_1.tableWidget.setColumnCount(5)
    tela_freezer_1.tableWidget.setColumnWidth(0,50)
    tela_freezer_1.tableWidget.setColumnWidth(1,350)
    tela_freezer_1.tableWidget.setColumnWidth(2,75)
    tela_freezer_1.tableWidget.setColumnWidth(3,120)
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
    tela_freezer_2.tableWidget.setColumnWidth(0,50)
    tela_freezer_2.tableWidget.setColumnWidth(1,350)
    tela_freezer_2.tableWidget.setColumnWidth(2,75)
    tela_freezer_2.tableWidget.setColumnWidth(3,120)
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
    tela_freezer_3.tableWidget.setColumnWidth(0,50)
    tela_freezer_3.tableWidget.setColumnWidth(1,350)
    tela_freezer_3.tableWidget.setColumnWidth(2,75)
    tela_freezer_3.tableWidget.setColumnWidth(3,120)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_freezer_3.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def freezer_4():
    tela_freezer_4.show()
    cursor = banco.cursor()
    #comando_SQL = "SELECT * FROM estoque"
    comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 4' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_4.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_4.tableWidget.setColumnCount(5)
    tela_freezer_4.tableWidget.setColumnWidth(0,50)
    tela_freezer_4.tableWidget.setColumnWidth(1,350)
    tela_freezer_4.tableWidget.setColumnWidth(2,75)
    tela_freezer_4.tableWidget.setColumnWidth(3,120)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_freezer_4.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))




def alterar_dados():
    linha = tela_saida.tableWidget.currentRow()
    coluna = tela_saida.tableWidget.currentColumn()
    veredit = tela_saida.comboBox.currentText()

    #print(linha,coluna)
    cursor = banco.cursor()
    if veredit == "Freezer 1" and coluna==2:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 1'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        local = dados_lidos[linha][coluna]
        tela_editar_qt.show()
        print(dados_lidos)
        print(local)
        print(linha,coluna)
        tela_editar_qt.lineEdit.setText(str(local))
        tela_editar_qt.label_10.setText(str(local))
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
        tela_editar_qt.show()
        print(dados_lidos)
        print(local)
        print(linha,coluna)
        tela_editar_qt.lineEdit.setText(str(local))
        tela_editar_qt.label_10.setText(str(local))
        idproduto = str(dados_lidos[linha][0])
        quantidade = cadastro.lineEdit.text()
        tela_editar_qt.label_6.setText(dados_lidos[linha][1])
        tela_editar_qt.label_7.setText(dados_lidos[linha][3])
        tela_editar_qt.label_9.setText(idproduto)
        tela_editar_qt.radioButton_2.setChecked(True)
        banco.commit()

    if veredit == "Freezer 3" and coluna==2:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 3'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        local = dados_lidos[linha][coluna]
        tela_editar_qt.show()
        print(dados_lidos)
        print(local)
        print(linha,coluna)
        tela_editar_qt.lineEdit.setText(str(local))
        tela_editar_qt.label_10.setText(str(local))
        idproduto = str(dados_lidos[linha][0])
        quantidade = cadastro.lineEdit.text()
        tela_editar_qt.label_6.setText(dados_lidos[linha][1])
        tela_editar_qt.label_7.setText(dados_lidos[linha][3])
        tela_editar_qt.label_9.setText(idproduto)
        tela_editar_qt.radioButton_3.setChecked(True)
        banco.commit()
        
    if veredit == "Freezer 4" and coluna==2:
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 4'"
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        local = dados_lidos[linha][coluna]
        tela_editar_qt.show()
        print(dados_lidos)
        print(local)
        print(linha,coluna)
        tela_editar_qt.lineEdit.setText(str(local))
        tela_editar_qt.label_10.setText(str(local))
        idproduto = str(dados_lidos[linha][0])
        quantidade = cadastro.lineEdit.text()
        tela_editar_qt.label_6.setText(dados_lidos[linha][1])
        tela_editar_qt.label_7.setText(dados_lidos[linha][3])
        tela_editar_qt.label_9.setText(idproduto)
        tela_editar_qt.radioButton_4.setChecked(True)
        banco.commit()

def alterar_dados_2():
    quantidade = procurar_produto.label_2.text()
    local = procurar_produto.label_3.text()
    produto = procurar_produto.comboBox.currentText()
    print(produto,quantidade,local)
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM estoque2 WHERE descricao =%s" 
    #cursor.execute(comando_SQL, dados)
    cursor.execute(comando_SQL, [produto])
    dados_lidos = cursor.fetchall()
    print(dados_lidos)

def editar_qt():
        descricao = tela_editar_qt.label_6.text()
        quantidade = tela_editar_qt.label_10.text()
        quantidade2 = int(tela_editar_qt.lineEdit.text())
        novaquantidade = (int(quantidade)-quantidade2)
        print(novaquantidade)
        veredit = tela_saida.comboBox.currentText()
        data = tela_editar_qt.label_7.text()
        idproduto = tela_editar_qt.label_9.text()
        #print (data)
        cursor = banco.cursor()
        
        if novaquantidade == 0:
            excluir_dados()
        
        if tela_editar_qt.radioButton.isChecked() and novaquantidade >0:
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


        elif tela_editar_qt.radioButton_2.isChecked() and novaquantidade >0:
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
        elif tela_editar_qt.radioButton_3.isChecked() and novaquantidade >0:
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
        
        elif tela_editar_qt.radioButton_4.isChecked() and novaquantidade >0:
            print("Frezer 4 foi selecionado")
            local ="Frezer 4"
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
        
def excluir_dados():
    idproduto = int(tela_editar_qt.label_9.text())
    print(type(idproduto))
    cursor = banco.cursor()
    comando_SQL = """DELETE FROM estoque2 WHERE id = %s """
    #cursor.execute("DELETE FROM estoque2 WHERE id='%d'"% 10)
    cursor.execute(comando_SQL, (idproduto,))
    banco.commit()
    tela_editar_qt.close()
    
    
#def num_0():
    
    
    


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
        tela_saida.tableWidget.setColumnCount(5)
        tela_saida.tableWidget.setColumnWidth(0,50)
        tela_saida.tableWidget.setColumnWidth(1,350)
        tela_saida.tableWidget.setColumnWidth(2,75)
        tela_saida.tableWidget.setColumnWidth(3,120)
        tela_saida.tableWidget.setRowCount(len(dados_lidos))
        #print(dados_lidos)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 5):
                tela_saida.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    if veredit == "Freezer 2":
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 2' "
        cursor.execute(comando_SQL,dados)
        dados_lidos = cursor.fetchall()
        tela_saida.tableWidget.setColumnCount(5)
        tela_saida.tableWidget.setColumnWidth(0,50)
        tela_saida.tableWidget.setColumnWidth(1,350)
        tela_saida.tableWidget.setColumnWidth(2,75)
        tela_saida.tableWidget.setColumnWidth(3,120)
        tela_saida.tableWidget.setRowCount(len(dados_lidos))
        linha = tela_saida.tableWidget.currentRow() 
        coluna = tela_saida.tableWidget.currentColumn() 
        
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
        tela_saida.tableWidget.setColumnCount(5)
        tela_saida.tableWidget.setColumnWidth(0,50)
        tela_saida.tableWidget.setColumnWidth(1,350)
        tela_saida.tableWidget.setColumnWidth(2,75)
        tela_saida.tableWidget.setColumnWidth(3,120)
        tela_saida.tableWidget.setRowCount(len(dados_lidos))
        #print(dados_lidos)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 5):
                tela_saida.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    if veredit == "Freezer 4":
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM estoque2 WHERE local = 'Frezer 4' "
        cursor.execute(comando_SQL,dados)
        dados_lidos = cursor.fetchall()
        tela_saida.tableWidget.setColumnCount(5)
        tela_saida.tableWidget.setColumnWidth(0,50)
        tela_saida.tableWidget.setColumnWidth(1,350)
        tela_saida.tableWidget.setColumnWidth(2,75)
        tela_saida.tableWidget.setColumnWidth(3,120)
        tela_saida.tableWidget.setRowCount(len(dados_lidos))
        #print(dados_lidos)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 5):
                tela_saida.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def tela_procurar():
    procurar_produto.show()

def fecha_procurar():
    procurar_produto.close()
    
def procurar():
    produto=procurar_produto.comboBox.currentText()
    produto =(str(produto), )
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM estoque2 WHERE descricao = %s"
    cursor.execute(comando_SQL, produto)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    novaqt = 0
    local = ("Vazio")
    if dados_lidos != '':
        for x in dados_lidos:
            quantidade = int(x[2])
            novaqt=novaqt + quantidade                
            local = x[4]
    print(novaqt)
    procurar_produto.label_2.setText(str(novaqt))
    procurar_produto.label_3.setText(str(local))
                                     

    
    
    
def monitor_():
    tela_monitor.show()
    cursor = banco2.cursor()
    #comando_SQL = "SELECT hello_sensor FROM value ORDER BY recorded DESC LIMIT 1"
    comando_SQL = "SELECT * FROM freezer_1 ORDER BY num DESC LIMIT 1"
    cursor.execute(comando_SQL,dados)
    dados_lidos = str(cursor.fetchall())
    print(dados_lidos)
    print(dados_lidos[21:27])
    tela_monitor.label_3.setText(dados_lidos[21:27])

def desligar():
    os.system("sudo shutdown -h now")





app=QtWidgets.QApplication([])
### Carregar janelas ###
cadastro=uic.loadUi("cadastro_2.ui")
menu=uic.loadUi("menu.ui")
ver_estoque=uic.loadUi("telaview.ui")
tela_freezer_1=uic.loadUi("freezer_1.ui")
tela_freezer_2=uic.loadUi("freezer_2.ui")
tela_freezer_3=uic.loadUi("freezer_3.ui")
tela_freezer_4=uic.loadUi("freezer_4.ui")
tela_saida=uic.loadUi("saida.ui")
tela_monitor=uic.loadUi("monitor.ui")
tela_editar_qt=uic.loadUi("editar.ui")
procurar_produto=uic.loadUi("Procurar.ui")

### Verifica qual botão é apertado ###
tela_freezer_1.pushButton_4.clicked.connect(tela_estoque_)
tela_freezer_2.pushButton_4.clicked.connect(tela_estoque_)
tela_freezer_3.pushButton_4.clicked.connect(tela_estoque_)
tela_freezer_4.pushButton_4.clicked.connect(tela_estoque_)
menu.pushButton_2.clicked.connect(tela_estoque_)
menu.pushButton.clicked.connect(tela_estoque)
menu.pushButton_3.clicked.connect(tela_editar)
menu.pushButton_4.clicked.connect(monitor_)
menu.pushButton_5.clicked.connect(desligar)
menu.pushButton_6.clicked.connect(tela_procurar)
cadastro.pushButton.clicked.connect(funcao_princip)
cadastro.pushButton_2.clicked.connect(menu_)
cadastro.pushButton_3.clicked.connect(incrementa_10)
cadastro.pushButton_4.clicked.connect(incrementa_1)
cadastro.pushButton_5.clicked.connect(decrementa_10)
cadastro.pushButton_6.clicked.connect(decrementa_1)
ver_estoque.pushButton_4.clicked.connect(menu_)
tela_saida.pushButton_4.clicked.connect(menu_)
ver_estoque.pushButton.clicked.connect(freezer_1)
ver_estoque.pushButton_2.clicked.connect(freezer_2)
ver_estoque.pushButton_3.clicked.connect(freezer_3)
ver_estoque.pushButton_5.clicked.connect(freezer_4)
tela_saida.pushButton_5.clicked.connect(tela_editar)
tela_saida.pushButton_6.clicked.connect(alterar_dados)
tela_editar_qt.pushButton.clicked.connect(editar_qt)
tela_editar_qt.pushButton_2.clicked.connect(excluir_dados)
tela_editar_qt.pushButton_3.clicked.connect(incrementa_10_saida)
tela_editar_qt.pushButton_4.clicked.connect(incrementa_1_saida)
tela_editar_qt.pushButton_5.clicked.connect(decrementa_10_saida)
tela_editar_qt.pushButton_6.clicked.connect(decrementa_1_saida)
procurar_produto.pushButton.clicked.connect(procurar)
procurar_produto.pushButton_2.clicked.connect(fecha_procurar)
procurar_produto.pushButton_3.clicked.connect(alterar_dados_2)



#tela_editar_qt.pushButton_12.clicked.connect(num_0)




#estoque.show()
menu.show()
app.exec_()


""" create table estoque3 (
id INT NOT NULL AUTO_INCREMENT,
codigo INT,
descricao TEXT,  
quantidade INT(11),
local VARCHAR(20),
PRIMARY KEY (id));  """
# Endereco MAC 	02:42:2b:5a:d9:71