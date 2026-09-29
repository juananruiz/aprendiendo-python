"""
Ejercicio 24 — Grafos y búsqueda en anchura

Contexto: en la lección 24 viste que BFS junta tres cosas que ya sabías:
un dict para el grafo, un deque como cola FIFO y un set de visitados que
evita los bucles infinitos.

Aquí lo construyes entero, y compruebas EN VIVO qué pasa si quitas el
conjunto de visitados (con una guarda para que no se te cuelgue).

Ejecuta el fichero cuando termines: hay asserts al final que deben pasar.
"""

from collections import deque


# --- Grafo de ejemplo (dirigido) ------------------------------------------

GRAFO = {
    "Ana":   ["Bruno", "Clara"],
    "Bruno": ["Diego"],
    "Clara": ["Diego", "Elena"],
    "Diego": ["Fran"],
    "Elena": ["Fran"],
    "Fran":  [],
}


# --- 1. Construir un grafo no dirigido -----------------------------------

def construir_grafo(relaciones):
    """
    Recibe una lista de pares (a, b) y devuelve un grafo NO dirigido como
    dict {nodo: [vecinos ordenados alfabéticamente]}.

    No dirigido = si a conoce a b, b conoce a a (la arista va en ambos
    sentidos).

    construir_grafo([("Ana","Bruno"), ("Ana","Clara")])
        -> {"Ana": ["Bruno","Clara"], "Bruno": ["Ana"], "Clara": ["Ana"]}

    Pista: collections.defaultdict(list) para no comprobar si la clave
    existe, y sorted() al construir el resultado final. Devuelve un dict
    normal.
    """
    # Escribe aquí tu código
    pass


# --- 2. BFS: distancias a todo lo alcanzable -----------------------------

def distancias_desde(grafo, inicio):
    """
    Devuelve {nodo: nº de saltos desde inicio} para todos los nodos
    alcanzables. El propio inicio está a distancia 0.

    distancias_desde(GRAFO, "Ana")
        -> {'Ana':0, 'Bruno':1, 'Clara':1, 'Diego':2, 'Elena':2, 'Fran':3}

    Estructura del algoritmo:
      - dict 'distancias' con {inicio: 0}  (hace también de "visitados")
      - deque con [inicio]
      - mientras la cola no esté vacía: popleft(), y por cada vecino que
        no esté ya en distancias, apuntar distancia+1 y encolarlo.

    Usa grafo.get(nodo, []) para que no reviente con nodos sin salida.
    """
    # Escribe aquí tu código
    pass


# --- 3. BFS: recuperar el camino -----------------------------------------

def camino_mas_corto(grafo, inicio, destino):
    """
    Devuelve la LISTA de nodos del camino más corto, o None si no hay.
    Si inicio == destino, devuelve [inicio].

    camino_mas_corto(GRAFO, "Ana", "Fran") -> ['Ana','Bruno','Diego','Fran']
    camino_mas_corto(GRAFO, "Fran", "Ana") -> None   (el grafo es dirigido)

    Pista: en vez de encolar NODOS, encola CAMINOS (listas). Empiezas con
    deque([[inicio]]) y vas extendiendo: camino + [vecino].
    """
    # Escribe aquí tu código
    pass


# --- 4. Grados de separación ---------------------------------------------

def grados_de_separacion(grafo, a, b):
    """
    Número de saltos mínimos entre a y b. None si no hay camino.
    Un nodo consigo mismo son 0 grados.

    Pista: puedes reutilizar una de las dos funciones anteriores en una
    sola línea. Cuidado con el None.
    """
    # Escribe aquí tu código
    pass


# --- 5. Amigos de amigos (la sugerencia de las redes sociales) -----------

def amigos_de_amigos(grafo, persona):
    """
    Devuelve el conjunto (set) de nodos que están EXACTAMENTE a 2 saltos:
    los "quizá conozcas". No incluye a la propia persona ni a sus
    contactos directos.

    Pista: distancias_desde() ya te da todas las distancias. Filtra las
    que valgan 2.
    """
    # Escribe aquí tu código
    pass


# --- 6. ¿Está todo conectado? --------------------------------------------

def es_conexo(grafo):
    """
    True si desde CUALQUIER nodo se puede llegar a todos los demás.
    Un grafo vacío se considera conexo (True).

    Para un grafo NO dirigido basta comprobar desde un nodo cualquiera:
    si alcanzas a todos, es conexo.

    Pista: compara len(distancias_desde(grafo, un_nodo)) con len(grafo).
    """
    # Escribe aquí tu código
    pass


# --- 7. El experimento: BFS SIN visitados --------------------------------

def bfs_sin_visitados(grafo, inicio, limite=10_000):
    """
    BFS deliberadamente ROTO: recorre el grafo SIN llevar registro de los
    nodos ya visitados.

    Devuelve el número de nodos que llega a procesar antes de terminar.

    Como en un grafo con ciclos esto no termina nunca, lleva una guarda:
    si procesas más de 'limite' nodos, lanza RuntimeError. Así ves el
    problema sin colgar el intérprete.

    Estructura: igual que distancias_desde, pero SIN la comprobación
    `if vecino not in visitados`. Encola todos los vecinos siempre.
    """
    # Escribe aquí tu código
    pass


# --- Comprobación ---------------------------------------------------------

if __name__ == "__main__":
    # 1
    g = construir_grafo([("Ana", "Bruno"), ("Ana", "Clara"), ("Bruno", "Diego")])
    assert g["Ana"] == ["Bruno", "Clara"]
    assert g["Bruno"] == ["Ana", "Diego"], "no dirigido: la arista va en ambos sentidos"
    assert g["Diego"] == ["Bruno"]
    assert construir_grafo([]) == {}

    # 2
    d = distancias_desde(GRAFO, "Ana")
    assert d == {"Ana": 0, "Bruno": 1, "Clara": 1, "Diego": 2, "Elena": 2, "Fran": 3}
    assert distancias_desde(GRAFO, "Fran") == {"Fran": 0}, "Fran no tiene salidas"

    # 3
    camino = camino_mas_corto(GRAFO, "Ana", "Fran")
    assert camino[0] == "Ana" and camino[-1] == "Fran"
    assert len(camino) == 4, f"el más corto tiene 4 nodos (3 saltos), no {len(camino)}"
    assert camino_mas_corto(GRAFO, "Fran", "Ana") is None
    assert camino_mas_corto(GRAFO, "Ana", "Ana") == ["Ana"]

    # 4
    assert grados_de_separacion(GRAFO, "Ana", "Fran") == 3
    assert grados_de_separacion(GRAFO, "Ana", "Ana") == 0
    assert grados_de_separacion(GRAFO, "Fran", "Ana") is None

    # 5
    assert amigos_de_amigos(GRAFO, "Ana") == {"Diego", "Elena"}
    assert amigos_de_amigos(GRAFO, "Fran") == set()

    # 6
    conexo = construir_grafo([("A", "B"), ("B", "C")])
    desconectado = construir_grafo([("A", "B"), ("C", "D")])
    assert es_conexo(conexo) is True
    assert es_conexo(desconectado) is False
    assert es_conexo({}) is True

    # 7: el experimento del ciclo infinito
    con_ciclo = construir_grafo([("A", "B"), ("B", "C"), ("C", "A")])
    # con visitados: termina y encuentra los 3 nodos
    assert len(distancias_desde(con_ciclo, "A")) == 3

    # sin visitados: NO termina (la guarda lo corta)
    try:
        bfs_sin_visitados(con_ciclo, "A", limite=5000)
    except RuntimeError:
        print("✅ Confirmado: sin el set de visitados, el ciclo A→B→C→A no termina nunca")
    else:
        raise AssertionError("bfs_sin_visitados debería dispararse en un grafo con ciclo")

    # sin ciclos sí termina, aunque repita trabajo
    sin_ciclo = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    procesados = bfs_sin_visitados(sin_ciclo, "A", limite=5000)
    assert procesados >= 4, "sin visitados procesa nodos repetidos (D dos veces)"
    print(f"   en un grafo SIN ciclos de 4 nodos, sin visitados procesa {procesados} (repite trabajo)")

    print("\n✅ Todo correcto. BFS dominado: distancias, caminos y por qué hace falta el set.")

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from herramientas.progreso import registrar_completado
    registrar_completado(__file__)


# --- Preguntas de reflexión ---------------------------------------------
# 1. En distancias_desde, el propio dict de distancias hace de "visitados".
#    ¿Por qué funciona? ¿Qué ventaja tiene sobre llevar un set aparte?
# 2. camino_mas_corto encola listas enteras (camino + [vecino]). Eso copia
#    la lista cada vez. ¿Cómo lo harías guardando solo "de quién vengo"?
#    (pista: un dict {nodo: padre} y reconstruir al final)
# 3. BFS cuenta saltos, no distancias. Si cada arista tuviera un peso
#    (kilómetros, minutos), ¿seguiría funcionando? ¿Qué algoritmo hace
#    falta entonces?
# 4. amigos_de_amigos usa distancia exactamente 2. En una red social real
#    con millones de usuarios, ¿te atreverías a calcular distancias_desde
#    completo? ¿Cómo lo limitarías?
