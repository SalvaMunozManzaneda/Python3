def message(prize):
    print("Congratulations! You have won a {} !".format(prize))

def which_price(points):
    """
    Returns the prize-winning message, given a number of points
    """
    if points <= 50:
        message("wooden rabbit")
    elif points <= 150:
        message("Oh dear, no prize this time.")
    elif points <= 180:
        message("wafer-thin mint")
    elif points <= 200:
        message("penguin")
    else:
        print("Numero incorrecto.")



which_price(180)
