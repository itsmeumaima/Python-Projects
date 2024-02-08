import cv2

from tkinter import*
import math

def click(value):
    answer=""
    ex=entryfield.get()
    try:
        if value=="C":
            ex=ex[0:len(ex)-1]
            entryfield.delete(0,END)
            entryfield.insert(0,ex)

        elif value=='CE':
            entryfield.delete(0,END)

        elif value=="π":
            answer=math.pi

        elif value=="√":
            answer=math.sqrt(eval(ex))

        elif value=="cos":
            answer=math.cos(math.radians(eval(ex)))

        elif value=="sin":
            answer=math.sin(math.radians(eval(ex)))

        elif value=="tan":
            answer=math.tan(math.radians(eval(ex)))

        elif value=="cosh":
            answer=math.cosh(eval(ex))

        elif value=="sinh":
            answer=math.sinh(eval(ex))

        elif value=="tanh":
            answer=math.tanh(eval(ex))

        elif value=="e":
            answer=math.e

        elif value=="x3":
            answer=eval(ex)**3

        elif value=="x²":
            answer=eval(ex)**2

        elif value=="∛":
            answer=eval(ex)**(1/3)

        elif value=="ln":
            answer=math.log2(eval(ex))

        elif value=="deg":
            answer=math.degrees(eval(ex))

        elif value=="rad":
            answer=math.radians(eval(ex))

        elif value=="!":
            answer=math.factorial(eval(ex))

        elif value=="/":
            entryfield.insert(END,"/")
            return

        elif value=="=":
            answer=eval(ex)

        else:
            entryfield.insert(END,value)
            return

        entryfield.delete(0, END)
        entryfield.insert(0, answer)

    except SyntaxError:
        pass

root=Tk()
root.title("Scientific Calculator")
root.config(bg="black")
root.geometry("440x640")


entryfield=Entry(root,bg="light blue",fg="black",font=("Ariel",18),relief=SUNKEN,bd=10,width=20)
entryfield.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

button_text_list=["C","CE","deg","rad","π","cos","tan","sin","ln","x3",
                  "cosh","sinh","tanh","x²","∛","7","8","9","-",
                  "/","4","5","6","+","√","1","2","3","*","e",
                  "0",".","=","%","!"]
row_value=1
column_value=0
for i in button_text_list:
    button=Button(root,text=i,bg="grey",fg="white",font=("Ariel",18),width=5,height=2,relief=SUNKEN,command=lambda button=i: click(button))
    button.grid(row=row_value,column=column_value,padx=4,pady=4)
    column_value+=1
    if column_value>4:
        row_value+=1
        column_value=0



root.mainloop()