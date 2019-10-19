'''
Write a program to roll a dice for as much time as the user wishes to. 

Hints: 
    import random module. 
    Take help about a function in the random module which generates random numbers.
    A dice has 6 sides consisting of values 1-6.
    Use indefinite loop.
'''


import random
min = 1
max = 6
roll_again = input("I am ready. Do you want to roll the dices? (yes/y or no/n):")


while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Roll the dices again? (yes/y or no/n):")
else:
    print ("Ok, Bye! Take Care")

