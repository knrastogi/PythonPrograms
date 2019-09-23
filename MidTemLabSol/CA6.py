##Q6. Write a program to demonstrate the use of end and sep in print() function with different end values and separators.


###########################################################################################################################
##Program Objective: to demonstrate the use of end and sep in print() function with different end values and separators. ##                                                                    ##
##Coded by: KNR                                                                                                          ##
##Date: 17/09/2019 22:20                                                                                                 ##
##Lang: Python 3.7.4                                                                                                     ##
##Version: 1.0                                                                                                           ##
###########################################################################################################################

print("--------------------------------------------------------------------------------------------------------------------------------------------")
yourName = input("Enter your name:")
yourAge = int(input("Enter your age:"))
yourPer = float(input("Enter your percentage:"))
print(yourName,yourAge,yourPer, sep = ",") # , separator
print(yourName,yourAge,yourPer, sep = ":") # : separator
print(yourName,yourAge,yourPer, sep = ";") # ; separator
print(yourName,yourAge,yourPer, sep = "\t") # tab separator
print(yourName,yourAge,yourPer, sep = "\n") # newline separator
print(yourName,yourAge,yourPer, sep = ".") # . separator
print("Krish Rastogi", end = "\n")
print("Bye")
print("Krish Rastogi", end = "\t")
print("Bye")



