print("Hello World")

# Tipos de datos

nombre = "Daniela"
apellido = "Rodriguez"
edad = 18
altura = 1.57
activo  = True
telefono = "3106061938"
cedula = "1054285696"

# Castear tipos de datos

telefono_int = int(telefono)
edad_float = float(edad)
altura_int = int(altura)
cedula_str = str(cedula)

print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(telefono), telefono)
print(type(telefono_int), telefono_int)
print(type(edad_float), edad_float)
print(type(altura_int), altura_int)
print(type(cedula_str), cedula_str)     


# Identación en python 
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

# Input
nombre_completo = input("Ingrese su nombre completo... ")
print("Hola ", nombre_completo)

# Imprir con formato f-string
edad_aprendiz = int(input("Ingrese su edad... "))
print(f"Hola {nombre_completo} tienes {edad_aprendiz} años...")
print(type(edad_aprendiz))
