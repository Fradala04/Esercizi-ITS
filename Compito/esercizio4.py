somma = 0
i = 0
massimo:int = 0
minimo:int = 100000000000000000000000
while True:
    n:float = float(input("Inserisci una serie di numeri: "))
    
    if n < 0:
        break

    if n.is_integer() == True:
        somma +=n
        i +=1
        m = somma/i
    if n > massimo:
        massimo = n
    if n < minimo:
        minimo = n
    
print(f"La media tra i numeri interi è {m}")
print(f"Il massimo è {massimo}")
print(f"Il minimo è {minimo}")