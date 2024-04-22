# el promedio de n argumentos 
def promedio (*numeros) -> float:
    sum : float = 0
    for numero in numeros:
        sum += numero
    return sum / len(numeros)
    # La función len() devuelve el numero de elementos usados

if __name__ == "__main__":
    
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    n4 = float(input("Ingrese el cuarto número: "))
    n5 = float(input("Ingrese el quinto número: "))
    print(f"Promedio de los dos primeros números: {promedio(n1, n2)}")
    print(f"Promedio de los tres primeros números: {promedio(n1, n2, n3)}")
    print(f"Promedio de los cuatro primeros números: {promedio(n1, n2, n3, n4)}")
    print(f"Promedio de los cinco números: {promedio(n1, n2, n3, n4, n5)}")
