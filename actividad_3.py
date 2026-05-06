#Actividad 3: Clasificador de indice de masa corporal

print("=" * 50)
print("Clasificador de IMC")
print("=" * 50)

# Le pide al usuario que ingrese su nombre, su peso y su altura

nombre = input("Ingrese tu nombre: ")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print("-" * 50)


# Se hace un condicion que si se pone una altura y un peso menos de
# cero se imprimira un error y se acabara el programa


if peso <= 0 or altura <= 0:
    print("Error: El peso y la altura deben ser mayores a cero.")
    exit()
print("-" * 50)

# Este condicional mostrara que clasificacion de peso tiene

if imc < 18.5:
    print(nombre, "tu IMC es: ", round(imc,2))
    print("Clasificación: Bajo peso")
elif imc >= 18.5 and imc < 24.9:
    print(nombre, "tu IMC es: ", round(imc,2))
    print("Clasificación: Peso normal")
elif imc >= 25 and imc < 29.9:
    print(nombre, "tu IMC es: ", round(imc,2))
    print("Clasificación: Sobrepeso")
else:
    print(nombre,"tu IMC es: ", round(imc,2))
    print("Clasificación: Obesidad")
print("-" * 50)