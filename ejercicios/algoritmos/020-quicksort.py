"""
Ejercicio 20 — Quicksort: implementar, particionar in-place y medir

Contexto: en la lección 20 viste la versión "de libro" de quicksort (con
comprehensions, sin mutar nada) y comprobamos con números reales que:
  - con pivote = primer elemento, una lista YA ORDENADA es el peor caso: O(n²)
  - con pivote ALEATORIO, hasta una lista ordenada se comporta como O(n log n)

Aquí vas a escribir tu propia versión desde cero (no copiar el libro),
añadir una partición in-place (más eficiente en memoria que crear listas
nuevas en cada llamada), y reproducir con tu propio código la tabla de
comparaciones de la lección.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

import random


# --- 1. Tu propia versión "de libro" (con comprehensions) ---------------

def quicksort_propio(lista):
    """
    Devuelve una lista NUEVA con los elementos ordenados.
    No debe modificar 'lista'.

    Caso base: listas de 0 o 1 elemento ya están ordenadas.
    Caso recursivo: pivote = primer elemento; separa el resto en menores
    (<=) y mayores (>) con comprehensions; combina
    quicksort_propio(menores) + [pivote] + quicksort_propio(mayores).
    """
    
    if len(lista) < 2:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quicksort_propio(menores) + [pivote] + quicksort_propio(mayores)


# --- 2. Partición in-place (esquema de Lomuto) ---------------------------

def particion_lomuto(lista, bajo, alto):
    """
    Particiona lista[bajo:alto+1] IN-PLACE usando lista[alto] como pivote.
    Al terminar, todos los elementos <= pivote deben quedar a su izquierda
    y todos los > pivote a su derecha, DENTRO del mismo rango.

    Devuelve el índice final donde queda colocado el pivote.

    Pista clásica (esquema de Lomuto):
        pivote = lista[alto]
        i = bajo - 1   # frontera de "elementos <= pivote ya colocados"
        for j in range(bajo, alto):
            if lista[j] <= pivote:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
        return i + 1
    Intenta escribirlo tú antes de mirar la pista de arriba.
    """
    # Escribe aquí tu código
    pass


def quicksort_inplace(lista, bajo=0, alto=None):
    """
    Ordena 'lista' IN-PLACE (no crea listas nuevas) usando
    particion_lomuto(). No devuelve nada relevante: modifica 'lista'.

    Pista: 'alto' por defecto debe ser len(lista) - 1 la primera vez que
    se llama (cuidado con el gotcha del argumento por defecto mutable de
    la lección 011 — aquí 'alto' es un int, no una lista, así que no hay
    trampa, pero sí tienes que inicializarlo dentro de la función si es
    None).

    Caso base: si bajo >= alto, ese trozo ya está ordenado (0 o 1 elementos).
    Caso recursivo: particiona, y llama recursivamente a los dos lados
    del índice del pivote (sin incluirlo, porque el pivote ya está en su
    sitio definitivo).
    """
    # Escribe aquí tu código
    pass


# --- 3. Medir comparaciones: pivote fijo vs. aleatorio -------------------

def quicksort_contando(lista, aleatorio=False):
    """
    Versión de quicksort_propio() que además CUENTA comparaciones.

    Devuelve una tupla (resultado_ordenado, numero_de_comparaciones).

    Si aleatorio=True, antes de elegir el pivote intercambia el primer
    elemento del trozo con uno elegido al azar dentro de ese mismo trozo
    (así el "pivote = primer elemento" de siempre pasa a ser aleatorio).

    Pista: necesitas una función interna (o un contador en una lista de
    1 elemento, ya que no puedes hacer 'nonlocal' de un int fácilmente
    sobre llamadas recursivas anidadas) para acumular el conteo a través
    de las llamadas recursivas. Suma 1 por cada elemento comparado contra
    el pivote (no por cada llamada).
    """
    # Escribe aquí tu código
    pass


# --- Pruebas --------------------------------------------------------------

if __name__ == "__main__":
    # 1. quicksort_propio no muta y ordena bien
    original = [5, 3, 8, 1, 9, 2, 7]
    copia = list(original)
    resultado = quicksort_propio(original)
    assert original == copia, "quicksort_propio no debe mutar la lista de entrada"
    assert resultado == sorted(original)
    print(f"1. quicksort_propio={resultado}")

    # 2. particion_lomuto coloca el pivote en su sitio definitivo
    prueba = [5, 3, 8, 1, 9, 2, 7]
    idx = particion_lomuto(prueba, 0, len(prueba) - 1)
    pivote = prueba[idx]
    assert all(x <= pivote for x in prueba[:idx]), "todo lo de la izquierda debe ser <= pivote"
    assert all(x > pivote for x in prueba[idx + 1:]), "todo lo de la derecha debe ser > pivote"

    # 3. quicksort_inplace ordena de verdad, mutando la lista
    lista = [5, 3, 8, 1, 9, 2, 7]
    quicksort_inplace(lista)
    assert lista == [1, 2, 3, 5, 7, 8, 9]

    # 4. Reproduce la tabla de la lección (con tus propios números)
    n = 500
    lista_ordenada = list(range(n))
    lista_aleatoria = list(range(n))
    random.shuffle(lista_aleatoria)

    _, comparaciones_ordenada = quicksort_contando(lista_ordenada)
    _, comparaciones_aleatoria = quicksort_contando(lista_aleatoria)
    _, comparaciones_ordenada_random_pivot = quicksort_contando(lista_ordenada, aleatorio=True)

    print(f"n={n}")
    print(f"Ordenada, pivote fijo:      {comparaciones_ordenada} comparaciones (esperado cerca de n²/2 = {n*n//2})")
    print(f"Aleatoria, pivote fijo:     {comparaciones_aleatoria} comparaciones (esperado cerca de n·log2(n))")
    print(f"Ordenada, pivote aleatorio: {comparaciones_ordenada_random_pivot} comparaciones (debería parecerse a la fila de arriba, no a la primera)")

    assert comparaciones_ordenada > comparaciones_aleatoria * 10, \
        "el pivote fijo sobre lista ordenada debería disparar muchísimas más comparaciones"
    assert comparaciones_ordenada_random_pivot < comparaciones_ordenada / 5, \
        "el pivote aleatorio debería arreglar el caso de la lista ordenada"

    print("\n✅ Todo correcto: implementaste quicksort y confirmaste su complejidad con datos propios.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)

# --- Preguntas de reflexión ---------------------------------------------
# 1. ¿Por qué particion_lomuto es más eficiente en memoria que la versión
#    con comprehensions, aunque las dos sean O(n) en tiempo por partición?
# 2. Si en vez de pivote aleatorio usaras "mediana de tres" (comparar el
#    primero, el del medio y el último, y quedarte con el de en medio),
#    ¿arreglaría también el caso de la lista ordenada? ¿Por qué?
# 3. quicksort_inplace no es una función pura (muta su argumento) —
#    ¿contradice esto lo aprendido en la lección 011, o hay una razón
#    legítima para elegir mutar aquí? (pista: ¿cuánto costaría en memoria
#    la alternativa pura para una lista de un millón de elementos?)
