##Q4. Write a program to find factorial of a number entered by user.



#############################################################################################################
##Program Objective: to find factorial of a number entered by user.                                        ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################


##Method-1: Using for loop

##n= int(input("Enter a number to calculate is factorail:"))
##if n < 0:
##    print("There is no factorial of -ve values.")
##elif n == 1 or n == 0:
##    print("The factorial is 1")
##else:
##fact = 1
##n= int(input("Enter a number to calculate is factorail:"))
##for x in range(n,0,-1):
##	fact *= x
##print("The factorial is", fact)


##Method-2: Using while loop

##n= int(input("Enter a number to calculate is factorail:"))
##if n < 0:
##    print("There is no factorial of -ve values.")
##elif n == 1 or n == 0:
##    print("The factorial is 1")
##else:
##    fact = 1
##    i = 1
##    while i<= n:
##        fact *= i
##        i+=1
##    print("The factorial of %d is %d" %(n,fact))

##Method-2: Fact() of math module

from math import factorial
n= int(input("Enter a number to calculate is factorail:"))
print("The factorial of %d is %d" %(n,factorial(n)))
