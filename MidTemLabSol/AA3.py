##Q3. Write a program to calculate SI and compound interest.


##########################################################################
##Program Objective: to calculate SI and compound interest              ##                      ##
##Coded by: KNR                                                         ##
##Date: 17/09/2019 22:20                                                ##
##Lang: Python 3.7.4                                                    ##
##Version: 1.0                                                          ##
##########################################################################

print("----------------------------------------------------------------------------------------------------")
print("\t\t\t\tSimple Interest")
print("----------------------------------------------------------------------------------------------------")
principleAmt = int(input("Enter Principle Amount:"))
timeDuration = int(input("Enter duration of deposite:"))
rateOfInterest = float(input("Enter Rate of Interest:"))
simpleInterest = (principleAmt * rateOfInterest * timeDuration) / 100
print("The Simple Interest earned: ₹ %8.2f" %(simpleInterest))
print("----------------------------------------------------------------------------------------------------")

print("----------------------------------------------------------------------------------------------------")
print("\t\t\t\tCompound Interest")
print("----------------------------------------------------------------------------------------------------")
principleAmt = int(input("Enter Principle Amount:"))
timeDuration = int(input("Enter duration of deposite:"))
rateOfInterest = float(input("Enter Rate of Interest:"))
compoundInterest = (principleAmt * (1 + rateOfInterest/100) ** timeDuration) - principleAmt
print("The Compound Interest earned: ₹ %8.2f" %(compoundInterest))
print("----------------------------------------------------------------------------------------------------")

