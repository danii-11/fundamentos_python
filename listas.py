# Listas

# Indice     0             1           2
listas = ["objeto_1", "objeto 2", "objeto_3"]
print(type(listas))

# Lista de aprendices sena ADSo

aprendices = ["Daniela", "Santiago", "Juan","Simon", "Valentina", "Sofia"]

# Acceder un elemento de la lista
print(aprendices[1])

# Modificar un elemento de la lista

aprendices[1] = "Daniel"
print(aprendices)

lista_mixta = ["Daniela", 3.14, 18, True, [1,2,3]]

#consultar rango de elementos de la lista
print(aprendices[0:2]) #imprime desde el indice 0 hasta el indice 1
print(aprendices[:2]) #imprime desde el indice 0 hasta el indice 2
print(aprendices[2:4]) #imprime desde el indice 2 hasta el final de la lista
print(aprendices[2:5]) #imprime desde el indice 2 hasta el final de la lista
print(aprendices[2:1]) #imprime desde el indice 2 hasta el final de la lista

#contatenar listas

aprendices_ficha_3321349 = ["Andres", "Daniela", "Sebastian", "Accosta", "Simon"]
aprendices_ficha_3256784 = ["Camilo", "Sofia", "Valentina", "Juan", "Maria","Daniela"]

aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_3256784
print(aprendices_adso)

# Listas con extend 

aprendices_ficha_3321349.extend(aprendices_ficha_3256784)
print(aprendices_ficha_3321349)

# Medir el rango con len()

print(len(aprendices_ficha_3321349))

# Contar elementos con count()

count_Daniela = aprendices_adso.count("Daniela")
print(f"El nombre Daniela aparece {count_Daniela} veces en la lista")

# Obtener el indice de un elemento con index

indice_maria = aprendices_adso.index("Maria")
print(f"El nombre Maria se encuentra en el indice {indice_maria} de la lista aprendices")

# Copiar una lista con copy()

nueva_lista_adso = aprendices_adso.copy()
print(nueva_lista_adso)

# Agregar un elemento a la lista (append e insert)

nueva_lista_adso.append("Sofia")
print(nueva_lista_adso)

nueva_lista_adso.insert(1, "Paola")
print(nueva_lista_adso)

# Eliminar elementos (pop, remove)

nueva_lista_adso.remove("Sebastian")
print(nueva_lista_adso)

nueva_lista_adso.pop(3)
print(nueva_lista_adso)

# Comprobar pertenencia (in)

if "Daniela" in nueva_lista_adso:
    print("Daniela esta en la lista de aprendices ADSO")
else:
    print("Daniela no esta en la lista de aprendices ADSO")

# Ordenar (sort y reverse)

nueva_lista_adso.sort()
print(nueva_lista_adso)

nueva_lista_adso.reverse()
print(nueva_lista_adso)

nueva_lista_adso.clear()
print(nueva_lista_adso)