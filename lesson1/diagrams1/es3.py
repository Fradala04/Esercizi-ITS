# Inizializzazione delle variabili
sum_value:float = 0.0
cont:int = 0

# Ciclo per 5 iterazioni
while True:
    n = float(input("Inserisci un numero: "))  # Legge il numero
    if n > 0:  # Se il numero è positivo, lo aggiunge alla somma
        sum_value += n
    cont += 1  # Incrementa il contatore
    if cont == 5:
        break

# Stampa il risultato
print("La somma dei numeri positivi è:", sum_value)