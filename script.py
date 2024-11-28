from tkinter import *
from mysql.connector import Error
from db.database import Database

def cadastrarUsuario(self):
    usuario = self.nome.get()
    senha = self.senha.get()

    if not usuario or not senha:
        self.mensagem["text"] = "Preencha todos os campos"
        return

    try:
        # Chama a função para inserir dados
        self.inserirDados(usuario, senha)
        self.mensagem["text"] = "Usuário cadastrado com sucesso!"
    except Error as e:
        self.mensagem["text"] = f"Erro: {e}"
# Inicializando a conexão com o banco de dados
db = Database("localhost", "root", "", "calebeloja")

conecta = db.connect()  # Conexão com o banco de dados

master = None
# Configurações da interface
fontePadrao = ("Arial", "10")
primeiroContainer = Frame(master)
primeiroContainer["pady"] = 10
primeiroContainer.pack()

segundoContainer = Frame(master)
segundoContainer["padx"] = 20
segundoContainer.pack()

terceiroContainer = Frame(master)
terceiroContainer["padx"] = 20
terceiroContainer.pack()

quartoContainer = Frame(master)
quartoContainer["pady"] = 20
quartoContainer.pack()

titulo = Label(primeiroContainer, text="Dados do usuário")
titulo["font"] = ("Arial", "10", "bold")
titulo.pack()

nomeLabel = Label(segundoContainer, text="Nome", font=fontePadrao)
nomeLabel.pack(side=LEFT)

nome = Entry(segundoContainer)
nome["width"] = 30
nome["font"] = fontePadrao
nome.pack(side=LEFT)

senhaLabel = Label(terceiroContainer, text="Senha", font=fontePadrao)
senhaLabel.pack(side=LEFT)

senha = Entry(terceiroContainer)
senha["width"] = 30
senha["font"] = fontePadrao
senha["show"] = "*"
senha.pack(side=LEFT)

cadastrar = Button(quartoContainer)
cadastrar["text"] = "Cadastrar"
cadastrar["font"] = ("Calibri", "8")
cadastrar["width"] = 12
cadastrar["command"] = cadastrarUsuario()  # Chama o método de cadastro
cadastrar.pack()

mensagem = Label(quartoContainer, text="", font=fontePadrao)
mensagem.pack()



    # Método que realiza a inserção no banco
def inserirDados(self, nome, senha):
    try:
        cursor = self.conexao.cursor()
        query = "INSERT INTO teste (nome, senha) VALUES (%s, %s)"
        values = (nome, senha)
        cursor.execute(query, values)
        self.conexao.commit()
    except Error as e:
        raise e


# Inicializando o banco e a interface
root = Tk()
root.geometry("1300x750")

root.mainloop()
