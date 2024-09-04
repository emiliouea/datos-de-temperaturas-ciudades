# generador_temperaturas.py

import random

def generar_temperaturas(num_dias=7, temp_min=60, temp_max=100):
    """
    Genera una lista de temperaturas aleatorias.

    Parámetros:
    num_dias (int): Número de días para los que se generarán las temperaturas.
    temp_min (int): Temperatura mínima posible.
    temp_max (int): Temperatura máxima posible.

    Retorna:
    list: Lista de temperaturas aleatorias.
    """
    temperaturas = [random.randint(temp_min, temp_max) for _ in range(num_dias)]
    return temperaturas

