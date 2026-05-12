# Primer punto
productos = ["cuaderno", "lapiz", "borrador", "esferos", "tijeras", "cartucheras"]

# Segundo punto
precios = [4.500, 1.200, 1.000, 1.800, 2.300, 12.000]

# Tercer punto
cantidad = [7, 5, 3, 10, 12, 20]

# Cuarto punto
cantidad_productos = len(productos)

print("Inventario de la Tienda Escolar:"
      "\nProductos:",productos,
      "\nPrecios:",precios,
       "\nCantidades:",cantidad,
       "\nCantidad de productos:",cantidad_productos)

print(f"El produnto: {productos[0]} tiene un precio de {precios[0]} y una cantidad disponible de {cantidad[0]}")
print(f"El produnto: {productos[1]} tiene un precio de {precios[1]} y una cantidad disponible de {cantidad[1]}")
print(f"El produnto: {productos[2]} tiene un precio de {precios[2]} y una cantidad disponible de {cantidad[2]}")
print(f"El produnto: {productos[3]} tiene un precio de {precios[3]} y una cantidad disponible de {cantidad[3]}")
print(f"El produnto: {productos[4]} tiene un precio de {precios[4]} y una cantidad disponible de {cantidad[4]}")
print(f"El produnto: {productos[5]} tiene un precio de {precios[5]} y una cantidad disponible de {cantidad[5]}")


# Quinto punto
print(type(productos)) # class list

print(type(productos[0])) # class string

