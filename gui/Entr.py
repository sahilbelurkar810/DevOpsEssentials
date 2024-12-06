from tkinter import *

window = Tk()

window.geometry("1920x1080")
window.title("Entry Box")
ent = Entry(window,width=20)

ent.place(x=20,y=10)

def send():
    enter = ent.get()
    labl= Label(window,text=enter)
    labl.place(x=240,y=10)
    print(enter)
    ent.delete(0,END)
    

btn = Button(window,text="Send",command=send)
btn.place(x=180,y=10)


window.mainloop()
