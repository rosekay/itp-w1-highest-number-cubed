"""This is the entry point of the program."""


def highest_number_cubed(limit):
    #the highest number cubed that is still less than the input 'limit'
    number = 1
    while number ** 3 < limit:
        number += 1
        if number ** 3 > limit:
            return number-1
    

    
