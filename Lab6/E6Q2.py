##Assignment Operator
##
##=,+=, -=, *=,/=,//=, **=
##
##Write program(s) to demonstrate the use of all assignment operators.

 
############################################################################
a,b=[int(x) for x in input("Enter two numbers:").split()]
print("Numbers assigned to a and b are: {} and {}\nHere is the Assignments Operations results.".format(a,b))
#Assignment
c=b*b
print("c is assigned with b*b and the value of c is: {}".format(c))

#Addition Assignment
a+=b # This is equivalent to a=a+b
print("The Addition Assignment is: {}".format(a))

#Subtration Assignment
a-=b # This is equivalent to a=a-b
print("The Subtration Assignment is: {}".format(a))

#Multiplication Assignment
a*=b # This is equivalent to a=a*b
print("The Multiplication Assignment is: {}".format(a))

#Division Assignment
a/=b # This is equivalent to a=a/b
print("The Division Assignment is: {}".format(a))

#Modulus Assignment
a%=b # This is equivalent to a=a%b
print("The Modulus Assignment is: {}".format(a))

#Floor Division Assignment
a//=b # This is equivalent to a=a//b
print("The Floor Division Assignment is: {}".format(a))

#Exponential Assignment
a**=b # This is equivalent to a=a**b
print("The Exponential Assignment is: {}".format(a))
############################################################################
