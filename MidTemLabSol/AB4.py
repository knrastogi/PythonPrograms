##Q4. Write a program to display even nos. till 100.

#############################################################################################################
##Program Objective: to display even nos. till 100                                                         ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

# Method 1: Using for loop
##print("--------------------------------------------------------------------------------------------------------------------------------------------------")
##for i in range(2,101,2):
##    print(i, end = " ")
##
##print("\n--------------------------------------------------------------------------------------------------------------------------------------------------")
##


##
### Method 2: Using while loop
##print("--------------------------------------------------------------------------------------------------------------------------------------------------")
##
##i = 2
##while i <=100:
##    print(i, end = " ")
##    i+=2
##print("\n--------------------------------------------------------------------------------------------------------------------------------------------------")
##

# Method 3: Using while loop and decision control. Not a good sol.
##print("--------------------------------------------------------------------------------------------------------------------------------------------------")
##
##i = 1
##while i <=100:
##    if i%2 == 0:
##        print(i, end = " ")
##    i+=1
##print("\n--------------------------------------------------------------------------------------------------------------------------------------------------")
##

#Medod 4: Using for loop and decision control. Not a good sol.

print("--------------------------------------------------------------------------------------------------------------------------------------------------")
for i in range(1,101):
    if i%2 == 0:
        print(i, end = " ")

print("\n--------------------------------------------------------------------------------------------------------------------------------------------------")


