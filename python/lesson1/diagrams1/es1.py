# Leggi a e b
a:float = float(input("Inserisci il valore di a: "))
b:float = float(input("Inserisci il valore di b: "))

# Controlla la condizione a > b
if a > b:
    c:float = (a**2 - b**2) ** (1/2)
    print("Il valore di c è:", c)
else:
    print("Errore")