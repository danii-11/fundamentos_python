# Conjuntos

# Estructura de un conjunto
conjunto = {}
print(type(conjunto)) # Esto no es un conjunto, es un diccionario vacio

# Creacion de un conjunto
lenguajes = {"Python", "Java", "C++", "JavaScript"}
print(type(lenguajes)) # Esto es un conjunto

conjunto_vacio = set() # Esto es un conjunto vacio
print(type(conjunto_vacio))

# Metodos de modificacion de conjuntos
frutas = {"manzana", "banana", "naranja"}

frutas.add("pera") # Agregar un elemento al conjunto
print(frutas)

frutas.remove("banana") # Eliminar un elemento del conjunto
print(frutas)

frutas.discard("uva") # Eliminar un elemento del conjunto sin generar error si no existe
print(frutas)

elem = frutas.pop() # Eliminar un elemento aleatorio del conjunto y devolverlo
print(frutas)

# Verificar pertenencia

print("manzana" in frutas) # Verificar si un elemento pertenece al conjunto
print("banana" in frutas) # Verificar si un elemento pertenece al conjunto

python_devs = {"camila", "juana", "manuela"}
java_devs = {"camila", "sofia", "valentina"}

todos = python_devs.union(java_devs) # Unir dos conjuntos
print("Union:", todos)    

interseccion = python_devs.intersection(java_devs) # Obtener la interseccion de dos conjuntos
print("Intersección:", interseccion)

solo_python = python_devs.difference(java_devs) # Obtener los elementos que estan en un conjunto pero no en el otro
print("Sólo Python:", solo_python)

solo_java = java_devs.difference(python_devs) # Obtener los elementos que estan en un conjunto pero no en el otro
print("Sólo Java:", solo_java)

exclusivos = python_devs.symmetric_difference(java_devs) # Obtener los elementos que estan en un conjunto o en el otro pero no en ambos
print("Exclusivos:", exclusivos)


