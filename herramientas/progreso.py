"""
Seguimiento de progreso del curso, en modo texto (sin gráficos).

Cada ejercicio que verifica su solución con asserts llama a
registrar_completado() justo después de confirmarla. Los datos se guardan
en personal/progreso.json (fuera de git: tu avance es tuyo).

Para ver el resumen completo:

    python -m herramientas.progreso
"""

import json
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIR_EJERCICIOS = RAIZ / "ejercicios"
DIR_PERSONAL = RAIZ / "personal"
FICHERO_PROGRESO = DIR_PERSONAL / "progreso.json"

MODULOS = {
    "fundamentos": "Módulo 1 — Fundamentos",
    "algoritmos": "Módulo 2 — Algoritmos",
    "matching": "Módulo 3 — Matching",
    "funcional": "Módulo 4 — Funcional",
}

ANCHO_BARRA = 20


def _cargar():
    if not FICHERO_PROGRESO.exists():
        return {"completados": {}, "racha": {"ultima_fecha": None, "dias": 0}}
    return json.loads(FICHERO_PROGRESO.read_text(encoding="utf-8"))


def _guardar(datos):
    DIR_PERSONAL.mkdir(exist_ok=True)
    FICHERO_PROGRESO.write_text(
        json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def _clave(ruta_ejercicio):
    ruta = Path(ruta_ejercicio).resolve()
    return f"{ruta.parent.name}/{ruta.name}"


def _ejercicios_de(modulo):
    carpeta = DIR_EJERCICIOS / modulo
    if not carpeta.exists():
        return []
    return sorted(
        p for p in carpeta.glob("*.py")
        if "registrar_completado" in p.read_text(encoding="utf-8")
    )


def _actualizar_racha(datos, hoy):
    racha = datos["racha"]
    ultima = racha["ultima_fecha"]
    if ultima == hoy.isoformat():
        return
    if ultima and date.fromisoformat(ultima).toordinal() == hoy.toordinal() - 1:
        racha["dias"] += 1
    else:
        racha["dias"] = 1
    racha["ultima_fecha"] = hoy.isoformat()


def registrar_completado(ruta_ejercicio):
    """Llamar justo después de confirmar que un ejercicio pasó sus asserts."""
    datos = _cargar()
    clave = _clave(ruta_ejercicio)
    ya_estaba = clave in datos["completados"]

    if not ya_estaba:
        datos["completados"][clave] = datetime.now().isoformat(timespec="seconds")
        _actualizar_racha(datos, date.today())
        _guardar(datos)

    modulo = Path(ruta_ejercicio).resolve().parent.name
    total_modulo = len(_ejercicios_de(modulo))
    hechos_modulo = sum(1 for k in datos["completados"] if k.startswith(f"{modulo}/"))
    nombre_modulo = MODULOS.get(modulo, modulo)

    if ya_estaba:
        print(f"(ya lo tenías registrado — {nombre_modulo}: {hechos_modulo}/{total_modulo})")
        return

    print(f"\n🏅 +1 ejercicio — {nombre_modulo}: {hechos_modulo}/{total_modulo}")
    if datos["racha"]["dias"] > 1:
        print(f"🔥 Racha: {datos['racha']['dias']} días seguidos")
    if hechos_modulo == total_modulo:
        print(f"🏆 ¡Módulo completado! ({nombre_modulo})")


def _barra(hechos, total):
    if total == 0:
        return "[" + "-" * ANCHO_BARRA + "] 0/0"
    llenas = round(ANCHO_BARRA * hechos / total)
    return f"[{'#' * llenas}{'-' * (ANCHO_BARRA - llenas)}] {hechos}/{total}"


def _siguiente_pendiente(datos, modulo):
    for ejercicio in _ejercicios_de(modulo):
        if _clave(ejercicio) not in datos["completados"]:
            return ejercicio.relative_to(RAIZ)
    return None


def resumen():
    datos = _cargar()
    total_hechos = len(datos["completados"])
    total_ejercicios = sum(len(_ejercicios_de(m)) for m in MODULOS)

    print("=" * 60)
    print("PROGRESO DEL CURSO — Aprendiendo Python")
    print("=" * 60)

    for modulo, nombre in MODULOS.items():
        ejercicios = _ejercicios_de(modulo)
        hechos = sum(1 for e in ejercicios if _clave(e) in datos["completados"])
        print(f"{nombre:<26}{_barra(hechos, len(ejercicios))}")

    print("-" * 60)
    nivel = total_hechos // 5 + 1
    print(f"Nivel {nivel}  —  {total_hechos}/{total_ejercicios} ejercicios completados")

    racha = datos["racha"]["dias"]
    if racha:
        print(f"Racha actual: {racha} día(s) seguidos")

    for modulo in MODULOS:
        siguiente = _siguiente_pendiente(datos, modulo)
        if siguiente:
            print(f"Siguiente recomendado: {siguiente}")
            break
    else:
        print("¡Todos los ejercicios con verificación están completados!")

    print("=" * 60)


if __name__ == "__main__":
    resumen()
