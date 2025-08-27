print("Vas a poder ingresar tres numeros para calcular el promedio.");

numeros = [];

# Pido los valores en un bucle y los agrego al array. 
# Se podria haber solucionado con tres variables y pedir con input el valor.
for i in range(3):
    num = float(input(f"Ingresa el numero {i+1}: "));
    numeros.append(num);

promedio = sum(numeros) / len(numeros);

print(f"El promedio de los numeros {numeros} es: {promedio}");