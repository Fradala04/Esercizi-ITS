n:int = int(input("Inserisci la lunghezza delle liste: "))
lista_a:list[int] = []
lista_b:list[int] = []
lista_c:list[int] = []
for i in range(1 ,n+1):
    lista_a.append(i)
    lista_b.append(i)

for i in range(n):
    somma = lista_a[i] + lista_b[n-1]
    i +=1
    n -=1
    lista_c.append(somma)
print(lista_a)
print(lista_b)
print(lista_c)