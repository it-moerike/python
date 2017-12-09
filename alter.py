# Eingabe
deutsch = input("Deutschnote? ")
mathe = input("Mathenote? ")
englisch = input("Englischnote? ")

# Verarbeiung
durchschnittsnote = (int(deutsch) + int(mathe) + int(englisch)) / 3

# Ausgabe
print("Deine Durchschnittsnote ist " + str(durchschnittsnote))
