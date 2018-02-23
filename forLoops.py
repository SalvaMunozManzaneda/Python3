def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for number in input_list:
        sum += number

    return sum



#These test cases check that list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))

"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and ends with a right angle bracket ">".
"""
#TODO: Define the tag_count function
def tag_count(palabras):
    for palabra in palabras:
        if "<" in palabra and ">" in palabra:
            print(palabra)



# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))


#TODO: Implement the nearest_square function
def nearest_square(limite):
    """
    The function takes an integer argument limit, and returns the largest
    square number that is less than limit. A square number is the product
    of an integer multiplied by itself, for example 36 is a square number
    because it equals 6*6.
    """
    num = 1
    while (num * num) <= limite:
        ultimo_valido = num * num
        num += 1

    return ultimo_valido

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))


headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs


for phrase in headlines:
    if len(news_ticker) + len(phrase) <= 140:
        news_ticker = news_ticker + " " + phrase
    else:
        break


print(len(news_ticker))
