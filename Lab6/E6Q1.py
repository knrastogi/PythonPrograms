##Arithmetic Operator
##
##+, -, *, /, %, //, **
##
##Write program(s) to demonstrate the use of all arithmetic operators.
############################################################################
a,b=[int(x) for x in input("Enter two numbers:").split()]
print("Numbers ented by you are {} and {}\nHere is the Arithmetic Operations results.".format(a,b))
#Addition
c = a + b
print("The Addition is: {}".format(c))

#Subtration
c = a - b
print("The Subtration is: {}".format(c))

#Multiplication
c = a * b
print("The Multiplication is: {}".format(c))

#Division
c = a / b
print("The Division is: {}".format(c))

#Modulus
c = a % b
print("The Modulus is: {}".format(c))

#Floor Division
c = a // b
print("The Floor Division is: {}".format(c))

#Exponential
c = a ** b
print("The Exponential is: {}".format(c))
############################################################################
