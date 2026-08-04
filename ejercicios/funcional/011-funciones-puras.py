"""
Ejercicio 11 — Funciones puras e inmutabilidad

Objetivo: entrenar el reflejo de "no mutar nada".

Cada bloque te da una versión impura que YA FUNCIONA. Tu trabajo no es
arreglar un bug: es reescribirla pura sin cambiar su comportamiento
observable desde fuera.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

from dataclasses import dataclass


# --- 1. Estado global ---------------------------------------------------

_total_acumulado = 0


def acumular_impura(nota):
    """IMPURA: depende de una variable global y la modifica."""
    global _total_acumulado
    _total_acumulado += nota
    return _total_acumulado


def acumular(notas):
    """
    PURA. Recibe una lista de notas y devuelve la suma.

    Pista: la impureza estaba en "recordar" entre llamadas. La versión
    pura recibe todo lo que necesita de golpe.
    """
    # Escribe aquí tu código
    pass


# --- 2. Mutación de argumentos ------------------------------------------

def subir_nota_impura(candidato, puntos):
    """IMPURA: modifica el diccionario que le pasan."""
    candidato["nota"] += puntos
    return candidato


def subir_nota(candidato, puntos):
    """
    PURA. Devuelve un candidato NUEVO con la nota subida.
    El diccionario original no debe cambiar.

    Pista: {**diccionario, "clave": valor_nuevo}
    """
    # Escribe aquí tu código
    pass


# --- 3. Ordenación sin mutar --------------------------------------------

def top_n_impura(candidatos, n):
    """IMPURA: .sort() reordena la lista original del que llama."""
    candidatos.sort(key=lambda c: c["nota"], reverse=True)
    return candidatos[:n]


def top_n(candidatos, n):
    """
    PURA. Devuelve los n mejores sin tocar la lista original.

    Pista: sorted() en vez de .sort()
    """
    # Escribe aquí tu código
    pass


# --- 4. El gotcha del argumento por defecto mutable ----------------------

def registrar_impura(nombre, historial=[]):
    """IMPURA Y ADEMÁS BUGGY: prueba a llamarla dos veces seguidas."""
    historial.append(nombre)
    return historial


def registrar(nombre, historial=None):
    """
    PURA. Devuelve un historial NUEVO con el nombre añadido al final.
    Si no se pasa historial, empieza uno vacío.
    """
    # Escribe aquí tu código
    pass


# --- 5. Un dato inmutable de verdad -------------------------------------

@dataclass(frozen=True)
class Candidato:
    nombre: str
    experiencia: float
    formacion: float
    idiomas: float


def baremo(candidato):
    """
    PURA. Devuelve la puntuación total según el baremo:
        experiencia * 0.5 + formacion * 0.3 + idiomas * 0.2

    Redondea a 2 decimales.
    """
    # Escribe aquí tu código
    pass


def con_bonus(candidato, puntos):
    """
    PURA. Devuelve un Candidato NUEVO con `puntos` más de formación.

    Pista: dataclasses.replace() — impórtalo arriba.
    """
    # Escribe aquí tu código
    pass


# --- 6. Empujar la impureza al borde ------------------------------------

def informe_impuro(candidatos):
    """IMPURA: calcula E imprime, todo mezclado. Imposible de testear."""
    for c in candidatos:
        print(f"{c['nombre']}: {c['nota']}")


def lineas_informe(candidatos):
    """
    PURA. Devuelve una LISTA de strings, una por candidato,
    con el formato "Nombre: nota". No imprime nada.

    Así el núcleo se testea y sólo el print() de main() es impuro.
    """
    # Escribe aquí tu código
    pass


# --- 7. Comprobación -----------------------------------------------------

if __name__ == "__main__":
    # 1
    assert acumular([7, 9, 5]) == 21
    assert acumular([7, 9, 5]) == 21, "debe dar lo mismo la segunda vez"

    # 2
    ana = {"nombre": "Ana", "nota": 7.0}
    ana2 = subir_nota(ana, 1.5)
    assert ana["nota"] == 7.0, "el original no debe cambiar"
    assert ana2["nota"] == 8.5

    # 3
    lista = [{"nombre": "A", "nota": 5}, {"nombre": "B", "nota": 9}]
    copia_previa = [dict(c) for c in lista]
    mejores = top_n(lista, 1)
    assert lista == copia_previa, "la lista original no debe reordenarse"
    assert mejores[0]["nombre"] == "B"

    # 4
    assert registrar("Ana") == ["Ana"]
    assert registrar("Carlos") == ["Carlos"], "¡nada de Ana fantasma!"
    previo = ["Ana"]
    assert registrar("Carlos", previo) == ["Ana", "Carlos"]
    assert previo == ["Ana"], "el historial previo no debe mutarse"

    # 5
    c = Candidato("Ana", experiencia=8.0, formacion=6.0, idiomas=10.0)
    assert baremo(c) == 7.8
    c2 = con_bonus(c, 2.0)
    assert c.formacion == 6.0, "el Candidato original es inmutable"
    assert c2.formacion == 8.0

    # 6
    assert lineas_informe([{"nombre": "Ana", "nota": 8.5}]) == ["Ana: 8.5"]

    print("✅ Todo correcto. Ninguna función mutó nada.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. ¿Por qué registrar_impura("Ana") y luego registrar_impura("Carlos")
#    devuelve ['Ana', 'Carlos']? ¿En qué momento exacto se crea esa lista?
# 2. top_n() copia la lista entera para devolver 3 elementos. ¿En qué tamaño
#    de datos empezaría eso a importarte de verdad? Estímalo, no lo adivines.
# 3. ¿Qué funciones de los scripts de algoritmos/ (orden_burbuja.py,
#    busqueda_binaria_01.py) son puras y cuáles no? ¿Por qué?
# 4. En OOP clásico se usan objetos con setters. ¿Qué pierdes al pasar a
#    @dataclass(frozen=True)? ¿Y qué ganas?
