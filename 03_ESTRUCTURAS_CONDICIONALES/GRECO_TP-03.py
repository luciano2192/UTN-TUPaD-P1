#EJERCICIO 1
edad = int(input("Ingresa tu edad: "))
edad_max = 18

if (edad > edad_max) :  
    print("Es mayor de edad")

#EJERCICIO 2
nota = float(input("Ingresa tu nota: "))
nota_max = 6

if (nota >= nota_max) :  
    print("Aprobado") 
else:   
    print("Desaprobado")

#EJERCICIO 3
num = float(input("Ingresa un numero par: "))
es_par = num%2

if (es_par == 0) :  
    print("Ha ingresado un número par") 
else:   
    print("Por favor, ingrese un número par")

#EJERCICIO 4
edad = int(input("Ingresa tu edad: "))

ninio_max = 12
adolescente_max = 18
adulto_joven_max = 30

if ( edad < ninio_max ) :  
    print("Niño/a: menor de 12 años.") 
elif ( edad >= ninio_max and edad < adolescente_max ) :   
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif ( edad >= adolescente_max and edad < adulto_joven_max ) : 
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif ( edad > adulto_joven_max ) :  
    print("Adulto/a: mayor o igual que 30 años.")

#EJERCICIO 5
user_pass = input("Ingresa una contraseña entre 8 y 14 caracteres: ")

min_len = 8
max_len = 14

pass_dentro_del_rango = len(user_pass) >= min_len and len(user_pass) <= max_len

if ( pass_dentro_del_rango ) :  
    print("Ha ingresado una contraseña correcta.")
else :  
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#EJERCICIO 6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

calc_mean = mean(numeros_aleatorios)
calc_mode = mode(numeros_aleatorios)
calc_median = median(numeros_aleatorios)

print(f"Los numeros utilizados para el calculo son: {numeros_aleatorios}")
print(f"La media es: {calc_mean}")
print(f"La mediana es: {calc_median}")
print(f"La moda es: {calc_mode}")

if ( calc_mean > calc_median and calc_median > calc_mode ) :    
    print("Sesgo positivo")
elif ( calc_mean < calc_median and calc_median < calc_mode ) :  
    print("Sesgo negativo")
elif ( calc_mean == calc_median == calc_mode ) :  
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#EJERCICIO 7
import re

frase = input("Ingresa una frase o palabra: ")

#obtengo el ultimo caracter de la cadena
ultimo_caracter = frase[-1]

# uso el modulo "re" para evaluar la expresion regular con las vocales
es_vocal = bool(re.match(r'[aeiouAEIOU]', ultimo_caracter))

if ( es_vocal ) :
    print(f"{frase}!")
else :
    print(frase)

#EJERCICIO 8
nombre = input("Ingrese solo su nombre: ")

print("Teniendo en cuenta las siguientes opciones, ingrese el numero de opcion que desee.")
print("Opción 1: Si quiere su nombre en mayúsculas.")
print("Opción 2: Si quiere su nombre en minúsculas.")
print("Opción 3: Si quiere su nombre con la primera letra mayúscula.")

opcion = int(input("Ingrese el numero de la opcion que desee: "))

if ( opcion == 1 ) :
    print(nombre.upper())
elif ( opcion == 2 ) :
    print(nombre.lower())
elif ( opcion == 3 ) :
    print(nombre.title())
else :
    print("Opción incorrecta.")

#EJERCICIO 9
mag_terremoto = int(input("Ingrese la magnitud del terremoto: "))

if ( mag_terremoto < 3 ) :
    print("Muy leve")
elif ( mag_terremoto >= 3 and mag_terremoto < 4 ) :
    print("Leve")
elif ( mag_terremoto >= 4 and mag_terremoto < 5 ) :
    print("Moderado")
elif ( mag_terremoto >= 5 and mag_terremoto < 6 ) :
    print("Fuerte")
elif ( mag_terremoto >= 6 and mag_terremoto < 7 ) :
    print("Muy Fuerte")
elif ( mag_terremoto >= 7 ) :
    print("Extremo")

#EJERCICIO 10
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if (hemisferio == "N"):  # Hemisferio Norte
    if ((mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20)):
        estacion = "Invierno"
    elif ((mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20)):
        estacion = "Primavera"
    elif ((mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20)):
        estacion = "Verano"
    elif ((mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20)):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif (hemisferio == "S"):  # Hemisferio Sur
    if ((mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20)):
        estacion = "Verano"
    elif((mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20)):
        estacion = "Otoño"
    elif ((mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20)):
        estacion = "Invierno"
    elif ((mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20)):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "un hemisferio inválido"

print(f"Estás en {estacion}.")