from tkinter import *

# Initialize the main window
window = Tk()
window.geometry("1920x1080")
window.title("Tasks")

# Global variable for the label
lbl2 = None


def check_opened():
    """Destroy the existing label if present."""
    global lbl2
    if lbl2:  
        lbl2.destroy()
        lbl2 = None


def display_text(text):
    """Display a label with the specified text."""
    global lbl2
    check_opened()  
    lbl2 = Label(window, text=text, bg="lightgrey", fg="#182024", font=("Jokerman", 9))
    lbl2.place(x=100, y=200)


def name():
    display_text("Sahil Belurkar")


def age():
    display_text("22")


def place():
    display_text("Login Ware")


def number():
    display_text("9483304516")


def closed():
    """Close the label."""
    check_opened()


# Buttons
btnName = Button(window, text="Name", command=name)
btnAge = Button(window, text="Age", command=age)
btnPlace = Button(window, text="Place", command=place)
btnNumber = Button(window, text="Number", command=number)
btnClose = Button(window, text="Close", command=closed)

# Place buttons
btnName.place(x=10, y=10)
btnAge.place(x=10, y=40)
btnPlace.place(x=10, y=70)
btnNumber.place(x=10, y=100)
btnClose.place(x=10, y=130)

# Run the Tkinter event loop
window.mainloop()
