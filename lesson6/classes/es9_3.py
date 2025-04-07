class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"Summary: {self.first_name}, {self.last_name}, {self.age}, {self.gender}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}")
        
francesco = User("Francesco", "D'Alascio", 20, "Male")
luca = User("Luca", "D'Ambra", 21, "Male")
silvia = User("Silvia", "Pesce", 21, "Woman")

francesco.describe_user()
francesco.greet_user()

luca.describe_user()
luca.greet_user()

silvia.describe_user()
silvia.greet_user()