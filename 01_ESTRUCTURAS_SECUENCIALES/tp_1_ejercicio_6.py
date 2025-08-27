print("Vamos a mostrarte la tabla de multiplicacion del numero que quieras");

numero = int(input("Ingresa un numero: "));

for i in range (1,11):
    multiplicacion = numero * i;
    print(f"{numero} x {i} = {multiplicacion}");