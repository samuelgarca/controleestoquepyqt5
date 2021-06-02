import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'kGCIwgJslnry9hjO',
    'host': '35.247.216.160',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'
}

# now we establish our connection
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()  # initialize connection cursor
config['database'] = 'cadastro_estoques'  # add new database to config dict
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()
cursor.execute("CREATE TABLE estoque ("
               "descricao text,"
               "quantidade INT(11),"
               "data VARCHAR(20),"
               "local VARCHAR(20) )")

cnxn.commit()  # this commits changes to the database
