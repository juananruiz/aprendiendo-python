"""
Ejercicio 34 — Errores y excepciones

Contexto: en la lección 34 viste que el objetivo no es que el programa "no
pete", sino capturar solo lo que sabes manejar y protestar pronto y claro
cuando algo va mal.

Ocho ejercicios: conversión segura, else/finally, arreglar un except
demasiado goloso, validar con raise, excepción propia, encadenar con from,
y reescribir en estilo EAFP.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""


# --- 1. Conversión segura ------------------------------------------------

def a_entero(texto, por_defecto=0):
    """
    Convierte 'texto' a int. Si no se puede, devuelve 'por_defecto'.

    a_entero("42")     -> 42
    a_entero("abc")    -> 0
    a_entero(None)     -> 0     ← ojo: int(None) lanza TypeError, no ValueError

    Pista: necesitas capturar DOS excepciones distintas. Puedes agruparlas
    en una tupla: except (ValueError, TypeError).
    """
    # Escribe aquí tu código
    pass


# --- 2. El orden de ejecución: try / except / else / finally -------------

def traza_ejecucion(fallar):
    """
    Devuelve una LISTA con los bloques que se ejecutan, en orden.

    traza_ejecucion(False) -> ["try", "else", "finally"]
    traza_ejecucion(True)  -> ["try", "except", "finally"]

    Estructura: crea `pasos = []`, y ve añadiendo el nombre de cada bloque
    dentro del bloque correspondiente. Dentro del try, si fallar es True,
    lanza un ValueError.
    """
    # Escribe aquí tu código
    pass


# --- 3. finally se ejecuta AUNQUE haya return ----------------------------

def cerrar_siempre(registro):
    """
    Debe devolver "resultado", pero ANTES de devolverlo tiene que añadir
    la cadena "cerrado" a la lista 'registro' desde un bloque finally.

    Al terminar: registro == ["cerrado"] y el retorno es "resultado".

    Esto demuestra que finally corre incluso cuando ya hay un return
    esperando. Es el sitio donde se cierran ficheros y conexiones.
    """
    # Escribe aquí tu código
    pass


# --- 4. Un except demasiado goloso ---------------------------------------

def buscar_nota_golosa(candidatos, nombre):
    """
    ESTÁ MAL A PROPÓSITO: captura Exception, así que esconde CUALQUIER
    fallo — incluidos tus propios bugs. Déjala como referencia.
    """
    try:
        return candidatos[nombre]
    except Exception:
        return None


def buscar_nota(candidatos, nombre):
    """
    Igual, pero capturando SOLO lo que de verdad esperas: que la clave no
    exista. Si le pasan algo que ni siquiera es un dict (por ejemplo una
    lista o None), el TypeError debe propagarse, NO ser silenciado.

    buscar_nota({"Ana": 88}, "Ana")   -> 88
    buscar_nota({"Ana": 88}, "Nadie") -> None
    buscar_nota(None, "Ana")          -> debe LANZAR TypeError
    """
    # Escribe aquí tu código
    pass


# --- 5. Fallar pronto con raise ------------------------------------------

def validar_nota(nota):
    """
    Devuelve la nota si es válida. Si no, lanza ValueError con un mensaje
    que incluya el valor recibido.

    Válida = número (int o float) entre 0 y 10, ambos incluidos.

    validar_nota(8.5)   -> 8.5
    validar_nota(11)    -> ValueError
    validar_nota(-1)    -> ValueError
    validar_nota("ocho")-> ValueError

    Pista: comprueba primero el tipo con isinstance(nota, (int, float)),
    porque "ocho" < 0 lanzaría TypeError en vez de tu ValueError.
    """
    # Escribe aquí tu código
    pass


# --- 6. Tu propia excepción ----------------------------------------------

class SaldoInsuficienteError(Exception):
    """
    Ya está declarada. Fíjate en lo poco que hace falta: heredar de
    Exception y poco más.
    """


def retirar(saldo, cantidad):
    """
    Devuelve el saldo restante. Si 'cantidad' supera 'saldo', lanza
    SaldoInsuficienteError con un mensaje que incluya ambos números.

    retirar(100, 30)  -> 70
    retirar(100, 200) -> SaldoInsuficienteError
    """
    # Escribe aquí tu código
    pass


# --- 7. Encadenar con raise ... from -------------------------------------

def leer_puerto(config):
    """
    Devuelve config["puerto"]. Si la clave no existe, lanza un
    ValueError("falta la clave 'puerto' en la configuración") PERO
    conservando la excepción original como causa.

    Después, este assert debe cumplirse:
        type(error.__cause__) is KeyError

    Pista: captura KeyError como e, y usa `raise ValueError(...) from e`.
    """
    # Escribe aquí tu código
    pass


# --- 8. De LBYL a EAFP ---------------------------------------------------

def dividir_lbyl(a, b):
    """Estilo 'mira antes de saltar'. Correcto, pero no idiomático."""
    if b == 0:
        return None
    return a / b


def dividir_eafp(a, b):
    """
    Mismo comportamiento, en estilo EAFP: inténtalo y captura el fallo.

    dividir_eafp(10, 2) -> 5.0
    dividir_eafp(10, 0) -> None

    Pista: ZeroDivisionError.
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    # 1
    assert a_entero("42") == 42
    assert a_entero("abc") == 0
    assert a_entero(None) == 0, "int(None) lanza TypeError, no ValueError"
    assert a_entero("abc", por_defecto=-1) == -1

    # 2
    assert traza_ejecucion(False) == ["try", "else", "finally"]
    assert traza_ejecucion(True) == ["try", "except", "finally"]

    # 3
    registro = []
    assert cerrar_siempre(registro) == "resultado"
    assert registro == ["cerrado"], "finally debe correr aunque haya return"

    # 4
    assert buscar_nota({"Ana": 88}, "Ana") == 88
    assert buscar_nota({"Ana": 88}, "Nadie") is None
    try:
        buscar_nota(None, "Ana")
    except TypeError:
        pass   # correcto: NO debes silenciar esto
    else:
        raise AssertionError("un TypeError no debe quedar escondido")

    # 5
    assert validar_nota(8.5) == 8.5
    assert validar_nota(0) == 0
    assert validar_nota(10) == 10
    for malo in (11, -1, "ocho"):
        try:
            validar_nota(malo)
        except ValueError:
            pass
        else:
            raise AssertionError(f"validar_nota({malo!r}) debería lanzar ValueError")

    # 6
    assert retirar(100, 30) == 70
    try:
        retirar(100, 200)
    except SaldoInsuficienteError as e:
        assert "100" in str(e) and "200" in str(e), "el mensaje debe dar contexto"
    else:
        raise AssertionError("debería lanzar SaldoInsuficienteError")

    # 7
    assert leer_puerto({"puerto": 8080}) == 8080
    try:
        leer_puerto({})
    except ValueError as e:
        assert type(e.__cause__) is KeyError, "usa 'raise ... from e' para conservar la causa"
    else:
        raise AssertionError("debería lanzar ValueError")

    # 8
    assert dividir_eafp(10, 2) == 5.0
    assert dividir_eafp(10, 0) is None
    assert dividir_eafp(10, 0) == dividir_lbyl(10, 0)

    print("✅ Todo correcto. Ya sabes fallar bien.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. En el ejercicio 4, ¿qué clase de bug tuyo podría quedar escondido para
#    siempre detrás de un `except Exception: return None`?
# 2. ¿Por qué en validar_nota() hay que comprobar el tipo ANTES de comparar
#    con 0 y 10? Prueba a quitar el isinstance y pasarle "ocho".
# 3. LBYL vs EAFP: en dividir() son casi iguales. ¿Se te ocurre un caso
#    (pista: ficheros) donde LBYL tenga una ventana de tiempo peligrosa?
# 4. Vuelve a algún script de algoritmos/. ¿Qué pasa si le das una entrada
#    inesperada? ¿Falla pronto y claro, o produce un resultado absurdo?
