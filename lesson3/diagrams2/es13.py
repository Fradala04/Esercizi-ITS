x_val:int = int(input("Inserire x positiva: "))
y_val:int = int(input("Inserire una y positiva: "))
z_val:int = int(input("Inserire una z posititva: "))
if x_val+y_val+z_val % 2 == 0 and x_val % 3 == 0 and y_val % 5 == 0 and z_val % 7 == 0:
    print("Regole rispettate")
else:
    print("Regole non rispettate")