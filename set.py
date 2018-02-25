def remove_duplicates(lista):
    """
    Elimina duplicados de una lista.
    """
    target = []
    for element in lista:
        #si no esta dentro de la lista nueva se añade.
        if element not in target:
            target.append(element)
    return target


def most_prolific(diccionario):
    release = {}
    year = 0
    for disco in diccionario:
        if diccionario.get(disco) in release:
            release[diccionario.get(disco)] += 1
        else:
            release[diccionario.get(disco)] = 1
    for anio in release:
        if release.get(anio) > year: #comprobar el numero sacar el año.
            year == release.get(anio)
    return year

    

    def most_prolific(discs):
#We will store a dictionary of years
#and number of albums per year
    years = {}
    maxyears = []
    maxnumber = 0
    for disc in discs:
        year = discs[disc]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

#find the year in which the maximum
#number of albums was published
#there are more elegant ways of accomplishing this,
#but the code below works
    for year in years:
        if years[year] > maxnumber:
            maxyears=[]
            maxyears.append(year)
            maxnumber = years[year]
        elif years[year] == maxnumber and not (year in maxyears):
            maxyears.append(year)
    if (len(maxyears) == 1):
        return maxyears[0]
    else:
        return maxyears
