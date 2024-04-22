if __name__ == '__main__':
    C = float(input("Ingrese el monto del préstamo: "))
    i = float(input("Ingrese la tasa de interés anual: "))
    n = int(input("Ingrese la cantidad de veces que el interés se compone al año: "))
    t = float(input("Ingrese el número de años del préstamo: "))
    resultado = (lambda C, i, n, t : C * (1 + i/n) ** (n*t))(C, i, n, t)
    print(f"El monto total del préstamo es: {resultado}")
    