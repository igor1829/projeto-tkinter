from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql.cursors

conexao = pymysql.connect(  # faz o login no banco de dados
		host = "localhost",
		user = "root",
		password = "31102001Ig@r",
		database = "teste"
		)

class Cliente:
    def __init__(self, root):
        root = Tk()
        self.root = root  # Agora armazenamos corretamente a referência do root
        self.root.title("Cadastro de Clientes")
        root.title("Cadastro de Clientes")
        mainframe = ttk.Frame(root, padding="48 48 192 192")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Nome Cliente").grid(column=1, row=1, sticky=W)
        self.client = StringVar()
        self.cliente_entry = ttk.Entry(mainframe, width=30, textvariable=self.client)
        self.cliente_entry.grid(column=1, row=2, sticky=(W, E))

        ttk.Label(mainframe, text="CPF do Cliente").grid(column=1, row=4, sticky=W)
        self.cpf = StringVar()
        self.cpf_entry = ttk.Entry(mainframe, width=30, textvariable=self.cpf)
        self.cpf_entry.grid(column=1, row=5, sticky=(W, E))

        ttk.Label(mainframe, text="Telefone").grid(column=1, row=7, sticky=W)
        self.telefone = StringVar()
        self.telefone_entry = ttk.Entry(mainframe, width=30, textvariable=self.telefone)
        self.telefone_entry.grid(column=1, row=9, sticky=(W, E))

        ttk.Label(mainframe, text="Endereço").grid(column=1, row=11, sticky=W)
        self.endereco = StringVar()
        self.endereco_entry = ttk.Entry(mainframe, width=30, textvariable=self.endereco)
        self.endereco_entry.grid(column=1, row=13, sticky=(W, E))

        ttk.Button(mainframe, text="Cadastrar Cliente", command=self.cadastro_cliente).grid(column=1, row=15, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.cliente_entry.focus()
        root.bind("<Return>", self.cadastro_cliente)

    def cadastro_cliente(self, *args):
        nome_cl = self.cliente_entry.get()
        cpf_cl = self.cpf_entry.get()
        tel = self.telefone_entry.get()
        end = self.endereco_entry.get()
        cursor = conexao.cursor()
        sql = "INSERT INTO `clientes` (`nome_cliente`, `cpf_cliente`, `telefone`, `endereco`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome_cl, cpf_cl, tel, end))
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        conexao.commit()
        conexao.close()