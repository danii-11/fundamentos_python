# Condicional if/elif/else

if False:
    print("La condiciones verdadera")
elif False:
    print("La segunda condicion es verdadera en elif")
elif True:
    print("La tercera condicion  es verdadera es elif")
else:
    print("La condiciones falsa")

# Ejercicio: Clasificacion de edad

edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


# Ejercicio: clasificacion de edad if anidado

edad = int(input("Ingresa tu edad: "))

if edad < 18:
    if edad > 12 and edad < 18:
        print("Eres adolescente")
    else:
        print("Eres un niño")
else:
    if edad >= 18 and edad < 60:
        print("Eres un adulto")
    else:
        print("Eres un adulto mayor")

# Operador ternario

numero = 4

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

print("El numero es par" if numero % 2 == 0 else "El numero es impar")

