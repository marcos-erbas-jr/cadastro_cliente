from tkinter import *
import os
import subprocess

color = 'lightblue'
#Código para mostrar janela da área do Colaborador

pastaApp = os.path.dirname(__file__)

def semComando():
    print('')

def novoCliente():
    """Abre uma nova janela"""
    #exec(open(pastaApp+"\\interface_database.py").read(), {'x':10})
    subprocess.Popen(["python", "colabregcliente.py"])

def pesqCliente():
    subprocess.Popen(["python", "colabpesqcliente.py"])

def pesqColab():
    subprocess.Popen(["python", "colabpesqcolab.py"])

def logout():
    app.quit()

app = Tk()

app.title("Área do Colaborador")
app.geometry("500x300")
app.configure(background="lightblue")


barraMenu = Menu(app)

#Menu colaboradores
menuColaboradores = Menu(barraMenu, tearoff=0)
menuColaboradores.add_command(label='Pesquisar', command=pesqColab)
barraMenu.add_cascade(label='Colaboradores', menu=menuColaboradores)

#Menu clientes
menuClientes = Menu(barraMenu, tearoff=0)
menuClientes.add_command(label='Registrar', command=novoCliente)
menuClientes.add_separator()
menuClientes.add_command(label='Pesquisar', command=pesqCliente)
menuClientes.add_separator()
menuClientes.add_command(label='Relatório', command=semComando)
menuClientes.add_separator()
menuClientes.add_command(label='Deletar', command=semComando)
barraMenu.add_cascade(label='Clientes', menu=menuClientes)


#Menu ajuda
menuManutencao = Menu(barraMenu, tearoff=0)
menuManutencao.add_command(label='Pedir ajuda', command=semComando)
barraMenu.add_cascade(label='Ajuda', menu=menuManutencao)

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
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="lightblue",
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="lightblue",
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)

app.mainloop()