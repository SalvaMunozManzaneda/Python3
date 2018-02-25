def total_takings(monthly_takings):
    """
    Suma el total de beneficios de cada mes.
    """
    suma = 0
    for clave, valor in monthly_takings.items():# iterar los item del diccionario
        for cadaValor in valor: # iterar los elementos
            suma += cadaValor # sumar los elementos y guardarlos
    return suma

#otra forma.
def total_takings(monthly_takings):
    #total is used to sum up the monthly takings
    total = 0
    for month in monthly_takings.keys():
        #I use the Python function sum to sum up over
        #all the elements in a list
        total = total + sum(monthly_takings[month])
    return total
