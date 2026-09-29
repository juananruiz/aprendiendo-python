"""
Ejercicio 33 — Funciones a fondo

Contexto: en la lección 33 viste el error más famoso de Python (el argumento
por defecto mutable), *args/**kwargs, el desempaquetado, los parámetros
keyword-only y las reglas de scope.

Aquí hay ocho ejercicios. El primero es un bug real que debes arreglar; el
resto son funciones que debes escribir desde cero.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""


# --- 1. EL BUG: argumento por defecto mutable ----------------------------

def registrar_roto(nombre, historial=[]):
    """
    ESTA FUNCIÓN TIENE EL BUG. Déjala como está: es tu referencia de
    lo que NO hay que hacer. Pruébala llamándola dos veces seguidas.
    """
    historial.append(nombre)
    return historial


def registrar(nombre, historial=None):
    """
    Versión arreglada. Debe comportarse así:
      - registrar("Ana")                 -> ["Ana"]     (siempre, no acumula)
      - registrar("Ana", ["Carlos"])     -> ["Carlos", "Ana"]
      - NO debe modificar la lista que le pasan (créala nueva o copia)

    Pista: el idioma es `if historial is None: historial = []`.
    Para no mutar la lista recibida, devuelve [*historial, nombre].
    """
    # Escribe aquí tu código
    pass


# --- 2. *args: número variable de posicionales ---------------------------

def media(*numeros):
    """
    Devuelve la media aritmética de todos los números recibidos.
    Con cero argumentos debe devolver 0.0 (no reventar).

    Debe poder llamarse así:  media(1, 2, 3)  ->  2.0

    Pista: *numeros llega como una tupla.
    """
    # Escribe aquí tu código
    pass


# --- 3. **kwargs: número variable por nombre -----------------------------

def describir(**datos):
    """
    Devuelve una lista de strings "clave=valor", ORDENADA alfabéticamente
    por clave.

    describir(nombre="Ana", edad=28) -> ["edad=28", "nombre=Ana"]

    Pista: **datos llega como un dict. sorted() sobre .items().
    """
    # Escribe aquí tu código
    pass


# --- 4. Desempaquetar al llamar ------------------------------------------

def crear_punto(x, y, z):
    """Ya está hecha. La usarás desde las dos siguientes."""
    return (x, y, z)


def punto_desde_lista(coordenadas):
    """
    Recibe una lista de 3 números y llama a crear_punto() repartiéndolos
    en sus tres parámetros, SIN escribir coordenadas[0], [1], [2].

    Pista: el operador * al llamar.
    """
    # Escribe aquí tu código
    pass


def punto_desde_dict(datos):
    """
    Recibe un dict {"x":..., "y":..., "z":...} y llama a crear_punto()
    repartiéndolo por nombre.

    Pista: el operador ** al llamar.
    """
    # Escribe aquí tu código
    pass


# --- 5. Keyword-only: forzar la legibilidad ------------------------------

def formatear_nota(nota, *, con_decimales=False, sufijo=""):
    """
    YA ESTÁ ESCRITA la firma; complétala tú.

    Devuelve la nota como string:
      formatear_nota(8.567)                      -> "9"
      formatear_nota(8.567, con_decimales=True)  -> "8.57"
      formatear_nota(8.0, sufijo=" pts")         -> "8 pts"

    Y por el * de la firma, esto DEBE fallar con TypeError:
      formatear_nota(8.567, True)

    Pista: round(nota, 2) con decimales; round(nota) sin ellos. Ojo a que
    round() de un float devuelve int cuando no le das decimales.
    """
    # Escribe aquí tu código
    pass


# --- 6. Scope: nonlocal --------------------------------------------------

def hacer_contador():
    """
    Devuelve una FUNCIÓN que, cada vez que se llama, devuelve un número
    incrementado: 1, 2, 3...

    Cada contador creado debe ser independiente de los demás.

    Pista: define n=0 aquí y una función interna que use `nonlocal n`.
    """
    # Escribe aquí tu código
    pass


# --- 7. Scope: por qué global es mala idea -------------------------------

total_global = 0


def acumular_con_global(cantidad):
    """
    ESTA FUNCIÓN ESTÁ MAL DISEÑADA a propósito: modifica estado de fuera.
    Déjala como está, es tu referencia.
    """
    global total_global
    total_global += cantidad
    return total_global


def acumular(total_actual, cantidad):
    """
    Versión limpia: en vez de modificar una global, RECIBE el total actual
    y DEVUELVE el nuevo. Sin efectos secundarios.

    Pista: es una línea. Esto es una función pura (lección 011).
    """
    # Escribe aquí tu código
    pass


# --- 8. Retorno múltiple -------------------------------------------------

def estadisticas(numeros):
    """
    Devuelve una tupla (minimo, maximo, media) de la lista recibida.
    Con lista vacía devuelve (None, None, 0.0).

    Pista: puedes reutilizar tu media() del ejercicio 2 con *numeros,
    y las built-ins min/max con el parámetro default (lección 031).
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    # 1: demostrar primero el bug, luego que el tuyo NO lo tiene
    assert registrar_roto("Ana") == ["Ana"]
    assert registrar_roto("Carlos") == ["Ana", "Carlos"], "el bug original acumula"

    assert registrar("Ana") == ["Ana"]
    assert registrar("Carlos") == ["Carlos"], "¡tu versión NO debe acumular!"
    previo = ["Carlos"]
    assert registrar("Ana", previo) == ["Carlos", "Ana"]
    assert previo == ["Carlos"], "no debes mutar la lista recibida"

    # 2
    assert media(1, 2, 3) == 2.0
    assert media(10) == 10.0
    assert media() == 0.0, "sin argumentos debe devolver 0.0, no reventar"

    # 3
    assert describir(nombre="Ana", edad=28) == ["edad=28", "nombre=Ana"]
    assert describir() == []

    # 4
    assert punto_desde_lista([1, 2, 3]) == (1, 2, 3)
    assert punto_desde_dict({"x": 9, "y": 8, "z": 7}) == (9, 8, 7)

    # 5
    assert formatear_nota(8.567) == "9"
    assert formatear_nota(8.567, con_decimales=True) == "8.57"
    assert formatear_nota(8.0, sufijo=" pts") == "8 pts"
    try:
        formatear_nota(8.567, True)
    except TypeError:
        pass   # correcto: el * de la firma lo impide
    else:
        raise AssertionError("con_decimales debe ser keyword-only")

    # 6: contadores independientes
    c1 = hacer_contador()
    c2 = hacer_contador()
    assert (c1(), c1(), c1()) == (1, 2, 3)
    assert c2() == 1, "cada contador debe llevar su propia cuenta"

    # 7
    assert acumular(100, 25) == 125
    assert acumular(0, 5) == 5

    # 8
    assert estadisticas([3, 1, 4]) == (1, 4, 8 / 3)
    assert estadisticas([]) == (None, None, 0.0)

    print("✅ Todo correcto. Ya sabes qué pasa entre los paréntesis.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. Ejecuta registrar_roto.__defaults__ después de los asserts. ¿Qué ves
#    dentro? ¿Entiendes ahora por qué el bug es inevitable con ese diseño?
# 2. En el ejercicio 6, ¿qué pasaría si quitaras el `nonlocal`? Pruébalo:
#    ¿qué excepción exacta sale, y por qué?
# 3. acumular_con_global() y acumular() hacen lo mismo. ¿Cuál de las dos
#    puedes testear sin preocuparte del orden de los tests, y por qué?
# 4. formatear_nota tiene 2 parámetros keyword-only. ¿Qué habría pasado si
#    los hubieras dejado posicionales y mañana añades un tercero en medio?
