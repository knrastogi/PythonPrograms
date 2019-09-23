##Q5. Write a program to convert a decimal number to its equivalent Hexadecimal, Octal and Binary and vice versa.


############################################################################################################################
##Program Objective: to convert a decimal number to its equivalent Hexadecimal, Octal and Binary and vice versa.          ##                               
##Coded by: KNR                                                                                                           ##
##Date: 17/09/2019 22:20                                                                                                  ##
##Lang: Python 3.7.4                                                                                                      ##
##Version: 1.0                                                                                                            ##
############################################################################################################################



dec = int(input("Enter a decimal number"))
print("Bainary:", bin(dec))
print("Octal:", oct(dec))
print("Hexa:", hex(dec))
hexa = input("Enter a Hexadecimal number")
octal = input("Enter a Octal number")
binary = input("Enter a Binary number")


print("Hexdecimal to Decimal: {}".format(int(hexa, base=16)))
print("Octal to Decimal: {}".format(int(octal , base=8)))
print("Binary to Decimal: {}".format(int(binary, base=2)))
