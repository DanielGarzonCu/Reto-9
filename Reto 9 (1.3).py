if __name__ == "__main__":

    P = int(input("Ingrese el número de panes: "))
    M = int(input("Ingrese el número de bolsas de leche: "))
    H = int(input("Ingrese el número de huevos: "))
    B = int(input("Ingrese el valor del billete en pesitos colombianos: "))
    precio_pan = 3300
    precio_huevo = 350 
    precio_leche = 3300

    cambio = (lambda P, M, H, B, precio_pan, precio_huevo, precio_leche: B - (precio_pan * P + precio_leche * M + precio_huevo * H))(P, M, H, B, precio_pan, precio_huevo, precio_leche)

    print(f"El cambio es: {cambio:.2f} pesitos colombianos.")