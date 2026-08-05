"""
Ejercicio — Diferencia diagonal

Contexto: en `diferencia-diagonal.py` (esta misma carpeta) tienes tu
versión interactiva, que pide los números por input() y calcula todo en un
único bucle. Funciona, pero tiene dos problemas: no se puede testear
automáticamente (necesita que alguien teclee) y mezcla en el mismo sitio
leer datos, validar y calcular.

Este ejercicio es la refactorización: las mismas ideas, pero en funciones
puras que reciben la matriz ya construida y devuelven un valor. Así se
pueden verificar con asserts, que es lo que hace este fichero al final.

Recordatorio de qué es cada diagonal, en una matriz 3x3:

        [ a  .  b ]      principal:  a, e, i   (esquina sup. izq -> inf. der)
        [ .  e  . ]      secundaria: b, e, g   (esquina sup. der -> inf. izq)
        [ g  .  i ]

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""


# --- 1. Validar la matriz -------------------------------------------------

def es_matriz_cuadrada(matriz):
    """
    True si la matriz tiene el mismo número de filas que de columnas, y
    no está vacía.

    es_matriz_cuadrada([[1,2],[3,4]])  -> True
    es_matriz_cuadrada([[1,2],[3]])    -> False   (la 2ª fila es más corta)
    es_matriz_cuadrada([])             -> False   (vacía)

    Pista: el número de filas es len(matriz). Cada fila debe medir
    exactamente eso. La built-in all() con un generador te lo resuelve en
    una línea (lección 031).
    """
    # Escribe aquí tu código
    pass


# --- 2. Las dos diagonales ------------------------------------------------

def suma_diagonal_principal(matriz):
    """
    Suma los elementos de la diagonal principal: las posiciones donde el
    índice de fila y el de columna coinciden -> matriz[i][i].

    suma_diagonal_principal([[11,2,4],[4,5,6],[10,8,-12]]) -> 4
        (11 + 5 + (-12) = 4)

    Pista: sum() con un generador sobre range(len(matriz)) (lección 031).
    """
    # Escribe aquí tu código
    pass


def suma_diagonal_secundaria(matriz):
    """
    Suma la otra diagonal: la que va de la esquina superior DERECHA a la
    inferior izquierda.

    En la fila i, la columna que toca es (n - 1 - i), siendo n el tamaño.

    suma_diagonal_secundaria([[11,2,4],[4,5,6],[10,8,-12]]) -> 19
        (4 + 5 + 10 = 19)
    """
    # Escribe aquí tu código
    pass


# --- 3. El cálculo pedido -------------------------------------------------

def diferencia_diagonal(matriz):
    """
    Devuelve el VALOR ABSOLUTO de la diferencia entre ambas diagonales.

    Si la matriz no es cuadrada o está vacía, lanza ValueError con un
    mensaje claro (lección 034: fallar pronto y con contexto).

    diferencia_diagonal([[11,2,4],[4,5,6],[10,8,-12]]) -> 15
        (|4 - 19| = 15)

    Pista: valida primero, calcula después. La built-in abs() hace el
    valor absoluto.
    """
    # Escribe aquí tu código
    pass


# --- 4. Construir la matriz desde texto ----------------------------------

def matriz_desde_texto(lineas):
    """
    Convierte una lista de strings en una matriz de enteros.

    Es lo que hacía tu input() original, pero separado del cálculo: así
    esta función se puede probar sin que nadie teclee nada.

    matriz_desde_texto(["11 2 4", "4 5 6"]) -> [[11,2,4], [4,5,6]]
    matriz_desde_texto([])                  -> []

    Ojo: entrada.split(" ") falla si hay espacios de más. Usa .split()
    sin argumentos, que separa por cualquier cantidad de espacios
    (referencia 02-strings).
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    MATRIZ = [[11, 2, 4],
              [4, 5, 6],
              [10, 8, -12]]

    # 1
    assert es_matriz_cuadrada(MATRIZ) is True
    assert es_matriz_cuadrada([[1, 2], [3, 4]]) is True
    assert es_matriz_cuadrada([[1]]) is True
    assert es_matriz_cuadrada([[1, 2], [3]]) is False, "la 2ª fila es más corta"
    assert es_matriz_cuadrada([[1, 2, 3], [4, 5, 6]]) is False, "2 filas, 3 columnas"
    assert es_matriz_cuadrada([]) is False, "una matriz vacía no es cuadrada"

    # 2
    assert suma_diagonal_principal(MATRIZ) == 4
    assert suma_diagonal_secundaria(MATRIZ) == 19
    assert suma_diagonal_principal([[5]]) == 5
    assert suma_diagonal_secundaria([[5]]) == 5, "en 1x1 ambas diagonales son la misma celda"

    # 3
    assert diferencia_diagonal(MATRIZ) == 15
    assert diferencia_diagonal([[1, 2], [3, 4]]) == abs((1 + 4) - (2 + 3)) == 0
    for mala in ([[1, 2], [3]], []):
        try:
            diferencia_diagonal(mala)
        except ValueError:
            pass
        else:
            raise AssertionError(f"diferencia_diagonal({mala}) debería lanzar ValueError")

    # 4
    assert matriz_desde_texto(["11 2 4", "4 5 6", "10 8 -12"]) == MATRIZ
    assert matriz_desde_texto([]) == []
    assert matriz_desde_texto(["1   2"]) == [[1, 2]], "usa .split() sin argumentos"

    # el circuito completo, sin input()
    texto = ["11 2 4", "4 5 6", "10 8 -12"]
    assert diferencia_diagonal(matriz_desde_texto(texto)) == 15

    print("✅ Todo correcto.")
    print(f"   principal={suma_diagonal_principal(MATRIZ)} "
          f"secundaria={suma_diagonal_secundaria(MATRIZ)} "
          f"diferencia={diferencia_diagonal(MATRIZ)}")


# --- Preguntas de reflexión ---------------------------------------------
# 1. Tu versión de diferencia-diagonal.py hace todo en un solo bucle
#    mientras lee. Esta lo hace en varias funciones. ¿Cuál es más rápida?
#    ¿Cuál puedes testear sin teclear nada? ¿Cuál preferirías mantener?
# 2. matriz_desde_texto está separada del cálculo a propósito. Eso es el
#    patrón "núcleo funcional, cáscara imperativa" de la lección 011.
#    ¿Dónde pondrías el input() para no romperlo?
# 3. En una matriz de n x n, ¿cuántas sumas hace este algoritmo? ¿Es
#    O(n) u O(n²)? Cuidado: no es lo mismo recorrer las diagonales que
#    recorrer la matriz entera (lección 021).
# 4. es_matriz_cuadrada devuelve False con []. ¿Estarías de acuerdo si
#    devolviera True, argumentando que una matriz vacía es "trivialmente
#    cuadrada"? No hay respuesta única: decide y documenta tu criterio.
