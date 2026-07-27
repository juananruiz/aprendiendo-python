candidatos = {
    "Sofía":  {"nota": 88, "preferencia_destinos": ["Madrid", "Bilbao", "Toledo", "Girona"]},
    "Miguel": {"nota": 72, "preferencia_destinos": ["Bilbao", "Girona", "Toledo", "Madrid"]},
    "Lucía":  {"nota": 95, "preferencia_destinos": ["Madrid", "Girona", "Bilbao", "Toledo"]},
    "Jorge":  {"nota": 65, "preferencia_destinos": ["Toledo", "Bilbao", "Madrid", "Girona"]},
    "Elena":  {"nota": 80, "preferencia_destinos": ["Girona", "Madrid", "Toledo", "Bilbao"]},
}

#candidatos_ord = sorted(candidatos.items(), key=lambda item: item[1]["nota"], reverse=True)

#for nombre, datos in candidatos.items():
#    print(nombre, datos["nota"])

# for valores in candidatos.values():
#     for claves, valores in valores.items():
#         print(f"{claves}: {valores}")

# Es como si candidatos.values() devolviera un conjunto con 
# nota: 88, preferencia_destinos: ['Madrid', 'Bilbao', 'Toledo', 'Girona'], nota: 72, preferencia_destinos: ['Bilbao', 'Girona', 'Toledo', 'Madrid'], ...


candidatos = [
    {"nombre": "Ana",     "nota": 85, "edad": 30},
    {"nombre": "Carlos",  "nota": 85, "edad": 28},
    {"nombre": "Beatriz", "nota": 78, "edad": 32},
]

# Ordena por nombre, por nota y por edad
print(sorted(candidatos, key = lambda x: x["nombre"]))
print(sorted(candidatos, key = lambda x: x["nota"], reverse=True))

# Ordena por nota y luego por edad (nota más alta y edad mas baja)
print(sorted(candidatos, key = lambda x: (-x["nota"], x["edad"])))

# Ordena por nota y luego por nombre (nota más alta y nombre mas "bajo")
print(sorted(candidatos, key = lambda x: (x["nota"], x["nombre"])))

# Mezcla de criterios (nota descendente, nombre ascendente)
# print(sorted(candidatos, key = lambda x: (x["nota"], -x["nombre"]))) # Esto no funcionaría
# Aquí no sirve un único reverse=True porque invierte todo. 
# Haz dos ordenaciones estables:
# Secundario (nombre ascendente)
tmp = sorted(candidatos, key=lambda d: d["nombre"])
# Primario (nota descendente)
ordenados = sorted(tmp, key=lambda d: d["nota"], reverse=True)

print(ordenados)