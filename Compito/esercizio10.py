from collections import Counter

lista_number:list[int] = []
somma = 0
num_dispari:int = 0
somma_dispari = 0
while True:
    n:int = int(input("Inserisci un numero (0 per terminare): "))
    if n == 0:
        break
    else:
        lista_number.append(n)
    if n%2==0:
        somma = somma + n
    elif n%2==1:
        num_dispari +=1
        somma_dispari = somma_dispari + n
        med = somma_dispari/num_dispari

    count = 0
    freq = 0
    for i in lista_number:
        if lista_number.count(i) > count:
            count = lista_number.count(i)
            freq = i

    freq_common = 0
    for i in lista_number:
        if lista_number.count(i) > count:
            count = lista_number.most_common(i)
            freq_common = lista_number.most_common(i)

print(lista_number)
print(f"La somma dei numeri pari è {somma}")
print(f"La media dei numeri dispari è {med}")
print(f"Il numero più frequente della lista è {freq}")
print(f"I numeri più frequenti sono {freq}: {freq_common}")