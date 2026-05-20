# Primer punto
grupo = {
    321349: {
        "nombre": "Ana",
        "edad": 19,
        "notas": [4.0, 3.5, 4.2, 4.8],
        "ciudad": "Bogotá"
    },

    321350: {
        "nombre": "Luis",
        "edad": 21,
        "notas": [2.5, 3.0, 2.8, 3.2],
        "ciudad": "Medellín"
    },

    321351: {
        "nombre": "Marta",
        "edad": 20,
        "notas": [4.5, 4.7, 4.3, 4.9],
        "ciudad": "Cali"
    },

    321352: {
        "nombre": "Carlos",
        "edad": 22,
        "notas": [3.0, 3.2, 3.1, 2.9],
        "ciudad": "Tunja"
    }
}

# Segundo punto
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Tercer punto
print("Reporte de aprendices\n")

for ficha, datos in grupo.items():

    promedio = calcular_promedio(datos["notas"])

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Ciudad: {datos['ciudad']}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")
    print("----------------------")

# Cuarto punto
grupo[321353] = {
    "nombre": "Sofía",
    "edad": 18,
    "notas": [4.1, 3.9, 4.0, 4.3],
    "ciudad": "Sogamoso"
}

# Actualizar ciudad
grupo[321350]["ciudad"] = "Nueva Ciudad"


# Quinto punto
# Ordenar de mayor a menor promedio
print("\nAprendices ordenados por promedio\n")

aprendices_ordenados = sorted(
    grupo.items(),
    key=lambda x: calcular_promedio(x[1]["notas"]),
    reverse=True
)

for ficha, datos in aprendices_ordenados:
    promedio = calcular_promedio(datos["notas"])

    print(f"{datos['nombre']} - Promedio: {promedio:.2f}")