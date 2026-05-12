# Primer punto
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# Segundo punto
print(f"La temperatura del primer dia es: {temperaturas[0]}")
print(f"La temperatura del ultimo dia es: {temperaturas[-1]}")
print(f"La temperatura del dia 7 es: {temperaturas[6]}")
print(f"La temperatura del penultimo dia es: {temperaturas[-2]}")

# Tercer punto

print(f"Primera semana {temperaturas[0:7]}")
print(f"Segunda semana {temperaturas[7:14]}")
print(f"Dias pares de la quincena {temperaturas[1::2]}")
print(f"La temperatura en orden invertido {temperaturas[::-1]}")

# Cuarto punto

temperaturas_semana1 = temperaturas[0:7]
temperaturas_semana2 = temperaturas[7:14]
promedio_semana1 = sum(temperaturas_semana1) / len(temperaturas_semana1)
promedio_semana2 = sum(temperaturas_semana2) / len(temperaturas_semana2)

print(f"El promedio de temperatura de la semana 1 es: {promedio_semana1} grados")
print(f"El promedio de temperatura de la semana 2 es: {promedio_semana2} grados")

# Quinto punto

if promedio_semana1 > promedio_semana2:
    print("La semana 1 tuvo un promedio mayor de temperatura que la semana 2.")
elif promedio_semana1 < promedio_semana2:
    print("La semana 2 tuvo un promedio mayor de temperatura que la semana 1.")
else:
    print("Ambas semanas tuvieron el mismo promedio de temperatura.")

