from tkinter import *
import sqlite3
connec = sqlite3.connect('abc.db')

def insert():
  '''''  print("user id ", user_id)
    print('password', password)
    print('first name', first_name)
    print('last name', last_name)
    print('gender', var)
    print('email', email)
    print("registration form  seccussfully created...")

    if (user_id.get() == "" and pass_id.get() == "" and firs.get() == "" and form_no_field.get() == "" and contact_no_field.get() == "" and email_id_field.get() == "" and address_field.get() == ""):
        print('empty input')'''

  print("registration form  seccussfully created...")
  print('email', function.user_id)






def function():
    root=Tk()
    root.geometry("500x580")
    root.title("Student Registration form")

    label_0 = Label(root, text="Student Registration form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)

    #first name
    label_1 = Label(root, text="First name", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    first_name = Entry(root)
    first_name.place(x=240, y=130)

    # last name
    label_2 = Label(root, text="Last name", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    last_name = Entry(root)
    last_name.place(x=240, y=180)

    # user name
    label_3 = Label(root, text="User id", width=20, font=("bold", 10))
    label_3.place(x=68, y=230)
    user_id = Entry(root)
    user_id.place(x=240, y=230)

    # password
    label_4 = Label(root, text="password", width=20, font=("bold", 10))
    label_4.place(x=68, y=280)
    password = Entry(root)
    password.place(x=240, y=280)

    #gender
    label_5 = Label(root, text="Gender", width=20, font=("bold", 10))
    label_5.place(x=70, y=330)
    var = IntVar()
    Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=330)
    Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=330)

    # contact no.
    label_6 = Label(root, text="Contact Number", width=20, font=("bold", 10))
    label_6.place(x=68, y=380)
    con_num = Entry(root)
    con_num.place(x=240, y=380)

    # reg_type
    label_7 = Label(root, text="Reg_type", width=20, font=("bold", 10))
    label_7.place(x=68, y=430)
    reg_type = Entry(root)
    reg_type.place(x=240, y=430)

    #email
    label_8 = Label(root, text="Email", width=20, font=("bold", 10))
    label_8.place(x=68, y=480)
    email = Entry(root)
    email.place(x=240, y=480)

    Button(root, text='Submit', width=20, bg='brown', fg='white',command=insert).place(x=180, y=530)
    # it is use for display the registration form on the window
    root.mainloop()


function()
