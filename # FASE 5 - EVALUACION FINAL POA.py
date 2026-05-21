# FASE 5 - EVALUACION FINAL POA
# Programa realizado en Python
#
# Autoría propia:
# Laura Geraldin Martínez Camacho
# Curso: Fundamentos de Programación
# Grupo: 213022_459
# Universidad Nacional Abierta y a Distancia - UNAD
# =========================================================


# Matriz con la información de las sesiones
# Formato:
# [ID Cliente, Duración, Clics]

sesiones = [
    [101, 240, 12],
    [102, 45, 2],
    [103, 250, 10],
    [104, 300, 15],
    [105, 70, 1]
]


# Función para clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Mostrar informe final
print("==========================================")
print(" INFORME DE CLASIFICACION DE SESIONES ")
print("==========================================")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("\nID Cliente:", id_cliente)
    print("Duracion:", duracion, "segundos")
    print("Cantidad de clics:", clics)
    print("Nivel de compromiso:", clasificacion)

print("\nFin del informe")
