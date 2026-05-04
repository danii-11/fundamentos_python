import random
import math

#Operadores aritmeticos

a = 10
b = 5

# Suma
suma = a + b
print(f"Suma: {suma}")

# Resta
resta = a - b
print(f"Resta: {resta}")

# Multiplicacion
multiplicacion = a * b
print(f"Multiplicacion: {multiplicacion}")

# Division
division = a / b
print(f"Division: {division}")

# Division entera
division_entera = a // b
print(f"Division entera: {division_entera}")

# Modulo
modulo = a % b
print(f"Modulo: {modulo}")

# Potencia
potencia = a ** b
print(f"Potencia: {potencia}")

#precencia de operadores 

resultado = a + b * 2
print(f"El resultado de la operacion es: {resultado}")

resultado_2 = (a + b) * 2
print(f"El resultado de la operacion con parentesis es: {resultado_2}")

resultado_3 = a * b // 3
print(f"El resultado de la operacion con potencia es: {resultado_3}")

resultado_4 = (a * b) // 3
print(f"El resultado de la operacion es: {resultado_4}")

resultado_5 = a *( b // 3 )   
print(f"El resultado de la operacion es: {resultado_5}")

resultado_6 = ((a + b) * (a - b) / (a * b)) - ((a ** b) % 3)
print(f"El resultado de la operacion es: {resultado_6}")

print(math.pi)
print(math.e)
print(math.sqrt(16))


random.random()
numero_aleatorio = random.randint(1,10)
print(numero_aleatorio)