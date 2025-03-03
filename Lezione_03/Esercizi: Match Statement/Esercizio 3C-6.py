mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone"]    
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco"]
pesci = ["squalo", "trota", "salmone", "carpa"]

animale:str = input("Inserire nome animale: ")

match animale:
    case animale if animale in mammiferi:
        print("L'animale è un mammifero.")
    case animale if animale in rettili:
        print("L'animale è un rettile.")
    case animale if animale in uccelli:
        print("L'animale è un uccello.")
    case animale if animale in pesci:
        print("L'animale è un pesce.")
    case _:
        print("Il programma non è in grado di classificare l'animale inserito.")

