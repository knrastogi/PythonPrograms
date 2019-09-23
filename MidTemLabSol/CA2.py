##Q2. Write a program to display data types of values entered by user.
#############################################################################################################
##Program Objective: to display data types of values entered by user.                                      ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

data = eval(input("Enter any type of data:[Int, Float, String, List, Tuple, Dict, Set etc]:"))                                      
print("The datatype of your data is {}".format(type(data)))
print("Your data is stored at {} location in memory".format(id(data)))
