##Q2. Write a program to swap two no. 


##########################################################################
##Program Objective: to swap two no.                                    ##
##Coded by: KNR                                                         ##
##Date: 17/09/2019 22:20                                                ##
##Lang: Python 3.7.4                                                    ##
##Version: 1.0                                                          ##
##########################################################################


### Method-1: Using multiple assignment
##print("--------------------------------------------------")
##num1 = int(input("Enter number #1:"))
##num2 = int(input("Enter number #2:"))
##print("Before swapping A: {0}, B: {1}".format(num1, num2))
##num1, num2 = num2, num1
##print("After swapping A: {0}, B: {1}".format(num1, num2))
##print("--------------------------------------------------")


### Method-2: Using a temporary variable
##print("--------------------------------------------------")
##num1 = int(input("Enter number #1:"))
##num2 = int(input("Enter number #2:"))
##print("Before swapping A: {0}, B: {1}".format(num1, num2))
##temp = num1
##num1 = num2
##num2 = temp
##print("After swapping A: {0}, B: {1}".format(num1, num2))
##print("--------------------------------------------------")


###Method-3: Without using a temporary variable v1
##print("--------------------------------------------------")
##num1 = int(input("Enter number #1:"))
##num2 = int(input("Enter number #2:"))
##print("Before swapping A: {0}, B: {1}".format(num1, num2))
##num1 = num1 + num2
##num2 = num1 - num2
##num1 = num1 - num2
##print("After swapping A: {0}, B: {1}".format(num1, num2))
##print("--------------------------------------------------")

# Method-4: Without using a temporary variable v2
print("--------------------------------------------------")
num1 = int(input("Enter number #1:"))
num2 = int(input("Enter number #2:"))
print("Before swapping A: {0}, B: {1}".format(num1, num2))
num1 = num1 * num2
num2 = num1 // num2
num1 = num1 // num2
print("After swapping A: {0}, B: {1}".format(num1, num2))
print("--------------------------------------------------")
