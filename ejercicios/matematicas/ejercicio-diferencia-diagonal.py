# Ejercicio de diferencia diagonal

rango_matriz = 3
matriz = []


for posicion in range(rango_matriz):
	entrada = input("Escribe tres numeros separados por espacios, pulsa enter al terminar:")
	matriz.append(entrada.split(" ")


def diferencia_diagonal (matriz):
	diagonal_principal = 0
	diagonal_secundaria = 0
	posicion = 0
	if matriz > 0 and es_matriz_cuadrada(matriz):
		for fila in len(matriz):
			diagonal_principal += fila[0]
			diagonal_secundaria += fila[-1]
		
	else: 
		print ("La matriz no es cuadrada o está vacía")
	

def es_matriz_cuadrada (matriz)
	filas = len(matriz)
	columnas = 
