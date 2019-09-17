##Q4. Write a program to calculate the distance between the two points.



#############################################################################################################
##Program Objective: to calculate the distance between the two points.                                     ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------")
x1,y1 = [int(i) for i in input("Enter coordinates of first point:").split(",")]
x2,y2 = [int(i) for i in input("Enter coordinates of second point:").split(",")]
dist = ((x2-x1)**2 - (y2-y1)**2) ** 0.5
print("Distnace between two points are %8.2f:" %dist)
print("--------------------------------------------------")

