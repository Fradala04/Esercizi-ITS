età = int(input("inserisci l'età: "))
if (età >= 18) and (età <= 65):
    print("puoi partecipare all'attività")
if (età < 18):
    print("non puoi partecipare all'attività, sei minorenne")
if (età > 65):
    print("non puoi partecipare  all'attività, sei Over 65")
    
