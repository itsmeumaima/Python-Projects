from tkinter import *
from datetime import date
from tkinter import messagebox
from tkinter import ttk
import pyodbc
m=Tk()
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v_1=StringVar()
v_2=StringVar()
v_3=StringVar()
m.title("Student Registration System")
m.geometry("1280x750")

m.config(bg="#06283D")

def insert(v1,v3,v5,v2,v4,v_1,v_2,v_3):
    con=pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                        r'DBQ=E:\student management system.accdb;'))
    cursor1=con.cursor()
    cursor1.execute(f"INSERT INTO student(Name,Class,Gender,DateofBirth,Course,Fathername,Mothername,Fatheroccupation) values ('{v1}','{v3}','{v5}','{v2}','{v4}','{v_1}','{v_2}','{v_3}')")
    cursor1.commit()
    messagebox.showinfo("One record has been added")
    con.close()
def delete():
    con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=E:\student management system.accdb;'))
    cursor1=con.cursor()
    cursor1.execute(f"DELETE FROM student where Name={v1.get()} and Fathername={v_1.get()}")
    cursor1.commit()
    messagebox.showinfo("One record has been deleted")
    con.close()

l=Label(m,text="Student Registration System",fg="white",bg="#c36464",font=("bold",20))
l.pack(side=TOP,fill=X)

# b1=Button(m,text="Display",bg="light blue",fg="black",relief=SUNKEN,width=15,height=3)
# b1.place(x=990,y=160)
b2=Button(m,text="Insert",bg="light pink",fg="black",relief=SUNKEN,width=15,height=3,command=lambda: insert(e1.get(),e3.get(),e5.get(),e2.get(),e4.get(),e_1.get(),e_2.get(),e_3.get()))
b2.place(x=990,y=270)
b2=Button(m,text="Delete",bg="light green",fg="black",relief=SUNKEN,width=15,height=3,command=delete)
b2.place(x=990,y=380)


f=Frame(bg="light grey",width=800,height=250)
f.place(x=50,y=70)
l1=Label(f,text="Student Detail",fg="black",font=("bold",14))
l1.place(x=30,y=20)
l3=Label(f,text="Full name:",bg="light grey",fg="black")
l3.place(x=30,y=60)
e1=Entry(f,bg="white",fg="black",textvariable=v1,relief=SUNKEN)
e1.place(x=150,y=60)

l4=Label(f,text="Date of Birth:",bg="light grey",fg="black")
l4.place(x=30,y=100)
e2=Entry(f,bg="white",fg="black",textvariable=v2,relief=SUNKEN)
e2.place(x=150,y=100)

l5=Label(f,text="Class:",bg="light grey",fg="black")
l5.place(x=320,y=60)
e3=Entry(f,bg="white",fg="black",textvariable=v3,relief=SUNKEN)
e3.place(x=430,y=60)

l6=Label(f,text="Course:",bg="light grey",fg="black")
l6.place(x=320,y=100)
e4=Entry(f,bg="white",fg="black",textvariable=v4,relief=SUNKEN)
e4.place(x=430,y=100)

l7=Label(f,text="Gender:",bg="light grey",fg="black")
l7.place(x=30,y=160)
e5=Entry(f,bg="white",fg="black",textvariable=v5,relief=SUNKEN)
e5.place(x=150,y=160)

f1=Frame(bg="light grey",width=800,height=250)
f1.place(x=50,y=370)
l2=Label(f1,text="Parents Detail",fg="black",font=("bold",14))
l2.place(x=30,y=20)

l_3=Label(f1,text="Father name:",bg="light grey",fg="black")
l_3.place(x=30,y=80)
e_1=Entry(f1,bg="white",fg="black",textvariable=v_1,relief=SUNKEN)
e_1.place(x=150,y=80)

l_4=Label(f1,text="Mother name:",bg="light grey",fg="black")
l_4.place(x=330,y=80)
e_2=Entry(f1,bg="white",fg="black",textvariable=v_2,relief=SUNKEN)
e_2.place(x=450,y=80)

l_5=Label(f1,text="Father occupation:",bg="light grey",fg="black")
l_5.place(x=200,y=140)
e_3=Entry(f1,bg="white",fg="black",textvariable=v_3,relief=SUNKEN)
e_3.place(x=350,y=140)
m.mainloop()
