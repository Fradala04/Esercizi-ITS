lista_pizza:list[str] = ["Margherita","Diavola","Quattro formaggi"]
for i in lista_pizza:
    print(i)

# metodo for alternativo
# for i in range(,len(pizza)):
# print(f"Mi piace la {pizza[i]}")

for i in lista_pizza:
    print(f"Mi piace la {i}")

print("Mi piace un sacco la pizza")
friend_pizzas:list[str] = ["Margherita","Diavola","Quattro formaggi"]
lista_pizza.append("Capricciosa")
friend_pizzas.append("Boscaiola")
for i in lista_pizza:
    print(f"My favorite pizzas are {lista_pizza[0:4]}")
for i in friend_pizzas:
    print(f"My favorite pizzas are {friend_pizzas[0:4]}")