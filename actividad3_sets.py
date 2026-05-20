# Análisis de Matrículas del Centro de Formación

# Punto 1
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}
java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}
bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

# Punto 2

# Unión de los tres cursos
total_aprendices = python_curso.union(java_curso).union(bd_curso)
print("Total de aprendices únicos en los tres programas:", len(total_aprendices))

# Aprendices cursando Python y Java simultáneamente
python_java = python_curso.intersection(java_curso)
print("\nAprendices que cursan Python y Java simultáneamente:", python_java)

# Aprendices que solo están en Python
solo_python = python_curso.difference(java_curso).difference(bd_curso)
print("\nAprendices que solo están en Python:", len(solo_python))

# Aprendices que están exactamente en dos programas
dos_programas = (
    (python_curso & java_curso) |
    (python_curso & bd_curso) |
    (java_curso & bd_curso)
) - (python_curso & java_curso & bd_curso)

print("\nAprendices que están exactamente en dos programas:", dos_programas)

# Punto 3
inscripciones = [
    'Ana', 'Luis', 'Ana', 'Marta',
    'Carlos', 'Luis', 'Sofia',
    'Pedro', 'Ana'
]

aprendices_unicos = set(inscripciones)

print("\nAprendices únicos inscritos:", aprendices_unicos)

# Punto 4
# Número de programas a los que está inscrita cada persona

conteo_programas = {}

for aprendiz in aprendices_unicos:
    cantidad = inscripciones.count(aprendiz)
    conteo_programas[aprendiz] = cantidad

print("\nCantidad de inscripciones por aprendiz:", conteo_programas)

# Punto 5 Bonus
# Verificar si hay aprendices inscritos en los tres programas

tres_programas = python_curso & java_curso & bd_curso

if tres_programas:
    print("\nHay aprendices inscritos en los tres programas")
else:
    print("\nNo hay aprendices inscritos en los tres programas")