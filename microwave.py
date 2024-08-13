import time
import threading
from tkinter import *

#Janela TK

janela = Tk()
janela.title("Micro-Ondas")
janela.geometry("900x400")

# Variáveis globais
tempo_restante = 0
tempo_acumulado = 0


#Função para atualizar o tempo

def atualizar_tempo():
    global tempo_restante, tempo_ativo
    if tempo_restante > 0:
        tela_microondas.config(bg = "yellow")
        minutos, segundos = divmod(tempo_restante, 60)
        tempo_str = f"{minutos:02}:{segundos:02}"
        lbl_timer.config(text=tempo_str)
        tempo_restante -= 1
        janela.after(1000, atualizar_tempo)  # Chama a função novamente após 1 segundo
    else:
        tela_microondas.config(bg = "#505050")


#Funções para iniciar e parar o timer

def iniciar():
    global tempo_restante
    tempo_restante = tempo_acumulado
    if tempo_restante > 0:
        atualizar_tempo() 

def limpar():
    global tempo_restante
    tempo_restante = 0
    lbl_timer.config(text="00:00")

#Funções para os tempos fixos de cada um dos botões 

def carne():
    global tempo_acumulado
    tempo_acumulado = 360  # Definir o tempo de descongelar a carne (6min)
    iniciar()

def aves():
    global tempo_acumulado
    tempo_acumulado = 300  # Definir o tempo de descongelar as aves (5min)
    iniciar()

def feijao():
    global tempo_acumulado
    tempo_acumulado = 240  # Definir o tempo de descongelar o feijão (4min)
    iniciar()

#Função para atualizar o tempo acumulado com base no botão pressionado
def adicionar_tempo(tempo):
    global tempo_acumulado
    tempo_acumulado += tempo
    minutos, segundos = divmod(tempo_acumulado, 60)
    tempo_str = f"{minutos:02}:{segundos:02}"
    lbl_timer.config(text=tempo_str)

#Funções para os botões numéricos, once cada número irá adicionar 10 segundos em relação ao botão anterior

def btn1_func():
    adicionar_tempo(10)

def btn2_func():
    adicionar_tempo(20)

def btn3_func():
    adicionar_tempo(30)

def btn4_func():
    adicionar_tempo(40)

def btn5_func():
    adicionar_tempo(50)

def btn6_func():
    adicionar_tempo(60)

def btn7_func():
    adicionar_tempo(70)

def btn8_func():
    adicionar_tempo(80)

def btn9_func():
    adicionar_tempo(90)

def btn0_func():
    adicionar_tempo(100)


#Criando Botões

tela = Frame(janela, width = 620, height = 380, bg = "#000")
tela.grid(column = 0, row = 0, padx = 5, pady = 10, sticky = N, rowspan = 40)

tela_microondas = Frame(tela, width = 400, height = 200, bg = "#505050")
tela_microondas.place(x = 100, y = 90)

tela_timer = Frame(janela, width = 380, height = 60, bg = "#505050")
tela_timer.grid(column = 1, row = 0, sticky = N, pady = 10, columnspan = 3)

lbl_timer = Label(tela_timer, text="00:00", font = ("Helvetica", 30), bg = "#505050", fg = "white")
lbl_timer.pack(expand = TRUE)

btn_carne = Button(janela, text = "Carne", width = 10, height = 2, bg = "blue", fg = "white", command = carne)
btn_carne.grid(column = 1, row = 1)

btn_aves = Button(janela, text = "Aves", width = 10, height = 2, bg = "blue", fg = "white", command = aves)
btn_aves.grid(column = 2, row = 1)

btn_feijao = Button(janela, text = "Feijão", width = 10, height = 2, bg = "blue", fg = "white", command = feijao)
btn_feijao.grid(column = 3, row = 1)

btn1 = Button(janela, text = "1", width = 5, height = 2, bg = "green", command = btn1_func)
btn1.grid(column = 1, row = 2, padx = (5, 0), pady = 10)

btn2 = Button(janela, text = "2", width = 5, height = 2, bg = "green", command = btn2_func)
btn2.grid(column = 2, row = 2, pady = 10)

btn3 = Button(janela, text = "3", width = 5, height = 2, bg = "green", command = btn3_func)
btn3.grid(column = 3, row = 2, pady = 10)

btn4 = Button(janela, text = "4", width = 5, height = 2, bg = "green", command = btn4_func)
btn4.grid(column = 1, row = 3, padx = (5, 0))

btn5 = Button(janela, text = "5", width = 5, height = 2, bg = "green", command = btn5_func)
btn5.grid(column = 2, row = 3)

btn6 = Button(janela, text = "6", width = 5, height = 2, bg = "green", command = btn6_func)
btn6.grid(column = 3, row = 3)

btn7 = Button(janela, text = "7", width = 5, height = 2, bg = "green", command = btn7_func)
btn7.grid(column = 1, row = 4, padx = (5, 0), pady = 15)

btn8 = Button(janela, text = "8", width = 5, height = 2, bg = "green", command = btn8_func)
btn8.grid(column = 2, row = 4, pady = 15)

btn9 = Button(janela, text = "9", width = 5, height = 2, bg = "green", command = btn9_func)
btn9.grid(column = 3, row = 4, pady = 15)

btn0 = Button(janela, text = "0", width = 5, height = 2, bg = "green", command = btn0_func)
btn0.grid(column = 2, row = 5)

btn_start = Button(janela, text = "Começar", width = 10, height = 2, bg = "cyan", command = iniciar)
btn_start.grid(column = 1, row = 6, sticky = E, pady = 15)

btn_limpar = Button(janela, text = "Parar/Limpar", width = 10, height = 2, bg = "cyan", command = limpar)
btn_limpar.grid(column = 3, row = 6, sticky = W, pady = 15)

janela.mainloop()