##Q5.Write a program to calculate the total amount of money in the piggybank given the coins of Rs 10, Rs 5, Rs 2, Rs 1, 50 Paisa and 25 Paisa.



##########################################################################
##Program Objective: to count total money in piggybank.                 ##
##Coded by: KNR                                                         ##
##Date: 17/09/2019 22:20                                                ##
##Lang: Python 3.7.4                                                    ##
##Version: 1.0                                                          ##
##########################################################################

print("--------------------------------------------------")
noOf10R = int(input("Enter no. of 10 rupess coins:"))
noOf5R = int(input("Enter no. of 5 rupess coins:"))
noOf2R = int(input("Enter no. of 2 rupess coins:"))
noOf1R = int(input("Enter no. of 1 rupess coins:"))
noOf50P = int(input("Enter no. of 50 paise coins:"))
noOf25P = int(input("Enter no. of 25 paise coins:"))


totalMoney = noOf10R * 10 + noOf5R * 5 + noOf2R * 2 + noOf1R * 1 + noOf50P * 0.5 + noOf25P * .25
print("The Total Money in you Piggybank is {0}".format(totalMoney))
print("--------------------------------------------------")

