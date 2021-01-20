from PyQt5 import uic,QtWidgets
import mysql.connector

data = ""
dados = ""
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="samuelgarcia",
    database="cadastro_estoques"
)


def funcao_princip():
    codigo = cadastro.lineEdit.text()
    descricao = cadastro.lineEdit_2.text()
    quantidade = cadastro.lineEdit_3.text()

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

    
    print("test")
    print("gravado", codigo, descricao, quantidade)


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO estoque (codigo,descricao,quantidade,local) VALUES (%s,%s,%s,%s)"
    dados = (str(codigo),str(descricao),int(quantidade),local)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    ## Limpa Campos ##
    cadastro.lineEdit.setText("")
    cadastro.lineEdit_2.setText("")
    cadastro.lineEdit_3.setText("")


def pegar_data():
    data = str(cadastro.calendarWidget.selectedDate())
    print(data)
    verificames = (data[26])
    verificadia = (data[29])
    carrymes = False
    carrydia = True
    dia = data[28:30]
    #print(verificadia)
    #############  VERIFICA SE ATINGIU CARRY DO DÍGITO #######################
    if verificames == ",":
        mes = int(data[25])
    else:
        mes=int(data[25:27])
        carrymes = True
        print("chegou aqui")
    ###########################################################################

    if verificadia == ")":
        dia = int(data[28])
        carrydia = False
        #print(dia)
    if carrydia and carrymes == True:
        print("entrou aqui aqui")
        print(data[28:30])
    print("MES", mes)
    print("DIA", dia)
    #mes = data[25]
        

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
    comando_SQL = "SELECT * FROM estoque WHERE local = 'Frezer 2' "
    cursor.execute(comando_SQL,dados)
    dados_lidos = cursor.fetchall()
    tela_freezer_1.tableWidget.setRowCount(len(dados_lidos))
    tela_freezer_1.tableWidget.setColumnCount(5)
    tela_freezer_1.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem(str(dados_lidos[0][3])))
    print(dados_lidos)
    #datetime = QDateTime.currentDateTime()
    #print(datetime.toString())
    #for i in range(0, len(dados_lidos)):
     #   for j in range(0, 5):
            #quantidade_lida= 0
      #      tela_freezer_1.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            #soma_quantidade =sum(dados_lidos[i][3])
            #quantidade_lida = dados_lidos[i][3]
            #quantidade_leu = quantidade_lida+quantidade_leu
            

def freezer_2():
    tela_freezer_2.show()
    print("freezer2")

def freezer_3():
    print("freezer3")
    tela_freezer_3.show()

    


    



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
cadastro.calendarWidget.selectionChanged.connect(pegar_data)
#cadastro.dateEdit.clicked.connect(funcao_princip)
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