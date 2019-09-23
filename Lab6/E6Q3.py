##Logical Operator
##
##and, or, not
##
##Write program(s) to demonstrate the use of all logical operators.
############################################################################
a= True
b= True
print(a and b)
print(a or b)
print(not a)
print(not b)

a= True
b= False
print(a and b)
print(a or b)
print(not a)
print(not b)

a= False
b= True
print(a and b)
print(a or b)
print(not a)
print(not b)

a= False
b= False
print(a and b)
print(a or b)
print(not a)
print(not b)


############################################################################
a=4
b=9
print("Demonstration of and logical operator")
print(a==4 and b==9)
print(a==4 and b!=9)
print(a>4 and b==9)
print(a<4 and b<9)


print("Demonstration of or logical operator")
print(a==4 or b==9)
print(a==4 or b!=9)
print(a>4 or b==9)
print(a<4 or b<9)


print("Demonstration of not logical operator")
print(not (a==4))
print(not (a!=4))
print(not (b>=4))
print(not (b!=4))

