""" 
Ordenamiento por selección
---
Nota didáctica: esta implementación es correcta, con un matiz

Funciona bien, pero usa una variante ligeramente distinta a la clásica:
- **Clásica**: intercambias el mínimo con la posición actual dentro de la misma lista (`lista[i], lista[j] = lista[j], lista[i]`), sin crear una lista nueva.
- **Esta versión**: extrae el mínimo con `pop()` y lo vas acumulando en `lista_ordenada`, una lista nueva.

Ambas son válidas y correctas; esta es más fácil de entender pero tiene un coste extra: `list.pop(j)` en una posición que no es el final es **O(n)** (tiene que desplazar los elementos), así que es ligeramente menos eficiente que la clásica, aunque la complejidad total sigue siendo **O(n²)** en ambos casos.
"""

frutas = ["pera", "sandia", "melón", "naranja", "plátano", "manzana", "piña", "melocotón", "albaricoque", "fresa"]

def extraer_menor(lista):
	print(lista) # Esto es solo para ver como va disminuyendo la lista original
	j = 0
	for i in range(len(lista)):
		if lista[i] < lista[j]:
			j = i
	return lista.pop(j)

def ordenar_secuencial(lista):
	lista_ordenada = []
	for i in range(len(lista)):
		lista_ordenada.append(extraer_menor(lista))
	print(lista_ordenada)

if __name__ == "__main__":
	ordenar_secuencial(frutas)