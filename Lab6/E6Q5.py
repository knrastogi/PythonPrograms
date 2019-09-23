##Bitwise Operator
##
##&, |, ~, ^,>>, <<
##
##Write program(s) to demonstrate the use of all bitwise operators.

##############################################################################

a=0B1001
b=0B1000
print(bin(a & b))
print(bin(a | b))
print(bin(a ^ b))
print(bin(~a))
print(bin(~b))
print(bin(a>>1))
print(bin(a<<1))
print(bin(b>>1))
print(bin(b<<1))
n=int(input("How many times you want to Left Shift or Right Shift a"))
print("a After Left Shifting {} times si {}".format(n, bin(a<<n)))
print("a After Right Shifting {} times si {}".format(n, bin(a>>n)))
############################################################################
