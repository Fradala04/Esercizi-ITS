##############WHILE#####################
# Legge il primo valore
max_value:float = float(input("Inserisci il primo numero: "))
cont:int = 1

while cont < 4:
    cont += 1  # Incrementa contatore
    n:float = float(input("Inserisci un numero: "))  # Legge il numero
    if n > max_value:  # Controlla se è maggiore
        max_value = n
print("Il massimo valore è:", max_value)

##############REPEAT#####################
# Legge il primo valore
max_value:float = float(input("Inserisci il primo numero: "))
cont:int = 1

while True:
    n:float = float(input("Inserisci un numero: "))  # Legge il numero
    if n > max_value:  # Controlla se è maggiore
        max_value = n
    cont += 1  # Incrementa contatore
    if cont == 4:  # Condizione di uscita
        break
print("Il massimo valore è:", max_value)

##############CICLO FOR#####################
# Legge il primo valore
max_value:float = float(input("Inserisci il primo numero: "))

for i in range(3):  # Il ciclo si ripete 3 volte
    n:float = float(input("Inserisci un numero: "))  # Legge il numero
    if n > max_value:  # Controlla se è maggiore
        max_value = n
print("Il massimo valore è:", max_value)