"""
Ejercicio 25 — Algoritmos voraces

Contexto: en la lección 25 viste que la estrategia voraz (coger siempre lo
que mejor pinta ahora) a veces da el óptimo y a veces no. Aquí implementas
las dos caras: los casos donde falla y los casos donde está demostrado que
acierta.

El ejercicio 2 es el más importante: vas a DEMOSTRAR con código que el
voraz falla, comparándolo contra una solución exacta.

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

from itertools import combinations


# --- 1. Cambio de monedas voraz ------------------------------------------

def cambio_voraz(cantidad, monedas):
    """
    Devuelve una LISTA de monedas que suman 'cantidad', cogiendo siempre
    la moneda más grande que quepa. Si no se puede formar la cantidad
    exacta, devuelve None.

    cambio_voraz(30, [1,5,10,25]) -> [25, 5]
    cambio_voraz(0, [1,5])        -> []

    Pista: recorre las monedas de mayor a menor (sorted(..., reverse=True))
    y usa un while para meter tantas como quepan de cada una.
    """
    # Escribe aquí tu código
    pass


# --- 2. La solución exacta, para demostrar que el voraz falla ------------

def cambio_optimo(cantidad, monedas):
    """
    Devuelve el MÍNIMO número de monedas necesario (solo el número, no la
    lista), o None si es imposible.

    cambio_optimo(6, [1,3,4]) -> 2    (3+3)
    cambio_voraz(6, [1,3,4])  -> [4,1,1], que son 3   ← ¡el voraz pierde!

    Impleméntalo con programación dinámica sencilla:
      - crea una lista 'minimos' de tamaño cantidad+1, llena de infinito
      - minimos[0] = 0
      - para cada valor v de 1 a cantidad, y para cada moneda m <= v:
            minimos[v] = min(minimos[v], minimos[v-m] + 1)
      - al final, minimos[cantidad] (o None si sigue siendo infinito)

    Pista: usa float("inf") como infinito.
    """
    # Escribe aquí tu código
    pass


# --- 3. Cobertura de conjuntos (el ejemplo del libro) --------------------

def cobertura_voraz(necesarios, conjuntos):
    """
    necesarios: set de elementos que hay que cubrir
    conjuntos:  dict {nombre: set de elementos que cubre}

    Devuelve la LISTA de nombres elegidos, en el orden en que los eligió
    el algoritmo: en cada paso, el conjunto que cubra MÁS elementos de los
    que aún faltan.

    Si en algún momento ningún conjunto aporta nada nuevo, para y devuelve
    lo que lleve (no se puede cubrir todo).

    Pista: while con los pendientes; max(conjuntos, key=...) con la
    longitud de la intersección (&) contra los pendientes; y luego
    pendientes -= lo cubierto.
    """
    # Escribe aquí tu código
    pass


def cobertura_exacta(necesarios, conjuntos):
    """
    La solución óptima por fuerza bruta: prueba TODAS las combinaciones
    de conjuntos, de menor a mayor tamaño, y devuelve el número mínimo de
    conjuntos que cubren todo. None si es imposible.

    Solo devuelve el NÚMERO, no los nombres.

    Pista: itertools.combinations(conjuntos, k) para k de 1 a len(conjuntos);
    en cuanto encuentres una combinación cuya unión cubra 'necesarios',
    devuelve k. Para unir varios sets: set().union(*varios_sets).
    """
    # Escribe aquí tu código
    pass


# --- 4. Selección de actividades (un voraz que SÍ es óptimo) ------------

def maximas_actividades(actividades):
    """
    actividades: lista de tuplas (nombre, inicio, fin)

    Devuelve la lista de NOMBRES del máximo número de actividades que
    caben sin solaparse, ordenada por hora de fin.

    Dos actividades no se solapan si una empieza cuando la otra ya ha
    terminado (fin <= inicio siguiente).

    LA ESTRATEGIA VORAZ ÓPTIMA: ordenar por hora de FIN y coger siempre la
    que termina antes de entre las compatibles. Esto SÍ da el óptimo
    garantizado (a diferencia del cambio de monedas).

    maximas_actividades([("A",1,4), ("B",3,5), ("C",5,7)]) -> ["A","C"]

    Pista: ordena por el tercer elemento de la tupla, lleva una variable
    'fin_ultima' y ve cogiendo las que empiecen >= fin_ultima.
    """
    # Escribe aquí tu código
    pass


# --- 5. Mochila fraccionaria (otro voraz óptimo) ------------------------

def mochila_fraccionaria(objetos, capacidad):
    """
    objetos: lista de tuplas (nombre, peso, valor)
    capacidad: peso máximo que aguanta la mochila

    Puedes partir los objetos: si cabe media unidad, te llevas la mitad
    del valor. Devuelve el VALOR TOTAL máximo, redondeado a 2 decimales.

    LA ESTRATEGIA VORAZ ÓPTIMA: coger primero lo que tenga mejor
    proporción valor/peso, y del último llevarte solo la fracción que
    quepa. (Ojo: si NO se pudieran partir, el voraz ya no sería óptimo:
    ese es el problema de la mochila 0/1, que necesita programación
    dinámica.)

    mochila_fraccionaria([("oro",10,60),("plata",20,100)], 25) -> 135.0
        El oro rinde 6 por kilo y la plata 5, así que primero el oro
        entero (10 kg, valor 60). Quedan 15 kg de capacidad para la
        plata, que pesa 20: te llevas 15/20 de ella -> 75. Total: 135.0

    Pista: ordena por valor/peso descendente, ve restando capacidad, y
    cuando un objeto no quepa entero llévate la fracción proporcional.
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    # 1: el voraz funciona con el sistema europeo
    assert cambio_voraz(30, [1, 5, 10, 25]) == [25, 5]
    assert cambio_voraz(0, [1, 5]) == []
    assert cambio_voraz(7, [1, 5]) == [5, 1, 1]
    assert cambio_voraz(3, [2]) is None, "3 no se puede formar solo con monedas de 2"

    # 2: LA DEMOSTRACIÓN — el voraz falla con el sistema 1,3,4
    assert cambio_optimo(6, [1, 3, 4]) == 2, "el óptimo son dos monedas de 3"
    voraz_6 = cambio_voraz(6, [1, 3, 4])
    assert len(voraz_6) == 3, f"el voraz usa 3 monedas: {voraz_6}"
    assert len(voraz_6) > cambio_optimo(6, [1, 3, 4]), "aquí el voraz NO es óptimo"
    print(f"✅ Demostrado: para 6 con monedas [1,3,4]")
    print(f"     voraz  -> {voraz_6} ({len(voraz_6)} monedas)")
    print(f"     óptimo -> 2 monedas (3+3)")

    # con el sistema europeo, voraz y óptimo coinciden
    for cantidad in (30, 41, 67, 99):
        assert len(cambio_voraz(cantidad, [1, 5, 10, 25])) == cambio_optimo(cantidad, [1, 5, 10, 25]), \
            f"con el sistema europeo deberían coincidir para {cantidad}"
    print("     (con el sistema europeo 1-5-10-25, voraz y óptimo SÍ coinciden)")

    # 3: cobertura de conjuntos
    emisoras = {
        "E1": {"Sevilla", "Cádiz", "Huelva"},
        "E2": {"Cádiz", "Málaga"},
        "E3": {"Huelva", "Badajoz"},
        "E4": {"Málaga", "Granada"},
        "E5": {"Sevilla", "Granada"},
    }
    provincias = {"Sevilla", "Cádiz", "Huelva", "Málaga", "Granada", "Badajoz"}

    elegidas = cobertura_voraz(provincias, emisoras)
    cubierto = set().union(*(emisoras[e] for e in elegidas))
    assert cubierto == provincias, "el voraz debe cubrir todas las provincias"
    assert elegidas[0] == "E1", "la primera elegida es la que más cubre (3 provincias)"

    exacta = cobertura_exacta(provincias, emisoras)
    print(f"\n   cobertura: voraz usa {len(elegidas)} emisoras {elegidas}, el óptimo son {exacta}")
    assert len(elegidas) >= exacta, "el voraz nunca puede usar MENOS que el óptimo"

    # imposible de cubrir
    assert cobertura_exacta({"Madrid"}, emisoras) is None

    # 4: selección de actividades
    assert maximas_actividades([("A", 1, 4), ("B", 3, 5), ("C", 5, 7)]) == ["A", "C"]
    assert maximas_actividades([]) == []
    agenda = [("reunion", 9, 11), ("cafe", 10, 11), ("comida", 11, 13),
              ("taller", 12, 16), ("cierre", 14, 15)]
    resultado = maximas_actividades(agenda)
    assert len(resultado) == 3, f"caben 3 actividades, no {len(resultado)}: {resultado}"

    # 5: mochila fraccionaria
    valor = mochila_fraccionaria([("oro", 10, 60), ("plata", 20, 100)], 25)
    assert valor == 135.0, f"todo el oro (60) + 15/20 de plata (75) = 135.0, no {valor}"
    assert mochila_fraccionaria([], 10) == 0
    assert mochila_fraccionaria([("x", 5, 50)], 10) == 50, "si cabe entero, todo su valor"

    print("\n✅ Todo correcto. Sabes cuándo el voraz gana y cuándo pierde.")


# --- Preguntas de reflexión ---------------------------------------------
# 1. cobertura_exacta prueba todas las combinaciones: 2^n. Con las 5
#    emisoras son 31 pruebas. ¿Cuántas serían con 30 emisoras? ¿Y cuánto
#    tardaría a un millón de combinaciones por segundo?
# 2. La mochila FRACCIONARIA se resuelve con voraz óptimo, pero la 0/1
#    (no puedes partir objetos) no. ¿Por qué crees que poder partir lo
#    cambia todo?
# 3. maximas_actividades ordena por hora de FIN. ¿Qué pasaría si ordenaras
#    por hora de INICIO, o por duración? Pruébalo: encuentra un caso donde
#    esas estrategias den peor resultado.
# 4. Gale-Shapley (lección 007) también es voraz: cada proponente va a por
#    su mejor opción disponible. Pero SÍ tiene garantías demostradas.
#    ¿Qué tiene ese problema que no tiene el cambio de monedas?
