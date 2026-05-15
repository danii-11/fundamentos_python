# Diccionarios

# Creacion  de un diccionario

# Estructura de un diccionario
diccioario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}

# Diccionario Vacio
diccionario_vacio = {}

diccionario_aprendiz = {
    "nombre": "Daniela",
    "apellido": "Rodriguez",
    "programa": "ADSO",
    "ficha": "3321349",
    "edad": 18
}

print(type(diccionario_aprendiz))

# Acceder a los valores de un diccionario
print(diccionario_aprendiz["nombre"])
print(diccionario_aprendiz.get("programa")) 

#  Ontener las claves de un diccionario

print(diccionario_aprendiz.keys())

# Obtener solo los valores de un diccionario
print(diccionario_aprendiz.values())

# Obtener las claves y los valores de un diccionario
print(diccionario_aprendiz.items())

# Agregar un nuevo elemento a un diccionario
diccionario_aprendiz["correo"] = "daniiela.rodriguez112@gmail.com"
print(diccionario_aprendiz)

# Modificar un elemento de un diccionario
diccionario_aprendiz["edad"] = 19
print(diccionario_aprendiz)

# Metodo update (actualizar un diccionario)
diccionario_aprendiz.update({"programa": "Analisis y Desarrollo de Software"})
print(diccionario_aprendiz)

# Comprobar pertenencia 

if "ficha" in diccionario_aprendiz:
    print("La clave 'ficha' existe en el diccionario")  

# Recorrer solo los valores de un diccionario
for valor in diccionario_aprendiz.values():
    print(valor)

# Recorrer solo las claves de un diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)

# Recorrer las claves y los valores de un diccionario
for clave, valor in diccionario_aprendiz.items():
    print(f"Clave: {clave}, Valor: {valor}")  

# Eliminar un elemento de un diccionario
diccionario_aprendiz.popitem()
print(diccionario_aprendiz)

diccionario_aprendiz.pop("programa")
print(diccionario_aprendiz)

diccionario_aprendiz.clear()
print(diccionario_aprendiz)

#  Diccionarios anidados

aprendices = {
    "aprendiz_1": {
        "nombre": "Daniela",
        "apellido": "Rodriguez",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 18
    }, 
    "aprendiz_2": {
        "nombre": "Juan",
        "apellido": "Perez",
        "programa": "ADSO",
        "ficha": "3321350",
        "edad": 20
    },
    "aprendiz_3": {
        "nombre": "Maria",
        "apellido": "Gomez",
        "programa": "ADSO",
        "ficha": "3321351",
        "edad": 19
    }
}

# Acceder a los datos de un diccionario anidado
print(aprendices["aprendiz_1"]["nombre"])
print(aprendices["aprendiz_2"]["apellido"])
print(aprendices["aprendiz_3"]["programa"])

# Recorrer un diccionario anidado
for aprendiz, datos in aprendices.items():
    print(f"Datos del {aprendiz}:")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
    print()


