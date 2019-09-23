##Q4. Calculate the area of circle using Pi value and pow function of math module.


#############################################################################################################
##Program Objective: to Calculate the area of circle using Pi value and pow function of math module.       ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

from math import pi, pow
print("--------------------------------------------------")
readiusOfCir = float(input("Enter radius of circle:"))
areaOfCir  =  pi * pow(readiusOfCir,2)
print("Area of circle: {}".format(areaOfCir))
print("--------------------------------------------------")

