##Q5. Python Program to calculate the square root and power of a user inputted no. without using any function.


#############################################################################################################
##Program Objective: to calculate the square root and power of a user inputted no. without using any fun   ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------")
num = int(input("Enter your number to calculate square root:"))
sqrtNum =  num ** 0.5
pwr = int(input("Enter power:"))
pwrVal = num ** pwr
print("Square root of {} = {}".format(num, sqrtNum))
print("{} to the power {}= {}".format(num, pwr, pwrVal))

print("--------------------------------------------------")

