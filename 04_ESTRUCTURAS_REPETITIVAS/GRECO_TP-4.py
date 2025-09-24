import random

#Ejercicio 1
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (1, 101) :
    print(i)

#Ejercicio 2
#Desarrolla un programa que solicite al usuario un número entero 
# y determine la cantidad de dígitos que contiene.

num_usuario = int(input("Ingresa un número entero: "))

# Si es negativo, lo paso a positivo
num_a_analizar = abs(num_usuario)

cantidad_digitos = 0
while num_a_analizar > 0 :
    num_a_analizar //= 10   # Saco el último dígito
    cantidad_digitos += 1

print(f"Tiene {cantidad_digitos} dígitos.")


#Ejercicio 3
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num_limite_uno = int(input("Ingresa el primer limite: "))
num_limite_dos = int(input("Ingresa el segundo limite: "))

# Aseguramos el orden de los límites
num_menor = min(num_limite_uno, num_limite_dos)
num_mayor = max(num_limite_uno, num_limite_dos)

valores_sumados = 0

for j in range (num_menor+1, num_mayor) :
    valores_sumados += j

print(f"La suma de los números comprendidos entre esos dos valores es: {valores_sumados}")

#Ejercicio 4
#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

acumulado = 0
while (True) : # lo obligo a entrar al while para no duplicar la linea 49
    valor_ingresado = int(input("Ingresa un número entero: "))
    if (valor_ingresado == 0) : break
    acumulado += valor_ingresado

print(f"La suma de los valores ingresados es {acumulado}")

#Ejercicio 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
#Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Genera un número aleatorio entre 0 y 9
num_random = random.randint(0, 9)

cant_intentos = 0
adivino = False

print("Adivina el número entre 0 y 9")

while not adivino: # invierto el valor de "adivino" para que ingrese al while
    numero_usuario = int(input("Ingresa un número: "))
    cant_intentos += 1
    
    if numero_usuario == num_random:
        adivino = True # cambio el valor y al estar negado sale del bucle
    else:
        print("Incorrecto, segui participando...")

print(f"Correcto! El número era {num_random}.")
print(f"Lo lograste en {cant_intentos} intento(s).")

#Ejercicio 6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for k in range(100, -1, -2):
    print(k)

#Ejercicio 7
#Crea un programa que calcule la suma de todos los números comprendidos 
#entre 0 y un número entero positivo indicado por el usuario.

num_entero_positivo = int(input("Ingresa un número entero positivo: "))

if num_entero_positivo < 0:
    print("El número debe ser positivo.")
else:
    suma_total = 0
    for i in range(num_entero_positivo + 1):
        suma_total += i

    print(f"La suma de los números de 0 a {num_entero_positivo} es: {suma_total}")

#Ejercicio 8
#Escribe un programa que permita al usuario ingresar 100 números enteros. 
#Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, 
#cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar 
#una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# cantidad de valores que queremos procesar
cant_num_limite = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cant_num_limite):
    numero_ingresado = int(input(f"Ingrese el número {i+1}: "))
    
    # Contar pares e impares
    if numero_ingresado % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contar positivos y negativos (0 lo dejamos fuera de ambos)
    if numero_ingresado > 0:
        positivos += 1
    elif numero_ingresado < 0:
        negativos += 1

print(f"Resultados después de {cant_num_limite} números:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#Ejercicio 9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, 
#pero debe poder procesar 100 números cambiando solo un valor).

# Número de valores que queremos procesar
cant_num_limite_procesar = 100

suma_total_valores = 0

for i in range(cant_num_limite_procesar):
    num_ingresado = int(input(f"Ingrese el número {i+1}: "))
    suma_total_valores += num_ingresado

# Calculamos la media
media = suma_total_valores / cant_num_limite_procesar

# Mostramos el resultado
print(f"La media de los {cant_num_limite_procesar} números ingresados es: {media}")

#Ejercicio 10
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
#Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_a_invertir = int(input("Ingresa un número entero: "))

es_negativo = numero_a_invertir < 0
num_positivo = abs(numero_a_invertir)

numero_invertido = 0

while num_positivo > 0:
    digito = num_positivo % 10           # sacamos el último dígito
    numero_invertido = numero_invertido * 10 + digito
    num_positivo //= 10                  # eliminamos el último dígito

if es_negativo:
    numero_invertido = -numero_invertido

print(f"El número invertido es: {numero_invertido}")