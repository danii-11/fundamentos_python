def funcion():
   
   return print("Hola, soy una función")

#llamamos a la función
funcion()

#funcion  con parametros
def funcion_con_parametros(nombre):
    return print(f"Hola, soy {nombre}")

funcion_con_parametros("daniel")

# Funcion saludar
def saludar(nombre, apellido, programa = "ADSO"):
    print(f"Hola {nombre} {apellido} del programa {programa}")

#operadores matematicos en funciones

#suma
def suma(a,b): return a + b
print(suma(5,3))

#resta
def resta(a,b): return a - b
print(resta(5,3))

#multiplicacion
def multiplicacion(a,b): return a * b   
print(multiplicacion(5,3))

#division
def division(a,b): return a / b
print(division(5,3))

#validar edad
def clasificar_edad(edad):
    if edad < 18:
        if edad > 12 and edad < 18:
            print("Eres un adolescente")
        else:
            print("Eres un niño")
    else:
        if edad >= 18 and edad < 60:
            print("Eres un adulto")
    
""" edad= int(input("Ingresa tu edad: "))
clasificar_edad(edad) """

#usuarios del sena 
ficha_aprendices_3321349= ["Daniel", "Santiago", "Camilo", "Andres", "Jorge"] 

def mostrar_aprendices(ficha):
    for aprendiz in ficha:
        print(aprendiz)

mostrar_aprendices(ficha_aprendices_3321349)

#funcion para agregar nuevo aprendiz a la ficha
def agregar_aprendiz(ficha, aprendiz):
    ficha.append(aprendiz)
    print(f"Aprendiz {aprendiz} agregado a la ficha")

agregar_aprendiz(ficha_aprendices_3321349, "María") 

#modificatr aprendiz
def modificar_aprendiz(ficha, aprendiz_viejo, aprendiz_nuevo):
    if aprendiz_viejo in ficha:
        index = ficha.index(aprendiz_viejo)
        ficha[index] = aprendiz_nuevo
        print(f"Aprendiz {aprendiz_viejo} modificado a {aprendiz_nuevo}")
    else:
        print(f"Aprendiz {aprendiz_viejo} no encontrado en la ficha")

modificar_aprendiz(ficha_aprendices_3321349, "Camilo", "Ana")

#eliminar aprendiz
def eliminar_aprendiz(ficha, aprendiz):
    if aprendiz in ficha:
        ficha.remove(aprendiz)
        print(f"Aprendiz {aprendiz} eliminado de la ficha")
    else:
        print(f"Aprendiz {aprendiz} no encontrado en la ficha")

eliminar_aprendiz(ficha_aprendices_3321349, "Ana")

#funcion lambda

x = lambda a: a + 10
print(x(5))