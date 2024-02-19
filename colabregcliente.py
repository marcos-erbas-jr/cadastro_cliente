from tkinter import *
import database
from tkinter import messagebox
color = 'light blue'
#Tela de registro de Colaborador
def gravarDados():
    if cnome.get() != "":
        vnome = cnome.get()
        vendereco = cendereco.get()
        vemail = cemail.get()
        vtel = ctel.get()

        vquery = (F"INSERT INTO clientes(NOME_CLIENTE,ENDERECO_CLIENTE,"
                  F"EMAIL_CLIENTE, TELEFONE_CLIENTE) VALUES("
                  F"'{vnome}',"
                  F"'{vendereco}','{vemail}','{vtel}');")
        database.dml(vquery)

        cnome.delete(0, END)
        cendereco.delete(0, END)
        cemail.delete(0, END)
        ctel.delete(0, END)

        messagebox.showinfo(title="Registro",
                             message="Cliente registrado com sucesso.")
    else:
        messagebox.showwarning(title="Registro",
                            message="Ocorreu algum erro no registro.")
def voltar():
    app.quit()

app = Tk()

app.title("Registro de Clientes")
app.geometry("500x300")
app.configure(background=color)

#anchor -> N = norte, S = sul, E = leste, W = oeste
Label(app, text='Nome:', background=color, foreground='#009',
      anchor=W).place(x=20, y=10, width=100, height=20)
cnome = Entry(app) #entrada de texto
cnome.place(x=20, y=30, width=200, height=20)


Label(app, text='Endereço:', background=color, foreground='#009',
      anchor=W).place(x=20, y=60, width=100, height=20)
cendereco = Entry(app) #entrada de texto
cendereco.place(x=20, y=80, width=200, height=20)


Label(app, text='E-mail:', background=color, foreground='#009',
      anchor=W).place(x=270, y=10, width=100, height=20)
cemail = Entry(app) #entrada de texto
cemail.place(x=270, y=30, width=200, height=20)

Label(app, text='Telefone:', background=color, foreground='#009',
      anchor=W).place(x=270, y=60, width=100, height=20)
ctel = Entry(app) #entrada de texto
ctel.place(x=270, y=80, width=200, height=20)


btn = Button(app, text="Registrar", command=gravarDados)
btn.place(x=400, y=180, width=70, height=20)

btn2 = Button(app, text="Voltar", command=voltar)
btn2.place(x=20, y=180, width=70, height=20)



##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background=color,
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background=color,
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)


app.mainloop()