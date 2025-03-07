n:int = int(input("Inserire n: "))
for i in range (n):
    x:int = int(input("Inserire x: "))
    y:int = int(input("Inserire y: "))
    if x > 0 and y > 0:
        print(f"{x*y}")
    elif x < 0 or y < 0:
        print(f"{x+y}")