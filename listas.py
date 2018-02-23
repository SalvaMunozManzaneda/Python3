#Listas/Arrays
def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return days_in_month[month_number - 1]

# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))

#Slicing listas/trozos de Listas
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


recents = eclipse_dates[-3:]  #los tres ultimos
# TODO: Modify this line so it prints the last three elements of the list
#print(eclipse_dates)
print(recents)


#define the  html_list function
def html_list(argument):
    #CODE
    print("<ul>");
    for palabra in argument:
        print("<li>" + palabra + "</li>");
    print("</ul>");

html_list(['first string', 'second string']);

def starbox(width, height):
    """print a box made up of asterisks.
    
    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box

    # print sides of box
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")

    print("*" * width) #print bottom edge of box
