"""
Ejercicio 17 — Decoradores de propósito general

Recuerda la equivalencia, y no la olvides en todo el ejercicio:

    @decorador
    def f(): ...

    es EXACTAMENTE

    def f(): ...
    f = decorador(f)

Ejecuta el fichero al terminar: los asserts del final deben pasar.

AVISO sobre este ejercicio en concreto: los decoradores se aplican en el
momento de DEFINIR la función, no al llamarla. Así que hasta que no tengas
escritos los bloques 1 a 4, el fichero ni siquiera arranca — fallará con
"TypeError: 'NoneType' object is not callable" en la primera línea `@algo`.
Es normal. Ve de arriba abajo y ejecuta cuando hayas cubierto los cuatro.
"""

import time
from functools import wraps


# --- 1. El decorador mínimo ---------------------------------------------

def cronometrar(funcion):
    """
    Mide el tiempo de ejecución y lo guarda en el atributo
    `envoltorio.ultimo_tiempo` (en segundos).

    Requisitos:
      - acepta cualquier firma → *args, **kwargs
      - devuelve el resultado de la función original
      - lleva @wraps

    Pista: time.perf_counter()
    """
    # Escribe aquí tu código
    pass


def contar_llamadas(funcion):
    """
    Cuenta cuántas veces se ha llamado a la función.
    El contador vive en `envoltorio.llamadas` y empieza en 0.

    Pista: no puedes hacer `llamadas += 1` sobre una variable del closure
    sin declararla `nonlocal`. Prueba las dos formas y quédate con la que
    entiendas mejor.
    """
    # Escribe aquí tu código
    pass


def trazar(funcion):
    """
    Guarda en `envoltorio.registro` (una lista) un string por llamada
    con el formato:  "nombre(args) -> resultado"

    Ejemplo:  "sumar(2, 3) -> 5"
    Pista: ", ".join(map(repr, args))
    """
    # Escribe aquí tu código
    pass


# --- 2. Decorador con parámetros (tres niveles) -------------------------

def reintentar(veces=3, espera=0.0):
    """
    Reintenta la función si lanza una excepción.
    Si agota los intentos, deja que la excepción salga (raise).
    Guarda en `envoltorio.intentos` cuántos intentos hicieron falta.

    Estructura:
        def reintentar(veces, espera):     # fábrica
            def decorador(funcion):         # decorador
                @wraps(funcion)
                def envoltorio(*a, **k):    # envoltorio
                    ...
                return envoltorio
            return decorador
    """
    # Escribe aquí tu código
    pass


def limitar_a(maximo):
    """
    Decorador paramétrico: si el resultado numérico de la función supera
    `maximo`, devuelve `maximo`. Si no, el resultado tal cual.

    (Es un tope de baremo: por muchos méritos, no pasas de 10.)
    """
    # Escribe aquí tu código
    pass


# --- 3. Memoización a mano (lo que hace lru_cache por dentro) -----------

def memoizar(funcion):
    """
    Guarda los resultados en un dict del closure y los reutiliza.
    Expón la caché como `envoltorio.cache` para poder inspeccionarla.

    Pista: la clave puede ser (args, tuple(sorted(kwargs.items()))).
    ¿Por qué no vale kwargs directamente como clave? (lección 011)
    """
    # Escribe aquí tu código
    pass


# --- 4. Registro estilo Flask -------------------------------------------

TAREAS = {}


def tarea(nombre):
    """
    Decorador paramétrico que REGISTRA la función en el dict TAREAS
    bajo la clave `nombre`, y devuelve la función SIN envolverla.

    Es el patrón de @app.route de Flask.
    """
    # Escribe aquí tu código
    pass


def ejecutar_tarea(nombre, *args, **kwargs):
    """Busca la tarea en TAREAS y la ejecuta. KeyError si no existe."""
    # Escribe aquí tu código
    pass


# --- 5. Funciones de prueba ---------------------------------------------

@cronometrar
@contar_llamadas
def sumar_rango(n):
    """Suma 0..n-1."""
    return sum(range(n))


@trazar
def sumar(a, b):
    return a + b


@memoizar
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@limitar_a(10)
def baremo(experiencia, formacion):
    return experiencia * 0.7 + formacion * 0.5


_fallos_restantes = [2]


@reintentar(veces=5, espera=0.0)
def api_inestable():
    """Falla las 2 primeras veces y luego funciona."""
    if _fallos_restantes[0] > 0:
        _fallos_restantes[0] -= 1
        raise ConnectionError("caída simulada")
    return "ok"


@tarea("saludar")
def saludar(nombre):
    return f"Hola, {nombre}"


# --- 6. El orden importa -------------------------------------------------

def demostrar_orden():
    """
    Define DOS funciones idénticas, una con

        @cronometrar
        @memoizar

    y otra con

        @memoizar
        @cronometrar

    Llámalas dos veces cada una con el mismo argumento e imprime
    `ultimo_tiempo`. Explica la diferencia en las reflexiones.

    (Pista: en un caso el cronómetro mide el acierto de caché; en el otro
    la caché guarda el resultado del cronometrado y ya no vuelve a medir.)
    """
    # Escribe aquí tu código
    pass


# --- 7. Comprobación -----------------------------------------------------

if __name__ == "__main__":
    # 1
    assert sumar_rango(1000) == 499500, "debe devolver el resultado real"
    assert sumar_rango.__name__ == "sumar_rango", "falta @wraps"
    assert sumar_rango.__doc__ == "Suma 0..n-1.", "falta @wraps"
    assert hasattr(sumar_rango, "ultimo_tiempo")
    sumar_rango(10)
    # contar_llamadas está por dentro, accesible por __wrapped__
    print(f"   tiempo última llamada: {sumar_rango.ultimo_tiempo:.6f}s")

    assert sumar(2, 3) == 5
    assert sumar(a=2, b=3) == 5
    print(f"   traza: {sumar.registro}")
    assert "-> 5" in sumar.registro[0]

    # 2
    assert api_inestable() == "ok"
    assert api_inestable.intentos == 3, "2 fallos + 1 éxito"
    assert baremo(10, 10) == 10, "el tope debe aplicarse"
    assert baremo(5, 4) == 5.5, "por debajo del tope, sin tocar"

    # 3
    assert fib(60) == 1548008755920
    assert len(fib.cache) == 61
    print(f"   entradas en caché de fib: {len(fib.cache)}")

    # 4
    assert "saludar" in TAREAS
    assert saludar("Ana") == "Hola, Ana", "el registro NO debe envolver"
    assert ejecutar_tarea("saludar", "Marta") == "Hola, Marta"
    try:
        ejecutar_tarea("inexistente")
        raise AssertionError("debía lanzar KeyError")
    except KeyError:
        pass

    # 6
    demostrar_orden()

    print("✅ Caja de decoradores completa.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. Escribe a mano, sin la sintaxis @, lo que hace realmente:
#        @cronometrar
#        @contar_llamadas
#        def sumar_rango(n): ...
#    ¿En qué orden se aplican? ¿Y en qué orden se ejecutan al llamar?
# 2. memoizar() usa un dict del closure. ¿Qué pasa si la función recibe
#    una lista como argumento? ¿Por qué lru_cache tiene el mismo problema?
# 3. El decorador `tarea` devuelve la función SIN envolver. ¿Sigue siendo
#    un decorador? ¿Qué gana al no envolver?
# 4. ¿En qué se parece este mecanismo a los middlewares que ya usas en
#    tus proyectos PHP? ¿Y en qué se diferencia?
# 5. Vuelve a lo que has escrito en demostrar_orden(). Si un compañero te
#    dijera "el @lru_cache no está funcionando, el cronómetro sigue
#    midiendo", ¿qué le preguntarías primero?
