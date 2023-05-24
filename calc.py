from tkinter import *
from tkinter import ttk
import math


def Entrada(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == ".":
        ent2.set(ent2.get() + tecla)

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if ent2.get() and not ent1.get():
            ent1.set(ent2.get() + tecla)
            ent2.set("")
        elif ent2.get() and ent1.get():
            calcular()
            ent1.set(ent2.get() + tecla)
            ent2.set("")
    if tecla == "^":
        ent1.set(ent2.get() + "^2")
        res = eval(ent1.get())
        ent2.set(res)


def Entrada2(event):
    tecla = event.char
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        ent2.set(ent2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if ent2.get() and not ent1.get():
            ent1.set(ent2.get() + tecla)
            ent2.set("")
        elif ent2.get() and ent1.get():
            calcular()
            ent1.set(ent2.get() + tecla)
            ent2.set("")
    if tecla == '=' or tecla == '\r':
        calcular()
    if tecla == "^":
        ent1.set(ent2.get() + "^2")
        res = eval(ent1.get())
        ent2.set(res)


def calcular():
    if ent1.get() and ent2.get():
        expresion = ent1.get() + ent2.get()
        resultado = eval(expresion)
        ent2.set(resultado)
        ent1.set("")
        ent1.set("")


def borrar(*args):
    ent2.set(ent2.get()[:-1])


def borrar_todo():
    ent1.set("")
    ent2.set("")


def sqr():
    if ent2.get():
        resultado = math.sqrt(float(ent2.get()))
        ent2.set(resultado)

def pot():
    ent1.set('')
    res = math.pow(float(ent2.get()), 2)
    ent2.set(res)


ventana = Tk()
ventana.title("Calculadora <3")
ventana.geometry("340x365")
ventana.config(cursor="hand2")

ent1 = StringVar()
ent2 = StringVar()

entrada = Entry(ventana, textvariable=ent2, width=32, justify="left", font=("Arial", 12))
entrada.place(x=30, y=10)

botce = Button(ventana, text='CE', fg="HotPink3", font=("Arial black", 10), width=5, command=borrar_todo)
botce.place(x=30, y=87)

botmasmen = Button(ventana, text='+/-', fg="HotPink3", font=("Arial black", 10), width=5)
botmasmen.place(x=86, y=87)

botpot = Button(ventana, text='^2', fg="HotPink3", font=("Arial black", 10), width=5, command=pot)
botpot.place(x=145, y=87)

botback = Button(ventana, text='<<<', fg="HotPink3", font=("Arial black", 10), width=5, command=borrar)
botback.place(x=204, y=87)

botsqr = Button(ventana, text='sqr', fg="HotPink3", font=("Arial black", 10), width=5, command=sqr)
botsqr.place(x=261, y=87)

bot9 = Button(ventana, text='9', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('9'))
bot9.place(x=145, y=134)

bot8 = Button(ventana, text='8', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('8'))
bot8.place(x=86, y=134)

bot7 = Button(ventana, text='7', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('7'))
bot7.place(x=30, y=134)

bot6 = Button(ventana, text='6', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('6'))
bot6.place(x=145, y=182)

bot5 = Button(ventana, text='5', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('5'))
bot5.place(x=86, y=182)

bot4 = Button(ventana, text='4', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('4'))
bot4.place(x=30, y=182)

bot3 = Button(ventana, text='3', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('3'))
bot3.place(x=145, y=230)

bot2 = Button(ventana, text='2', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('2'))
bot2.place(x=86, y=230)

bot1 = Button(ventana, text='1', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('1'))
bot1.place(x=30, y=230)

bot0 = Button(ventana, text='0', fg="HotPink3", font=("Arial black", 10), width=11, command=lambda: Entrada('0'))
bot0.place(x=30, y=278)

botpun = Button(ventana, text='.', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('.'))
botpun.place(x=145, y=278)

botdiv = Button(ventana, text='/', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('/'))
botdiv.place(x=204, y=134)

botporc = Button(ventana, text='%', fg="HotPink3", font=("Arial black", 10), width=5)
botporc.place(x=261, y=134)

botmult = Button(ventana, text='*', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('*'))
botmult.place(x=204, y=182)

botfrac = Button(ventana, text='1/x', fg="HotPink3", font=("Arial black", 10), width=5)
botfrac.place(x=261, y=182)

botmenos = Button(ventana, text='-', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('-'))
botmenos.place(x=204, y=230)

botmas = Button(ventana, text='+', fg="HotPink3", font=("Arial black", 10), width=5, command=lambda: Entrada('+'))
botmas.place(x=204, y=278)

botigual = Button(ventana, text='=', fg="HotPink3", font=("Arial black", 10), width=5, height=4, command=calcular)
botigual.place(x=263, y=225)

Label(ventana, text="Samanthing 2023 <3", fg="dark orchid", font=("Arial Black", 8)).place(x=215, y=340)

ventana.bind('<Key>', Entrada2)
ventana.bind('<KeyPress-b>', borrar)

ventana.mainloop()
