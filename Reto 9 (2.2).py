# Promedio multiplipicativo 
def promedio_multiplicativo (*numeros) -> float:
    suma : float = 0
    for num in numeros:
      suma +=  num
    return suma ** 1 / len(numeros)

if __name__ == '__main__':

    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    n4 = float(input("Ingrese el cuarto número: "))
    n5 = float(input("Ingrese el quinto número: "))
    print(f"Promedio multiplicativo de los dos primeros números: {promedio_multiplicativo(n1, n2)}")
    print(f"Promedio multiplicativo de los tres primeros números: {promedio_multiplicativo(n1, n2, n3)}")
    print(f"Promedio multiplicativo de los cuatro primeros números: {promedio_multiplicativo(n1, n2, n3, n4)}")
    print(f"Promedio multiplicativo de los cinco números: {promedio_multiplicativo(n1, n2, n3, n4, n5)}")
