"""
Ejercicio 35 — Consolidación: agenda de contactos e inventario

Este ejercicio no tiene lección propia: es el CAPSTONE de los fundamentos.
Aquí se juntan las cuatro últimas lecciones y tienes que decidir tú qué
usar en cada momento:

  - 031: any/all, min/max con key, sum, sorted
  - 032: elegir bien entre dict, set, lista y tupla
  - 033: argumentos por nombre, valores por defecto, retorno múltiple
  - 034: fallar pronto con raise, y capturar solo lo que sabes manejar

Son los dos ejercicios de consolidación que el TEMARIO tenía pendientes:
una agenda de contactos (parte A) y un inventario (parte B).

REGLA DE ORO DE TODO EL EJERCICIO: ninguna función debe modificar los
datos que recibe. Siempre devuelve una estructura nueva. (Sí, es el estilo
funcional de la lección 011 — aquí lo aplicas sin que te lo recuerden.)

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

from collections import defaultdict


# =========================================================================
# PARTE A — Agenda de contactos
#
# Estructura elegida: dict {nombre: {"telefono": ..., "ciudad": ...}}
# Piensa por qué un dict y no una lista de tuplas (pista: lección 032).
# =========================================================================

def añadir_contacto(agenda, nombre, telefono, ciudad):
    """
    Devuelve una agenda NUEVA con el contacto añadido. Si el nombre ya
    existe, sus datos se sobrescriben.

    No modifiques la agenda recibida.

    Pista: {**agenda, nombre: {...}}
    """
    # Escribe aquí tu código
    pass


def eliminar_contacto(agenda, nombre):
    """
    Devuelve una agenda NUEVA sin ese contacto.
    Si el nombre no existe, lanza KeyError con el nombre en el mensaje.

    Pista: comprueba primero y lanza; luego construye con una dict
    comprehension que salte esa clave.
    """
    # Escribe aquí tu código
    pass


def telefono_de(agenda, nombre, por_defecto=None):
    """
    Devuelve el teléfono de un contacto, o 'por_defecto' si no está.
    NO debe lanzar excepción cuando no existe.

    Pista: agenda.get(...) devuelve None si falta; encadénalo con cuidado
    para no reventar al pedir ["telefono"] de un None.
    """
    # Escribe aquí tu código
    pass


def contactos_por_ciudad(agenda):
    """
    Devuelve {ciudad: [nombres ordenados alfabéticamente]}.

    contactos_por_ciudad(agenda) -> {"Sevilla": ["Ana", "Carlos"], ...}

    Pista: defaultdict(list) para agrupar, y sorted() al construir el
    resultado final. Devuelve un dict normal, no un defaultdict.
    """
    # Escribe aquí tu código
    pass


def buscar_por_prefijo(agenda, prefijo):
    """
    Devuelve la lista ORDENADA de nombres que empiezan por 'prefijo',
    ignorando mayúsculas y minúsculas.

    buscar_por_prefijo(agenda, "a") -> ["Ana"]

    Pista: str.lower() y str.startswith().
    """
    # Escribe aquí tu código
    pass


def ciudades(agenda):
    """
    Devuelve el CONJUNTO de ciudades distintas presentes en la agenda.

    ¿Por qué un set y no una lista? Piénsalo antes de escribirlo.
    """
    # Escribe aquí tu código
    pass


# =========================================================================
# PARTE B — Inventario de productos
#
# Estructura elegida: lista de dicts. Cada producto tiene
# nombre, precio, stock y categoria.
# =========================================================================

class StockInsuficienteError(Exception):
    """Se pide más cantidad de la disponible. Ya está declarada."""


def valor_total(inventario):
    """
    Suma el valor de todo el inventario: precio * stock de cada producto.
    Con inventario vacío devuelve 0.

    Pista: una sola línea con sum() y un generador (lección 031).
    """
    # Escribe aquí tu código
    pass


def bajo_stock(inventario, umbral=5):
    """
    Devuelve la lista ORDENADA de nombres de productos cuyo stock es
    ESTRICTAMENTE menor que 'umbral'.

    Fíjate en que 'umbral' tiene valor por defecto (lección 033).
    """
    # Escribe aquí tu código
    pass


def producto_mas_caro(inventario):
    """
    Devuelve el nombre del producto más caro. Con inventario vacío
    devuelve None (no debe lanzar).

    Pista: max() con key= y default= (lección 031). Cuidado: max() te
    devolverá el DICT completo, y aquí quieres solo el nombre.
    """
    # Escribe aquí tu código
    pass


def aplicar_descuento(inventario, porcentaje):
    """
    Devuelve un inventario NUEVO con todos los precios rebajados ese
    porcentaje, redondeados a 2 decimales. El original no debe cambiar.

    aplicar_descuento(inv, 10) -> precios al 90%

    Pista: [{**p, "precio": ...} for p in inventario]
    """
    # Escribe aquí tu código
    pass


def agrupar_por_categoria(inventario):
    """
    Devuelve {categoria: [nombres ordenados]}.
    Mismo patrón que contactos_por_ciudad.
    """
    # Escribe aquí tu código
    pass


def registrar_venta(inventario, nombre, cantidad):
    """
    Devuelve un inventario NUEVO con el stock de ese producto reducido.

    Debe fallar pronto y claro (lección 034):
      - Si el producto no existe            -> KeyError
      - Si no hay stock suficiente          -> StockInsuficienteError,
        con un mensaje que incluya el stock disponible y la cantidad pedida
      - Si cantidad no es positiva          -> ValueError

    registrar_venta(inv, "teclado", 3) -> stock de teclado baja en 3
    """
    # Escribe aquí tu código
    pass


def resumen(inventario):
    """
    Devuelve una TUPLA con tres valores (retorno múltiple, lección 033):
        (nº de productos distintos, nº de unidades totales, valor total)

    Con inventario vacío: (0, 0, 0)
    """
    # Escribe aquí tu código
    pass


# =========================================================================
# Comprobación
# =========================================================================

if __name__ == "__main__":
    # ----- PARTE A -----
    agenda = {}
    agenda = añadir_contacto(agenda, "Ana", "600111222", "Sevilla")
    agenda = añadir_contacto(agenda, "Carlos", "600333444", "Sevilla")
    agenda = añadir_contacto(agenda, "Lucía", "600555666", "Cádiz")

    assert len(agenda) == 3
    assert agenda["Ana"]["telefono"] == "600111222"

    # inmutabilidad: añadir sobre una agenda no la modifica
    original = dict(agenda)
    _ = añadir_contacto(agenda, "Jorge", "600777888", "Huelva")
    assert agenda == original, "añadir_contacto no debe modificar la agenda recibida"

    # sobrescribir
    actualizada = añadir_contacto(agenda, "Ana", "699999999", "Málaga")
    assert actualizada["Ana"]["ciudad"] == "Málaga"
    assert agenda["Ana"]["ciudad"] == "Sevilla", "el original sigue intacto"

    # eliminar
    sin_carlos = eliminar_contacto(agenda, "Carlos")
    assert "Carlos" not in sin_carlos and len(sin_carlos) == 2
    assert "Carlos" in agenda, "el original sigue intacto"
    try:
        eliminar_contacto(agenda, "Nadie")
    except KeyError:
        pass
    else:
        raise AssertionError("eliminar un contacto inexistente debe lanzar KeyError")

    # consultar sin reventar
    assert telefono_de(agenda, "Lucía") == "600555666"
    assert telefono_de(agenda, "Nadie") is None
    assert telefono_de(agenda, "Nadie", por_defecto="sin teléfono") == "sin teléfono"

    # agrupar y buscar
    assert contactos_por_ciudad(agenda) == {"Sevilla": ["Ana", "Carlos"], "Cádiz": ["Lucía"]}
    assert buscar_por_prefijo(agenda, "a") == ["Ana"], "debe ignorar mayúsculas"
    assert buscar_por_prefijo(agenda, "C") == ["Carlos"]
    assert buscar_por_prefijo(agenda, "z") == []
    assert ciudades(agenda) == {"Sevilla", "Cádiz"}
    assert isinstance(ciudades(agenda), set), "aquí un set tiene más sentido que una lista"

    # ----- PARTE B -----
    inventario = [
        {"nombre": "teclado", "precio": 25.0, "stock": 10, "categoria": "informatica"},
        {"nombre": "raton",   "precio": 12.5, "stock": 3,  "categoria": "informatica"},
        {"nombre": "silla",   "precio": 89.0, "stock": 0,  "categoria": "mobiliario"},
    ]

    assert valor_total(inventario) == 287.5
    assert valor_total([]) == 0

    assert bajo_stock(inventario) == ["raton", "silla"]
    assert bajo_stock(inventario, umbral=1) == ["silla"]
    assert bajo_stock(inventario, umbral=0) == []

    assert producto_mas_caro(inventario) == "silla"
    assert producto_mas_caro([]) is None

    rebajado = aplicar_descuento(inventario, 10)
    assert rebajado[0]["precio"] == 22.5
    assert rebajado[1]["precio"] == 11.25
    assert inventario[0]["precio"] == 25.0, "el inventario original no debe cambiar"

    assert agrupar_por_categoria(inventario) == {
        "informatica": ["raton", "teclado"],
        "mobiliario": ["silla"],
    }

    # ventas y sus tres formas de fallar
    tras_venta = registrar_venta(inventario, "teclado", 3)
    assert tras_venta[0]["stock"] == 7
    assert inventario[0]["stock"] == 10, "el inventario original no debe cambiar"

    try:
        registrar_venta(inventario, "monitor", 1)
    except KeyError:
        pass
    else:
        raise AssertionError("un producto inexistente debe lanzar KeyError")

    try:
        registrar_venta(inventario, "silla", 1)
    except StockInsuficienteError as e:
        assert "0" in str(e) and "1" in str(e), "el mensaje debe dar contexto"
    else:
        raise AssertionError("sin stock debe lanzar StockInsuficienteError")

    try:
        registrar_venta(inventario, "teclado", 0)
    except ValueError:
        pass
    else:
        raise AssertionError("una cantidad no positiva debe lanzar ValueError")

    assert resumen(inventario) == (3, 13, 287.5)
    assert resumen([]) == (0, 0, 0)

    print("✅ Consolidación superada. Agenda e inventario funcionando,")
    print("   sin mutar nada y fallando donde toca.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. La agenda es un dict {nombre: datos}; el inventario, una lista de
#    dicts. ¿Por qué esa asimetría? ¿Qué se rompería si la agenda fuera
#    una lista de dicts con el nombre dentro?
# 2. registrar_venta() recorre la lista entera para encontrar el producto:
#    O(n). Si el inventario tuviera 100.000 productos y vendieras miles de
#    veces, ¿qué estructura elegirías? (lección 032)
# 3. Todas las funciones devuelven estructuras nuevas en vez de modificar.
#    ¿Qué te costaría eso en un inventario de un millón de productos?
#    ¿En qué punto cambiarías de opinión?
# 4. ciudades() devuelve un set. Si en su lugar devolviera una lista,
#    ¿qué le estarías prometiendo al que la llama sin querer?
