from tkinter import *
import subprocess
import database
from tkinter import messagebox

#Tela de busca de clientes
color = "light blue"
def pesquisar():
    var = vfiltro.get()
    varquery = search.get()
    if var == 'Nome':
        query = f"SELECT * FROM clientes WHERE NOME_CLIENTE LIKE '%{varquery}%'"
        res = database.dql(query)
        print(res)
        resultado = ''
        try:
            x = res[0]
            for c in res:
                resultado += f"{c[1]} - {c[4]} \n"
            Label(app, text=f'Resultado:\n {resultado}', background="white",
                  foreground="#000").place(x=50, y=130, width=400, height=120)
        except:
            messagebox.showerror("Erro", "Cliente não encontrado")

    elif var == 'Endereço':
        query = f"SELECT * FROM clientes WHERE ENDERECO_CLIENTE LIKE" \
                f" '%{varquery}%'"

        res = database.dql(query)
        resultado = ''
        try:
            x = res[0][1]
            for c in res:
                resultado += f"{c[1]} - {c[2]} \n"
            Label(app, text=f'Resultado:\n {resultado}', background="white",
                  foreground="#000").place(x=50, y=130, width=400, height=120)

        except:
            messagebox.showerror("Erro", "Endereço não encontrado")

    elif var == 'Telefone':
        query = f"SELECT * FROM clientes WHERE TELEFONE_CLIENTE LIKE " \
                f"'%{varquery}%'"
        res = database.dql(query)
        resultado = ''
        try:
            x = res[0][1]
            for c in res:
                resultado += f"{c[1]} - {c[4]} \n"
            Label(app, text=f'Resultado:\n {resultado}', background="white",
                  foreground="#000").place(x=50, y=130, width=400, height=120)

        except:
            messagebox.showerror("Erro", "Telefone não encontrado")


def semComando():
    print('')

def pesqColab():
    subprocess.Popen(["python", "pesqcolab.py"])

def pesqCliente():
    subprocess.Popen(["python", "colabpesqcliente.py"])

def novoCliente():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "colabregcliente.py"])

def logout():
    app.quit()

app = Tk()

app.title("Área do Colaborador")
app.geometry("500x300")
app.configure(background=color)


barraMenu = Menu(app)

#Menu colaboradores
menuColaboradores = Menu(barraMenu, tearoff=0)
menuColaboradores.add_command(label='Pesquisar', command=semComando)
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

##Parte do Filtro

listaFiltro = ["Nome", "Endereço", "Telefone"]

vfiltro = StringVar()
vfiltro.set(listaFiltro[0])  # Valor padrão

bl_filtro = Label(app, text="Pesquisar cliente por:")
bl_filtro.place(x=130, y=10, width=150, height=30)

op_filtro = OptionMenu(app, vfiltro, *listaFiltro)  # Foi usado um * para
# utilizar todos os valores da lista
op_filtro.place(x=280, y=10, width=90, height=30)

search = Entry(app)
search.place(x=130, y=50, width=232, height=30)

btn_filtro = Button(app, text="Pesquisar", command=pesquisar)
btn_filtro.place(x=280, y=90, width=80, height=25)



##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background=color,
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background=color,
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)

app.mainloop()