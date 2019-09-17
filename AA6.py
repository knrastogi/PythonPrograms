##Q6.Write  a program to solve quadratic equation.


##########################################################################
##Program Objective: to solve quadratic equation                        ##
##Coded by: KNR                                                         ##
##Date: 17/09/2019 22:20                                                ##
##Lang: Python 3.7.4                                                    ##
##Version: 1.0                                                          ##
##########################################################################
from math import sqrt
print("--------------------------------------------------")
a,b,c = [int(x) for x in input("Enter all three coefficients of the quadratic equation separated by comma").split(",")]
D = b*b - (4*a*c)
sqrtD = sqrt(D)
x1= (-b + sqrtD)/2 * a
x2= (-b - sqrtD)/2 * a
print("The Qudaratic Equation is:")
print("{}x^2 +{}x + {} = 0".format(a,b,c))
print("Roots of Quadratic Equation are:", x1, x2)
print("--------------------------------------------------")

