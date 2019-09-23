##Q3. Write a program to calculate volume of a box.


#############################################################################################################
##Program Objective: to calculate volume of a box.                                                         ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------")
l,b,h = [eval(x) for x in input("Enter three sides of the box").split()]
volumeOfBox = l*b*h
print("The volume of the box is: {}".format(volumeOfBox))
print("--------------------------------------------------")

