punto_x:int = int(input("Inserire x: "))
punto_y:int = int(input("Inserire y: "))
coordinate:tuple = (punto_x, punto_y)
match coordinate:
    case (0, 0):
        print("Il punto si trova sull'origine.")
    case (0, punto_y):
        print("Il punto si trova sull'asse x.")
    case (punto_x, 0):
        print("Il punto si trova sull'asse y.")
    case (punto_x, punto_y) if punto_x > 0 and punto_y > 0:
        print("Il punto si trova nel primo quadrante.")
    case (punto_x, punto_y) if punto_x < 0 and punto_y > 0:
        print("Il punto si trova nel secondo quadrante.")
    case (punto_x, punto_y) if punto_x < 0 and punto_y < 0:
        print("Il punto si trova nel terzo quadrante.")
    case (punto_x, punto_y) if punto_x > 0 and punto_y < 0:
        print("Il punto si trova nel quarto quadrante.")