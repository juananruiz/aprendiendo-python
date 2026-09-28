"""
Ejercicio 22 — Ordenación por inserción

Contexto: en la lección 22 viste que inserción es O(n²) como burbuja, pero
con un mejor caso de O(n) que la hace 44 veces más rápida sobre datos casi
ordenados. Aquí lo implementas y lo demuestras con tus propios números.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

import random
import timeit


# --- 1. El algoritmo -----------------------------------------------------

def insercion(lista):
    """
    Ordena de menor a mayor. Devuelve una lista NUEVA (no muta la entrada).

    El algoritmo, paso a paso:
      - Recorre desde el índice 1 hasta el final.
      - Guarda el elemento actual.
      - Mientras el de la izquierda sea MAYOR que el actual, desplázalo
        una posición a la derecha.
      - Cuando ya no lo sea, coloca el actual en el hueco.

    Pista: el while interior necesita DOS condiciones con and, y el orden
    importa: `j >= 0 and lista[j] > actual` (lección 030, patrón centinela).
    """
    # Escribe aquí tu código
    pass


# --- 2. La versión que cuenta operaciones --------------------------------

def insercion_contando(lista):
    """
    Igual que insercion(), pero devuelve una tupla:
        (lista_ordenada, numero_de_comparaciones)

    Cuenta UNA comparación cada vez que compares dos elementos entre sí
    (es decir, cada vez que evalúes `lista[j] > actual`).

    Con una lista YA ordenada de n elementos debe dar n-1 comparaciones:
    entra al while una vez por elemento, comprueba y sale. Ese es el
    mejor caso O(n) de la lección.
    """
    # Escribe aquí tu código
    pass


# --- 3. Inserción binaria (la que usa Timsort por dentro) ----------------

def posicion_de_insercion(lista_ordenada, valor):
    """
    Devuelve el índice donde habría que insertar 'valor' para que la
    lista siga ordenada. Si hay elementos iguales, va DESPUÉS de ellos
    (para que la ordenación sea estable).

    Debe hacerlo por búsqueda BINARIA: O(log n), no recorriendo.

    posicion_de_insercion([1,3,5,7], 4) -> 2
    posicion_de_insercion([1,3,5,7], 0) -> 0
    posicion_de_insercion([1,3,5,7], 9) -> 4
    posicion_de_insercion([1,3,3,5], 3) -> 3   (después de los iguales)

    Pista: es una búsqueda binaria que, en vez de devolver None cuando no
    encuentra, devuelve dónde debería estar. Cuando lista[medio] <= valor,
    la posición está a la derecha.
    """
    # Escribe aquí tu código
    pass


# --- 4. Estabilidad ------------------------------------------------------

def ordenar_por_clave(pares, indice_clave=1):
    """
    Ordena una lista de tuplas por el elemento en la posición
    'indice_clave', usando inserción, de forma ESTABLE: los elementos con
    la misma clave deben conservar su orden original.

    ordenar_por_clave([("b",2), ("a",2), ("c",1)])
        -> [("c",1), ("b",2), ("a",2)]      <- b antes que a, como al principio

    Pista: la estabilidad sale sola si en el while usas ESTRICTAMENTE
    mayor (>) y no mayor-o-igual (>=). Piensa por qué.
    """
    # Escribe aquí tu código
    pass


# --- Referencias para comparar (ya escritas, no las toques) --------------

def burbuja(lista):
    l = list(lista)
    for i in range(len(l)):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def seleccion(lista):
    l = list(lista)
    for i in range(len(l)):
        minimo = min(range(i, len(l)), key=lambda k: l[k])
        l[i], l[minimo] = l[minimo], l[i]
    return l


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    # 1: ordena bien y no muta
    prueba = [5, 2, 9, 1, 7, 3]
    copia = list(prueba)
    assert insercion(prueba) == [1, 2, 3, 5, 7, 9]
    assert prueba == copia, "no debes modificar la lista recibida"
    assert insercion([]) == []
    assert insercion([1]) == [1]
    assert insercion([3, 3, 1]) == [1, 3, 3]
    # coincide con los otros dos algoritmos
    aleatoria = random.sample(range(1000), 50)
    assert insercion(aleatoria) == burbuja(aleatoria) == seleccion(aleatoria) == sorted(aleatoria)

    # 2: el mejor caso es n-1 comparaciones
    ordenada_100 = list(range(100))
    resultado, comparaciones = insercion_contando(ordenada_100)
    assert resultado == ordenada_100
    assert comparaciones == 99, f"en lista ya ordenada deben ser n-1=99, no {comparaciones}"
    # y en una lista invertida, el peor caso: muchas más
    invertida = list(range(100, 0, -1))
    _, comparaciones_peor = insercion_contando(invertida)
    assert comparaciones_peor > 4000, "el peor caso debe dispararse (≈n²/2)"
    print(f"   comparaciones: lista ordenada={comparaciones} | invertida={comparaciones_peor}")

    # 3: inserción binaria
    assert posicion_de_insercion([1, 3, 5, 7], 4) == 2
    assert posicion_de_insercion([1, 3, 5, 7], 0) == 0
    assert posicion_de_insercion([1, 3, 5, 7], 9) == 4
    assert posicion_de_insercion([1, 3, 3, 5], 3) == 3, "debe ir DESPUÉS de los iguales"
    assert posicion_de_insercion([], 5) == 0

    # 4: estabilidad
    datos = [("b", 2), ("a", 2), ("c", 1)]
    assert ordenar_por_clave(datos) == [("c", 1), ("b", 2), ("a", 2)], \
        "inserción debe ser estable: 'b' iba antes que 'a' y debe seguir así"

    print("✅ Algoritmo correcto. Ahora la demostración:\n")

    # --- El superpoder: datos casi ordenados -----------------------------
    n = 600
    aleatoria = random.sample(range(n * 10), n)
    casi_ordenada = sorted(aleatoria)
    casi_ordenada[0], casi_ordenada[-1] = casi_ordenada[-1], casi_ordenada[0]

    for nombre, datos in [("aleatoria", aleatoria), ("casi ordenada", casi_ordenada)]:
        t_ins = timeit.timeit(lambda: insercion(datos), number=3) / 3 * 1000
        t_bur = timeit.timeit(lambda: burbuja(datos), number=3) / 3 * 1000
        print(f"   {nombre:15} inserción {t_ins:7.2f} ms | burbuja {t_bur:7.2f} ms"
              f" | inserción es {t_bur/t_ins:5.1f}x más rápida")

    # sobre datos casi ordenados la ventaja debe ser MUCHO mayor
    t_ins_casi = timeit.timeit(lambda: insercion(casi_ordenada), number=3)
    t_ins_alea = timeit.timeit(lambda: insercion(aleatoria), number=3)
    assert t_ins_casi < t_ins_alea, "sobre datos casi ordenados inserción debe volar"

    print("\n✅ Demostrado: el mejor caso O(n) de inserción no es teoría.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. En ordenar_por_clave, ¿por qué usar > en vez de >= hace que el
#    algoritmo sea estable? Pruébalo cambiándolo y mira qué pasa.
# 2. posicion_de_insercion encuentra el hueco en O(log n), pero insertar
#    ahí sigue costando O(n) por el desplazamiento. ¿Merece la pena la
#    búsqueda binaria entonces? (pista: comparar es caro si son strings
#    largos; desplazar es barato porque lo hace C)
# 3. Con n=20, ¿crees que inserción le gana a quicksort? Pruébalo. ¿Por
#    qué las librerías reales cambian a inserción para trozos pequeños?
# 4. Compara tu insercion() con sorted(). ¿Cuánto más rápido es sorted()?
#    ¿Te sorprende, sabiendo que está escrito en C?
