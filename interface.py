from tkinter import *
#import os
import subprocess

#Código para mostrar a janela inicial

user_colab = None
sen_colab = None
#pastaApp = os.path.dirname(__name__)

def verifiquecolab():
    subprocess.Popen(["python", "logincolab.py"])

def verifiqueadm():
    """Abre uma nova janela"""
    subprocess.Popen(["python", "loginadm.py"])



app = Tk()

app.title("Registro de Cliente")
app.geometry("500x300")
app.configure(background="#dde")
titulo_label = Label(app, text="Acessar Conta",background="#dde",
                     font=("Helvetica",17, "bold"))
titulo_label.place(x=150, y=-150, width=200, height=401)

btn = Button(app, text="Colaborador", command=verifiquecolab)
btn.place(x=200, y=90, width=100, height=40)

btn2 = Button(app, text="Administrador", command=verifiqueadm)
btn2.place(x=200, y=170, width=100, height=40)




##Rodapé
txt1 = Label(app, text='Criado por Marcos Erbas Jr', background="#dde",
             foreground="#000")
txt1.place(x=10, y=270, width=150, height=30)

txt1 = Label(app, text='Versão: 1.0.24', background="#dde",
             foreground="#000")
txt1.place(x=350, y=270, width=150, height=30)

app.mainloop()