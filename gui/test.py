# import tkinter as tk

from tkinter import*


window=Tk()
print("WIndow is open")
window.geometry("500x600")
window.title("Note Pad")
window.configure(bg="white")

lblbar = Label(window, text="", bg="lightgrey", width=200, font=("Jokerman", 9))
lbl = Label(window, text="File", 
            bg="lightgrey",
            fg="#000000",
            font=("Jokerman",
                   9,
            #       "bold",
            #       "italic",
            #       "underline"
            ),
            justify=LEFT)
# lbl1 = Label(window, text="Edit", bg="lightgrey", fg="#182024", font=("Jokerman", 9))
lbl2 = Label(window, text="View", bg="lightgrey", fg="#182024", font=("Jokerman", 9))
lbl.place(x=10,y=0)
# lbl1.place(x=40,y=0)
lbl2.place(x=70,y=0)
lblbar.place(x=0,y=0)
def add():
    lbl1 = Label(
        window, text="Edit", bg="lightgrey", fg="#182024", font=("Jokerman", 9)
    )
    lbl1.place(x=40, y=0)
btn = Button(window,text="CLick me",command=add)
btn.place(x=430,y=570)

window.mainloop()
