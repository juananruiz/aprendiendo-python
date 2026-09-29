"""
Ejercicio — Cuadrado mágico

Un cuadrado mágico es una matriz cuadrada donde TODAS las filas, TODAS las
columnas y las DOS diagonales suman exactamente lo mismo.

El más famoso es el Lo Shu chino, con más de 2.000 años de historia:

        [ 2  7  6 ]      cada fila suma 15
        [ 9  5  1 ]      cada columna suma 15
        [ 4  3  8 ]      cada diagonal suma 15

Alberto Durero incluyó uno de 4x4 en su grabado "Melancolía I" (1514), con
el año grabado en las dos celdas centrales de la última fila.

Este ejercicio reutiliza lo que hiciste en `ejercicio-diferencia-diagonal.py`:
las dos diagonales son exactamente las mismas. Puedes copiar aquí aquellas
funciones o importarlas.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""


# --- 1. La constante mágica ----------------------------------------------

def constante_magica(n):
    """
    Devuelve cuánto DEBE sumar cada fila, columna y diagonal en un cuadrado
    mágico de n x n que use los números del 1 al n².

    La fórmula es n(n²+1)/2. Sale de repartir la suma total de 1..n²
    (que es n²(n²+1)/2) entre las n filas.

    constante_magica(3) -> 15
    constante_magica(4) -> 34

    Pista: usa la división entera // para devolver un int, no un float.
    """
    # Escribe aquí tu código
    pass


# --- 2. Las piezas de la comprobación ------------------------------------

def es_cuadrada(matriz):
    """
    True si la matriz no está vacía y tiene tantas columnas como filas.
    (La misma que en ejercicio-diferencia-diagonal.py.)
    """
    # Escribe aquí tu código
    pass


def sumas_de_filas(matriz):
    """
    Devuelve la lista con la suma de cada fila.

    sumas_de_filas([[2,7,6],[9,5,1],[4,3,8]]) -> [15, 15, 15]

    Pista: una list comprehension con sum().
    """
    # Escribe aquí tu código
    pass


def sumas_de_columnas(matriz):
    """
    Devuelve la lista con la suma de cada columna.

    sumas_de_columnas([[2,7,6],[9,5,1],[4,3,8]]) -> [15, 15, 15]

    Pista: la columna c son los elementos matriz[f][c] para cada fila f.
    Alternativa muy idiomática: zip(*matriz) transpone la matriz, y
    entonces cada "fila" del resultado es una columna original.
    """
    # Escribe aquí tu código
    pass


def sumas_de_diagonales(matriz):
    """
    Devuelve una tupla (principal, secundaria).

    sumas_de_diagonales([[2,7,6],[9,5,1],[4,3,8]]) -> (15, 15)

    Principal:  matriz[i][i]
    Secundaria: matriz[i][n-1-i]
    """
    # Escribe aquí tu código
    pass


# --- 3. La verificación completa -----------------------------------------

def es_cuadrado_magico(matriz):
    """
    True si la matriz es un cuadrado mágico: cuadrada, y con todas sus
    filas, columnas y las dos diagonales sumando lo mismo.

    NO debe lanzar excepción con entradas raras: si no es cuadrada o está
    vacía, simplemente devuelve False.

    es_cuadrado_magico([[2,7,6],[9,5,1],[4,3,8]]) -> True
    es_cuadrado_magico([[1,2,3],[4,5,6],[7,8,9]]) -> False
    es_cuadrado_magico([[1,2],[3]])               -> False

    Pista: toma como objetivo la suma de la primera fila y comprueba que
    todo lo demás coincide. La built-in all() con generadores lo deja en
    muy pocas líneas (lección 031) — y se corta en cuanto encuentra un
    fallo, sin seguir comprobando.
    """
    # Escribe aquí tu código
    pass


def usa_numeros_consecutivos(matriz):
    """
    True si la matriz usa EXACTAMENTE los números del 1 al n², cada uno
    una sola vez.

    Un cuadrado mágico "clásico" cumple esto; pero se puede ser mágico sin
    cumplirlo (por ejemplo multiplicando todas las celdas de uno clásico).

    usa_numeros_consecutivos([[2,7,6],[9,5,1],[4,3,8]]) -> True
    usa_numeros_consecutivos([[4,14,12],[18,10,2],[8,6,16]]) -> False

    Pista: aplana la matriz a un solo conjunto y compáralo con el conjunto
    {1, 2, ..., n²}. Un set te resuelve de golpe el "sin repetidos"
    (lección 032). Cuidado: si hay repetidos, el set los oculta — compara
    también las longitudes.
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    LO_SHU = [[2, 7, 6],
              [9, 5, 1],
              [4, 3, 8]]

    DURERO = [[16,  3,  2, 13],
              [ 5, 10, 11,  8],
              [ 9,  6,  7, 12],
              [ 4, 15, 14,  1]]

    NO_MAGICO = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

    # 1
    assert constante_magica(3) == 15
    assert constante_magica(4) == 34
    assert constante_magica(1) == 1
    assert isinstance(constante_magica(3), int), "usa // para devolver un entero"

    # 2
    assert es_cuadrada(LO_SHU) is True
    assert es_cuadrada([[1, 2], [3]]) is False
    assert es_cuadrada([]) is False

    assert sumas_de_filas(LO_SHU) == [15, 15, 15]
    assert sumas_de_columnas(LO_SHU) == [15, 15, 15]
    assert sumas_de_diagonales(LO_SHU) == (15, 15)

    assert sumas_de_filas(NO_MAGICO) == [6, 15, 24]
    assert sumas_de_columnas(NO_MAGICO) == [12, 15, 18]
    assert sumas_de_diagonales(NO_MAGICO) == (15, 15), "las diagonales SÍ suman 15 aquí"

    # 3: la verificación completa
    assert es_cuadrado_magico(LO_SHU) is True
    assert es_cuadrado_magico(DURERO) is True, "el de Melancolía I también lo es"
    assert es_cuadrado_magico(NO_MAGICO) is False, \
        "ojo: sus diagonales suman 15, pero sus filas no"
    assert es_cuadrado_magico([[5]]) is True, "un 1x1 es trivialmente mágico"

    # cambiar UNA celda lo rompe
    casi = [fila[:] for fila in LO_SHU]
    casi[2][2] = 7
    assert es_cuadrado_magico(casi) is False

    # entradas raras: devuelve False, no revienta
    assert es_cuadrado_magico([[1, 2], [3]]) is False
    assert es_cuadrado_magico([]) is False

    # 4
    assert usa_numeros_consecutivos(LO_SHU) is True
    assert usa_numeros_consecutivos(DURERO) is True
    doblado = [[celda * 2 for celda in fila] for fila in LO_SHU]
    assert es_cuadrado_magico(doblado) is True, "sigue siendo mágico..."
    assert usa_numeros_consecutivos(doblado) is False, "...pero ya no usa 1..n²"

    print("✅ Todo correcto.")
    print(f"   Lo Shu: constante {constante_magica(3)}, mágico={es_cuadrado_magico(LO_SHU)}")
    print(f"   Durero: constante {constante_magica(4)}, mágico={es_cuadrado_magico(DURERO)}")
    print(f"   Fíjate en la última fila del de Durero: 4, 15, 14, 1 -> el año 1514")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. NO_MAGICO tiene las dos diagonales sumando 15, pero no es mágico.
#    ¿Por qué no basta con comprobar las diagonales? ¿Qué habría pasado si
#    tu es_cuadrado_magico solo mirara esas?
# 2. Para una matriz n x n, ¿cuántas sumas hace tu verificación? ¿Cuál es
#    su complejidad en función de n? (lección 021)
# 3. all() se corta en cuanto encuentra un fallo. ¿En qué orden conviene
#    comprobar filas, columnas y diagonales para descartar antes los casos
#    malos? ¿Importa de verdad?
# 4. En ejercicios/funcional/018-imperativo-vs-funcional.py se te pide esta
#    misma función pero SIN un solo bucle explícito. Compara ambas
#    versiones cuando llegues allí: ¿cuál se lee mejor? ¿Cuál habrías
#    escrito antes?
# 5. Reto: escribe generar_cuadrado_magico(n) para n IMPAR, con el método
#    siamés: empieza el 1 en el centro de la fila superior y ve moviéndote
#    en diagonal arriba-derecha; si te sales, das la vuelta por el otro
#    lado; si la casilla está ocupada, bajas una fila.
