a = int(input("inserisci a: "))
b= int(input("inserisci b: "))
i = a
somma = 0
if a >= b:
    print("errore")
else:
    while i <= b:
        somma = somma + i
        i+=1
print(somma)

