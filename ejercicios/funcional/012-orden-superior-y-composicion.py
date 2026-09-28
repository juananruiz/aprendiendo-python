"""
Ejercicio 12 — Orden superior y composición: fábrica de validadores

Vas a montar un validador de solicitudes de plaza SIN escribir un solo
if/elif de despacho. Todo saldrá de closures, funciones de orden superior
y un diccionario de funciones.

Ejecuta el fichero al terminar: los asserts del final deben pasar.
"""

from functools import reduce


# --- 1. Closures: fábricas de validadores -------------------------------

def rango_valido(minimo, maximo):
    """
    Devuelve una FUNCIÓN que recibe un número y devuelve True si está
    entre minimo y maximo (ambos incluidos).

    Uso esperado:
        nota_ok = rango_valido(0, 10)
        nota_ok(7.5)   -> True
        nota_ok(11)    -> False

    Pista: define una función dentro y devuélvela SIN paréntesis.
    """
    # Escribe aquí tu código
    pass


def longitud_minima(n):
    """
    Devuelve una FUNCIÓN que recibe un string y devuelve True si tiene
    al menos n caracteres (ignorando espacios al principio y al final).
    """
    # Escribe aquí tu código
    pass


def uno_de(opciones):
    """
    Devuelve una FUNCIÓN que recibe un valor y devuelve True si está
    dentro de `opciones`.

    Piensa: ¿qué tipo debería ser `opciones` por dentro para que la
    comprobación sea O(1) en vez de O(n)?
    """
    # Escribe aquí tu código
    pass


# --- 2. Combinadores: funciones que combinan funciones ------------------

def todos(*validadores):
    """
    Devuelve una FUNCIÓN que aplica todos los validadores al mismo valor
    y devuelve True sólo si TODOS pasan.

    Pista: la builtin all() y una generator expression.
    """
    # Escribe aquí tu código
    pass


def alguno(*validadores):
    """Igual que todos(), pero basta con que UNO pase."""
    # Escribe aquí tu código
    pass


def negar(validador):
    """Devuelve una FUNCIÓN que da True justo cuando `validador` da False."""
    # Escribe aquí tu código
    pass


# --- 3. Composición ------------------------------------------------------

def componer(*funciones):
    """
    Devuelve una FUNCIÓN que aplica todas en orden, de IZQUIERDA a DERECHA.

        componer(f, g, h)(x)  ==  h(g(f(x)))

    Pista: reduce(lambda acc, f: f(acc), funciones, valor)
    """
    # Escribe aquí tu código
    pass


def limpiar(s):
    return s.strip()


def minusculas(s):
    return s.lower()


def sin_tildes(s):
    return s.translate(str.maketrans("áéíóúüñ", "aeiouun"))


# Construye `normalizar` componiendo las tres de arriba, en ese orden.
normalizar = None  # ← sustitúyelo por la composición


# --- 4. Despachador con diccionario de funciones ------------------------

# Rellena este diccionario. Las claves son nombres de campo y los valores
# son validadores construidos con las fábricas de arriba:
#   - "nombre": al menos 3 caracteres
#   - "nota": entre 0 y 10
#   - "cuerpo": uno de "A1", "A2", "C1", "C2"
REGLAS = {
    # "nombre": ...,
    # "nota": ...,
    # "cuerpo": ...,
}


def validar_solicitud(solicitud):
    """
    Devuelve una LISTA con los nombres de los campos que NO validan.
    Lista vacía = la solicitud es correcta.

    Un campo que falta en la solicitud cuenta como inválido.

    Pista: recorre REGLAS.items(), no la solicitud. Y hazlo con una
    comprehension, no con un bucle acumulador.
    """
    # Escribe aquí tu código
    pass


# --- 5. Orden superior sobre colecciones --------------------------------

def contar_si(elementos, condicion):
    """Cuántos elementos cumplen la condición. Sin bucle acumulador."""
    # Escribe aquí tu código
    pass


def particionar(elementos, condicion):
    """
    Devuelve una tupla (los_que_cumplen, los_que_no).
    """
    # Escribe aquí tu código
    pass


# --- 6. Comprobación -----------------------------------------------------

if __name__ == "__main__":
    # 1
    nota_ok = rango_valido(0, 10)
    assert nota_ok(7.5) and nota_ok(0) and nota_ok(10)
    assert not nota_ok(-1) and not nota_ok(10.1)
    assert longitud_minima(3)("Ana") and not longitud_minima(3)("Al ")
    assert uno_de(["A1", "A2"])("A2") and not uno_de(["A1", "A2"])("C1")

    # 2
    assert todos(nota_ok, lambda n: n % 1 == 0)(8) is True
    assert todos(nota_ok, lambda n: n % 1 == 0)(8.5) is False
    assert alguno(lambda n: n < 0, nota_ok)(5) is True
    assert negar(nota_ok)(99) is True

    # 3
    assert normalizar("  Sevilla ESTE  ") == "sevilla este"
    assert componer(limpiar, minusculas)("  ABC ") == "abc"

    # 4
    buena = {"nombre": "Ana", "nota": 8.5, "cuerpo": "A2"}
    mala = {"nombre": "Al", "nota": 12, "cuerpo": "X9"}
    assert validar_solicitud(buena) == []
    assert sorted(validar_solicitud(mala)) == ["cuerpo", "nombre", "nota"]
    assert validar_solicitud({"nombre": "Ana"}) != []

    # 5
    notas = [3, 5, 7, 9, 4]
    assert contar_si(notas, lambda n: n >= 5) == 3
    aprobados, suspensos = particionar(notas, lambda n: n >= 5)
    assert aprobados == [5, 7, 9] and suspensos == [3, 4]

    print("✅ Validador compuesto sin un solo if de despacho.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. rango_valido(0, 10) no valida nada por sí misma. ¿Qué devuelve
#    exactamente, y dónde vive el 0 y el 10 después de que la función
#    haya terminado?
# 2. Prueba esto y explica el resultado:
#        fs = [lambda x: x + i for i in range(3)]
#        print([f(10) for f in fs])
#    ¿Cómo lo arreglarías?
# 3. REGLAS es un dict de funciones. En OOP habrías usado el patrón
#    Strategy con una interfaz y tres clases. ¿Qué se pierde al no tener
#    esa interfaz? ¿Cuándo echarías de menos el tipado?
# 4. componer() sólo encadena funciones de UN argumento. Busca un caso de
#    tu propio código donde eso no baste. ¿Merece la pena forzarlo?
