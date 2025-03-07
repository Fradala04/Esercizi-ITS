giorno:int = int(input("inserire giorno: "))
mese:int = int(input("Inserire mese: "))
data:tuple = (giorno, mese)
match data:
    case (1, 1):
        print("Capodanno!")
    case (14, 2):
        print("San Valentino!")
    case (2, 6):
        print("Festa della Repubblica Italiana!")
    case (15, 8):
        print("Ferragosto!")
    case (31, 10):
        print("Halloween!")
    case (25, 12):
        print("Natale!")
    case _:
        print("Nessuna festività importante in questa data!")