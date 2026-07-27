"""
Ejercicio 15 — functools: reduce, partial, lru_cache, wraps

Cuatro herramientas, cuatro bloques. En cada uno primero lo construyes a
mano y luego usas la versión de la librería, para ver que no hay magia.

Ejecuta el fichero al terminar: los asserts del final deben pasar.
"""

import time
from functools import lru_cache, partial, reduce, wraps


# --- 1. reduce: entenderlo construyéndolo -------------------------------

def mi_reduce(funcion, iterable, inicial):
    """
    Reimplementa reduce() con un bucle for.
    funcion recibe (acumulado, elemento) y devuelve el nuevo acumulado.

    Hazlo a mano ANTES de usar el de functools: es la única forma de que
    reduce deje de parecer magia.
    """
    # Escribe aquí tu código
    pass


def producto(numeros):
    """Producto de todos los números, con reduce. Neutro: 1."""
    # Escribe aquí tu código
    pass


def fusionar(diccionarios):
    """
    Fusiona una lista de dicts en uno solo, sin mutar ninguno.
    Las claves posteriores ganan.

    Pista: {**a, **b}
    """
    # Escribe aquí tu código
    pass


def interseccion(conjuntos):
    """Intersección de una lista de sets, con reduce."""
    # Escribe aquí tu código
    pass


def componer(*funciones):
    """
    Otra vez componer(), pero ahora escrito con reduce por dentro.
    Aplica de izquierda a derecha.
    """
    # Escribe aquí tu código
    pass


def maximo_con_reduce(numeros):
    """
    El máximo, usando reduce. (Sí, existe max(). El objetivo es ver que
    max() ES un reduce con una función concreta.)
    """
    # Escribe aquí tu código
    pass


# --- 2. partial: configurar sin reescribir ------------------------------

def baremar(experiencia, formacion, idiomas, peso_exp, peso_form, peso_idio):
    """Baremo genérico. Los pesos deben sumar 1."""
    return round(
        experiencia * peso_exp + formacion * peso_form + idiomas * peso_idio, 2
    )


# Crea con partial() tres baremos ya configurados:
#   baremo_2024: 50% experiencia, 30% formación, 20% idiomas
#   baremo_2025: 70% experiencia, 20% formación, 10% idiomas
#   baremo_2026: 40% experiencia, 40% formación, 20% idiomas
baremo_2024 = None  # ← sustitúyelo
baremo_2025 = None  # ← sustitúyelo
baremo_2026 = None  # ← sustitúyelo


def hacer_baremo_a_mano(peso_exp, peso_form, peso_idio):
    """
    El mismo efecto que partial(), pero escrito como closure a mano.
    Sirve para comprobar que partial no hace nada que no supieras hacer.
    """
    # Escribe aquí tu código
    pass


def parsear_binario(texto):
    """
    Convierte un string binario a int usando partial(int, base=2).
    Define el partial fuera o dentro, como prefieras.
    """
    # Escribe aquí tu código
    pass


# --- 3. lru_cache: la pureza cobra su recompensa ------------------------

def fib_lento(n):
    """Fibonacci recursivo SIN caché. No lo llames con n > 33."""
    return n if n < 2 else fib_lento(n - 1) + fib_lento(n - 2)


# Escribe fib_rapido: exactamente lo mismo pero con @lru_cache(maxsize=None)
def fib_rapido(n):
    # Añade el decorador arriba y el mismo cuerpo
    pass


def comparar_tiempos(n=30):
    """
    Devuelve (segundos_lento, segundos_rapido) para fib(n).

    Pista: time.perf_counter() antes y después.
    Acuérdate de fib_rapido.cache_clear() antes de medir, o medirás
    una caché ya calentita.
    """
    # Escribe aquí tu código
    pass


def contar_llamadas_sin_cache(n):
    """
    ¿Cuántas veces se llama a fib_lento para calcular fib(n)?
    Cuéntalo (puedes usar una lista mutable como contador, o un atributo
    de función). Sólo aquí se permite la impureza: es instrumentación.
    """
    # Escribe aquí tu código
    pass


@lru_cache(maxsize=None)
def distancia(origen, destino):
    """
    Distancia ficticia entre dos ciudades. Cacheable porque es PURA.
    Devuelve abs(hash(origen) - hash(destino)) % 1000 — determinista
    dentro de una misma ejecución.
    """
    return abs(hash(origen) - hash(destino)) % 1000


def por_que_falla_con_listas():
    """
    Intenta llamar a distancia(["Sevilla"], "Cádiz") dentro de un
    try/except TypeError y devuelve el mensaje de error como string.
    Explica en las reflexiones por qué falla.
    """
    # Escribe aquí tu código
    pass


# --- 4. wraps: no perder la identidad -----------------------------------

def cronometrar_sin_wraps(funcion):
    """Decorador SIN @wraps. Mide el tiempo e imprime nada; sólo envuelve."""
    def envoltorio(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        envoltorio.ultimo_tiempo = time.perf_counter() - inicio
        return resultado
    return envoltorio


def cronometrar(funcion):
    """
    El MISMO decorador, pero con @wraps(funcion) sobre el envoltorio.
    Copia el cuerpo de arriba y añade el decorador.
    """
    # Escribe aquí tu código
    pass


@cronometrar_sin_wraps
def tarea_a(n):
    """Documentación de la tarea A."""
    return sum(range(n))


@cronometrar
def tarea_b(n):
    """Documentación de la tarea B."""
    return sum(range(n))


# --- 5. Comprobación -----------------------------------------------------

if __name__ == "__main__":
    # 1
    assert mi_reduce(lambda a, x: a + x, [1, 2, 3, 4], 0) == 10
    assert mi_reduce(lambda a, x: a * x, [1, 2, 3, 4], 1) == 24
    assert producto([1, 2, 3, 4, 5]) == 120
    assert fusionar([{"a": 1}, {"b": 2}, {"a": 9}]) == {"a": 9, "b": 2}
    original = [{"a": 1}, {"b": 2}]
    fusionar(original)
    assert original == [{"a": 1}, {"b": 2}], "no debe mutar los originales"
    assert interseccion([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]) == {3}
    assert componer(str.strip, str.lower)("  ABC ") == "abc"
    assert maximo_con_reduce([3, 9, 2, 7]) == 9

    # 2
    assert baremo_2024(experiencia=8, formacion=6, idiomas=10) == 7.8
    assert baremo_2025(experiencia=8, formacion=6, idiomas=10) == 7.8
    assert baremo_2026(experiencia=8, formacion=6, idiomas=10) == 7.6
    a_mano = hacer_baremo_a_mano(0.5, 0.3, 0.2)
    assert a_mano(8, 6, 10) == 7.8
    assert parsear_binario("1011") == 11

    # 3
    lento, rapido = comparar_tiempos(30)
    print(f"   fib(30) sin caché: {lento:.4f}s")
    print(f"   fib(30) con caché: {rapido:.6f}s")
    assert rapido < lento / 100, "la caché debe ser órdenes de magnitud mejor"
    assert fib_rapido(100) == 354224848179261915075
    print(f"   {fib_rapido.cache_info()}")
    print(f"   llamadas sin caché para fib(20): {contar_llamadas_sin_cache(20):,}")
    assert "unhashable" in por_que_falla_con_listas()

    # 4
    tarea_a(1000)
    tarea_b(1000)
    print(f"   sin wraps → __name__ = {tarea_a.__name__!r}, __doc__ = {tarea_a.__doc__!r}")
    print(f"   con wraps → __name__ = {tarea_b.__name__!r}, __doc__ = {tarea_b.__doc__!r}")
    assert tarea_a.__name__ == "envoltorio", "sin wraps se pierde el nombre"
    assert tarea_b.__name__ == "tarea_b", "con wraps se conserva"
    assert tarea_b.__doc__ == "Documentación de la tarea B."

    print("✅ functools dominado.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. producto() y maximo_con_reduce() ya existen como math.prod() y max().
#    ¿En qué caso real de tu trabajo usarías reduce en vez de una builtin?
# 2. partial(baremar, peso_exp=0.7) y hacer_baremo_a_mano(0.7, ...) hacen
#    lo mismo. ¿Cuál prefieres leer? ¿Y cuál prefieres depurar?
# 3. distancia() se cachea sin problema, pero obtener_saldo(cuenta) no
#    debería. ¿Qué propiedad de la lección 011 marca la diferencia?
# 4. Compara los dos __name__ del bloque 4. Ahora imagina un traceback en
#    producción con 5 funciones decoradas sin @wraps. ¿Qué verías?
# 5. @lru_cache(maxsize=None) sobre una función que recibe IDs de usuario:
#    ¿qué pasa a las tres semanas de uptime?
