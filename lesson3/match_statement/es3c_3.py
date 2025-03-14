oggetti:list = []
for i in range (3):
    inserimento = (input("Inserire oggetto: "))
    oggetti.append (inserimento)
print(oggetti)
match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale didattico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")