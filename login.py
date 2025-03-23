from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql.cursors
from subs import cad_cliente

conexao = pymysql.connect(  # faz o login no banco de dados
		host = "localhost",
		user = "root",
		password = "31102001Ig@r",
		database = "teste"
		)

class Usuario:
	def __init__(self, root):
		root.title("Tela de Login")

		mainframe = ttk.Frame(root, padding="24 24 96 96")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)

		self.user = StringVar()
		user_entry = ttk.Entry(mainframe, width=30, textvariable=self.user)
		user_entry.grid(column=2, row=1, sticky=(W, E))
		self.senha = StringVar()
		senha_entry = ttk.Entry(mainframe, width=30, textvariable=self.senha, show='*')
		senha_entry.grid(column=2, row=3, sticky=(W, E))

		ttk.Button(mainframe, text="Login", command=self.login).grid(column=5, row=5, sticky=W)

		for child in mainframe.winfo_children():
			child.grid_configure(padx=5, pady=5)

		user_entry.focus()
		root.bind("<Return>", self.login)

	def login(self, *args):	
		cursor = conexao.cursor() # faz a conexão com o banco
		cursor.execute("SELECT login FROM usuario;")
		user1 = cursor.fetchone()
		cursor.execute("SELECT senha FROM usuario;")
		senha1 = cursor.fetchone()
		for i in user1:  # converte a tupla gerada pelo cursor para string
			user = i
		for i in senha1:  # converte a tupla gerada pelo cursor para string
			senha = i
		usuario = str(self.user.get())
		password = str(self.senha.get())
		if usuario == user and password == senha:
			messagebox.showinfo(message='Login com sucesso')
			cadastro = cad_cliente.Cliente(root)
			root.destroy()
		else:
			messagebox.showinfo(message='Login incorreto')

root = Tk()
Usuario(root)
root.mainloop()