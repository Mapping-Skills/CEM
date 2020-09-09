from tkinter import messagebox
import sqlite3


def login_successful():
    # put after login fuction @nupur
    print("Login")


def login(username, password):

    conn = sqlite3.connect('test5.db')
    c = conn.cursor()
    c.execute("SELECT username,password from DETAILS WHERE username = ? ", (username,))
    data = c.fetchall()

    if len(data) != 0:
        if data[0][0] == username and data[0][1] == password:
            login_successful()
        else:
            messagebox.showinfo("Invalid Details", "Username Or Password Wrong")

    else:
        messagebox.showinfo("Invalid Details", "Username Or Password Wrong")

    c.close()
    conn.close()
