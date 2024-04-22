def elevar_cuadrado (base : float, potencia : float) -> float:

    if potencia == 0:
        return 1
    
    elif potencia == 1:
        return base
    
    else :
        return base * elevar_cuadrado(base, potencia - 1)
    
if __name__ == "__main__":

    base = float(input("Ingrese la base: "))
    potencia = float(input("Ingrese la potencia: "))

    resultado = elevar_cuadrado(base, potencia)
    print(f"El resultado de {base} elevado a la {potencia} es: {resultado}")