'''
Random Number Chooser

Chooses 3 random numbers from a list of n numbers

'''
import random


# Give the function params if it's not going to take in an input from the user's i/o
def random_number(n: int):
    # Take an input for the number of goals
    # n = int(input("How many goals do you currently have active (ex: 5): "))
    
    # Map/Enum the value of n to an empty list
    options = list(range(1, n+1))
    # print(options)

    # Check if the input is greater than 3
    if n > 3:
        result = random.sample(options, k=3)
        print(result)
    else:
        print(options)
    # If greater, choose 3 random ints from 1 to `n`, else return 1 to `n`


# Loop to test how random.sample() is different from random.choices()    
for i in range(50):
    random_number(1)
    # With choices, numbers repeat, with random, once a number is chosen, it doesn't repeat
