# Ejercicio creativo: Catalogo de beterinaria

print("-" * 45)
print("Tienda de mascotas 🐾")
print("-" * 45)

print("Catalogo 🧸  \n1. Perro \n2. Conejos \n3. Gatos")
print("-" * 45)

# Variables para que el usuario ingrese los datos

nombre = input("Ingrese el nombre del dueño: ")
opcion = int(input("Ingrese el tipo de mascota que tiene: "))
print("-" * 45)

# Condicional para saber que opcion de servicio desea

if opcion == 1:
    print("Tipo de servicio 📋 \n1. Desparacitacion \n2. Baño \n3. Corte")
    print("-" * 45)
    servicio = int(input("El servicio que eligio fue: "))
    # Dependiendo del servicio cada uno tiene su precio
    if servicio == 1:
        print(nombre,"el valor de la desparasitacion es: 76.000")
        print("-" * 45)
        precio = 76000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)
    elif servicio == 2:
        print(nombre,"el valor del baño es: 50.000")
        print("-" * 45)
        precio = 50000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)
    elif servicio == 3:
        print(nombre,"el valor del corte es: 40.000")
        print("-" * 45)
        precio = 40000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)
    else:
        print(nombre,"esa opción no es valida")

elif opcion == 2:
    print("Tipo de servicio 📋 \n1. Desparacitacion \n2. Baño \n3. Corte")
    print("-" * 45)
    servicio = int(input("El servicio que eligio fue: "))

    if servicio == 1:
        print(nombre,"el valor de la desparasitacion es: 68.000")
        print("-" * 45)
        precio = 68000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)

    elif servicio == 2:
        print(nombre,"el valor del baño es: 36.000")
        print("-" * 45)
        precio = 36000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)

    elif servicio == 3:
        print(nombre,"el valor del corte es: 65.000")
        print("-" * 45)
        precio = 65000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)
    else:
        print(nombre,"esa opción no es valida")

elif opcion == 3:
    print("Tipo de servicio 📋 \n1. Desparacitacion \n2. Baño \n3. Corte")
    print("-" * 45)
    servicio = int(input("El servicio que eligio fue: "))

    if servicio == 1:
        print(nombre,"el valor de la desparasitacion es: 60.000")
        print("-" * 45)
        precio = 60000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)
    elif servicio == 2:
        print(nombre,"el valor del baño es: 57.000")
        print("-" * 45)
        precio = 57000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)
    elif servicio == 3:
        print(nombre,"el valor del corte es: 34.000")
        print("-" * 45)
        precio = 34000
        valor = float(input("Ingrese su dinero: "))
        cambio = int(valor - precio)
        print(nombre,"tu cambio es:", cambio)
    else:
        print(nombre,"esa opción no es valida")
else:
    print(nombre,"la opcion no es valida")