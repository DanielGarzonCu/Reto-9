if __name__ == "__main__":
    F = int(input("Ingrese el número de gallinas: "))
    M = int(input("Ingrese el número de gallos: "))
    K = int(input("Ingrese el número de pollitos: "))
    peso_gallina = 6 
    peso_gallo = 7  
    peso_pollito = 1  
    total_carne = (lambda F, M, K, peso_gallina, peso_gallo, peso_pollito : F * peso_gallina + M * peso_gallo + K * peso_pollito)(F, M, K, peso_gallina, peso_gallo, peso_pollito)
    print(f"El total de carne es: {total_carne} kg")