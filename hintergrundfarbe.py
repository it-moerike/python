# Module importieren
from turtle import Screen, Turtle
from time import sleep

# Bildschirm festlegen
bildschirm = Screen()

# Schildkröte festlegen
fred = Turtle()

# Dauerschleife
while True:
    # Nutzer nach der Farbe fragen
    farbe = input("Farbe: ")

    # Hintergrundfarbe verändern
    bildschirm.bgcolor(farbe)

    # 1 Sekunde warten
    sleep(1)
