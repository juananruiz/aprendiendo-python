"""
Ejercicio 21 — La notación Big O

Contexto: en la lección 21 viste que Big O no mide cuánto tarda un
algoritmo, sino cómo empeora al crecer los datos. Y que la teoría se
cumple: al doblar n, un O(n) tarda el doble y un O(n²) cuatro veces más.

Este ejercicio tiene tres partes:
  A) Clasificar código mirándolo (sin ejecutarlo)
  B) MEDIR si acertaste
  C) Arreglar un O(n²) escondido

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

import timeit


# =========================================================================
# PARTE A — Clasificar mirando el código
#
# Rellena el diccionario RESPUESTAS de más abajo con la complejidad de
# cada función. Usa exactamente estas cadenas:
#     "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n²)"
# =========================================================================

def funcion_a(datos):
    """Devuelve el primer elemento."""
    return datos[0] if datos else None


def funcion_b(datos):
    """Suma todos los elementos."""
    total = 0
    for x in datos:
        total += x
    return total


def funcion_c(datos):
    """Todos los pares posibles."""
    pares = []
    for a in datos:
        for b in datos:
            pares.append((a, b))
    return pares


def funcion_d(datos):
    """Recorre la lista dos veces, una detrás de otra."""
    total = 0
    for x in datos:
        total += x
    for x in datos:
        total -= x
    return total


def funcion_e(lista_ordenada, objetivo):
    """Búsqueda binaria."""
    bajo, alto = 0, len(lista_ordenada) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista_ordenada[medio] == objetivo:
            return medio
        elif lista_ordenada[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return None


def funcion_f(datos):
    """Ordena y devuelve el primero."""
    return sorted(datos)[0] if datos else None


def funcion_g(datos, otra_lista):
    """OJO con esta: mira lo que hace el 'in' por dentro."""
    comunes = []
    for x in datos:
        if x in otra_lista:      # otra_lista es una LISTA
            comunes.append(x)
    return comunes


# --- TU RESPUESTA: rellena los valores ----------------------------------

RESPUESTAS = {
    "funcion_a": "",   # ¿?
    "funcion_b": "",   # ¿?
    "funcion_c": "",   # ¿?
    "funcion_d": "",   # ¿? (cuidado: dos bucles SEGUIDOS, no anidados)
    "funcion_e": "",   # ¿?
    "funcion_f": "",   # ¿? (¿cuánto cuesta sorted()?)
    "funcion_g": "",   # ¿? (el coste escondido del 'in' sobre una lista)
}


# =========================================================================
# PARTE B — Medir el factor de crecimiento
# =========================================================================

def factor_de_crecimiento(funcion, n_pequeno=500, n_grande=1000, repeticiones=5):
    """
    Ejecuta 'funcion' con una lista de n_pequeno elementos y otra de
    n_grande, y devuelve cuántas veces más tarda la grande.

    funcion recibe UNA lista y no devuelve nada relevante.

    Un resultado cercano a 1 sugiere O(1) u O(log n);
    cercano a 2, O(n);
    cercano a 4, O(n²).

    Pista: usa timeit.timeit(lambda: funcion(datos), number=repeticiones)
    para cada tamaño, y devuelve el cociente tiempo_grande / tiempo_pequeno.
    Cuidado con dividir entre cero: si el tiempo pequeño es 0, devuelve 1.0.
    """
    # Escribe aquí tu código
    pass


def clasificar_por_factor(factor):
    """
    Traduce un factor de crecimiento medido a una etiqueta.

    factor < 1.5           -> "constante o logarítmica"
    1.5 <= factor < 3.0    -> "lineal"
    factor >= 3.0          -> "cuadrática"
    """
    # Escribe aquí tu código
    pass


# =========================================================================
# PARTE C — Arreglar el O(n²) escondido
# =========================================================================

def elementos_comunes_lento(lista_a, lista_b):
    """
    O(n²): por cada elemento de A, recorre TODA la lista B.
    Funciona, pero se arrastra con listas grandes. Es tu referencia.
    """
    comunes = []
    for x in lista_a:
        if x in lista_b:
            comunes.append(x)
    return comunes


def elementos_comunes_rapido(lista_a, lista_b):
    """
    Mismo resultado (una LISTA, en el mismo orden que lista_a y con los
    mismos duplicados que tenga lista_a), pero en O(n).

    Pista: el problema no es el bucle, es el 'in' sobre una lista.
    ¿Qué estructura hace esa comprobación en O(1)? (lección 032)
    """
    # Escribe aquí tu código
    pass


def tiene_duplicados_lento(datos):
    """O(n²). Tu referencia."""
    for i, x in enumerate(datos):
        for y in datos[i + 1:]:
            if x == y:
                return True
    return False


def tiene_duplicados_rapido(datos):
    """
    True si hay algún elemento repetido. Debe ser O(n).

    Pista: ¿qué le pasa a la longitud de una colección cuando le quitas
    los duplicados?
    """
    # Escribe aquí tu código
    pass


# =========================================================================
# Comprobación
# =========================================================================

if __name__ == "__main__":
    # ----- PARTE A -----
    CORRECTAS = {
        "funcion_a": "O(1)",
        "funcion_b": "O(n)",
        "funcion_c": "O(n²)",
        "funcion_d": "O(n)",
        "funcion_e": "O(log n)",
        "funcion_f": "O(n log n)",
        "funcion_g": "O(n²)",
    }
    fallos = [k for k, v in CORRECTAS.items() if RESPUESTAS.get(k) != v]
    if fallos:
        print("❌ Revisa tu clasificación de:", ", ".join(fallos))
        for k in fallos:
            print(f"     {k}: dijiste {RESPUESTAS.get(k)!r}, es {CORRECTAS[k]!r}")
        raise AssertionError("clasificación incorrecta en la PARTE A")
    print("✅ PARTE A: clasificación correcta")

    # ----- PARTE B -----
    f_lineal = factor_de_crecimiento(funcion_b)
    f_cuadratico = factor_de_crecimiento(funcion_c, n_pequeno=200, n_grande=400, repeticiones=3)

    print(f"\n   factor medido de funcion_b (O(n)):  x{f_lineal:.1f} -> {clasificar_por_factor(f_lineal)}")
    print(f"   factor medido de funcion_c (O(n²)): x{f_cuadratico:.1f} -> {clasificar_por_factor(f_cuadratico)}")

    assert clasificar_por_factor(1.0) == "constante o logarítmica"
    assert clasificar_por_factor(2.1) == "lineal"
    assert clasificar_por_factor(3.9) == "cuadrática"
    # el O(n²) debe crecer claramente más que el O(n)
    assert f_cuadratico > f_lineal, "el cuadrático debería crecer más deprisa que el lineal"
    print("✅ PARTE B: mediciones coherentes con la teoría")

    # ----- PARTE C -----
    A = [1, 2, 3, 4, 5, 3]
    B = [3, 5, 7]
    assert elementos_comunes_rapido(A, B) == elementos_comunes_lento(A, B) == [3, 5, 3]
    assert elementos_comunes_rapido([], B) == []
    assert elementos_comunes_rapido(A, []) == []

    assert tiene_duplicados_rapido([1, 2, 3]) is False
    assert tiene_duplicados_rapido([1, 2, 1]) is True
    assert tiene_duplicados_rapido([]) is False

    # y ahora la prueba de que de verdad es más rápido
    grande_a = list(range(3000))
    grande_b = list(range(1500, 4500))
    t_lento = timeit.timeit(lambda: elementos_comunes_lento(grande_a, grande_b), number=1)
    t_rapido = timeit.timeit(lambda: elementos_comunes_rapido(grande_a, grande_b), number=1)
    print(f"\n   con 3.000 elementos: lento {t_lento*1000:.1f} ms | rápido {t_rapido*1000:.2f} ms")
    print(f"   tu versión es {t_lento/t_rapido:.0f} veces más rápida")
    assert t_rapido < t_lento, "tu versión debería ser más rápida"

    print("\n✅ Todo correcto. Ya sabes leer, medir y arreglar la complejidad.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. funcion_d recorre la lista DOS veces y sigue siendo O(n). ¿Significa
#    eso que tarda lo mismo que recorrerla una vez? ¿Qué mide Big O
#    exactamente, entonces?
# 2. funcion_f usa sorted(), que es O(n log n), para devolver el mínimo.
#    ¿Qué built-in resolvería lo mismo en O(n)? (lección 031)
# 3. Mide el factor de crecimiento de funcion_e (binaria). ¿Por qué sale
#    tan cerca de 1 aunque la lista sea el doble de larga?
# 4. En elementos_comunes_rapido conviertes lista_b a set: eso cuesta O(n)
#    una vez. ¿Por qué compensa igualmente?
