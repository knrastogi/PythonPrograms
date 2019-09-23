##Q3. Write a program to calculate area of a triangle whose three sides are entered by user.


#############################################################################################################
##Program Objective: to calculate area of a triangle whose three sides are entered by user                 ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################
import math
print("--------------------------------------------------")
side1, side2, side3 = [int(x) for x in input("Enter all three sides of the triangle separated by (,):").split(",")]
s = side1 + side2 + side3
areaOfTraiangle = math.sqrt(s * (s - side1)* (s - side2) * (s - side3)) # Heron's Formulla
print("Area of triangle: {}".format(areaOfTraiangle))
print("--------------------------------------------------")

