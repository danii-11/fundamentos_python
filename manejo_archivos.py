# Open(nombre, modo) -> Funcion de python manipular archivos

# R (read) -> Leer un archivo
# W (write) -> Escribir un archivo 
# X (create) -> Crear un nuevo archivo (genera error si el archivo ya existe)

# Leer un archivo del sistema

try:
    file = open("archivo.txt", "r")
    print(file.readline()) # Lee la primera linea del archivo
    file.close() # Cierra el archivo
except FileNotFoundError:
    print("Error: El archivo no existe")

# Uso del with para no cerrar el archivo manualmente

try:
    with open("archivo.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("Error: El archivo no existe")


# Sobrescribir un archivo del sistema

try:
    with open("archivo.txt", "w") as file:
        file.write("Texto sobrescrito")
    with open("archivo.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("Error: El archivo no existe")


# Agregar contenido a un archivo del sistema

try:
    with open("archivo.txt", "a") as file:
        file.write("\nTexto agregado")
    with open("archivo.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: El archivo no existe")

# Crear un nuevo archivo del sistema

try:
    with open("archivo_2.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    open("archivo_2.txt", "x") # Crea un nuevo archivo
    print("Error: El archivo no existe")

#Creacion de un codigo html en un archivo del sistema

def crear_html(script_html):
    try:
        with open("archivo_2.html", "w") as file:
            print(file.readline())
    except FileNotFoundError:
        open("archivo_2.html", "x")
        print("Archivo no encontrado")
        
    #escribir el codigo html en un archivo del sistema
    try:
        with open("archivo_2.html", "w") as file:
            file.write(script_html)
        with open("archivo_2.html", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Archivo no encontrado")