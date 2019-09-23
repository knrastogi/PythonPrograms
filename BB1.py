##Q1. Write a program that calculates no of Weeks, Days, Hours, Minutes and Seconds in a year.


#############################################################################################################
##Program Objective: to calculates no of Weeks, Days, Hours, Minutes and Seconds in a year.                ##
##Coded by: KNR                                                                                            ##
##Date: 17/09/2019 22:20                                                                                   ##
##Lang: Python 3.7.4                                                                                       ##
##Version: 1.0                                                                                             ##
#############################################################################################################

print("--------------------------------------------------")
noOfWeeks = 365//7
noOfDays = 365
noOfHours = 365*24
noOfMinutes = noOfHours*60
noOfSeconds = noOfMinutes*60
print("No of Weeks in a year are: {0} \
      \nNo of Days in a year are: {1} \
      \nNo of Hours in a year are: {2} \
      \nNo of Minutes in a year are: {3} \
      \nNo of Seconds in a year are: {4}".format(noOfWeeks,noOfDays,noOfHours,noOfMinutes,noOfSeconds))

print("--------------------------------------------------")

