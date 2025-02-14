tutor = 10

studenti_in_attesa = 40

while studenti_in_attesa < 50:
    studente = str(input("inserisci il nome dello studente: "))
    
    
    if tutor > 0:
        print("tutor assegnato")
        tutor-=1
    else:
        studenti_in_attesa+=1
        print("studente inserito nella sala d'attesa")

