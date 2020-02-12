# encoding: UTF-8
from tkinter import *
from tkinter import messagebox
import socket
import subprocess
import pymysql.cursors

#Setup
root = Tk()     #Janela Principal
root.resizable(width=False, height=False) #Fazer janela ficar nao redimensionavel
root.geometry('{}x{}'.format("310", "175")) #Setar tamanho da janela
#Top Frame
topFrame = Frame(root)
topFrame.pack()
#Bottom Frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
defaultFont = "Lucida Console" #Fonte padrao usada

'''
#Funcao para imagens
def set_image(parent, img):
    label = Label(parent, image=img)
    label.pack()
'''

def loginServer():
    userCheck = userVar.get()
    passCheck = passVar.get()
    if userCheck == '' or passCheck == '':
        print("TESTE2")
              
    else:
        print("TESTE3")        
        #HOST = '127.0.0.1'
        HOST = '192.168.50.235'    # Ip do Host alvo(tracker)
        PORT = 9999         # Porta do Tracker
        #Conexão usando Socket(TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = s.connect_ex((HOST, PORT))

        if resultado == 0:
            print("Tracker online, conectando ao BD!")
            # Tentando conexão com o banco
            try:
                connection = pymysql.connect(host='localhost',
                             user='root', #Usuario
                             password='', #Senha
                             db='xqdl', #Nome do banco
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                #Aqui pode executar comandos SQL
                with connection.cursor() as cursor:                
                    sqlQuery = "SELECT `user_ID`, `user_nome` FROM `user`"
                    cursor.execute(sqlQuery)
                    result = cursor.fetchone()
                    print(result)
            except pymysql.Error:
                print ("Erro na conexão com o DB!")
        else:
            msg = messagebox.showinfo("Error!" , "Tracker offline!")      

#img = PhotoImage(file='xqdl.png')

'''TITULO'''
root.title("XQDL")
title = Label(topFrame, text="XQDL - Chat/VoiceChat\n")
title.pack()
title.config(font=(defaultFont, 16, "bold"))
'''FIM TITULO'''

#set_image(topFrame, img) #Coloca Imagem

'''Usuario'''
userVar = StringVar()
usuario = Label(topFrame, text="Usuário:")
usuario.pack()
usuario.config(font=(defaultFont, 11))
loginTextUser = Entry(topFrame, textvariable=userVar) #Cria area de texto para usuario
loginTextUser.pack()
'''FIM USUARIO'''

'''SENHA'''
passVar = StringVar()
senha = Label(topFrame, text="Senha:") #Cria area de texto para senha
senha.pack()
senha.config(font=(defaultFont, 11))
loginTextPass = Entry(topFrame, textvariable=passVar) #Cria area de texto
loginTextPass.pack()
'''FIM SENHA'''

'''BOTAO LOGIN'''
buttonLogin = Button(bottomFrame, text="Login", command = loginServer) #Botao de login
buttonLogin.pack() #Faz botao aparecer
buttonLogin.config(font=(defaultFont, 11, "bold"))







root.mainloop()
