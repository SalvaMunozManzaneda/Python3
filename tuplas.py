def hours2days(hours):
    """
    Devuelve una TUPLA con los dias y las horas de una cantidad de horas
    determinada. 25h = 1 dia 1 hora.
    """
    dias = hours / 24
    horas = hours % 24
    return dias, horas
