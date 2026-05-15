# Primer punto

canciones = ["Imitadora", "Koko", "Enseñame a bailar", "Hilito", "Me rehuso"]

# Segundo punto

canciones.append("Me voy enamorando")
print(canciones)

canciones.insert(2,"Playa marina")
print(canciones)

nueva_lista = ["Bonus Track 1", "Bonus Track 2"]
nueva_lista.extend(canciones)
print(nueva_lista)

# Tercer punto

print("tercer")
nueva_lista.remove("Hilito")
print(nueva_lista)

nueva_lista.pop(-1)
print(nueva_lista)

# Cuarto punto

print(4)
nueva_lista.sort()
print(nueva_lista)

# Quinto punto

print(f"Se encuentran {len(nueva_lista)} canciones en la playlist")

print(f"La primera cancion que agregue se encuentra en el indice {nueva_lista.index("Playa marina")}")

print(f"El string Bonus Track 1 aparece {nueva_lista.count("Bonus Track 1")} vez en la lista")

