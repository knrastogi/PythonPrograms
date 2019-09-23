##Q2. Momentum is calculated as e=mc2., where m is the mass of the object and c is its velocity. Write a program that accepts an object’s mass (in KG)
#and velocity (in Meters per sec) and displays its momentum.


#############################################################################################################
##Program Objective: e=mc2                                                                                 ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------")
print("Enter the mass of the object (in KG)", end = ":")
mass = float(input())
print("Enter the mass of the object in Meters per sec)", end = ":")
velocity = float(input())
momentum = mass * velocity**2
print("Momentum is: {}".format(momentum))

print("--------------------------------------------------")

