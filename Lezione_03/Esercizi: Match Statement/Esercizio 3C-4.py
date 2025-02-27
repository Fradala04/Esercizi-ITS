mammiferi:list = []
rettili:list = []
uccelli:list = []
pesci:list = []

animale:str = str(input("Inserire un animale: "))

match animale:
    case "cane"|"gatto"|"cavallo"|"elefante"|"leone":
        print(f"{animale} appartiene alla categoria dei Mammiferi!")
    case "serpente"|"lucertola"|"tartaruga"|"coccodrillo":
        print(f"{animale} appartiene alla categoria dei Rettili!")
    case "aquila"|"pappagallo"|"gufo"|"falco":
        print(f"{animale} appartiene alla categoria degli Uccelli!")
    case "squalo"|"trota"|"salmone"|"carpa":
        print(f"{animale} appartiene alla categoria dei Pesci!")