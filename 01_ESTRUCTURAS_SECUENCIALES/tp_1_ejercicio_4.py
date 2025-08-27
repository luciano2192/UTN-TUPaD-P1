import math

print("Vamos a calcular el area y perimetro de un circulo, para eso ingresa los siguientes datos: ");

radio = int(input("Ingresa el radio del circulo: "));

area = math.pi * radio ** 2;
perimetro = 2 * math.pi * radio;

print(f"El area del circulo es : {area}");
print(f"El perimetro del circulo es : {perimetro}");