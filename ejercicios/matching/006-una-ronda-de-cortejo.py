"""
Ejercicio 6 — Una ronda de cortejo

Contexto: en la lección 6 trazaste a mano el algoritmo de aceptación
diferida, ronda a ronda, con el ejemplo 4x4 de Alba/Bruno/Cora/Dario y
Mar/Nora/Olga/Pau. Aquí vas a programar las DOS decisiones que ocurren en
cada ronda, sin montar todavía el bucle completo (eso es la lección 8):

    1. Un proponente libre elige a quién le propone.
    2. Un receptor, viendo sus pretendientes, decide con quién se queda.

Con esas dos piezas simularás UNA ronda y comprobarás que el resultado
coincide, casilla por casilla, con la tabla de la "Ronda 1" de la lección.

Representación del estado que usaremos:

    compromisos : dict {receptor: proponente}   compromisos provisionales
    tachados    : dict {proponente: set(...)}    receptores que ya lo rechazaron
    libres      : lista de proponentes sin compromiso

Los datos de abajo son EXACTAMENTE los de la lección 6.
"""

# --- Preferencias (idénticas a la lección 6) ---

prefs_proponentes = {
    "Alba":  ["Nora", "Mar", "Olga", "Pau"],
    "Bruno": ["Mar", "Nora", "Pau", "Olga"],
    "Cora":  ["Mar", "Olga", "Nora", "Pau"],
    "Dario": ["Pau", "Olga", "Nora", "Mar"],
}

prefs_receptores = {
    "Mar":  ["Cora", "Alba", "Bruno", "Dario"],
    "Nora": ["Bruno", "Alba", "Dario", "Cora"],
    "Olga": ["Alba", "Dario", "Cora", "Bruno"],
    "Pau":  ["Dario", "Bruno", "Alba", "Cora"],
}


# --- 1. ¿A quién le propone un proponente libre? ---

def siguiente_propuesta(preferencias_proponente, ya_rechazado_por):
    """
    Devuelve el receptor mejor valorado de 'preferencias_proponente' que
    NO esté en el conjunto 'ya_rechazado_por'.

    preferencias_proponente : lista ordenada de más a menos preferido
    ya_rechazado_por         : set de receptores que ya lo rechazaron

    Si no queda ninguna opción disponible, devuelve None.

    Pista: recorre la lista en orden; el primero que no esté tachado es
    la respuesta. Recuerda: un proponente NUNCA propone dos veces a la
    misma persona (por eso miramos 'ya_rechazado_por').
    """
    # Escribe aquí tu código
    pass


# --- 2. ¿Con quién se queda un receptor? ---

def receptor_decide(preferencias_receptor, pretendientes):
    """
    Dado el conjunto de 'pretendientes' (incluye el compromiso provisional
    actual, si lo hay, MÁS las nuevas propuestas de esta ronda), devuelve
    una tupla (elegido, rechazados):

        elegido    : el pretendiente que más prefiere
        rechazados : lista con el resto

    preferencias_receptor : lista ordenada de más a menos preferido
    pretendientes         : lista de proponentes que le proponen

    Pista: el "más preferido" es el que aparece ANTES en
    preferencias_receptor. Puedes usar preferencias_receptor.index(x)
    como clave para min(), o recorrer la lista de preferencias y quedarte
    con el primer pretendiente que encuentres.
    """
    # Escribe aquí tu código
    pass


# --- 3. Simular una ronda completa ---

def simular_una_ronda(prefs_prop, prefs_rec, compromisos, tachados, libres):
    """
    Aplica UNA ronda del cortejo y devuelve el nuevo estado como una tupla
    (compromisos, tachados, libres) YA actualizada.

    Pasos de una ronda:
      a) Cada proponente libre elige a quién proponer con
         siguiente_propuesta(). Agrupa las propuestas por receptor.
      b) Para cada receptor que recibe propuestas, junta sus nuevos
         pretendientes con su compromiso provisional (si tenía) y llama a
         receptor_decide().
      c) Actualiza:
           - compromisos[receptor] = elegido
           - a cada rechazado, márcalo tachado por ese receptor y vuelve
             a ponerlo libre
           - el elegido deja de estar libre

    Pista: trabaja sobre COPIAS de compromisos/tachados/libres para no
    liarte modificando mientras iteras. Empieza construyendo un dict
    {receptor: [proponentes que le proponen esta ronda]}.
    """
    # Escribe aquí tu código
    pass


# --- Pruebas: reproducir la Ronda 1 de la lección ---

if __name__ == "__main__":
    # Estado inicial: todos libres, sin compromisos ni rechazos
    compromisos = {}
    tachados = {p: set() for p in prefs_proponentes}
    libres = list(prefs_proponentes.keys())

    # --- Comprobaciones sueltas de las funciones 1 y 2 ---
    # Alba, sin rechazos, debería proponer a Nora (su primera opción)
    print("Alba propone a:", siguiente_propuesta(prefs_proponentes["Alba"], set()))
    # Mar, con Bruno y Cora compitiendo, debería quedarse con Cora
    print("Mar elige:", receptor_decide(prefs_receptores["Mar"], ["Bruno", "Cora"]))

    # --- Una ronda completa ---
    compromisos, tachados, libres = simular_una_ronda(
        prefs_proponentes, prefs_receptores, compromisos, tachados, libres
    )

    print("\nDespués de la Ronda 1:")
    print("  Compromisos:", compromisos)
    print("  Libres:", libres)

    # Según la lección, tras la Ronda 1 debe quedar:
    #   Alba-Nora, Cora-Mar, Dario-Pau  y  Bruno libre (rechazado por Mar)
    esperado = {"Nora": "Alba", "Mar": "Cora", "Pau": "Dario"}
    if compromisos == esperado and libres == ["Bruno"]:
        print("\n✅ ¡Coincide con la tabla de la Ronda 1 de la lección!")
    else:
        print("\n❌ Todavía no coincide. Repasa las tres funciones.")


# --- Preguntas de reflexión ---
# 1. En simular_una_ronda, ¿por qué es importante juntar el compromiso
#    provisional CON las nuevas propuestas antes de que el receptor decida?
#    ¿Qué pasaría si un receptor ignorara a su pareja provisional?
# 2. ¿Cuántas rondas más harían falta para llegar al matching final que
#    viste en la lección (Alba-Olga, Bruno-Nora, Cora-Mar, Dario-Pau)?
#    Puedes llamar a simular_una_ronda varias veces y verlo.
# 3. Reto: envuelve las llamadas en un bucle `while libres:` para obtener
#    el matching final completo. Acabas de esbozar la lección 8.
