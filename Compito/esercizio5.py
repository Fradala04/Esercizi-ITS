n:int = int(input("Inserisci quanti soldi hai: "))
#ogni baretta si ha un buono sconto ---6 barette = 6 buoni = 1 baretta gratis
if n%6==0:
    print(f"Hai sei buoni hai ottenuto una baretta gratuita, il numero di barrette totali è {n+n/6}")
    print(f"Questi sono i buoni che ti avanzano {n%6}")
else:
    print(f"Questi sono i buoni che ti avanzano {n%6}")