# Ejemplo de uso de listas en Python

# Crear una lista
frutas = ['manzana', 'plátano', 'naranja', 'pera', 'melón', 'sandía', 'fresa']
print("Lista original:", frutas)

# Acceder al primer y último elemento
print("\nAcceder a elementos:")
print("primer elemento: ", frutas[0], " - último elemento: ", frutas[-1])

# Modificar elementos
frutas[6] = 'granada'
print("\nLista después de modificar:", frutas)

# Añadir elementos
frutas.append('cerezas')
print("\nDespués de añadir un elemento:", frutas)

# Insertar en una posición específica
frutas.insert(2, 'papaya')
print("\nDespués de insertar en posición 2:", frutas)

# Eliminar elementos
fruta_eliminada = frutas.pop(3)

print("\nElemento eliminado:", fruta_eliminada)
print("Lista después de eliminar:", frutas)

# Longitud de la lista
print("\nLongitud de la lista:", len(frutas))

# Ordenar lista
frutas.sort()
print("\nLista ordenada alfabéticamente:", frutas)

# Revertir lista
frutas.reverse()
print("\nLista en orden inverso:", frutas)

# Buscar un elemento y mostrar su posición
fruta_deseada='mango'
if fruta_deseada in frutas:
    posicion = frutas.index(fruta_deseada)
    print("\nLa fruta '{}' está en la posición:".format(fruta_deseada), posicion)
else:
    print("\nLa fruta '{}' no está en la lista.".format(fruta_deseada))

# Comprobar si dos listas son iguales
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

if lista1 == lista2:
    print("\nLas listas son iguales.")
else:
    print("\nLas listas no son iguales.")
