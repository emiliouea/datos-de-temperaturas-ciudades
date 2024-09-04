from generador_temperaturas import generar_temperaturas;

# Días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def obtener_datos_temperaturas():
    # Generar temperaturas aleatorias
    results_temperaturas = generar_temperaturas(num_dias=len(dias_semana))

    # Crear la lista de diccionarios
    datos_temperaturas = [{"day": dia, "temp": temp} for dia, temp in zip(dias_semana, results_temperaturas)]

    return datos_temperaturas




# Definición de la matriz 3D con ciudades ecuatorianas
temperaturas = {
    "Quito": [
        [  # Semana 1
           obtener_datos_temperaturas(),
        ],
        [  # Semana 2
            obtener_datos_temperaturas(),
        ],
        [  # Semana 3
            obtener_datos_temperaturas(),
        ],
        [  # Semana 4
            obtener_datos_temperaturas(),
        ]
    ],
    "Guayaquil": [
        [  # Semana 1
            obtener_datos_temperaturas(),
        ],
        [  # Semana 2
            obtener_datos_temperaturas(),
        ],
        [  # Semana 3
            obtener_datos_temperaturas(),
        ],
        [  # Semana 4
            obtener_datos_temperaturas(),
        ]
    ],
    "Cuenca": [
        [  # Semana 1
            obtener_datos_temperaturas(),
        ],
        [  # Semana 2
            obtener_datos_temperaturas(),
        ],
        [  # Semana 3
            obtener_datos_temperaturas(),
        ],
        [  # Semana 4
            obtener_datos_temperaturas(),
        ]
    ]
}


# Función para calcular promedios
def calcular_promedios(temperaturas, ciudad):
    semanas = temperaturas[ciudad]
    promedios_ciudad = []

    for semana in semanas:
        suma_temperaturas = sum(dia["temp"] for dia in semana[0])  # Sumar todas las temperaturas de la semana
        cantidad_dias = len(semana[0])
        promedio = suma_temperaturas / cantidad_dias
        promedios_ciudad.append(promedio)

    return promedios_ciudad


# Función para mostrar resultados
def mostrar_resultados(temperaturas):
    for ciudad in temperaturas.keys():
        promedios_ciudad = calcular_promedios(temperaturas, ciudad)
        print(f"Ciudad: {ciudad}")

        for semana in range(len(promedios_ciudad)):
            print(f"  Semana {semana + 1}: Promedio = {promedios_ciudad[semana]:.2f}°C")


# Mostrar resultados
mostrar_resultados(temperaturas)
