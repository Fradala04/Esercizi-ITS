while True:
    parola:str = (input (f" Inserire parola: "))

    if parola == "fine":
        break
    if parola [0] == parola [-1]:
        print (f" La parola {parola} ha il prino e l'ultimo carattere uguali")
    else:
        print (f" La parola {parola} non ha il primo e l'ultimo carattere uguali")