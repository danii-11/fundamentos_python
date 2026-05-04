#Ejercicio Calculadora

print("Calculadora de Python")
print("Por favor ingrese dos numeros para realizar las operaciones aritmeticas")

Valor1= float (input("Ingresa el primer numero: "))
print(Valor1)
  
Valor2 = float (input("Ingresa el segundo numero: "))
print(Valor2)

print("Ingrese la operacion que desea realizar: \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division: ")

respuesta = int(input("La operacion que desea hacer es: "))

if respuesta == 1:
    resultado = Valor1 + Valor2
    print("El resultado de la suma es: ", resultado)
elif respuesta == 2:
    resultado = Valor1 - Valor2
    print("El resultado de la resta es: ", resultado)
elif respuesta == 3:
    resultado = Valor1 * Valor2
    print("El resultado de la multiplicacion es: ", resultado)
elif respuesta == 4:
    resultado = Valor1 / Valor2
    print("El resultado de la division es: ", resultado)
else:
    print("Opcion no valida, por favor ingrese una opcion del 1 al 4")