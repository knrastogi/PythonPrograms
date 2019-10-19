'''
Calculate the sqaures, cube, power n and squareroot, cuberoot and nth root of the values of a list and print the result as follow: 			10

---------------------------------------------------------------------------------------------------------------------------
List Index List Item SquareCubePowernSquare RootCube Root Nth Root	
---------------------------------------------------------------------------------------------------------------------------
myLst[0]           4                    16             64        16 (Power2)     16            2            X                 X	
---------------------------------------------------------------------------------------------------------------------------
'''

from mymath import *	
myLst = [2,5, 3, 4, 1,6,8,7,10,9]
n= int(input("Enter power"))
m= int(input("Enter the value for nth root"))
print("List Index List Item SquareCubePowernSquare RootCube Root Nth Root	")
for i in range(len(myLst)):
    print("myLst[{}]\t\t {}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i,myLst[i], square(myLst[i]),cube(myLst[i]), power(myLst[i],n), sqrt(myLst[i]),cubert(myLst[i]),nthroot(myLst[i], m)))
    
    
    
