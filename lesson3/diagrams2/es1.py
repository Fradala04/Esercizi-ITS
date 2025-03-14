posti = int(input("inserisci il numero massimo di posti: "))
occupati = 0
option: str = None


while option != "esci":
    option = str(input("inserisci opzione: "))
    if (option != "ingresso") and (option != "uscita") and (option != "stato") and (option != "esci"):
       print("errore")
    else:
        if option == "ingresso":
         if occupati < posti:
                occupati+=1
                posti-=1
         else:
             print("non ci  sono posti disponibili")
         
                
    if option == "uscita":
        if occupati > 0:
                posti+=1
                occupati-=1
        else:
            print("è già tutto libero")
    if option == "stato":
        print(f"i posti occupati sono: {occupati}, mentre quelli liberi sono: {posti}  ")



    
      
    

