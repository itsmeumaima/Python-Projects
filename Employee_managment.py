from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pyodbc

m=Tk()
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

def display():
    con=pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                        r'DBQ=E:\Database4.accdb;'))
    cursor1=con.cursor()
    cursor1.execute("select * from emp")
    rows=cursor1.fetchall()
    if len(rows)!=0:
        for i in rows:
            stable.insert('',END,values=i)


def add():
    con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=E:\Database4.accdb;'))
    cursor1=con.cursor()
    cursor1.execute(f"Insert into emp(empno,empname,Address,deptID) values ('{v1.get()}','{v2.get()}','{v3.get()}','{v4.get()}')")
    cursor1.commit()
    display()
    messagebox.showinfo("One record has been added")
    con.close()

def delete():
    con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=E:\Database4.accdb;'))
    cursor1=con.cursor()
    cursor1.execute(f"DELETE FROM emp where empno={v1.get()}")
    cursor1.commit()
    display()
    messagebox.showinfo("One record has been deleted")
    con.close()

def update():
    con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=E:\Database4.accdb;'))
    cursor1 = con.cursor()
    cursor1.execute(f"UPDATE emp set address='{v3.get()}' WHERE empno={v1.get()}")
    cursor1.commit()
    display()
    messagebox.showinfo("One record has been updated")
    con.close()

l=Label(m,text="Employee Management System",bg="black",fg="white",font=("Bold",26))
l.pack(side=TOP,fill=X)
f=Frame(m,bg="light blue")
f.place(x=0,y=55,width=450,height=700)

l1=Label(f,bg="dark blue",fg="white",text="Emp no",font=("Ariel",15),width=10,bd=5)
l1.place(x=20,y=100)

l2=Label(f,bg="dark blue",fg="white",text="Emp name",font=("Ariel",15),width=10,bd=5)
l2.place(x=20,y=170)

l3=Label(f,bg="dark blue",fg="white",text="Address",font=("Ariel",15),width=10,bd=5)
l3.place(x=20,y=240)

l4=Label(f,bg="dark blue",fg="white",text="Dept ID",font=("Ariel",15),width=10,bd=5)
l4.place(x=20,y=310)

e1=Entry(f,bg="white",fg="black",textvariable=v1,bd=10,width=15)
e1.place(x=200,y=100)

e2=Entry(f,bg="white",fg="black",textvariable=v2,bd=10,width=15)
e2.place(x=200,y=170)

e3=Entry(f,bg="white",fg="black",textvariable=v3,bd=10,width=15)
e3.place(x=200,y=240)

e4=Entry(f,bg="white",fg="black",textvariable=v4,bd=10,width=15)
e4.place(x=200,y=310)


b1=Button(text="Display",bg="pink",fg="black",width=15,command=display)
b1.place(x=30,y=480)

b2=Button(text="Delete",bg="pink",fg="black",width=15,command=delete)
b2.place(x=30,y=530)

b3=Button(text="Insert",bg="pink",fg="black",width=15,command=add)
b3.place(x=170,y=480)

b4=Button(text="Update",bg="pink",fg="black",width=15,command=update)
b4.place(x=170,y=530)

f2=Frame(m,bg="white")
f2.place(x=450,y=55,width=950,height=700)

stable=ttk.Treeview(f2,height=650,columns=('emp no','emp name','Address','dept ID'))
stable.pack()

m.mainloop()