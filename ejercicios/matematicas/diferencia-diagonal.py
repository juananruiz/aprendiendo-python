# diferencia-diagonal.py
# Las diagonales de la matriz son las que van de la esquina superior izquierda a la esquina inferior derecha y de la esquina superior derecha a la esquina inferior izquierda.
# La diferencia diagonal es la diferencia entre la suma de los valores de la diagonal principal y la suma de los valores de la diagonal secundaria.
# Esta operación es un ejercicio clásico de programación

#Probemos con una matriz de 3x3
rango_matriz = 3
matriz = []
diagonal_principal = 0
diagonal_secundaria = 0
posicion = 0
for fila in range(rango_matriz):
  entrada = input("Escribe " + str(rango_matriz) + " números separados por espacios y pulsa enter: ")
  matriz.append(entrada.split(" "))
  diagonal_principal += int(matriz[fila][posicion])
  diagonal_secundaria += int(matriz[fila][rango_matriz - 1 - posicion])
  posicion += 1
print("Matriz: " + str(matriz))
print("Diagonal principal: " + str(diagonal_principal))
print("Diagonal secundaria: " + str(diagonal_secundaria))
print("Diferencia diagonal: " + str(abs(diagonal_principal - diagonal_secundaria)))
