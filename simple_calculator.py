from tkinter import *
m=Tk()
m.geometry("350x350")
m.title("Calculator")
def calculate(value):
    answer=""
    ex=e1.get()
    if value=="C":
        e1.delete(0,END)
    elif value=="/":
        e1.insert(END, "/")
        return
    elif value=="=":
        answer = eval(ex)
    else:
        e1.insert(END, value)
        return
    e1.delete(0, END)
    e1.insert(0, answer)
e1=Entry(m,bg="light blue",fg="black",width=25,relief=SUNKEN,font=("Bold",18))
e1.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
b1=Button(text="1",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="1": calculate(button)).grid(row=3,column=0,padx=10,pady=10)
b2=Button(text="2",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="2": calculate(button)).grid(row=3,column=1,padx=10,pady=10)
b3=Button(text="3",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="3": calculate(button)).grid(row=3,column=2,padx=10,pady=10)
b4=Button(text="4",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="4": calculate(button)).grid(row=4,column=0,padx=10,pady=10)
b5=Button(text="5",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="5": calculate(button)).grid(row=4,column=1,padx=10,pady=10)
b6=Button(text="6",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="6": calculate(button)).grid(row=4,column=2,padx=10,pady=10)
b7=Button(text="7",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="7": calculate(button)).grid(row=5,column=0,padx=10,pady=10)
b8=Button(text="8",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="8": calculate(button)).grid(row=5,column=1,padx=10,pady=10)
b9=Button(text="9",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="9": calculate(button)).grid(row=5,column=2,padx=10,pady=10)
b10=Button(text="+",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="+": calculate(button)).grid(row=3,column=3,padx=10,pady=10)
b11=Button(text="-",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="-": calculate(button)).grid(row=4,column=3,padx=10,pady=10)
b12=Button(text="*",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="*": calculate(button)).grid(row=5,column=3,padx=10,pady=10)
b13=Button(text="C",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="C": calculate(button)).grid(row=6,column=0,padx=10,pady=10)
b14=Button(text="/",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="/": calculate(button)).grid(row=6,column=1,padx=10,pady=10)
b13=Button(text="=",bg="black",fg="yellow",width=5,font=("Bold",16),command=lambda button="=": calculate(button)).grid(row=6,column=2,padx=10,pady=10)
m.mainloop()
