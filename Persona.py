class Persona:
    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe Persona)
    Le informazioni saranno:
    - nome
    - cognome
    - età
    
    come li rappresento in Python?

    self.name:str (attributo di tipo stringa)
    self,lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo int)

    '''

    # costruttore della classe Persona
    def __init__(self, name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    # funzione che mostri in output tutti i dati di una persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEta': {self.age}")

fd = Persona("Francesco", "D'alascio", 20)

print(fd)

# mostra i dati di una persona  
fd.displayData()