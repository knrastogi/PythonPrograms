##Q6. Write a program to take two inputs from user in a single input() function and perform all relational operations on them.




#############################################################################################################
##Program Objective: to calculate the square root and power of a user inputted no. without using any fun   ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------")
num1, num2 = [int(x) for x in input("Enter two numbers:").split()]
print("Here is the relations between your numbers")
print("{} is > {} : {}".format(num1, num2, num1 > num2))
print("{} is < {} : {}".format(num1, num2, num1 < num2))
print("{} is == {} : {}".format(num1, num2, num1 == num2))
print("{} is != {} : {}".format(num1, num2, num1 != num2))
print("{} is >= {} : {}".format(num1, num2, num1 >=  num2))
print("{} is <= {} : {}".format(num1, num2, num1 <= num2))


print("--------------------------------------------------")

