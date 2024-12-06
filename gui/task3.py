from tkinter import *

window = Tk()

window.geometry("1920x1080")
window.title("Entry Box")
# ent = Entry(window, width=20)

# ent.place(x=20, y=10)
valx=100
valy=100
list1 = ["Name","age","Number","EmailId","College","Course","Usn","Gender"]
list2 = list1
for i in list1:  
    lbl2 = Label(window, text=i, bg="lightgrey", fg="#182024", font=("Jokerman", 9))
    lbl2.place(x=valx, y=valy)
    # valx += 50
    valy +=50
valx=200
valy=100
for i in range(len(list1)):
    list1[i] = Entry(window, width=20)
    list1[i].place(x=valx, y=valy)
    # valx
    valy+=50
    
def send():
    for i in range(len(list1)):
        print(f"{list2[i]} : {list1[i].get()}")
        list1[i].delete(0,END)


btn = Button(window, text="Send", command=send)
btn.place(x=150, y=valy+50)


window.mainloop()
