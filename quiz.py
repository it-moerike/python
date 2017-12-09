print("\033[92mHerzlich willkommen zum Quiz!\033[0m\n")

punkte = 0

print("Welcher bekannte Turm steht in Paris?")
print("a) Eiffelturm")
print("b) Turm von Pisa")
print("c) Fernsehturm")

antwort1 = input("Antwort: ")
if antwort1 == "a":
    print("\033[92m✔️ Richtig ✔️\033[0m")
    punkte += 1
else:
    print("\033[91m✖️ Falsch ✖️\033[0m")

print("\n\033[95mPunkte: " + str(punkte) + "\033[0m")
