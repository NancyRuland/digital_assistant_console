def taschenrechner():
            print("Herzlich Willkommen im Taschenrechner!")
            
            while True:
                try:
                    z1 = float(input("Gib die erste Zahl ein: "))
                    rechenzeichen = input("Gib ein Rechenzeichen ein (+, -, *, /): ")
                    
                    # Überprüfung des Rechenzeichens
                    if rechenzeichen not in ["+", "-", "*", "/"]:
                        print("Ungültiges Rechenzeichen!")
                        continue

                    z2 = float(input("Gib die zweite Zahl ein: "))

                    # Verarbeitung
                    if rechenzeichen == "+":
                        ergebnis = z1 + z2
                    elif rechenzeichen == "-":
                        ergebnis = z1 - z2
                    elif rechenzeichen == "*":
                        ergebnis = z1 * z2
                    elif rechenzeichen == "/":
                        if z2 == 0:
                            print("Division durch Null ist nicht erlaubt!")
                            continue
                        else:
                            ergebnis = z1 / z2
                    
                    print("Das Ergebnis ist:", ergebnis)

                    weiter_rechnen = input("Möchtest du eine weitere Berechnung durchführen? (j/n): ")
                    if weiter_rechnen.lower() != "j":
                        break

                except ValueError:
                    print("Ungültige Eingabe! Bitte gib eine Zahl ein.")
                    
taschenrechner()