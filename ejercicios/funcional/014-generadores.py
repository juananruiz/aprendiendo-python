"""
Ejercicio 14 — Generadores y evaluación perezosa

Vas a construir generadores, MEDIR el ahorro real (no creértelo) y montar
un pipeline de varias etapas sobre un fichero que se genera al vuelo.

Ejecuta el fichero al terminar: los asserts del final deben pasar.
"""

import sys
import tracemalloc
from itertools import islice
from pathlib import Path

RUTA_DATOS = Path(__file__).parent / "_datos_014.csv"


# --- 1. Tus primeros generadores ----------------------------------------

def contar_hasta(n):
    """
    Genera 1, 2, 3, ... n. Con yield, no con return.
    """
    # Escribe aquí tu código
    pass


def naturales():
    """
    Generador INFINITO: 0, 1, 2, 3, ...
    Sí, con `while True`. No, no se cuelga (mientras no lo consumas entero).
    """
    # Escribe aquí tu código
    pass


def fibonacci():
    """
    Generador INFINITO de Fibonacci: 0, 1, 1, 2, 3, 5, 8, ...

    Pista: a, b = 0, 1  y luego  a, b = b, a + b
    """
    # Escribe aquí tu código
    pass


def pares_de(iterable):
    """
    Generador que deja pasar sólo los números pares del iterable dado.
    Debe funcionar sobre un generador infinito.
    """
    # Escribe aquí tu código
    pass


# --- 2. Medir el ahorro (no te lo creas: mídelo) ------------------------

def comparar_memoria(n=1_000_000):
    """
    Devuelve una tupla (bytes_lista, bytes_generador) para la misma
    expresión `x * 2 for x in range(n)`, una con corchetes y otra con
    paréntesis, medidas con sys.getsizeof().
    """
    # Escribe aquí tu código
    pass


def pico_memoria_lista(n=200_000):
    """
    Usa tracemalloc para medir el PICO de memoria al construir
    [x * 2 for x in range(n)] y sumarla. Devuelve el pico en bytes.

    Esqueleto:
        tracemalloc.start()
        ...tu código...
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return pico
    """
    # Escribe aquí tu código
    pass


def pico_memoria_generador(n=200_000):
    """
    Lo mismo pero con un generador: sum(x * 2 for x in range(n)).
    Debe salir DRÁSTICAMENTE menor. Devuelve el pico en bytes.
    """
    # Escribe aquí tu código
    pass


# --- 3. Leer un fichero perezosamente -----------------------------------

def preparar_datos(filas=100_000):
    """Ya está hecho: crea un CSV de prueba con comentarios y líneas vacías."""
    with open(RUTA_DATOS, "w", encoding="utf-8") as f:
        f.write("# candidatos de prueba\n")
        for i in range(filas):
            if i % 1000 == 0:
                f.write("\n")
                f.write("# bloque nuevo\n")
            f.write(f"Candidato{i};{(i * 7) % 101 / 10}\n")


def leer_lineas(ruta):
    """
    Generador que entrega las líneas del fichero SIN el \\n final.
    Usa `with open(...)` y un for sobre el fichero (que ya es perezoso).
    NO uses readlines().
    """
    # Escribe aquí tu código
    pass


def sin_comentarios(lineas):
    """Deja pasar las líneas que NO empiezan por '#'."""
    # Escribe aquí tu código
    pass


def sin_vacias(lineas):
    """Deja pasar las líneas que tienen algo además de espacios."""
    # Escribe aquí tu código
    pass


def a_registro(lineas):
    """
    Convierte "Nombre;7.5" en {"nombre": "Nombre", "nota": 7.5}.
    """
    # Escribe aquí tu código
    pass


def pipeline(ruta):
    """
    Encadena las cuatro etapas de arriba y devuelve el generador final.
    NO debe leer nada todavía al llamarla.
    """
    # Escribe aquí tu código
    pass


# --- 4. yield from -------------------------------------------------------

def aplanar(anidado):
    """
    Aplana listas anidadas a cualquier profundidad, perezosamente.
        [1, [2, [3, [4, 5]], 6], 7] -> 1, 2, 3, 4, 5, 6, 7

    Pista: isinstance(elemento, list) y `yield from` recursivo.
    """
    # Escribe aquí tu código
    pass


# --- 5. La trampa: agotamiento ------------------------------------------

def demostrar_agotamiento():
    """
    Crea un generador de range(3), conviértelo a lista dos veces
    e imprime ambos resultados. Explica el segundo en las reflexiones.
    """
    # Escribe aquí tu código
    pass


# --- 6. Comprobación -----------------------------------------------------

if __name__ == "__main__":
    # 1
    assert list(contar_hasta(3)) == [1, 2, 3]
    assert list(islice(naturales(), 5)) == [0, 1, 2, 3, 4]
    assert list(islice(fibonacci(), 10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert list(islice(pares_de(naturales()), 4)) == [0, 2, 4, 6]

    # el generador infinito no debe colgar el programa
    primer_grande = next(f for f in fibonacci() if f > 1_000_000)
    assert primer_grande == 1346269

    # 2
    bytes_lista, bytes_gen = comparar_memoria()
    assert bytes_lista > bytes_gen * 1000, "la diferencia debe ser brutal"
    print(f"   lista: {bytes_lista:>10,} bytes")
    print(f"   gener: {bytes_gen:>10,} bytes")

    pico_l = pico_memoria_lista()
    pico_g = pico_memoria_generador()
    assert pico_l > pico_g * 100, "el pico del generador debe ser ínfimo"
    print(f"   pico lista:     {pico_l:>10,} bytes")
    print(f"   pico generador: {pico_g:>10,} bytes")

    # 3
    preparar_datos()
    registros = pipeline(RUTA_DATOS)
    assert not isinstance(registros, list), "pipeline() devuelve un generador"

    tracemalloc.start()
    aprobados = sum(1 for r in registros if r["nota"] >= 5)
    _, pico_pipeline = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    assert aprobados > 0
    print(f"   aprobados: {aprobados:,}  ·  pico pipeline: {pico_pipeline:,} bytes")

    # 4
    assert list(aplanar([1, [2, [3, [4, 5]], 6], 7])) == [1, 2, 3, 4, 5, 6, 7]

    # 5
    demostrar_agotamiento()

    RUTA_DATOS.unlink()
    print("✅ Pipeline perezoso funcionando.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. El pico de memoria del pipeline sobre 100.000 filas: ¿cuánto ha salido?
#    Cambia preparar_datos(filas=1_000_000) y vuelve a medir. ¿Ha crecido
#    el pico proporcionalmente? ¿Por qué?
# 2. En demostrar_agotamiento(), ¿por qué la segunda list() da []?
#    ¿Qué pasaría si en vez de un generador fuese una lista?
# 3. ¿Podrías hacer sorted(pipeline(ruta), key=...)? ¿Qué pasaría con la
#    ventaja de memoria? ¿Sigue mereciendo la pena el generador?
# 4. Las cuatro etapas del pipeline son funciones puras de las de la
#    lección 011. ¿Cómo testearías sin_comentarios() por separado, sin
#    tocar el disco?
