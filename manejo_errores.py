# Manejo de errores en Python

# Estructura try-except

try:
    print("Hola mundo")
except:
    print("Ocurrió un error")
finally:
    print("Esto sera ejecutado siendo exitoso o no el bloque")

# Ejemplo: convertir o castear dato de entrada del usuario 

try:
    edad_usuario = int(input("Ingresa tu edad: "))
    print(f"Tu edad es: {edad_usuario}")
except ValueError:
    print("Error: Por favor, ingrese solo valores numericos")

# Ejemplo: Variable no definida

# try:
#     print(x)
# except NameError:
#     print("Error: La variable no está definida")

# Ejemplo: División por cero

try:
    numero = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

