from tkinter import *
import database
from tkinter import messagebox
#import os
import subprocess

#Tela de login de Administrador

#pastaApp = os.path.dirname(__file__)

def validarAdm():
    vuser = user_adm.get()
    vsen = sen_adm.get()
    print(f"Usuário: {vuser}")
    print(f"Senha: {vsen}")
    if vuser != "" and vsen != "":
        query = (f"SELECT * FROM admins WHERE USER_ADMIN='{vuser}' AND SENHA_ADMIN="
                 f"'{vsen}'")
        res = database.dql(query)
        print(f"Resposta: {res}")
        if res:
            subprocess.Popen(["python", "areaadmin.py"])

            #exec(open(f"{pastaApp}\\loginadm.py", encoding='utf8').read())
            #exec(open(f"areaadmin.py", encoding='utf8').read())
        else:
            messagebox.showerror(title="Erro!",
                                 message="Usuário ou senha incorreto.")

def voltar():
    app.quit()

app = Tk()

app.title("Login Administrador")
app.geometry("500x300")
app.configure(background="#dde")

#anchor -> N = norte, S = sul, E = leste, W = oeste
Label(app, text='Usuário Administrador :', background="#dde", foreground='#009',
      anchor=W).place(x=150, y=10, width=130, height=20)
user_adm = Entry(app) #entrada de texto
user_adm.place(x=150, y=30, width=200, height=20)


Label(app, text='Senha', background="#dde", foreground='#009',
      anchor=W).place(x=150, y=60, width=100, height=20)
sen_adm = Entry(app) #entrada de texto
sen_adm.place(x=150, y=80, width=200, height=20)

btn = Button(app, text="Acessar", command=validarAdm)
btn.place(x=280, y=150, width=70, height=20)

btn2 = Button(app, text="Voltar", command=voltar)
btn2.place(x=150, y=150, width=70, height=20)

##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="#dde",
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="#dde",
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)

app.mainloop()