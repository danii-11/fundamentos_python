# Operadores logicos

#AND

print(True and True) #Si ambos son verdaderos = true
print(True and False) #Si uno es falso = false
print(False and True) #Si uno es falso = false
print(False and False) #Si ambos son falsos = false

#OR
print(True or True) #Si ambos son verdaderos = true
print(True or False) #Si uno es verdadero = true
print(False or True) #Si uno es verdadero = true
print(False or False) #Si ambos son falsos = false

# NOT

print(not True) # Si es verdadero = false
print(not False) # Si es falso = True

# Ejercicio AND

print(5 > 3 and 2 < 4) # true and true = true
print(5 > 3 and 2 > 4) # true and false = false
print(5 < 3 and 2 < 4) # false and true = false
print(5 < 3 and 2 > 4) # false and false = false 

# Ejercicio OR

print(5 > 3 or 2 < 4) # true or true = true
print(5 > 3 or 2 > 4) # true or false = true
print(5 < 3 or 2 < 4) # false or true = true
print(5 < 3 or 2 > 4) # false or false = false

# Ejercicio NOT

print(not 5 > 3) # not true = false
print(not 5 < 3) # not false = true