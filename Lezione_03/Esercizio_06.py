x = int(input("inserisci il valore di x: "))
i = 1
somma = 0
if x < 0:
    print("errore")
else:
    while i <= 10:
        n = int(input("inserisci numero: "))
        i+=1
        if (x % 2 == 0) and (n > (x / 2)):
            somma = somma + n
        if (x % 2 != 0) and (n < x):
            somma = somma + n
    print(somma)
        
