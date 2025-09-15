#Der digitale Assistent
#Ein Projekt das mitwächst, zum Lernen und Erweitern.
# Mögliche Inhalte: Einkaufsliste, Uhrzeit, Taschenrechner, Dateimanager,


#Hier beginnt "Hauptmenü"
fehlversuche = 0
while True:
    
    print("\nHallo, was möchtest Du tun?")
    print("1. Einkaufsliste")
    print("2. Uhrzeit anzeigen")
    print("3. Taschenrechner")
    print("4. Beenden")
    
    auswahl = input("Tippe die zugehörige Ziffer zur Auswahl: ")
    
    if auswahl == "1":
        
# hier beginnt Einkaufsliste (eigenes Projekt)

        meine_liste = []
        fehlversuche = 0
        #def einkaufsliste():
        #User fragen ob hinzufügen oder entfernen oder beenden:
        while len(meine_liste) < 100 :
                
                eingabe = input("Möchtest Du ein Produkt hinzufügen (+), entfernen (-) oder Programm beenden (b) ?")
                if eingabe == "+":
                    produkt = input("Gib das Produkt ein, dass der Einkaufsliste hinzugefügt werden soll: ")
                    meine_liste.append(produkt)
                    print(meine_liste)
                elif eingabe == "-":
                    produkt = input("Gib das Produkt ein, dass aus der Einkaufsliste entfernt werden soll: ")
                    meine_liste.remove(produkt)
                    print(meine_liste)
                elif eingabe == "b":
                    break
                elif fehlversuche >= 2:
                    print("Zu viele Fehlversuche. Programm wird beendet.")
                    break
                
                else:
                    fehlversuche = fehlversuche + 1
                    print("Ungültige Eingabe! Bitte gib (+), (-) oder (b) ein.")
                    pass
        #einkaufsliste()
                    
                







#Hier beginnt Uhrzeit
        
    elif auswahl == "2":
        from datetime import datetime

        # Hole das aktuelle Datum und die aktuelle Uhrzeit
        uhrzeit = datetime.now()
        datum = datetime.now()
        # Uhrzeit formatieren:
        # %H: Stunde (24-Stunden-Format)
        # %M: Minute
        # %S: Sekunde
        aktuelle_uhrzeit = uhrzeit.strftime("%H:%M")
        aktuelles_datum = datum.strftime("%d.%m.%y")
        
        print("\nHeute ist der:", aktuelles_datum)
        print("und es ist:", aktuelle_uhrzeit, "Uhr.")
        
        
        
        
 #Hier beginnt Taschenrechner!!!
            
            
            
            
            
            
            
            
            
        
    elif auswahl == "3":
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
                    
        taschenrechner()  #Funktion aufrufen! def funktion einbauen
        
    
#Ende Taschenrechner!!!
        
        
#Programm beenden
        
    elif auswahl == "4":
        break
    
    elif fehlversuche >= 2:
        print("Zu viele Fehlversuche. Programm wird beendet.")
        break
        

    else:
        fehlversuche = fehlversuche + 1
        print("Ungültige Eingabe!")
        pass 



















        
        
            

  
