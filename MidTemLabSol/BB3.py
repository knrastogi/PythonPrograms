##Q3. Write a program to calculate area of a triangle whose three sides are entered by user.


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

