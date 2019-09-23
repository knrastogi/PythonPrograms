##Q5. Write a program to convert a temperature given in Fahrenheit to centigrade and vice versa


#############################################################################################################
##Program Objective: to convert a temperature given in Fahrenheit to centigrade and vice versa             ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("Fahrenheit to centigrade")
print("Enter the temperature in Fahrenheit", end=":")
fht = float(input())
celc = (fht-32)*5/9
print("{} Fahrenheit = {} Centigrade".format(fht,celc) )
print("centigrade to Fahrenheit")
print("Enter the temperature in centigrade", end=":")
celc= float(input())
fht  = celc*9/5 +32
print("{} Centigrade = {} Fahrenheit ".format(celc,fht) )
print("--------------------------------------------------")

