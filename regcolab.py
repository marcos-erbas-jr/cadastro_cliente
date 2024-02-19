from tkinter import *
import database
from tkinter import messagebox

#Tela de registro de Colaborador

def gravarDados():
    if cnome.get() != "":
        vnome = cnome.get()
        vcargo = ccargo.get()
        vsetor = csetor.get()
        vuser = cuser.get()
        vsen = csen.get()

        vquery = (F"INSERT INTO colaboradores(NOME_COLAB,CARGO_COLAB,SETOR_COLAB, USER_COLAB, SENHA_COLAB) VALUES('{vnome}','{vcargo}','{vsetor}','{vuser}','{vsen}');")
        database.dml(vquery)

        cnome.delete(0, END)
        ccargo.delete(0, END)
        csetor.delete(0, END)
        cuser.delete(0, END)
        csen.delete(0, END)

        messagebox.showinfo(title="Registro",
                             message="Colaborador registrado com sucesso.")
    else:
        messagebox.showwarning(title="Registro",
                            message="Ocorreu algum erro no registro.")
def voltar():
    app.quit()

app = Tk()

app.title("Registro de Colaboradores")
app.geometry("500x300")
app.configure(background="light gray")

#anchor -> N = norte, S = sul, E = leste, W = oeste
Label(app, text='Nome:', background="light gray", foreground='#009',
      anchor=W).place(x=20, y=10, width=100, height=20)
cnome = Entry(app) #entrada de texto
cnome.place(x=20, y=30, width=200, height=20)


Label(app, text='Cargo:', background="light gray", foreground='#009',
      anchor=W).place(x=20, y=60, width=100, height=20)
ccargo = Entry(app) #entrada de texto
ccargo.place(x=20, y=80, width=200, height=20)


Label(app, text='Setor:', background="light gray", foreground='#009',
      anchor=W).place(x=270, y=10, width=100, height=20)
csetor = Entry(app) #entrada de texto
csetor.place(x=270, y=30, width=200, height=20)

Label(app, text='Usuário:', background="light gray", foreground='#009',
      anchor=W).place(x=270, y=60, width=100, height=20)
cuser = Entry(app) #entrada de texto
cuser.place(x=270, y=80, width=200, height=20)

Label(app, text='Senha:', background="light gray", foreground='#009',
      anchor=W).place(x=270, y=110, width=100, height=20)
csen = Entry(app) #entrada de texto
csen.place(x=270, y=130, width=200, height=20)



btn = Button(app, text="Registrar", command=gravarDados)
btn.place(x=400, y=180, width=70, height=20)

btn2 = Button(app, text="Voltar", command=voltar)
btn2.place(x=270, y=180, width=70, height=20)



##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="light gray",
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="light gray",
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)


app.mainloop()