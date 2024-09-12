from generador_temperaturas import generar_temperaturas  # Importa la función que genera las temperaturas aleatorias

# Definir los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def obtener_datos_temperaturas():
    """
    Función que genera temperaturas aleatorias para los días de la semana.

    :return: Una lista de diccionarios donde cada diccionario contiene el día y la temperatura correspondiente.
    """
    # Generar temperaturas aleatorias para 7 días de la semana
    results_temperaturas = generar_temperaturas(num_dias=len(dias_semana))

    # Crear la lista de diccionarios con los días y las temperaturas
    datos_temperaturas = [{"day": dia, "temp": temp} for dia, temp in zip(dias_semana, results_temperaturas)]

    return datos_temperaturas


# Diccionario que almacena las temperaturas por ciudad y semana
# Cada ciudad contiene una lista de semanas, y cada semana tiene una lista de temperaturas diarias
temperaturas = {
    "Quito": [
        [obtener_datos_temperaturas()],  # Semana 1
        [obtener_datos_temperaturas()],  # Semana 2
        [obtener_datos_temperaturas()],  # Semana 3
        [obtener_datos_temperaturas()],  # Semana 4
    ],
    "Guayaquil": [
        [obtener_datos_temperaturas()],  # Semana 1
        [obtener_datos_temperaturas()],  # Semana 2
        [obtener_datos_temperaturas()],  # Semana 3
        [obtener_datos_temperaturas()],  # Semana 4
    ],
    "Cuenca": [
        [obtener_datos_temperaturas()],  # Semana 1
        [obtener_datos_temperaturas()],  # Semana 2
        [obtener_datos_temperaturas()],  # Semana 3
        [obtener_datos_temperaturas()],  # Semana 4
    ]
}


# Función que calcula el promedio de temperaturas de una ciudad durante varias semanas
def calcular_promedio_temperaturas(temperaturas_por_ciudad):
    """
    Calcula el promedio de temperatura de una ciudad durante varias semanas.

    :param temperaturas_por_ciudad: Diccionario que contiene las temperaturas organizadas por ciudad,
                                    semana y día de la semana.
    :return: Diccionario con los promedios de temperatura por ciudad.
    """
    # Diccionario para almacenar los promedios calculados para cada ciudad
    promedios_ciudades = {}

    # Recorrer cada ciudad en el diccionario
    for ciudad, semanas in temperaturas_por_ciudad.items():
        suma_total = 0  # Acumula la suma total de temperaturas para una ciudad
        cantidad_dias_total = 0  # Cuenta el número total de días para los que se tiene temperatura

        # Recorrer cada semana en la ciudad
        for semana in semanas:
            for dia in semana[0]:  # Iterar sobre los días de la semana (semana[0] es la lista de días)
                suma_total += dia["temp"]  # Sumar la temperatura del día
                cantidad_dias_total += 1  # Aumentar el contador de días

        # Calcular el promedio de la ciudad
        promedio = suma_total / cantidad_dias_total
        promedios_ciudades[ciudad] = promedio  # Almacenar el promedio de la ciudad en el diccionario

    return promedios_ciudades


# Función para mostrar los resultados de los promedios calculados
def mostrar_resultados(temperaturas):
    """
    Muestra los promedios de temperatura semanales para cada ciudad.

    :param temperaturas: Diccionario que contiene las temperaturas por ciudad, semana y día.
    """
    # Calcular los promedios totales de temperatura por ciudad
    promedios_ciudad = calcular_promedio_temperaturas(temperaturas)

    # Mostrar los resultados
    print("Promedios de temperatura por ciudad:")
    for ciudad, promedio in promedios_ciudad.items():
        print(f"{ciudad}: {promedio:.2f}°C")


# Llamada a la función para mostrar los resultados finales
mostrar_resultados(temperaturas)
