import math

# Ejercicio 1

print("Primer punto")
nombre = "Daniela Rodriguez"
producto = 2000
promedio_asignatura = 4.8

print("Hola", nombre, "el valor de tu pizza es", producto, "y tu promedio de calificaciones es", promedio_asignatura)

# Ejercicio 2

print("Segundo punto")
variable_1_entera = int(input("Ingrese su numero entero:"))
variable_2_entera = int(input("Ingrese otro numero entero:"))
variable_float = float(input("Ingrese un numero decimal:"))
variable_1_string = str(input("Ingrese una palabra:"))
variable_2_string = str(input("Ingrese otra palabra:"))

suma_numeros = variable_1_entera + variable_2_entera + variable_float
print("La suma de los numeros es:", suma_numeros)

numero_mayor = max(variable_1_entera, variable_2_entera)
print("El numero mayor es:", numero_mayor)

print("La divison del numero decimal con el resto de la division entera  es:",variable_float/(variable_1_entera % variable_2_entera))

print("La concatenacion de las dos variables es:",variable_1_string , variable_2_string)

# Ejercicio 3

print("tercer punto")

base = float(input("Ingrese la base para elevar el numero: "))
exponente = float(input("Ingrese un numero para elevar la base: "))
print("El resultado de elevar la base con la potencia es: ", base ** exponente)

# Ejercicio 4

print("Cuarto punto")

operacion_raiz = int(input("Ingrese un numero entero:"))
print("La raiz cuadrada del numero es: ", math.sqrt(operacion_raiz))

# Ejercicio 5

print("Quinto punto")

nombre_estudiante = input("Ingresa tu nombre:")
nota1 = float(input("Ingrese su primera nota:"))
nota2 = float(input("Ingrese su segunda nota:"))
nota3 = float(input("Ingrese su tercera nota:"))
nota4 = float(input("Ingrese su cuarta nota:"))
nota5 = float(input("Ingrese su quinta nota:"))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("Hola", nombre_estudiante, "tu promedio de notas es:", promedio)

# Ejercicio 6

print("Sexto punto")

numeroUno = 8
numeroDos = 2

variable_auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = variable_auxiliar

print("El valor de numeroUno es:", numeroUno)
print("El valor de numeroDos es:", numeroDos)

# Ejercicio 7

print("Septimo punto")
Estado = (5 ==2) or (2>1)
print("El resultado de la operacion es:", Estado)

# Ejercicio 8

print("Octavo punto")
Resultado = (4 / 9) * (3 + 2) + (5 ** 2) + (6 * 3) - (7 % 2)
print("El resultado de la operacion es:", Resultado)

# Ejercicio 9

print("Noveno punto")
ladoCuadrado = 8
areaCuadrado = ladoCuadrado ** 2
perimetroCuadrado = 4 * ladoCuadrado   
print("El area del cuadrado es:", areaCuadrado, "Y el perimetro del cuadrado es:", perimetroCuadrado)

baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8
areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
perimetroTriangulo = baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo
print("El area del triangulo es:", areaTriangulo, "Y el perimetro del triangulo es:", perimetroTriangulo)

baseRectangulo = 8
alturaRectangulo = 6
areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)
print("El area del rectangulo es:", areaRectangulo, "Y el perimetro del rectangulo es:", perimetroRectangulo)

# Ejercicio 10

print("Decimo punto")

edad = int(input("Ingrese su edad: "))

if edad <= 18:    
    if edad >= 0 and edad <= 5:
        print("Eres un Infante")
    elif edad >= 6 and edad <= 10:
        print("Eres un niño")
    elif edad >= 11 and edad <= 15:
        print("Eres un preadolescente")
    elif edad >= 16 and edad <= 18:
        print("Eres un adolescente")
else:
    if edad >= 19 and edad <= 25:
        print("Eres un Pre adulto")
    elif edad >= 26 and edad <= 40:
        print("Eres un adulto")
    elif edad >= 41 and edad <= 55:
        print("Eres un Pre anciano")
    else:
        print("Eres un Anciano")