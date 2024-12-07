# game_logic.py

import random

def generar_cartas(n_pares=8):
    """
    Genera una lista de operaciones matemáticas en pares.
    Cada par contiene dos operaciones diferentes que resultan
    en el mismo resultado.
    """
    cartas = []
    for _ in range(n_pares):
        resultado = random.randint(2, 20)
        
        # Generar una operación de suma
        a = random.randint(1, resultado - 1)
        op_suma = f"{a} + {resultado - a}"
        
        # Generar una operación de multiplicación que tenga el mismo resultado
        # Intentamos varios factores
        factores = [(x, resultado // x) for x in range(1, resultado+1) if resultado % x == 0]
        if factores:
            x, y = random.choice(factores)
            op_mult = f"{x} × {y}"
        else:
            # Si no encontramos factores exactos (poco probable con este rango),
            # generamos otra suma
            b = random.randint(1, resultado - 1)
            op_mult = f"{b} + {resultado - b}"
        
        cartas.append((op_suma, resultado))
        cartas.append((op_mult, resultado))
    
    # Mezclamos todas las cartas
    random.shuffle(cartas)
    # Devolvemos solo las operaciones en orden, sin el resultado directamente,
    # lo guardamos por separado si es necesario
    # Aquí cada elemento es (operación, resultado), pero en la GUI usaremos la operación.
    return cartas

def comparar_resultados(cartas, idx1, idx2):
    """
    Compara el resultado de las dos cartas seleccionadas.
    Recibe la lista de cartas completa y los índices de las cartas.
    Cada carta es una tupla (operación, resultado).
    Retorna True si forman par, False en caso contrario.
    """
    return cartas[idx1][1] == cartas[idx2][1]
