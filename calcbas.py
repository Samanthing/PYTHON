from tkinter import *

def suma():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1+n2)
    signo.set("+")
    
def resta():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1-n2)
    signo.set("-")
    
def multi():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1*n2)
    signo.set("*")

def div():
    n1=int(num1.get())
    n2=int(num2.get())
    res.set(n1/n2)
    signo.set("/")
    
    
ventana = Tk()
ventana.title("Calculadora operaciones basicas <3")
ventana.geometry("450x275")

num1=StringVar()
num1.set("0")

num2=StringVar()
num2.set("0")

signo=StringVar()
signo.set(" ")

res=StringVar()
res.set("0")

marco_ops=LabelFrame(text='Operacion',fg="tomato",font=("Arial black", 10),relief="groove",bd=3,width=400,height=(72)).place(x=25,y=40)
tit1=Label(marco_ops,fg="pale violet red", text="Numero 1",font=("arial black",8)).place(x=57, y=59)
op=Label(marco_ops,font=("Arial", 22),textvariable=signo).place(x=144, y=67)
tit2=Label(marco_ops,fg="pale violet red", text="Numero 2:",font=("arial black",8)).place(x=197, y=59)
Label(marco_ops, text="=",font=("Arial", 22)).place(x=284, y=67)
tit3=Label(marco_ops,fg="pale violet red", text="Resultado:",font=("arial black",8)).place(x=335, y=59)

marco_oper=LabelFrame(text='Operadores',fg="tomato",font=("Arial black", 10),relief="groove",bd=3,width=400,height=(72)).place(x=25,y=151)
botsuma=Button(marco_oper,text='+',fg="sea green",font=("Arial black", 10), width=8, command=suma).place(x=50,y=174)
botresta=Button(marco_oper,text='-',fg="sea green",font=("Arial black", 10), width=8,command=resta).place(x=144,y=174)
botmulti=Button(marco_oper,text='*',fg="sea green",font=("Arial black", 10), width=8,command=multi).place(x=236,y=174)
botdiv=Button(marco_oper,text='/',fg="sea green",font=("Arial black", 10), width=8,command=div).place(x=330,y=174)

n1=Entry(marco_ops, width=15,textvariable=num1).place(x=41, y=75)
n2=Entry(marco_ops, width=15,textvariable=num2).place( x=181, y=75)
resul=Entry(marco_ops, width=15,textvariable=res).place( x=321, y=75)

Label(ventana, text="Samanthing 2023 <3",fg="dark orchid",font=("Helvetica", 8)).place(x=337, y=240)


ventana.mainloop()
