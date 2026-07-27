# Algoritmo recursivo que usa divide y vencerás para ver cual es la mayor cuadricula que me divide en cuadros iguales una parcela rectangular de ancho "x" y alto "y"

# El caso base es cuando x / y = 2

x = 2850
y = 127

def cuadra_parcela(x, y):
	if x < y:
		x, y = y, x 
	if x / y == 2:
		return x
	else:
		x = x - y
	
