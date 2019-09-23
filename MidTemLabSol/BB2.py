##Q2. Write a program convert a decimal no to its equivalent hexadecimal, octal and binary systems and vice versa.


##########################################################################################################################
##Program Objective: to convert a decimal no to its equivalent hexadecimal, octal and binary systems and vice versa.    ##
##Coded by: KNR                                                                                                         ##
##Date: 17/09/2019 22:20                                                                                                ##
##Lang: Python 3.7.4                                                                                                    ##
##Version: 1.0                                                                                                          ##
##########################################################################################################################

print("--------------------------------------------------")
dec = int(input("Enter a decimal No to convert into binary, Hexa and Octal code:"))
binary = bin(dec)
hexa  = hex(dec)
octa  = oct(dec)
print("Binary equivalent of {} is {}".format(dec, binary))
print("Hexadecimal equivalent of {} is {}".format(dec, hexa))
print("Octal equivalent of {} is {}".format(dec, octa))
print("Now doing reverse:")
print("Decimal equivalent of {} is {}".format(binary, int(binary,2)))
print("Decimal equivalent of {} is {}".format(hexa, int(hexa ,16)))
print("Decimal equivalent of {} is {}".format(octa, int(octa,8)))
