n = int(input("inserisci un valore intero positivo: "))
i = 1
divisibili = 0
if n < 0:
    print("errore")
else:
    while i <=10:

        v = int(input("inserisci numero: "))
        i+=1
        if (n % v == 0):
            divisibili+=1
print(divisibili)



