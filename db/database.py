import mysql.connector
from mysql.connector import Error 

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try: 
            conexao = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )

            if conexao.is_connected():
                return conexao
            
        except Error as e:
            print("Erro", e)
            return None