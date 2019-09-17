##Q6. Write a program to print name, age and percentage using format specifier as per following format:
##    Name: 20 left justified
##    Age: 20 right justified
##    Percent: 5.2 left justified in print() with %(format specifier)


#############################################################################################################
##Program Objective: formatted output                                                                      ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------------------------------------------------------------------------------------------------")
yourName = input("Enter your name:")
yourAge = int(input("Enter your age:"))
yourPer = float(input("Enter your percentage:"))
print("Name\t\t\t\t\t\t\tAge\t\t\tPercentage")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("%-20s\t\t\t%20d\t\t\t%-5.2f" %(yourName,yourAge,yourPer))
print("--------------------------------------------------------------------------------------------------------------------------------------------")



