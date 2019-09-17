##Q2. Write a program to calculate bike’s average consumption from the given total distance (integer value) traveled (in km) and spent fuel (in liters, float number – 2 decimal point).
#############################################################################################################
##Program Objective: to find out the average of a vehicle                                                  ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

dist = int(input("Input total distance in km:"))                                      
ltr = int(input("Input total fuel spent in liters:"))
          
print("Average consumption (km/lt) -> %5.2f" %(dist/ltr)) 
