"""
page = a random starting page
article_chain = []
while title of page isn't 'Philosophy' and we have not discovered a cycle:
    append page to article_chain
    download the page content
    find the first link in the content
    page = that link
    pause for a second
"""
import time

search_history = []
target_url = ""

def continue_crawl(search_history, target_url, max_steps=25):
    """
    comprueba que la lista no sea mayor de 25,
    que el link que estas comprobando no este ya en la lista,
    que el link no este repetido dos veces.

    CORREGIDO:
    def continue_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > 25:
        print("The search has gone on suspiciously long; aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen; aborting search!")
        return False
    else:
        return True
    """
    if len(search_history) >  max_steps:
        print ("Demasiados links en la busqueda...")
        return False
    elif target_url in search_history:
        print ("el link buscado ya estaba antes en lista, bucle...")
        return False
    elif len(search_history) > 1:
        for link in search_history:
            if link in search_history:
                print ("devuelve falso por que...")
                return False
    else:
        return True

def find_first_link(article):




while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article_chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)






#if continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],'https://en.wikipedia.org/wiki/Philosophy'):
#    print ("devuelve verdad")
#else:
#    print ("devuelve falso")
