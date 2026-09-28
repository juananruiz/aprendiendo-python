"""
Ejercicio 23 — Hash tables: construye tu propio dict

Contexto: en la lección 23 viste que el O(1) de los diccionarios no es
magia: es calcular la posición en vez de buscarla. Aquí construyes una
tabla hash completa desde cero, provocas colisiones para ver cómo degrada
a O(n), y la comparas con el dict nativo de Python.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

import timeit


# =========================================================================
# PARTE A — Tu tabla hash
# =========================================================================

class TablaHash:
    """
    Una tabla hash con resolución de colisiones por encadenamiento:
    cada cubo es una lista de pares (clave, valor).
    """

    def __init__(self, n_cubos=8):
        self.n_cubos = n_cubos
        self.cubos = [[] for _ in range(n_cubos)]

    def _indice(self, clave):
        """
        Devuelve el índice del cubo donde le toca a 'clave'.

        Esta es LA línea del algoritmo: hash() convierte la clave en un
        número, y el módulo lo reduce al rango de cubos disponibles.

        Pista: hash(clave) % self.n_cubos
        (usa abs() o confía en que el % de Python siempre da positivo)
        """
        # Escribe aquí tu código
        pass

    def poner(self, clave, valor):
        """
        Guarda el par. Si la clave YA existía, actualiza su valor
        (no debe quedar duplicada).

        Pista: busca la clave en el cubo; si la encuentras, sustituye esa
        posición; si no, haz append.
        """
        # Escribe aquí tu código
        pass

    def obtener(self, clave):
        """
        Devuelve el valor asociado. Si la clave no existe, lanza KeyError.
        """
        # Escribe aquí tu código
        pass

    def obtener_o(self, clave, por_defecto=None):
        """
        Como obtener(), pero devuelve 'por_defecto' si no existe, sin
        lanzar excepción. (Es el .get() del dict de Python.)

        Pista: reutiliza obtener() capturando su KeyError — estilo EAFP
        de la lección 034.
        """
        # Escribe aquí tu código
        pass

    def borrar(self, clave):
        """
        Elimina el par. Si la clave no existe, lanza KeyError.
        """
        # Escribe aquí tu código
        pass

    def contiene(self, clave):
        """True si la clave está en la tabla. No debe lanzar."""
        # Escribe aquí tu código
        pass

    def claves(self):
        """
        Devuelve una lista con todas las claves guardadas.
        El orden da igual (es una tabla hash: no promete ninguno).

        Pista: recorre todos los cubos y todos sus pares.
        """
        # Escribe aquí tu código
        pass

    def __len__(self):
        """
        Número total de pares guardados. Al implementarlo, len(tabla)
        funciona sobre tu objeto.
        """
        # Escribe aquí tu código
        pass

    def distribucion(self):
        """
        Ya está hecha. Devuelve cuántos elementos hay en cada cubo:
        útil para ver si el reparto es bueno o si todo colisiona.
        """
        return [len(cubo) for cubo in self.cubos]

    def factor_de_carga(self):
        """
        Ya está hecha. Elementos / cubos. Python redimensiona su dict
        cuando este valor pasa de ~0.66.
        """
        return len(self) / self.n_cubos


# =========================================================================
# PARTE B — Aplicaciones de las tablas hash
# =========================================================================

def indexar_por(registros, campo):
    """
    Convierte una lista de dicts en un dict indexado por uno de sus campos,
    para poder buscar en O(1) en vez de recorrer la lista.

    indexar_por([{"nombre":"Ana","nota":88}], "nombre")
        -> {"Ana": {"nombre":"Ana","nota":88}}

    Si dos registros comparten valor en ese campo, gana el último.
    """
    # Escribe aquí tu código
    pass


def primer_repetido(datos):
    """
    Devuelve el primer elemento que aparece por segunda vez, o None.
    Debe ser O(n): una sola pasada.

    primer_repetido([1,2,3,2,1]) -> 2   (el 2 se repite antes que el 1)
    primer_repetido([1,2,3])     -> None

    Pista: un set de "ya vistos" y comprobar antes de añadir.
    """
    # Escribe aquí tu código
    pass


def agrupar_anagramas(palabras):
    """
    Agrupa las palabras que son anagramas entre sí (mismas letras en
    distinto orden). Devuelve una lista de listas, cada grupo ordenado
    alfabéticamente, y la lista exterior ordenada por su primer elemento.

    agrupar_anagramas(["amor","roma","mora","casa"])
        -> [["amor","mora","roma"], ["casa"]]

    Pista: la CLAVE de agrupación son las letras ordenadas de cada
    palabra ("amor" -> "amor", "roma" -> "amor"). ¿Qué tipo debe tener
    esa clave para poder usarse en un dict? Piensa en tuple o str.
    """
    # Escribe aquí tu código
    pass


# =========================================================================
# Comprobación
# =========================================================================

if __name__ == "__main__":
    # ----- PARTE A -----
    t = TablaHash()
    for nombre, nota in [("Ana", 88), ("Carlos", 72), ("Lucía", 95), ("Jorge", 65)]:
        t.poner(nombre, nota)

    assert len(t) == 4
    assert t.obtener("Lucía") == 95
    assert t.contiene("Ana") is True
    assert t.contiene("Nadie") is False
    assert t.obtener_o("Nadie") is None
    assert t.obtener_o("Nadie", 0) == 0
    assert sorted(t.claves()) == ["Ana", "Carlos", "Jorge", "Lucía"]

    # actualizar no duplica
    t.poner("Ana", 99)
    assert t.obtener("Ana") == 99
    assert len(t) == 4, "actualizar una clave no debe crear un par nuevo"

    # borrar
    t.borrar("Carlos")
    assert len(t) == 3 and not t.contiene("Carlos")
    for clave_mala in ["Carlos", "Nadie"]:
        try:
            t.obtener(clave_mala)
        except KeyError:
            pass
        else:
            raise AssertionError(f"obtener({clave_mala!r}) debería lanzar KeyError")
    try:
        t.borrar("Nadie")
    except KeyError:
        pass
    else:
        raise AssertionError("borrar una clave inexistente debería lanzar KeyError")

    print("✅ Tu tabla hash funciona.\n")
    print("   distribución en 8 cubos:", t.distribucion())
    print(f"   factor de carga: {t.factor_de_carga():.2f}")

    # --- El peor caso: cuando todo colisiona -----------------------------
    degenerada = TablaHash(n_cubos=1)      # un solo cubo: colisión garantizada
    for i in range(20):
        degenerada.poner(f"clave{i}", i)
    assert degenerada.distribucion() == [20], "con 1 cubo todo debe caer en el mismo sitio"
    assert degenerada.obtener("clave19") == 19, "sigue funcionando, pero recorriendo: O(n)"
    print("\n   con 1 solo cubo:", degenerada.distribucion(), "-> degenera a O(n)")

    # con muchos cubos, el reparto es razonable
    amplia = TablaHash(n_cubos=64)
    for i in range(20):
        amplia.poner(f"clave{i}", i)
    cubos_usados = sum(1 for c in amplia.distribucion() if c > 0)
    assert cubos_usados > 10, "con 64 cubos y 20 claves el reparto debería estar disperso"
    print(f"   con 64 cubos: {cubos_usados} cubos distintos ocupados de 20 claves")

    # ----- PARTE B -----
    registros = [
        {"nombre": "Ana", "nota": 88},
        {"nombre": "Carlos", "nota": 72},
    ]
    indice = indexar_por(registros, "nombre")
    assert indice["Ana"]["nota"] == 88
    assert len(indice) == 2

    assert primer_repetido([1, 2, 3, 2, 1]) == 2
    assert primer_repetido([1, 2, 3]) is None
    assert primer_repetido([]) is None

    assert agrupar_anagramas(["amor", "roma", "mora", "casa"]) == [
        ["amor", "mora", "roma"], ["casa"]
    ]
    assert agrupar_anagramas([]) == []

    # --- Tu tabla contra el dict nativo (escrito en C) -------------------
    mi_tabla = TablaHash(n_cubos=1024)
    nativo = {}
    for i in range(2000):
        mi_tabla.poner(f"clave{i}", i)
        nativo[f"clave{i}"] = i

    t_mia = timeit.timeit(lambda: mi_tabla.obtener("clave1999"), number=10000)
    t_nativa = timeit.timeit(lambda: nativo["clave1999"], number=10000)
    print(f"\n   buscar 10.000 veces: tu tabla {t_mia*1000:.1f} ms | dict nativo {t_nativa*1000:.1f} ms")
    print(f"   el dict de Python es {t_mia/t_nativa:.0f}x más rápido (mismo algoritmo, pero en C)")

    print("\n✅ Todo correcto. Ya sabes lo que hay dentro de un dict.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. Tu tabla y el dict nativo tienen la MISMA complejidad O(1). ¿Por qué
#    entonces el nativo es tantas veces más rápido? ¿Qué mide Big O y qué
#    no mide?
# 2. Ejecuta el fichero dos veces y mira la distribución en cubos. ¿Cambia?
#    ¿Por qué? (pista: hash randomization, lección 23)
# 3. Tu tabla nunca crece: si metes 10.000 claves en 8 cubos, cada cubo
#    tendrá 1.250 elementos. ¿Cómo implementarías el redimensionado?
#    ¿Cuándo lo dispararías?
# 4. En agrupar_anagramas has usado como clave las letras ordenadas.
#    ¿Podrías haber usado una lista? ¿Por qué no? (lección 23, hashable)
