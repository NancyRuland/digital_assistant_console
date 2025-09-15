#Einkaufsliste (eigenes Projekt)

meine_liste = []
fehlversuche = 0

#User fragen ob hinzufügen oder entfernen oder beenden:
while len(meine_liste) < 100 :
    
    eingabe = input("Möchtest Du ein Produkt hinzufügen (+), entfernen (-) oder Programm beenden (b) ?")
    if eingabe == "+":
        produkt = input("Gib das Produkt ein, dass der Einkaufsliste hinzugefügt werden soll: ")
        meine_liste.append(produkt)
        for produkt in meine_liste:
            print("Einkaufen: ",produkt)
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
        
        
        
            

  
