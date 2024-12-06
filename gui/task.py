from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("OpenClose")

def check_opened():
    if lbl2:
        lbl2.destroy()

def open():
    check_opened()
    global lbl2 
    lbl2 = Label(window, text="Opened", bg="lightgrey", fg="#182024", font=("Jokerman", 9))
    lbl2.place(x=100,y=200)
def closed():
    try:
        lbl2.destroy()
    except:
        print("Label Not found")


lbl2 = None
btnOpen = Button(window, text="Open", command=open)
btnClose = Button(window, text="Close", command=closed)
btnClose.place(x=60,y=20)
btnOpen.place(x=10,y=20)

window.mainloop()
