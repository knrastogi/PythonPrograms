##Q3. Write a program to print table of 2


#############################################################################################################
##Program Objective: to print table of 2                                                                   ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################


# Method-1: Using for loop
##print("--------------------------------------------------")
##
##for i in range(1,11):
##    print("{} x {}   = {}".format(2,i,2*i))
##
##print("--------------------------------------------------")


# Method-2: Using while loop
print("--------------------------------------------------")
i = 1
while i<=10:
    print("{} x {}   = {}".format(2,i,2*i))
    i+=1

print("--------------------------------------------------")
