def calcular_contagiados(argumentos):

    dias_faltantes = D - 1
    potencia = 2 ** dias_faltantes
    total_contagiados = C * potencia

    return total_contagiados

if __name__ == "__main__":
    
    C = int(input("Ingresa el número de contagiados actuales de Covid-19 en NuncaLandia: "))
    D = int(input("Ingresa el número de días para predecir el número de contagiados: "))

    total_contagiados = calcular_contagiados(C, D)

    print (f"El número total de contagiados después de {D} días será {total_contagiados}")
