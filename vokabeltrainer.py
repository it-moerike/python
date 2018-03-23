from tkinter import filedialog
from tkinter import *


fenster = Tk()
fenster.title("Vokabeltrainer")


def dateiname_erfragen():
    dateiname = filedialog.askopenfilename()
    return dateiname


def vokabeln_auslesen(dateiname):
    vokabelliste = []
    datei = open(dateiname, "r")

    for zeile in datei.readlines():
        vokabel = {
            "frage": zeile.split(": ")[0],
            "antwort": zeile.split(": ")[1].replace("\n", "")
        }
        vokabelliste.append(vokabel)

    return vokabelliste


def weiter(a=None):
    global aktuelle_vokabel

    if lösung_eingabefeld.get().lower() == v[aktuelle_vokabel]["antwort"].lower():
        aktuelle_vokabel += 1
        frage_textfeld["text"] = v[aktuelle_vokabel]["frage"]

        lösung_eingabefeld.delete(0, END)
        lösung_eingabefeld.insert(0, "")


dateiname = dateiname_erfragen()
v = vokabeln_auslesen(dateiname)
aktuelle_vokabel = 0

vokabelliste_textfeld = Label(text="Vokabelliste: " + dateiname)
frage_textfeld = Label(text=v[aktuelle_vokabel]["frage"], font=("", 20))
lösung_eingabefeld = Entry(font=("", 20))
button = Button(text="Weiter", command=weiter)

vokabelliste_textfeld.pack()
frage_textfeld.pack()
lösung_eingabefeld.pack()
button.pack()

fenster.bind("<Return>", weiter)

fenster.mainloop()
