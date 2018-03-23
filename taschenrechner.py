from tkinter import *


def rechnen():
    if operator.curselection() == (0,):
        ausgabe["text"] = float(zahl1.get()) + float(zahl2.get())
    elif operator.curselection() == (1,):
        ausgabe["text"] = float(zahl1.get()) - float(zahl2.get())
    elif operator.curselection() == (2,):
        ausgabe["text"] = float(zahl1.get()) * float(zahl2.get())
    elif operator.curselection() == (3,):
        ausgabe["text"] = float(zahl1.get()) / float(zahl2.get())


window = Tk()
window.title("Taschenrechner")

zahl1 = Entry(window)
operator = Listbox(window)
operator.insert(0, "+")
operator.insert(1, "-")
operator.insert(2, "*")
operator.insert(3, "/")
zahl2 = Entry(window)
button = Button(window, command=rechnen, text="Los", bg='#FBD975')
ausgabe = Label(window)


zahl1.grid(row=0, column=0)
operator.grid(row=0, column=1)
zahl2.grid(row=0, column=2)
button.grid(row=1, column=2, sticky=E)
ausgabe.grid(row=2)

window.mainloop()
