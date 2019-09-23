##Q3. Write a program to create a simple calculator to perform all arithmetic operations.


#############################################################################################################
##Program Objective: to create a simple calculator to perform all arithmetic operations.                   ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################




num1, num2 = [int(x) for x in input("Enter two nos for arithmetic operation").split()]

print("Addition:", num1+num2)
print("Subtration:", num1-num2)
print("Multiplication:", num1*num2)
print("Division:", num1/num2)
print("Modulus:", num1%num2)
print("Exponetial:", num1**num2)
print("Floor Division:", num1//num2)
