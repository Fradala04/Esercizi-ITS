n1:int = int(input("Inserisci il valore di n1: "))
n2:int = int(input("Inserisci il valore di n2: "))
p = 1
for i in range(n1,n2+1):
    p*=i
if n1>=n2:
    p=n1*n2
print(f"il prodotto tra i numeri è {p}")