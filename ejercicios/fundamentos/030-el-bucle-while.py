"""
Ejercicio 30 — El bucle while, todos los patrones

Contexto: en la lección 30 viste seis formas en las que aparece el bucle
while en código real (incluido tu propio código: orden_burbuja.py,
busqueda_binaria_02.py y babylonian_square_root.py usan tres de ellas sin
que te dieras cuenta). Aquí implementas los seis desde cero.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""


# --- 1. Patrón contador -----------------------------------------------

def suma_multiplos(n, limite):
    """
    Suma todos los múltiplos de 'n' desde n hasta 'limite' (inclusive),
    usando un contador que avanza de n en n.

    Ejemplo: suma_multiplos(3, 10) -> 3 + 6 + 9 = 18
    """
    # Escribe aquí tu código
    pass


# --- 2. Patrón centinela ------------------------------------------------

def suma_hasta_centinela(numeros, centinela=-1):
    """
    Suma los números de la lista 'numeros' EMPEZANDO por el principio,
    hasta encontrar el valor 'centinela' (sin incluirlo). Si el centinela
    no aparece, suma la lista entera.

    Ejemplo: suma_hasta_centinela([3, 5, 2, -1, 100, 100]) -> 10
    (el 100, 100 del final no cuenta: están después del centinela)

    Pista: la condición del while necesita comprobar DOS cosas con 'and':
    que no te hayas salido del rango, Y que el elemento actual no sea el
    centinela. El orden de esas dos comprobaciones importa (ver la lección).
    """
    # Escribe aquí tu código
    pass


# --- 3. Patrón bandera ---------------------------------------------------

def esta_ordenada(lista):
    """
    Devuelve True si 'lista' está ordenada de menor a mayor, False si no.

    Usa una bandera booleana (como el 'cambio' de orden_burbuja.py, pero
    aquí la bandera dice "sigo pensando que está ordenada") que puede
    cortar el bucle en cuanto encuentres una inversión, sin tener que
    recorrer el resto de la lista.
    """
    # Escribe aquí tu código
    pass


# --- 4. while True + break -----------------------------------------------

def adivinar_por_biseccion(objetivo, minimo=1, maximo=100):
    """
    Simula el juego de "adivina el número" por bisección: en cada intento
    prueba el punto medio del rango [minimo, maximo], y estrecha el rango
    según si el intento quedó corto o largo.

    Devuelve el NÚMERO DE INTENTOS que hicieron falta para acertar.

    Usa while True + break (o return) en vez de una condición de entrada,
    porque no sabes de antemano cuántos intentos harán falta.
    """
    # Escribe aquí tu código
    pass


# --- 5. while / else ------------------------------------------------------

def busca_con_else(lista_ordenada, objetivo):
    """
    Búsqueda binaria sobre 'lista_ordenada' (ya viene ordenada).
    Imprime "Encontrado en la posición X" si lo encuentra (con break),
    o "No encontrado" mediante el else del while si agota el rango
    sin encontrarlo.

    Devuelve el índice si lo encuentra, o None si no.

    Calca la estructura de algoritmos/busqueda_binaria_02.py, pero esta
    vez tienes que escribirla tú.
    """
    # Escribe aquí tu código
    pass


# --- 6. Encuentra y arregla el bucle infinito -----------------------------

def cuenta_atras_rota(desde, maximo_iteraciones=10_000):
    """
    Esta función DEBERÍA devolver una lista contando hacia atrás desde
    'desde' hasta 0 (inclusive), pero tiene un bug: tal y como está,
    sería un bucle infinito de verdad.

    Se ha añadido una guarda de seguridad (maximo_iteraciones) para que,
    mientras la depuras, el script no se cuelgue: si se supera el límite,
    salta una excepción en vez de colgar el intérprete para siempre.

    Tu tarea: encuentra la línea que falta y arréglala.
    """
    resultado = []
    i = desde
    iteraciones = 0
    while i >= 0:
        resultado.append(i)
        # ¿Qué falta aquí para que 'i' se acerque a 0?

        iteraciones += 1
        if iteraciones > maximo_iteraciones:
            raise RuntimeError(
                "demasiadas iteraciones — probablemente sigue siendo un "
                "bucle infinito, revisa qué falta actualizar en la condición"
            )
    return resultado


# --- Pruebas ---------------------------------------------------------------

if __name__ == "__main__":
    # 1
    assert suma_multiplos(3, 10) == 18
    assert suma_multiplos(5, 5) == 5

    # 2
    assert suma_hasta_centinela([3, 5, 2, -1, 100, 100]) == 10
    assert suma_hasta_centinela([1, 2, 3]) == 6, "sin centinela, suma todo"

    # 3
    assert esta_ordenada([1, 2, 3, 4]) is True
    assert esta_ordenada([1, 3, 2, 4]) is False
    assert esta_ordenada([]) is True, "una lista vacía está trivialmente ordenada"

    # 4
    import math
    for objetivo in (1, 50, 100, 73):
        intentos = adivinar_por_biseccion(objetivo)
        cota = math.ceil(math.log2(100)) + 1
        assert intentos <= cota, f"demasiados intentos para {objetivo}: {intentos} (cota {cota})"
    print("intentos para adivinar 73:", adivinar_por_biseccion(73))

    # 5
    ordenada = [1, 3, 5, 7, 9, 11]
    assert busca_con_else(ordenada, 7) == 3
    assert busca_con_else(ordenada, 8) is None

    # 6
    assert cuenta_atras_rota(5) == [5, 4, 3, 2, 1, 0]
    assert cuenta_atras_rota(0) == [0]

    print("\n✅ Todo correcto. Dominas los seis patrones de while.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. En suma_hasta_centinela, ¿qué pasaría si escribieras la condición al
#    revés (comprobando primero numeros[i] y luego i < len(numeros))? Con
#    qué lista de entrada concreta fallaría, y por qué.
# 2. adivinar_por_biseccion es, en esencia, el mismo algoritmo que
#    busqueda_binaria_01.py/02.py. ¿Qué papel juega aquí el "objetivo"
#    comparado con el "número a buscar" de aquellos scripts?
# 3. En cuenta_atras_rota, ¿por qué la guarda de seguridad
#    (maximo_iteraciones) es una buena práctica al DEPURAR, pero no
#    deberías dejarla como solución final en código de producción?
# 4. Reescribe esta_ordenada() usando for en vez de while. ¿Cómo
#    consigues "cortar en cuanto encuentres una inversión" sin la
#    bandera, usando lo que sabes de la lección 0001 (for/else, break)?
