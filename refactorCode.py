def comprobar(respuestas, soluciones):
    """
    respuestas seran las respuestas dadas, y soluciones las correctas.
    en el codigo de abajo comprobaremos una por una si coincide la respuestas
    con la solucion.
    """
    results = []
    for numeroPregunta in range(len(respuestas)):
        if respuestas[numeroPregunta] == soluciones[numeroPregunta]:
            results.append(True)
        else:
            results.append(False)
    return results

def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results = comprobar(my_answers, answers)

    count_correct = 0
    for result in results:
        if result == True:
            count_correct += 1

    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    else:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
