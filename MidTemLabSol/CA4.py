##Q4. List all the functions and constants of math module.



#############################################################################################################
##Program Objective: to List all the functions and constants of math module.                               ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("------------------------------------------------------------------------------------")
import math
print("Here is the contents of math module:")
print(dir(math))
print("Lets print this one by one:")
print("------------------------------------------------------------------------------------")
for i in dir(math):
    print(i,  end= "\t")
print("------------------------------------------------------------------------------------")

