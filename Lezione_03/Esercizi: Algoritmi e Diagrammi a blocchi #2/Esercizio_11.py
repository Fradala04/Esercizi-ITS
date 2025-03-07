numero:int = int(input("Inserire un numero: "))

if numero % 2 == 0 and numero > 10:
    print("Numero valido.")
elif numero % 2 != 0 and numero < 10:
    print("Numero non valido.")