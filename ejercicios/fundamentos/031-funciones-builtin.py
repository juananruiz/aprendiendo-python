"""
Ejercicio 31 — Las funciones built-in: el bucle que no tenías que escribir

Contexto: en la lección 31 viste que muchos bucles no hay que escribirlos,
porque Python ya trae la función hecha. Aquí tienes nueve funciones escritas
con bucles explícitos. TODAS FUNCIONAN CORRECTAMENTE: tu trabajo no es
arreglar bugs, es reescribirlas usando la built-in adecuada sin cambiar su
comportamiento.

Ojo a los casos límite (listas vacías): ahí es donde está la gracia, y donde
una traducción descuidada cambia el comportamiento sin que te des cuenta.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""


# --- 1. ¿Alguno cumple? --------------------------------------------------

def hay_algun_aprobado_con_bucle(notas):
    """Versión original con bucle. No la toques: es tu referencia."""
    for n in notas:
        if n >= 50:
            return True
    return False


def hay_algun_aprobado(notas):
    """
    Reescríbela con una sola línea usando any().

    Pista: any(<expresión generadora>). Comprueba qué devuelve tu versión
    con una lista vacía y compárala con la original.
    """
    # Escribe aquí tu código
    pass


# --- 2. ¿Todos cumplen? --------------------------------------------------

def todos_aprobados_con_bucle(notas):
    """Versión original con bucle."""
    for n in notas:
        if n < 50:
            return False
    return True


def todos_aprobados(notas):
    """
    Reescríbela con all().

    Pista: fíjate en que la original, con lista vacía, devuelve True —
    la verdad vacua de la lección. Tu versión debe hacer lo mismo.
    """
    # Escribe aquí tu código
    pass


# --- 3. El mayor según un criterio ---------------------------------------

def palabra_mas_larga_con_bucle(palabras):
    """Versión original. Devuelve None si la lista está vacía."""
    mejor = None
    for p in palabras:
        if mejor is None or len(p) > len(mejor):
            mejor = p
    return mejor


def palabra_mas_larga(palabras):
    """
    Reescríbela con max().

    Pista: necesitas DOS parámetros de max() para replicar el
    comportamiento exacto — uno para el criterio de comparación y otro
    para no reventar con la lista vacía.
    """
    # Escribe aquí tu código
    pass


# --- 4. La clave con el valor más alto -----------------------------------

def mejor_candidato_con_bucle(candidatos):
    """
    candidatos: dict {nombre: nota}
    Devuelve el nombre con la nota más alta. Si hay empate, el primero.
    """
    mejor = None
    for nombre, nota in candidatos.items():
        if mejor is None or nota > candidatos[mejor]:
            mejor = nombre
    return mejor


def mejor_candidato(candidatos):
    """
    Reescríbela con max().

    Pista: max() sobre un dict recorre sus CLAVES. ¿Qué función puedes
    pasarle como key= para que compare por el valor asociado?
    (candidatos.get es un buen candidato... nunca mejor dicho)
    """
    # Escribe aquí tu código
    pass


# --- 5. Contar cuántos cumplen -------------------------------------------

def contar_notables_con_bucle(notas):
    """Cuenta cuántas notas son >= 80."""
    total = 0
    for n in notas:
        if n >= 80:
            total += 1
    return total


def contar_notables(notas):
    """
    Reescríbela con sum() y una expresión generadora.

    Pista: en Python, True vale 1 y False vale 0 al sumarlos.
    """
    # Escribe aquí tu código
    pass


# --- 6. Sumar con un valor de partida ------------------------------------

def saldo_final_con_bucle(movimientos, saldo_inicial):
    total = saldo_inicial
    for m in movimientos:
        total += m
    return total


def saldo_final(movimientos, saldo_inicial):
    """
    Reescríbela con sum() en una línea.

    Pista: sum() acepta un segundo argumento que casi nadie conoce.
    """
    # Escribe aquí tu código
    pass


# --- 7. Índice y valor, empezando en 1 -----------------------------------

def listado_numerado_con_bucle(nombres):
    """Devuelve ['1. Ana', '2. Carlos', ...]"""
    resultado = []
    i = 1
    for nombre in nombres:
        resultado.append(f"{i}. {nombre}")
        i += 1
    return resultado


def listado_numerado(nombres):
    """
    Reescríbela con enumerate() y una list comprehension.

    Pista: enumerate() acepta un parámetro para no empezar en 0.
    """
    # Escribe aquí tu código
    pass


# --- 8. Cociente y resto -------------------------------------------------

def segundos_a_minutos_con_bucle(total_segundos):
    """Devuelve (minutos, segundos). Ej: 125 -> (2, 5)"""
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    return (minutos, segundos)


def segundos_a_minutos(total_segundos):
    """
    Reescríbela con UNA sola llamada a una built-in.

    Pista: hay una función que hace la división entera y el resto a la vez,
    y devuelve justo la tupla que necesitas.
    """
    # Escribe aquí tu código
    pass


# --- 9. Recorrer al revés sin copiar -------------------------------------

def cuenta_atras_con_bucle(desde):
    """Devuelve [desde, desde-1, ..., 1]"""
    resultado = []
    i = desde
    while i >= 1:
        resultado.append(i)
        i -= 1
    return resultado


def cuenta_atras(desde):
    """
    Reescríbela combinando dos built-ins: una que genera el rango y otra
    que lo recorre al revés sin construir una copia intermedia.

    Pista: reversed(range(...)). Cuidado con los límites del range.
    """
    # Escribe aquí tu código
    pass


# --- 10. RETO: el bug silencioso -----------------------------------------

def emparejar_inseguro(nombres, notas):
    """
    Empareja nombres con notas. PARECE correcta, y con datos bien formados
    lo es. Pero si las dos listas no miden lo mismo, pierde datos SIN AVISAR.
    """
    return list(zip(nombres, notas))


def emparejar(nombres, notas):
    """
    Igual que la anterior, pero debe LANZAR ValueError si las dos listas
    no tienen la misma longitud, en vez de truncar en silencio.

    Pista: un solo parámetro de zip(), disponible desde Python 3.10.
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    NOTAS = [88, 72, 95]
    VACIA = []

    # 1 y 2: comportamiento idéntico al original, TAMBIÉN con lista vacía
    assert hay_algun_aprobado(NOTAS) == hay_algun_aprobado_con_bucle(NOTAS) is True
    assert hay_algun_aprobado(VACIA) == hay_algun_aprobado_con_bucle(VACIA) is False
    assert todos_aprobados(NOTAS) == todos_aprobados_con_bucle(NOTAS) is True
    assert todos_aprobados([88, 30]) == todos_aprobados_con_bucle([88, 30]) is False
    assert todos_aprobados(VACIA) is True, "verdad vacua: all([]) es True"

    # 3: incluido el caso vacío -> None
    PALABRAS = ["sol", "ventana", "mar"]
    assert palabra_mas_larga(PALABRAS) == "ventana"
    assert palabra_mas_larga(VACIA) is None, "con lista vacía debe devolver None, no lanzar"

    # 4: empate -> gana el primero
    assert mejor_candidato({"Ana": 88, "Carlos": 72, "Lucía": 95}) == "Lucía"
    assert mejor_candidato({"Ana": 90, "Carlos": 90}) == "Ana", "en empate, el primero"

    # 5 y 6
    assert contar_notables(NOTAS) == 2
    assert contar_notables(VACIA) == 0
    assert saldo_final([10, -5, 20], 100) == 125
    assert saldo_final(VACIA, 100) == 100

    # 7
    assert listado_numerado(["Ana", "Carlos"]) == ["1. Ana", "2. Carlos"]
    assert listado_numerado(VACIA) == []

    # 8
    assert segundos_a_minutos(125) == (2, 5)
    assert segundos_a_minutos(60) == (1, 0)

    # 9
    assert cuenta_atras(5) == [5, 4, 3, 2, 1]
    assert cuenta_atras(1) == [1]
    assert cuenta_atras(0) == []

    # 10: el reto
    assert emparejar(["Ana", "Carlos"], [88, 72]) == [("Ana", 88), ("Carlos", 72)]
    try:
        emparejar(["Ana", "Carlos", "Lucía"], [88, 72])
    except ValueError:
        pass   # correcto: debe protestar
    else:
        raise AssertionError("emparejar() debería lanzar ValueError con longitudes distintas")

    print("✅ Todo correcto. Nueve bucles menos que mantener.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. En el ejercicio 3, ¿qué habría pasado si hubieras usado max(palabras,
#    key=len) sin el otro parámetro, y la lista llegara vacía?
# 2. any() y all() se paran en cuanto saben la respuesta. ¿En cuál de los
#    nueve ejercicios de arriba ese ahorro sería más notable si la
#    colección tuviera un millón de elementos?
# 3. Vuelve a ejercicios/matching/004-detectar-par-bloqueante.py. ¿Puedes
#    reescribir es_matching_estable() con any()? ¿Queda más legible o menos?
# 4. ¿Qué built-in de las que has usado hoy NO conocías? Búscala en
#    https://docs.python.org/es/3/library/functions.html y lee su firma
#    completa: casi todas tienen algún parámetro que no habías visto.
