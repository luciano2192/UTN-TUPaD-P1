import math

# Ejercicio 1:
print("Hola Mundo!");

# Ejercicio 2:
nombre_ejer_2 = input("Ingresa tu nombre: ");
print(f"Hola {nombre_ejer_2}!");

# Ejercicio 3:
nombre_ejer_3 = input("Ingresa tu nombre: ");
apellido_ejer_3 = input("Ingresa tu apelldo: ");
edad_ejer_3 = int(input("Ingresa tu edad: "));
residencia_ejer_3 = input("Lugar de residencia: ");
print(f"Soy {nombre_ejer_3} {apellido_ejer_3}, tengo {edad_ejer_3} años y vivo en {residencia_ejer_3}");

# Ejercicio 4:
print("Vamos a calcular el area y perimetro de un circulo, para eso ingresa los siguientes datos: ");

radio_ejer_4 = int(input("Ingresa el radio del circulo: "));

area_ejer_4 = math.pi * radio_ejer_4 ** 2;
perimetro_ejer_4 = 2 * math.pi * radio_ejer_4;

print(f"El area del circulo es : {area_ejer_4}");
print(f"El perimetro del circulo es : {perimetro_ejer_4}");

# Ejercicio 5:
print("Vamos a calcular la cantidad de horas equivalentes a los segundos que ingreses");

segundos_ejer_5 = int(input("Ingresa los segundos: "));

horas_ejer_5 = segundos_ejer_5 / 3600;

print(f"{segundos_ejer_5} segundos equivalen a {horas_ejer_5} hora/s.");

# Ejercicio 6:
print("Vamos a mostrarte la tabla de multiplicacion del numero que quieras");

numero_ejer_6 = int(input("Ingresa un numero: "));

for i_ejer_6 in range (1,11):
    multiplicacion_ejer_6 = numero_ejer_6 * i_ejer_6;
    print(f"{numero_ejer_6} x {i_ejer_6} = {multiplicacion_ejer_6}");

# Ejercicio 7:
primerNum_ejer_7 = int(input("Ingresa el primer numero entero distinto de 0: "));
segundoNum_ejer_7 = int(input("Ingresa el segundo numero entero distinto de 0: "));

print(f"El resultado de sumarlos es: {primerNum_ejer_7+segundoNum_ejer_7}");
print(f"El resultado de dividirlos es: {primerNum_ejer_7/segundoNum_ejer_7}");
print(f"El resultado de multiplicarlos es: {primerNum_ejer_7*segundoNum_ejer_7}");
print(f"El resultado de restarlos es: {primerNum_ejer_7-segundoNum_ejer_7}");

# Ejercicio 8:
altura_ejer_8 = float(input("Ingresa tu altura: "));
peso_ejer_8 = float(input("Ingresa tu peso: "));

indiceMasaCorporal_ejer_8 = peso_ejer_8 / altura_ejer_8 ** 2;

print(f"Tu indice de masa corporal es: {indiceMasaCorporal_ejer_8}");

# Ejercicio 9:
tempCelsius_ejer_9 = float(input("Ingresa la temperatura en grados celsius: "));

tempFar_ejer_9 = tempCelsius_ejer_9 * 9/5 + 32;

print(f"{tempCelsius_ejer_9}°C equivalen a {tempFar_ejer_9}°F");

# Ejercicio 10:
print("Vas a poder ingresar tres numeros para calcular el promedio.");

numeros_ejer_10 = [];

# Pido los valores en un bucle y los agrego al array. 
# Se podria haber solucionado con tres variables y pedir con input el valor.
for i_ejer_10 in range(3):
    num_ejer_10 = float(input(f"Ingresa el numero {i_ejer_10+1}: "));
    numeros_ejer_10.append(num_ejer_10);

promedio_ejer_10 = sum(numeros_ejer_10) / len(numeros_ejer_10);

print(f"El promedio de los numeros {numeros_ejer_10} es: {promedio_ejer_10}");