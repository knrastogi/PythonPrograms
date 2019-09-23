##Q3. Create a program to determine the larger of two numbers.


#############################################################################################################
##Program Objective: to determine the larger of two numbers                                                ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################



print("--------------------------------------------------")
numA, numB = [eval(x) for x in input("Enter two nos:").split()]

if numA > numB:
    print("{} is greater than {}".format(numA,numB))
else:
    print("{} is greater than {}".format(numB,numA))
print("--------------------------------------------------")

