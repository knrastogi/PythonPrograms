##Q5. Write a program to display the ascii value of a user inputted character.


#############################################################################################################
##Program Objective: to check whether a String is palindrome or not                                        ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------")
yourStr = input("Enter your string:")
if yourStr == yourStr[::-1]:
    print("{} is a Polindrome".format(yourStr))
else:
    print("{} is not a Polindrome".format(yourStr))  

print("--------------------------------------------------")

