def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:#abrimos el archivo

        for line in f:
            #sacamos toda la linea (y guardada en un list cada bloque
            #separado por una coma) Ej:['Graham Chapman',
            #'  Various / ... (46 episodes', ' 1969-1974)\n']
            line_data = line.split(',')
            #print(line_data)
            #aqui solo cogemos el nombre que es el primer elemento.
            #append para no borrar lo que ya ahi
            cast_list.append(line_data[0])

    return cast_list

print (create_cast_list('flying_circus_cast.txt'))
