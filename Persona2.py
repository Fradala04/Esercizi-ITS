class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0
    
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEta': {self.age}")
    
    def setName(self, name:str) -> None:
        self.name = name

    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

    def setAge(self, age:int) -> None:
        if age > 0 or age < 130:
            self.age = 0
        else:
            self.age = age
    
        


# crea un oggetto di tipo Persona
fm:Persona = Persona()  

# stampa i dati della Persona creata
fm.displayData()

# Imposta il nome di una persona
fm.setName("Francesco")

# Imposta il cognome di una persona
fm.setLastname("D'Alascio")



fm.displayData()
