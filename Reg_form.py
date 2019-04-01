from tkinter import *

import pymysql

root=Tk()
root.geometry("500x500")
root.title("Registration Form")

s= StringVar()
f= StringVar()
m= StringVar()
e=StringVar()

def database():
    s_name = s.get()
    f_name = f.get()
    Mob = m.get()
    email = e.get()
    connection=pymysql.connect("localhost", "root", "rajat@123", "homework")
    cursor=connection.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS reg(StudentName varchar(50), FatherName varchar(50), MobNo char(12), email varchar(100)')
    cursor.execute("INSERT INTO reg VALUES('%s', '%s', '%s', '%s')"%(s_name, f_name, Mob, email))
    connection.commit()
    connection.close()
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

l0=Label(text="Registration Form", width=20, font=("bold",20))
l0.place(x=80,y=50)

l1=Label(text="Student Name", width=20, font=("bold",15))
l1.place(x=55,y=125)

e1=Entry(textvariable=s)
e1.place(x=240,y=130)

l2=Label(text="Father Name", width=20, font=("bold",15))
l2.place(x=55,y=175)

e2=Entry(textvariable=f)
e2.place(x=240,y=180)

l3=Label(text="Mob No.", width=20, font=("bold",15))
l3.place(x=55,y=225)

e3=Entry(textvariable=m)
e3.place(x=240,y=230)

l4=Label(text="Email", width=20, font=("bold",15))
l4.place(x=55,y=270)

e4=Entry(textvariable=e, width=30)
e4.place(x=240,y=275)

b1=Button(root,text="SUBMIT",bg="red",command=database,width=15)
b1.place(x=220,y=345)

root.mainloop()
























