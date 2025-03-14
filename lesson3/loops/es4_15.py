# Lista delle pizze preferite
lista_pizza: list[str] = ["Margherita", "Diavola", "Quattro formaggi"]
friend_pizzas: list[str] = ["Margherita", "Diavola", "Quattro formaggi"]

# Aggiunta di nuove pizze alle rispettive liste
lista_pizza.append("Capricciosa")
friend_pizzas.append("Boscaiola")

# Stampa delle pizze preferite
print("My favorite pizzas are:")
for pizza in lista_pizza:
    print(f"- {pizza}")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
