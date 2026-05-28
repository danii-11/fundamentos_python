import json

# some JSON
x = '{"nombre": "Daniel", "edad": 30, "profesion": "Analista"}'

#parse x:
y = json.loads(x)

#the result is python dictionay
print(y)

# pythom object (dict)
x = {
    "name": "Daniel",
    "age": 30,
    "city": "Duitama"
}

# convertir a json
y = json.dumps(x)

# the result is json
print(y)
