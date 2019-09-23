##Q6. List all the built in functions of python.


#############################################################################################################
##Program Objective: to list all the built in functions of python.                                      ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("------------------------------------------------------------------------------------------------")
print("Here is the list of all builin functions and objects:")
print(dir(__builtins__))
print("Let us give a nice list")
for i in dir(__builtins__):
    print(i, end = "\n")

print("------------------------------------------------------------------------------------------------")

