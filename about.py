from tkinter import *
def abut():
    top=Tk()
    top.geometry("1700x1700")
    top.title("about")
    top.configure(bg='blue')
    v0=(" Feroze Gandhi Institute of Professional Studies")
    v1=("\n\n* Feroze Gandhi Institute of Professional Studies is a premier institute, established with a vision to develop world class technical professionals.") 
    v2=("* FGIPS having a spectacular campus of 22.5 acre with several conspicuous features.")
    v3=("* It Offers an amiable, verdant and eco-friendly atmosphere to the students and fosters them to be more meditative, veracious and focused.")
    v4=("* Feroze Gandhi Institute of Professional Studies is a premier institute, established with a vision to produce the best technical professionals.")
    v5=("* FGIPS has a spectacular campus of 22.5 acre with several conspicuous features.")
    v6=("* It offers an amiable, verdant and eco-friendly atmosphere to students in order to make them more meditative, veracious and focused.")
    v7=("* Besides state-of-the-art Library and Computer Centre FGIPS also offers best residential facility for its students.")
    v8=("* The spacious campus includes recreation room, indoor-outdoor game facility, round the clock electric power supply and round the clock available reading facilities.")
    v9=("\n\nFounded:-2017\nSpecialties:-BBA and BCA \nAddress:- Ratapur, Rae Bareli, Uttar Pradesh")
    l0=Label(top,font=("Courier New",30,"bold"),text=v0,fg="black",bg="red")
    l0.grid(row=0,column=0)    
    l1=Label(top,font=("Comic Sans Ms",15,"bold"),text=v1,fg="black",bg="blue")
    l1.grid(row=5,column=0)
    l2=Label(top,font=("Comic Sans Ms",15,"bold"),text=v2,fg="black",bg="blue")
    l2.grid(row=6,column=0)
    l3=Label(top,font=("Comic Sans Ms",15,"bold"),text=v3,fg="black",bg="blue")
    l3.grid(row=7,column=0)
    l4=Label(top,font=("Comic Sans Ms",15,"bold"),text=v4,fg="black",bg="blue")
    l4.grid(row=8,column=0)
    l5=Label(top,font=("Comic Sans Ms",15,"bold"),text=v5,fg="black",bg="blue")
    l5.grid(row=9,column=0)
    l6=Label(top,font=("Comic Sans Ms",15,"bold"),text=v6,fg="black",bg="blue")
    l6.grid(row=10,column=0)
    l7=Label(top,font=("Comic Sans Ms",15,"bold"),text=v7,fg="black",bg="blue")
    l7.grid(row=11,column=0)
    l8=Label(top,font=("Comic Sans Ms",15,"bold"),text=v8,fg="black",bg="blue")
    l8.grid(row=12,column=0)
    l9=Label(top,font=("Comic Sans Ms",15,"bold"),text=v9,fg="red",bg="yellow")
    l9.grid(row=13,column=0)
    top.mainloop()