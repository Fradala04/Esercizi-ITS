nome:str = str(input("Inserire il tuo nome: "))
genere:str = str(input("Inserire il tuo genere: "))
match genere:
    case "m":
        print(f"{nome}, Maschio")
    case "f":
        print(f"{nome}, Femmina")
    case _:
        print(f"Errore, non è possibile generare un documento di identità.")