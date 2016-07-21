#hit fn - f5 to run program

import math
import random

def test(input_value):
    return input_value * 2

def main():
    something = 7.5
    something = test(something)
    print(something)

    #Print a pseudo-random value
    #Initialized with a seed (date and time)
    #We can initialize with our own seed (100)
    random.seed(100)
    #If we initialize with 100, we will always get the SAME 'random' number
    
    print(random.randint(1, 6))

main()
