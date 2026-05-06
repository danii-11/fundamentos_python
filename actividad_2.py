# Calculadora de notas
print("-" * 45)

print("Calculadora de notas")

print("-" * 45)

# Se le solicita al usuario que ingrese su nombre y tus notas, se convierte en float

nombre = input("Ingrese su nombre: ")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))


# Condicional que permite mirar que promedio tiene el usuario
# sale un aviso de error si el usuario ingresa un numero mayor a 5.0



if nota1 > 5.0 or nota2 > 5.0 or nota3 > 5.0:
    print("Error: debes poner una nota menor o igual a 5.0")
else:
    print("-" * 45)
    print("Sus notas ingresadas son:")
    print("Primera nota:", nota1)
    print("Segunda nota:", nota2)
    print("Tercera nota:", nota3)
    print("-" * 45)

    promedio = (nota1 + nota2 + nota3) / 3
    puntos_faltantes = 5.0 - promedio

    print("El promedio de tus notas es:", round(promedio, 2))
    print("Puntos para llegar a 5.0:", round(puntos_faltantes, 2))
    print("-" * 45)

    if promedio <= 2.9:
        print(nombre, "usted fue reprobado:", round(promedio, 2))
        print("Nivel de desempeño: Bajo")

    elif promedio >= 3.0 and promedio < 4.5:
        print(nombre, "usted ha sido aprobado:", round(promedio, 2))
        print("Nivel de desempeño: Alto")

    else:
        print(nombre, "has tenido un desempeño superior:", round(promedio, 2))
        print("Felicitaciones")

print("-" * 50)