import math

def safe_sqrt(number: float) -> float | str:
    """Calcola la radice quadrata di un numero positivo.
    
    Parameters:
    number (float): Il numero di cui calcolare la radice quadrata.

    Returns:
    float | str: La radice quadrata se il numero è positivo, altrimenti un messaggio di errore.
    """
    try:
        return math.sqrt(number)
    except ValueError:
        return "Errore: non è possibile calcolare la radice quadrata di un numero negativo."

# Esempio
print(safe_sqrt(9))
print(safe_sqrt(-1))
