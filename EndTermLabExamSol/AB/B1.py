import math
a = int(input(("Enter the coefficient of x^2:")))

b = int(input(("Enter the coefficient of x:")))
c = int(input(("Enter constant term:")))
print("The quadratic equation is: {}x^2+{}x+{}".format(a,b,c))

d = (b**2) - (4*a*c)
print(d)
r1= (-b + math.sqrt(d))/(2*a)
r2= (-b - math.sqrt(d))/(2*a)
if d>1:

        print("there are two real distinct roots")
        print("Root #1= %.2f"%r1)
        print("Root #2= %.2f"%r2)
elif d == 1:
        
        print("there are one real roots")
        print("Root #1= %.2f"%r1)
        print("Root #2= %.2f"%r2)


else:
    
        print("there are two distinct complex roots")
        print("Root #1= %.2f"%r1)
        print("Root #2= %.2f"%r2)
        
