from tkinter import *
from tkinter import messagebox
import database
import subprocess

#Tela de login de Colaborador

def validarcolab():
    vuser = user_colab.get()
    vsen = sen_colab.get()
    print(f"Usuário: {vuser}")
    print(f"Senha: {vsen}")
    if vuser != "" and vsen != "":
        query = (f"SELECT * FROM colaboradores WHERE USER_COLAB='{vuser}' AND SENHA_COLAB='{vsen}'")
        res = database.dql(query)
        print(f"Resposta: {res}")
        if res:
            subprocess.Popen(["python", "areacolab.py"])
            #exec(open(f"{pastaApp}\\areacolab.py", encoding='utf8').read())
        else:
            messagebox.showerror(title="Erro!",message="Usuário ou senha incorreto.")

def voltar():
    app.quit()

app = Tk()

app.title("Login Colaborador")
app.geometry("500x300")
app.configure(background="#dde")

#anchor -> N = norte, S = sul, E = leste, W = oeste
Label(app, text='Usuário:', background="#dde", foreground='#009',
      anchor=W).place(x=150, y=10, width=100, height=20)
user_colab = Entry(app) #entrada de texto
user_colab.place(x=150, y=30, width=200, height=20)


Label(app, text='Senha', background="#dde", foreground='#009',
      anchor=W).place(x=150, y=60, width=100, height=20)
sen_colab = Entry(app) #entrada de texto
sen_colab.place(x=150, y=80, width=200, height=20)

btn = Button(app, text="Acessar", command=validarcolab)
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