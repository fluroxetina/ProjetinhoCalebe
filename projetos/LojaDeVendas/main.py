from db.database import Database 
from tkinter import *
from tkinter import messagebox


def abrir_pagina_principal():
    login_window.destroy()  
    pagina_principal()

def ValidarLogin():

    usuario = campo_usuario.get()
    senha = campo_senha.get()   

    db = Database()
    db.connection.is_connected()

    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM teste WHERE nome = %s AND senha = %s", (usuario, senha))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
        abrir_pagina_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

def on_entry_click(event, entry):
   
    if entry.get() == entry.placeholder:
        entry.delete(0, "end")  
        entry.config(fg='black') 

def on_focusout(event, entry):
    
    if entry.get() == '':
        entry.insert(0, entry.placeholder)
        entry.config(fg='grey')


def pagina_principal():
    
    root = Tk()
    root.title("Página Principal")
    root.geometry("1300x700")

    label = Label(root, text="Bem-vindo à Página Principal!", font=("Arial", 24))
    label.pack(pady=20)

    sair_btn = Button(root, text="Sair", font=("Arial", 14), command=root.destroy)
    sair_btn.pack(pady=20)

    root.mainloop()



login_window = Tk()
login_window.title("Login")
login_window.geometry("1300x700")


login_label = Label(login_window, text="LOGIN", font=("Arial", 24))
login_label.place(relx=0.5, rely=0.4, anchor="center")


campo_usuario = Entry(login_window, width=30, font=("Arial", 14))
campo_usuario.placeholder = "Digite seu nome"
campo_usuario.insert(0, campo_usuario.placeholder)
campo_usuario.config(fg='grey')
campo_usuario.place(relx=0.5, rely=0.45, anchor="center")


campo_senha = Entry(login_window, width=30, font=("Arial", 14), show="*")
campo_senha.placeholder = "Digite a sua senha"
campo_senha.insert(0, campo_senha.placeholder)
campo_senha.config(fg='grey')
campo_senha.place(relx=0.5, rely=0.5, anchor="center")

entrar_btn = Button(
    login_window,
    text="Entrar",
    font=("Arial", 14),
    command=ValidarLogin,
)
entrar_btn.place(relx=0.5, rely=0.55, anchor="center")

campo_usuario.bind("<FocusIn>", lambda event, entry=campo_usuario: on_entry_click(event, entry))
campo_usuario.bind("<FocusOut>", lambda event, entry=campo_usuario: on_focusout(event, entry))

campo_senha.bind("<FocusIn>", lambda event, entry=campo_senha: on_entry_click(event, entry))
campo_senha.bind("<FocusOut>", lambda event, entry=campo_senha: on_focusout(event, entry))


login_window.mainloop()
