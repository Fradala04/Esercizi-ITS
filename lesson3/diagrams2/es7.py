somma = 0
i = 0
option: str = None
while True:
    option = str(input("vuoi inserire un voto ? : "))
    if option == "no":
        break
    if (option != "si") and (option != "no"):
        print("errore")
    else:
        if option == "si":
            voto = int(input("inserisci voto: "))
            i+=1
            somma = somma + voto
            media = somma / i
print(media)
