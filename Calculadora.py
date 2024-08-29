#importando o tkinter
from tkinter import *
from tkinter import ttk


#cores
cor1 = "#525252" #cinza escuro
cor2 = "#979c98" #cinza claro
cor3 = "#dedcd7" #branco
cor4 = "#8d6bd1" #roxo

#criado a janela

janela =Tk()
janela.title("calculadora")
janela.geometry("280x350")
janela.config(bg=cor1)

#frames da janela

frame_da_tela =Frame(janela, width=280, height=50, bg=cor2)
frame_da_tela.grid(row=0, column=0)

frame_do_corpo =Frame(janela, width=280, height=300, bg=cor1)
frame_do_corpo.grid(row=1, column=0)

#variavel todos valores

todos_valores = ''

#label
valor_texto =StringVar()

#funcao

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #passando valor para tela
    valor_texto.set(todos_valores)

#funcao calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

#funcao limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

app_label = Label(frame_da_tela, textvariable=valor_texto, width=19, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor1, fg=cor3)
app_label.place(x=0,y=0)


#botoes

b_1 = Button(frame_do_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE )
b_1.place(x=0, y=0)

b_2 = Button(frame_do_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=140, y=0)

b_3 = Button(frame_do_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor4, fg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE) 
b_3.place(x=210, y=0)

b_4 = Button(frame_do_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=60)

b_5 = Button(frame_do_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=70, y=60)

b_6 = Button(frame_do_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=140, y=60)

b_7 = Button(frame_do_corpo, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor4, fg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=210, y=60)

b_8 = Button(frame_do_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=120)

b_9 = Button(frame_do_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=70, y=120)

b_10 = Button(frame_do_corpo, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=140, y=120)

b_11 = Button(frame_do_corpo, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor4, fg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=210, y=120)

b_12 = Button(frame_do_corpo, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=180)

b_13 = Button(frame_do_corpo, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=70, y=180)

b_14 = Button(frame_do_corpo, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=140, y=180)

b_15 = Button(frame_do_corpo, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor4, fg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=210, y=180)

b_16 = Button(frame_do_corpo, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE )
b_16.place(x=0, y=240)

b_17 = Button(frame_do_corpo, command = lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=140, y=240)

b_18 = Button(frame_do_corpo, command = calcular , text="=", width=5, height=2, bg=cor4, fg=cor3, font=("Ivy 14 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=210, y=240)
