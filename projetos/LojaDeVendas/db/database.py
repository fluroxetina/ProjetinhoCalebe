import mysql.connector 
from mysql.connector import Error




class Database:
    def __init__(self):
        try: 
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='calebeloja'
            )
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")


