"""
Ejercicio 32 — Elegir la estructura de datos correcta

Contexto: en la lección 32 viste que la diferencia entre elegir una lista o
un conjunto puede ser de 22.000x en tiempo de búsqueda. Aquí tienes siete
funciones que FUNCIONAN, pero que eligieron mal la estructura: bucles
anidados que en realidad son intersecciones, listas usadas como índice de
búsqueda, deduplicaciones que destrozan el orden.

Tu trabajo: reescribirlas eligiendo bien, sin cambiar lo que devuelven.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar,
y una medición real de velocidad al terminar.
"""


# --- 1. Bucle anidado que en realidad es una intersección ---------------

def comunes_con_bucle(lista_a, lista_b):
    """Devuelve los elementos que están en AMBAS listas, sin duplicados."""
    resultado = []
    for a in lista_a:
        for b in lista_b:
            if a == b and a not in resultado:
                resultado.append(a)
    return resultado


def comunes(lista_a, lista_b):
    """
    Reescríbela con conjuntos. Devuelve un SET (no una lista): así el
    llamador no se hace ilusiones sobre el orden.

    Pista: el operador & entre dos sets.
    """
    # Escribe aquí tu código
    pass


# --- 2. Los que están en A pero no en B ----------------------------------

def solo_en_a_con_bucle(lista_a, lista_b):
    resultado = []
    for a in lista_a:
        if a not in lista_b and a not in resultado:
            resultado.append(a)
    return resultado


def solo_en_a(lista_a, lista_b):
    """
    Reescríbela con conjuntos. Devuelve un SET.

    Pista: el operador - entre dos sets (diferencia).
    """
    # Escribe aquí tu código
    pass


# --- 3. Deduplicar SIN perder el orden -----------------------------------

def sin_duplicados_con_bucle(datos):
    """Elimina duplicados conservando el orden de primera aparición."""
    resultado = []
    for d in datos:
        if d not in resultado:
            resultado.append(d)
    return resultado


def sin_duplicados(datos):
    """
    Reescríbela en UNA línea, conservando el orden.

    OJO: list(set(datos)) NO vale — deduplica pero desordena.
    Pista: las claves de un dict son únicas Y mantienen orden (Python 3.7+).
    """
    # Escribe aquí tu código
    pass


# --- 4. Un índice de búsqueda --------------------------------------------

def buscar_nota_con_lista(candidatos, nombre):
    """
    candidatos: lista de tuplas [(nombre, nota), ...]
    Devuelve la nota, o None si no está. Recorre toda la lista: O(n).
    """
    for n, nota in candidatos:
        if n == nombre:
            return nota
    return None


def construir_indice(candidatos):
    """
    Convierte la lista de tuplas [(nombre, nota), ...] en un dict
    {nombre: nota}, para poder buscar en O(1) tantas veces como quieras.

    Pista: dict() acepta directamente un iterable de pares.
    """
    # Escribe aquí tu código
    pass


# --- 5. Tupla como clave de diccionario ----------------------------------

def tabla_distancias():
    """
    Devuelve un dict que asocia CADA PAR de ciudades con su distancia:
        ("Sevilla", "Cádiz")   -> 125
        ("Sevilla", "Huelva")  -> 95

    Tienes que devolver exactamente esos dos pares.
    Pista: la clave debe ser inmutable — por eso una tupla y no una lista.
    """
    # Escribe aquí tu código
    pass


# --- 6. Contar frecuencias -----------------------------------------------

def contar_con_bucle(palabras):
    """Devuelve un dict {palabra: nº de veces que aparece}."""
    conteo = {}
    for p in palabras:
        if p in conteo:
            conteo[p] += 1
        else:
            conteo[p] = 1
    return conteo


def contar(palabras):
    """
    Reescríbela usando collections.Counter, pero devolviendo un dict normal
    (para que los asserts comparen bien).

    Pista: dict(Counter(palabras)). Recuerda importar Counter arriba.
    """
    # Escribe aquí tu código
    pass


# --- 7. Agrupar sin comprobar si la clave existe -------------------------

def agrupar_por_inicial_con_bucle(nombres):
    """Devuelve {inicial: [nombres que empiezan por esa letra]}"""
    grupos = {}
    for n in nombres:
        inicial = n[0]
        if inicial not in grupos:
            grupos[inicial] = []
        grupos[inicial].append(n)
    return grupos


def agrupar_por_inicial(nombres):
    """
    Reescríbela con collections.defaultdict, devolviendo un dict normal.

    Pista: defaultdict(list) crea la lista vacía sola la primera vez que
    tocas una clave nueva. Al final, dict(resultado) para convertirlo.
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    A = ["Ana", "Carlos", "Lucía", "Ana"]
    B = ["Carlos", "Lucía", "Jorge"]

    # 1 y 2: mismo contenido que la versión con bucle, pero como set
    assert comunes(A, B) == {"Carlos", "Lucía"}
    assert comunes(A, B) == set(comunes_con_bucle(A, B))
    assert solo_en_a(A, B) == {"Ana"}
    assert solo_en_a(A, B) == set(solo_en_a_con_bucle(A, B))

    # 3: el orden IMPORTA
    datos = [3, 1, 3, 2, 1, 5]
    assert sin_duplicados(datos) == [3, 1, 2, 5], "debe conservar el orden de aparición"
    assert sin_duplicados(datos) == sin_duplicados_con_bucle(datos)
    assert sin_duplicados([]) == []

    # 4
    candidatos = [("Ana", 88), ("Carlos", 72), ("Lucía", 95)]
    indice = construir_indice(candidatos)
    assert indice["Lucía"] == 95
    assert indice.get("Nadie") is None
    assert len(indice) == 3

    # 5
    tabla = tabla_distancias()
    assert tabla[("Sevilla", "Cádiz")] == 125
    assert tabla[("Sevilla", "Huelva")] == 95
    assert all(isinstance(k, tuple) for k in tabla), "las claves deben ser tuplas"

    # 6
    palabras = ["sol", "mar", "sol", "sol"]
    assert contar(palabras) == {"sol": 3, "mar": 1}
    assert contar(palabras) == contar_con_bucle(palabras)
    assert contar([]) == {}

    # 7
    nombres = ["Ana", "Alberto", "Carlos"]
    assert agrupar_por_inicial(nombres) == {"A": ["Ana", "Alberto"], "C": ["Carlos"]}
    assert agrupar_por_inicial(nombres) == agrupar_por_inicial_con_bucle(nombres)

    print("✅ Todo correcto. Ahora mide la diferencia:\n")

    # --- Mídelo tú mismo -------------------------------------------------
    import timeit
    n = 50_000
    datos_grandes = list(range(n))
    lista, conjunto = datos_grandes, set(datos_grandes)
    objetivo = n - 1          # el peor caso para la lista: el último

    t_lista = timeit.timeit(lambda: objetivo in lista, number=200)
    t_set = timeit.timeit(lambda: objetivo in conjunto, number=200)
    print(f"  Buscar en lista de {n:,}: {t_lista*1000:8.2f} ms")
    print(f"  Buscar en set   de {n:,}: {t_set*1000:8.2f} ms")
    print(f"  El set es {t_lista/t_set:,.0f} veces más rápido")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. En el ejercicio 4, construir el índice cuesta O(n) una vez. ¿A partir
#    de cuántas búsquedas compensa, frente a recorrer la lista cada vez?
# 2. El set es ~5x más pesado en memoria que la lista. ¿En qué situación
#    real preferirías la lista lenta a propósito?
# 3. ¿Por qué comunes() devuelve un set y no una lista? ¿Qué le estarías
#    prometiendo al que la llama si devolvieras una lista?
# 4. Busca en tus scripts de algoritmos/ algún `in` sobre una lista dentro
#    de un bucle. ¿Cuántas veces se ejecuta en total? ¿Compensaría un set?
