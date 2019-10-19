'''
Write a module named mymath consisting of following functions:

square(n)
cube(n)
power(a,n)
sqrt(n)
cubert(n) 
nthroot(n) # A function that finds nth root of a number.
PI # Create a constant PI with value 3.1415
e # Create a constant  e with value 2.71


Note: Write documentation string along with all the functions of the said module.
		
Perform the following tasks using your module.

a) Generate the Web Documentation using Pydoc Module.   			5
b) Print the contents of your module.                   5
c) Use all the functions of the module mymath into your program and calculate the area of a circle,also Calculate the sqaures, cube, power n and squareroot, cuberoot and nth root of the values of a list and print the result as follow: 
'''

#calculate the area of a circle
import mymath as mm
rad = float(input("Enter the radius of circle:"))
area = mm.PI * mm.square(rad)
print("The area of the circle is", area)
