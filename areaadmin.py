from tkinter import *
import os
import subprocess

#Código para mostrar janela da área do Administrador

pastaApp = os.path.dirname(__file__)

def abrirDB():
    caminho_sqlite_studio = r"C:\Program Files\SQLiteStudio\SQLiteStudio.exe"
    # Abrir o SQLite Studio
    subprocess.Popen([caminho_sqlite_studio,
                      r"C:\Users\marcos.erbas\Documents\clientdata\clientdatabase.db"])
def semComando():
    print('')

def novoColaborador():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "regcolab.py"])
    #exec(open("regcolab.py",encoding='utf8').read())

def novoAdministrador():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "regadmin.py"])

def novoCliente():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "regcliente.py"])

def pesqColab():
    subprocess.Popen(["python", "pesqcolab.py"])

def pesqAdmin():
    subprocess.Popen(["python", "pesqadm.py"])

def pesqClient():
    subprocess.Popen(["python", "pesqcliente.py"])

def excluirColab():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "deletcolab.py"])

def excluirClient():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "deletcliente.py"])

def excluirAdm():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "deletadm.py"])

def logout():
    app.quit()

app = Tk()

app.title("Área do Administrador")
app.geometry("500x300")
app.configure(background="light gray")


barraMenu = Menu(app)

#Menu colaboradores
menuColaboradores = Menu(barraMenu, tearoff=0)
menuColaboradores.add_command(label='Registrar', command=novoColaborador)
menuColaboradores.add_separator()
menuColaboradores.add_command(label='Pesquisar', command=pesqColab)
menuColaboradores.add_separator()
menuColaboradores.add_command(label='Relatório', command=semComando)
menuColaboradores.add_separator()
menuColaboradores.add_command(label='Deletar', command=excluirColab)
barraMenu.add_cascade(label='Colaboradores', menu=menuColaboradores)

#Menu administradores
menuAdministradores = Menu(barraMenu, tearoff=0)
menuAdministradores.add_command(label='Registrar', command=novoAdministrador)
menuAdministradores.add_separator()
menuAdministradores.add_command(label='Pesquisar', command=pesqAdmin)
menuAdministradores.add_separator()
menuAdministradores.add_command(label='Relatório', command=semComando)
menuAdministradores.add_separator()
menuAdministradores.add_command(label='Deletar', command=excluirAdm)
barraMenu.add_cascade(label='Administradores', menu=menuAdministradores)

#Menu clientes
menuClientes = Menu(barraMenu, tearoff=0)
menuClientes.add_command(label='Registrar', command=novoCliente)
menuClientes.add_separator()
menuClientes.add_command(label='Pesquisar', command=pesqClient)
menuClientes.add_separator()
menuClientes.add_command(label='Relatório', command=semComando)
menuClientes.add_separator()
menuClientes.add_command(label='Deletar', command=excluirClient)
barraMenu.add_cascade(label='Clientes', menu=menuClientes)



#Menu manutenção
menuManutencao = Menu(barraMenu, tearoff=0)
menuManutencao.add_command(label='Acessar Banco de dados', command=abrirDB)
barraMenu.add_cascade(label='Dados', menu=menuManutencao)

#Menu conta
menuConta = Menu(barraMenu, tearoff=0)
menuConta.add_command(label='Sair', command=logout)#futuramente
# colocar um desvio para minhas redes sociais
barraMenu.add_cascade(label='Conta', menu=menuConta)

#Menu sobre
menuSobre = Menu(barraMenu, tearoff=0)
menuSobre.add_command(label='Redes Sociais', command=semComando)#futuramente
# colocar um desvio para minhas redes sociais
barraMenu.add_cascade(label='Sobre', menu=menuSobre)

app.config(menu=barraMenu)




##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="light gray",
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)

app.mainloop()