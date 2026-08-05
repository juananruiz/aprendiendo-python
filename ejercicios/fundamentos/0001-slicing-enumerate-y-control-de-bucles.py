"""
Ejercicio 1 — Slicing, enumerate y control de bucles

Contexto: en la lección 0001 viste tres herramientas que aparecen en casi
todos los algoritmos que vas a escribir: el slicing para rebanar listas,
enumerate para no volver a escribir range(len(...)), y el trío
break/continue/else para controlar bucles.

Este ejercicio termina con lo que propone la lección: refactorizar tu
ordenamiento burbuja con enumerate, y quitarle la bandera a la búsqueda
binaria usando while/else.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""


# --- 1. Slicing: partir por la mitad -------------------------------------

def partir_por_la_mitad(lista):
    """
    Devuelve una tupla (izquierda, derecha) partiendo la lista en dos.
    Si tiene un número impar de elementos, el de más va a la DERECHA.

    partir_por_la_mitad([1,2,3,4])   -> ([1,2], [3,4])
    partir_por_la_mitad([1,2,3])     -> ([1], [2,3])

    Esto es literalmente el primer paso de los algoritmos "divide y
    vencerás" (lección 020, Quicksort).

    Pista: len(lista) // 2 y dos slices.
    """
    # Escribe aquí tu código
    pass


# --- 2. Slicing: los extremos --------------------------------------------

def sin_extremos(lista):
    """
    Devuelve la lista sin su primer ni su último elemento.

    sin_extremos([1,2,3,4,5]) -> [2,3,4]
    sin_extremos([1,2])       -> []
    sin_extremos([])          -> []

    Pista: un solo slice con índice negativo.
    """
    # Escribe aquí tu código
    pass


# --- 3. Slicing: trocear en bloques --------------------------------------

def en_bloques(datos, tamano):
    """
    Parte la lista en trozos de 'tamano' elementos. El último puede ser
    más corto.

    en_bloques([1,2,3,4,5,6,7], 3) -> [[1,2,3], [4,5,6], [7]]

    Pista: una list comprehension con range(0, len(datos), tamano) y un
    slice datos[i:i+tamano].
    """
    # Escribe aquí tu código
    pass


# --- 4. Slicing: palíndromos ---------------------------------------------

def es_palindromo(texto):
    """
    True si el texto se lee igual del derecho y del revés, ignorando
    mayúsculas, espacios y signos de puntuación.

    es_palindromo("Anita lava la tina") -> True
    es_palindromo("hola")               -> False

    Pista: primero quédate solo con los caracteres alfanuméricos en
    minúscula (c.isalnum() te ayuda), y luego compara con su [::-1].

    OJO a un detalle real: las tildes son caracteres distintos. El clásico
    "¿Acaso hubo búhos acá?" NO pasa esta prueba, porque al invertirlo la
    ú y la á caen en posiciones distintas. Es un palíndromo para el ojo
    humano, no para la comparación de cadenas. Ignorar tildes requeriría
    normalizar con unicodedata, y eso queda fuera de esta lección.
    """
    # Escribe aquí tu código
    pass


# --- 5. enumerate: numerar sin range(len(...)) ---------------------------

def con_posicion(nombres):
    """
    Devuelve una lista de strings "1. Ana", "2. Carlos"...

    NO uses range(len(nombres)): ese es justo el patrón que la lección
    te pide abandonar.

    Pista: enumerate(nombres, start=1) dentro de una list comprehension.
    """
    # Escribe aquí tu código
    pass


# --- 6. enumerate: encontrar TODAS las posiciones ------------------------

def posiciones_de(lista, objetivo):
    """
    Devuelve la lista de todos los índices donde aparece 'objetivo'.

    posiciones_de([3,1,3,2,3], 3) -> [0, 2, 4]
    posiciones_de([1,2], 9)       -> []

    (list.index() solo devuelve el primero; aquí los quieres todos.)
    """
    # Escribe aquí tu código
    pass


# --- 7. continue: saltar iteraciones -------------------------------------

def suma_pares_con_continue(numeros):
    """
    Suma solo los números pares, usando OBLIGATORIAMENTE un bucle for con
    `continue` para saltarte los impares.

    suma_pares_con_continue([3,8,2,7,10,5]) -> 20

    (Sí, sum(n for n in numeros if n % 2 == 0) es mejor — pero aquí el
    objetivo es practicar continue. Compáralo al final.)
    """
    # Escribe aquí tu código
    pass


# --- 8. for/else: el bloque sorpresa -------------------------------------

def primer_par(numeros):
    """
    Devuelve el primer número par de la lista, o None si no hay ninguno.

    Escríbela con un for que haga `break` al encontrarlo, y un bloque
    `else` del for que se encargue del caso "no había ninguno".

    primer_par([3,7,9])  -> None
    primer_par([3,8,9])  -> 8
    """
    # Escribe aquí tu código
    pass


# --- 9. Refactor: el burbuja con enumerate -------------------------------

def burbuja_original(lista):
    """
    La versión clásica con range(len(...)). Funciona. Es tu referencia.
    Devuelve una lista NUEVA ordenada (no toca la original).
    """
    lista = list(lista)
    n = len(lista)
    cambio = True
    while cambio:
        cambio = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                cambio = True
    return lista


def burbuja_con_enumerate(lista):
    """
    Misma lógica, pero recorriendo con enumerate en vez de range(len(...)).

    Devuelve una lista NUEVA ordenada, sin modificar la que recibe.

    Pista de la lección: `for i, valor in enumerate(lista[:-1])` — el
    [:-1] evita comparar el último con el siguiente, que no existe.
    """
    # Escribe aquí tu código
    pass


# --- 10. Refactor: búsqueda binaria sin bandera --------------------------

def buscar_con_bandera(lista_ordenada, objetivo):
    """
    Versión con la bandera `encontrado`. Funciona, pero la lección
    propone algo más limpio. Es tu referencia.
    """
    bajo, alto = 0, len(lista_ordenada) - 1
    encontrado = None
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista_ordenada[medio] == objetivo:
            encontrado = medio
            break
        elif lista_ordenada[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return encontrado


def buscar_sin_bandera(lista_ordenada, objetivo):
    """
    Misma búsqueda binaria, pero SIN la variable `encontrado`: devuelve el
    índice directamente con return, y usa el bloque `else` del while para
    el caso "no está".

    buscar_sin_bandera([1,3,5,7,9,11], 7) -> 3
    buscar_sin_bandera([1,3,5,7,9,11], 8) -> None
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    # 1
    assert partir_por_la_mitad([1, 2, 3, 4]) == ([1, 2], [3, 4])
    assert partir_por_la_mitad([1, 2, 3]) == ([1], [2, 3]), "el impar va a la derecha"
    assert partir_por_la_mitad([]) == ([], [])

    # 2
    assert sin_extremos([1, 2, 3, 4, 5]) == [2, 3, 4]
    assert sin_extremos([1, 2]) == []
    assert sin_extremos([]) == []

    # 3
    assert en_bloques([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
    assert en_bloques([1, 2], 5) == [[1, 2]]
    assert en_bloques([], 3) == []

    # 4
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("hola") is False
    assert es_palindromo("Sé verlas al revés") is True, "aquí las tildes sí quedan simétricas"
    assert es_palindromo("¿Acaso hubo búhos acá?") is False, "las tildes rompen la simetría — ver el docstring"

    # 5
    assert con_posicion(["Ana", "Carlos"]) == ["1. Ana", "2. Carlos"]
    assert con_posicion([]) == []

    # 6
    assert posiciones_de([3, 1, 3, 2, 3], 3) == [0, 2, 4]
    assert posiciones_de([1, 2], 9) == []

    # 7
    assert suma_pares_con_continue([3, 8, 2, 7, 10, 5]) == 20
    assert suma_pares_con_continue([1, 3]) == 0

    # 8
    assert primer_par([3, 7, 9]) is None
    assert primer_par([3, 8, 9]) == 8
    assert primer_par([]) is None

    # 9: mismo resultado que la versión original, sin tocar la entrada
    desordenada = [5, 3, 8, 1, 9, 2]
    copia = list(desordenada)
    assert burbuja_con_enumerate(desordenada) == [1, 2, 3, 5, 8, 9]
    assert desordenada == copia, "no debes modificar la lista recibida"
    assert burbuja_con_enumerate(desordenada) == burbuja_original(desordenada)
    assert burbuja_con_enumerate([]) == []
    assert burbuja_con_enumerate([1]) == [1]

    # 10
    ordenada = [1, 3, 5, 7, 9, 11]
    assert buscar_sin_bandera(ordenada, 7) == 3
    assert buscar_sin_bandera(ordenada, 1) == 0
    assert buscar_sin_bandera(ordenada, 8) is None
    assert buscar_sin_bandera([], 5) is None
    for objetivo in ordenada + [0, 4, 99]:
        assert buscar_sin_bandera(ordenada, objetivo) == buscar_con_bandera(ordenada, objetivo)

    print("✅ Todo correcto. Slicing, enumerate y control de bucles dominados.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. partir_por_la_mitad() usa slicing, que COPIA. Para una lista de un
#    millón de elementos en un quicksort recursivo, ¿cuánta memoria extra
#    supone eso? (pista: lección 020, partición in-place)
# 2. En el ejercicio 7 has usado continue por obligación. Escribe también
#    la versión con sum() y un generador. ¿Cuál lees mejor a los 6 meses?
# 3. El bloque `else` del for/while es de las cosas menos usadas de Python.
#    ¿Te parece más claro que la bandera, o menos? No hay respuesta
#    correcta — pero decide tu criterio y sé coherente.
# 4. Compara tu burbuja_con_enumerate con algoritmos/orden_burbuja.py.
#    ¿Cuál de las dos versiones te resultaría más fácil de depurar?
