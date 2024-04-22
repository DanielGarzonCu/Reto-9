# Reto-9
# ¡PYTHON FC!

<details>
  <summary>¡ESCUDO!</summary>
  
  [![PYTHON-F-C-B.jpg](https://i.postimg.cc/1Xpw71f0/PYTHON-F-C-B.jpg)](https://postimg.cc/jnSDC96C)

</details>

# 1
De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
```ruby
# El valor de un prestamo C usando un interes i, compuesto n veces al año durante t años.
if __name__ == '__main__':
    C = float(input("Ingrese el monto del préstamo: "))
    i = float(input("Ingrese la tasa de interés anual: "))
    n = int(input("Ingrese la cantidad de veces que el interés se compone al año: "))
    t = float(input("Ingrese el número de años del préstamo: "))
    resultado = (lambda C, i, n, t : C * (1 + i/n) ** (n*t))(C, i, n, t)
    print(f"El monto total del préstamo es: {resultado}")
    
```
```ruby
# Cantidad de kilos de carne de cierto numero de gallinas, gallos y pollitos
if __name__ == "__main__":
    F = int(input("Ingrese el número de gallinas: "))
    M = int(input("Ingrese el número de gallos: "))
    K = int(input("Ingrese el número de pollitos: "))
    peso_gallina = 6 
    peso_gallo = 7  
    peso_pollito = 1  
    total_carne = (lambda F, M, K, peso_gallina, peso_gallo, peso_pollito : F * peso_gallina + M * peso_gallo + K * peso_pollito)(F, M, K, peso_gallina, peso_gallo, peso_pollito)
    print(f"El total de carne es: {total_carne} kg")
```
```ruby
# "Las vueltas" si compro P numero de panes, M numero de bolsas de leche y H numero de huevos, pagando con un billete de B pesitos colombianos
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
```
# 2
De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
```ruby
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
```
```ruby
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

```
```ruby
def calcular_contagiados(*argumentos):

    dias_faltantes = D - 1
    potencia = 2 ** dias_faltantes
    total_contagiados = C * potencia

    return total_contagiados

if __name__ == "__main__":
    
    C = int(input("Ingresa el número de contagiados actuales de Covid-19 en NuncaLandia: "))
    D = int(input("Ingresa el número de días para predecir el número de contagiados: "))
    total_contagiados = calcular_contagiados(C, D)
    print (f"El número total de contagiados después de {D} días será {total_contagiados}")

```

# 3
Escriba una función recursiva para calcular la operación de la potencia.
```ruby
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
```
# 4
Utilice la siguiente plantilla de code para contar el tiempo:
```ruby
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
```ruby
import time

start_time = time.time()
# Sumatoria de fibonacci con funcion recursiva

def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  

if __name__ == "__main__":
  num = int(input("Ingrese un numero: "))
  serieFibo = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))

end_time = time.time()

timer = end_time - start_time
print(f"tardo {timer} segundos")


start_time = time.time()
# sumatoria de fibonacci usando iteracion

def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  num = int(input("Ingrese el mismo numero: "))
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))

end_time = time.time()

timer = end_time - start_time
print(f"tardo {timer} segundos")

```
Tras probar y probar y volver a probar miramos que apartir de 39 la diferenccia de tiempo se vuelve significativa pues la funcion recursiva tardo 10.040335655212402 segundos mientras que la Iteracion tardo 0.7955052852630615 segundos lo cual a mi parecer ya es una ddiferencia considerable, a partir de aqui la diferencia empeza a ser exponencial y despues de 60 se traba jaja

# 5

Crear cuenta en stackoverflow y adjuntar imagen en el repo

[![Captura-de-pantalla-2024-04-21-232813.png](https://i.postimg.cc/0jygJjxW/Captura-de-pantalla-2024-04-21-232813.png)](https://postimg.cc/xJhpw0XM)

# 6

Cosas de adultos....;) ;) ;)...ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

mi humilde perfil :)

https://www.linkedin.com/in/daniel-garzon-cuasquen-401466305/
