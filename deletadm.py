from tkinter import *
import subprocess
import database
from tkinter import messagebox

#Tela de exclusão de administradores

def pesquisar():
    var = vfiltro.get()
    varquery = search.get()
    if var == 'Nome':
        query = f"SELECT * FROM admins WHERE NOME_ADMIN LIKE '" \
                f"%{varquery}%'"
        res = database.dql(query)
        resultado = ''
        try:
            x = res[0][1]
        except:
            messagebox.showerror("Erro","Administrador não encontrado")

        else:
            def deletar():
                vardelet = vcolab.get()
                querydelet = f"DELETE FROM admins WHERE NOME_ADMIN =" \
                             f"'{vardelet}';"
                database.dml(querydelet)
                excluir = messagebox.askyesno("Atenção!", "Deseja confirma a "
                                                    "exclusão "
                                                f"de {vardelet}?")
                if excluir:
                    querydelet = f"DELETE FROM admins WHERE NOME_ADMIN =" \
                                 f"'{vardelet}';"
                    database.dml(querydelet)
                    print("Exclusão realizada.")

            lista = []
            for c in res:
                lista.append(str(c[1]))
                print(lista)
            vcolab = StringVar()
            vcolab.set(lista[0])  # Valor padrão
            op_filtro = OptionMenu(app, vcolab,*lista)  # Foi
            # usado um * para
            # utilizar todos os valores da lista
            op_filtro.place(x=130, y=140, width=230, height=45)

            btn_filtro = Button(app, text="Deletar", command=deletar)
            btn_filtro.place(x=210, y=200, width=80, height=25)

            ##Rodapé
            txt1 = Label(app, text='Criado por Marcos Erbas Jr',
                         background="light gray",
                         foreground="#000")
            txt1.place(x=10, y=270, width=150, height=30)

            txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
                         foreground="#000")
            txt1.place(x=350, y=270, width=150, height=30)


    elif var == 'Usuário':
        query = f"SELECT * FROM admins WHERE USER_ADMIN LIKE " \
                f"'%{varquery}%'"
        res = database.dql(query)
        resultado = ''
        try:
            x = res[0][1]
        except:
            messagebox.showerror("Erro", "Usuário não encontrado")

        else:
            def deletar():
                vardelet = vcolab.get()
                excluir = messagebox.askyesno("Atenção!", "Deseja confirma a "
                                                          "exclusão "
                                                          f"de {vardelet}?")
                if excluir:
                    querydelet = f"DELETE FROM admins WHERE USER_ADMIN =" \
                                 f"'{vardelet}';"
                    database.dml(querydelet)
                    print("Exclusão realizada.")

            lista = []
            for c in res:
                lista.append(str(c[4]))
                print(lista)
            vcolab = StringVar()
            vcolab.set(lista[0])  # Valor padrão
            op_filtro = OptionMenu(app, vcolab, *lista)  # Foi
            # usado um * para
            # utilizar todos os valores da lista
            op_filtro.place(x=130, y=140, width=230, height=45)

            btn_filtro = Button(app, text="Deletar", command=deletar)
            btn_filtro.place(x=210, y=200, width=80, height=25)

            ##Rodapé
            txt1 = Label(app, text='Criado por Marcos Erbas Jr',
                         background="light gray",
                         foreground="#000")
            txt1.place(x=10, y=270, width=150, height=30)

            txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
                         foreground="#000")
            txt1.place(x=350, y=270, width=150, height=30)


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

def pesqColab():
    subprocess.Popen(["python", "pesqcolab.py"])

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
menuColaboradores.add_command(label='Deletar', command=semComando)
barraMenu.add_cascade(label='Colaboradores', menu=menuColaboradores)

#Menu administradores
menuAdministradores = Menu(barraMenu, tearoff=0)
menuAdministradores.add_command(label='Registrar', command=novoAdministrador)
menuAdministradores.add_separator()
menuAdministradores.add_command(label='Pesquisar', command=semComando)
menuAdministradores.add_separator()
menuAdministradores.add_command(label='Relatório', command=semComando)
menuAdministradores.add_separator()
menuAdministradores.add_command(label='Deletar', command=semComando)
barraMenu.add_cascade(label='Administradores', menu=menuAdministradores)

#Menu clientes
menuClientes = Menu(barraMenu, tearoff=0)
menuClientes.add_command(label='Registrar', command=semComando())
menuClientes.add_separator()
menuClientes.add_command(label='Pesquisar', command=semComando)
menuClientes.add_separator()
menuClientes.add_command(label='Relatório', command=semComando)
menuClientes.add_separator()
menuClientes.add_command(label='Deletar', command=semComando)
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

Label(app, text=f'Exclusão de Administrador', background="light gray",
                    foreground="#000",font=("Helvetica",10, "bold")).place(
    x=130, y=-40, width=170,height=120)

##Parte do Filtro

listaFiltro = ["Nome","Usuário"]

vfiltro = StringVar()
vfiltro.set(listaFiltro[0])  # Valor padrão

bl_filtro = Label(app, text="Pesquisar administrador por:")
bl_filtro.place(x=130, y=35, width=150, height=30)

op_filtro = OptionMenu(app, vfiltro, *listaFiltro)  # Foi usado um * para
# utilizar todos os valores da lista
op_filtro.place(x=280, y=35, width=80, height=30)

search = Entry(app)
search.place(x=130, y=70, width=232, height=30)

btn_filtro = Button(app, text="Pesquisar", command=pesquisar)
btn_filtro.place(x=280, y=110, width=80, height=25)



##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="light gray",
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)

app.mainloop()

