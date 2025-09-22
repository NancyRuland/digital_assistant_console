
#Hier beginnt der Taschnrechner
#Eingabe
#Zahl1 = z1
#Zahl2 = z2

print("Herzlich Willkommen im Taschenrechner!")
fehlversuche = 0

while True:
    if fehlversuche >= 3:
        print("Zu viele Falscheingaben. Programm wird beendet.")
        pass
    
    try:
        z1 = int(input("Gib eine Zahl ein: " ))
        
    except ValueError:
        fehlversuche = fehlversuche + 1
        print("Ungültige Eingabe! Bitte Zahl eingeben:")
        continue    
    rechenzeichen = input("Gib ein Rechenzeichen ein (+, -, *, /)")              
    try:
        z2 = int(input("Gib eine Zahl ein: "))
         
    except ValueError:
        fehlversuche = fehlversuche + 1
        print("Ungültige Eingabe! Bitte Zahl eingeben:")
        continue
       #Verarbeitung
#Rechenweg ausführen    
    if rechenzeichen not in ["+", "-", "*", "/"]:
        fehlversuche = fehlversuche +1
        print("Ungültige Eingabe! Gib +, -, *, /, ein!")
        continue
    elif rechenzeichen == "+":
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
        
    print("Das Ergebnis ist: " , ergebnis)
   
    #Ausgabe
#Das Ergebniss ist
    

#Merke:
# "if" = wenn   ":" = dann
#Zeilen müssen richtig angeordnet sein bsp. exit() beendet das program immer
#wenn nicht unter richtig (hier unter else) angeordnet