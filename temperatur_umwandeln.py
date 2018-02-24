# Datei celsius.txt lesen

with open("C:\\users\\tmgDefaultProfile\\Desktop\\celsius.txt", "r") as datei:
    inhalt_der_datei = datei.read()
werte = inhalt_der_datei.split("\n")[:-1]
print(werte)

# jeden Celsius-Wert in Fahrenheit umwandeln

neue_datei = open("C:\\users\\tmgDefaultProfile\\Desktop\\fahrenheit2.txt", "w")
neue_datei.write("Hallo Welt!")

for wert in werte:
    neuer_wert = int(wert) * 1.8 + 32
    print(neuer_wert)
    neue_datei.write(str(neuer_wert) + "\n")
    

# Werte in fahrenheit.txt schreiben
