from tkinter import*
from tkinter import ttk
import math


ventana = Tk()
ventana.title("Calculadora <3")
ventana.geometry("340x365")
ventana.config(cursor="hand2")

entrada=Text(ventana, width=35,height=4).place( x=30, y=10)
ent=StringVar()

def Entrada(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == ".":
        ent2.set(ent2.get() + tecla)
            
    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            ent1.set(ent2.get() + "*")
        elif tecla == "/":
            ent1.set(ent2.get() + "/")
        elif tecla == "+":
            ent1.set(ent2.get() + "+")
        elif tecla == "-":
            ent1.set(ent2.get() + "-")
        if tecla == '=':
            ent1.set(ent1.get() + ent2.get())    
            res= eval(ent1.get())
            ent2.set(res)
            
def Entrada2(event):
    tecla = event.char
    if tecla >='0' and tecla<='9' or tecla =='(' or tecla == ')' or tecla =='.' :
        ent2.set(ent2.get() + tecla)
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla=='-':
        if tecla == '*':
            ent1.set(ent2.get() + '*')
        elif tecla == '/':
            ent1.set(ent2.get() + '/')
        elif tecla == '+':
            ent1.set(ent2.get() + '+')
        elif tecla == '-':
            ent1.set(ent2.get() + '-')
        ent2.set('')
    if tecla == '=':
        ent1.set(ent1.get() + ent2.get())    
        res=eval(ent1.get())
        ent2.set(res)

def sqr():
    ent1.set('')
    res=math.sqrt(float(ent2.get()))
    ent2.set(res)
    
def borrar(*args):
    inicio = 0
    final = len(ent2.get())

    ent.set(ent2.get()[inicio:final-1])

def borrar_todo():

    ent1.set('')
    ent2.set('')

ent1= StringVar()
label_ent1 = ttk.Label(ventana,textvariable=ent1,style="Label1.TLabel")
label_ent1.place(x=120, y=20)

ent2 = StringVar()
label_ent2 = ttk.Label(ventana,textvariable=ent2)
label_ent2.place(x=120, y=20)




botce=Button(ventana,text='CE',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: borrar_todo()).place(x=30,y=87)
botmasmen=Button(ventana,text='+/-',fg="HotPink3",font=("Arial black", 10), width=5).place(x=86,y=87)
botpot=Button(ventana,text='^2',fg="HotPink3",font=("Arial black", 10), width=5).place(x=145,y=87)
botback=Button(ventana,text='<<<',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: borrar()).place(x=204,y=87)
botsqr=Button(ventana,text='sqr',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: sqr()).place(x=261,y=87)
bot9=Button(ventana,text='9',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('9')).place(x=145,y=134)
bot8=Button(ventana,text='8',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('8')).place(x=86,y=134)
bot7=Button(ventana,text='7',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('7')).place(x=30,y=134)
bot6=Button(ventana,text='6',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('6')).place(x=145,y=182)
bot5=Button(ventana,text='5',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('5')).place(x=86,y=182)
bot4=Button(ventana,text='4',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('4')).place(x=30,y=182)
bot3=Button(ventana,text='3',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('3')).place(x=145,y=230)
bot2=Button(ventana,text='2',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('2')).place(x=86,y=230)
bot1=Button(ventana,text='1',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('1')).place(x=30,y=230)
bot0=Button(ventana,text='0',fg="HotPink3",font=("Arial black", 10), width=11,command=lambda: Entrada('0') ).place(x=30,y=278)
botpun=Button(ventana,text='.',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('.')).place(x=145,y=278)
botdiv=Button(ventana,text='/',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('/')).place(x=204,y=134)
botporc=Button(ventana,text='%',fg="HotPink3",font=("Arial black", 10), width=5).place(x=261,y=134)
botmult=Button(ventana,text='*',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('*')).place(x=204,y=182)
botfrac=Button(ventana,text='1/x',fg="HotPink3",font=("Arial black", 10), width=5).place(x=261,y=182)
botmenos=Button(ventana,text='-',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('-')).place(x=204,y=230)
botmas=Button(ventana,text='+',fg="HotPink3",font=("Arial black", 10), width=5, command=lambda: Entrada('+')).place(x=204,y=278)
botigual=Button(ventana,text='=',fg="HotPink3",font=("Arial black", 10), width=5,height=4, command=lambda: Entrada('=')).place(x=263,y=225)

Label(ventana, text="Samanthing 2023 <3",fg="dark orchid",font=("Arial Black", 8)).place(x=215, y=340)


ventana.bind('<Key>',Entrada2)
ventana.bind('<KeyPress-b>',borrar)

ventana.mainloop()