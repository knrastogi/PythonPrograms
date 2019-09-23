1)      Write a program to enter two integers and then perform all arithmetic operations on them

num1= int(input("Enter a no.:"))
num2= int(input("Enter another no.:"))
sum= num1+num2
sub= num1-num2
mul= num1*num2
div= num1/num2
mod= num1%num2
fDiv= num1//num2
exp= num1**num2
print("Addition:",sum)
print("Subtration:",sub)
print("Multiplication:",mul)
print("Division:",div)
print("Modulus:",mod)
print("Floor Division:",fDiv)
print("Exponetialtion:",exp)


2)      Repeat the program in Q1 using floating point numbers

num1= float(input("Enter a no.:"))
num2= float(input("Enter another no.:"))
sum= num1+num2
sub= num1-num2
mul= num1*num2
div= num1/num2
mod= num1%num2
fDiv= num1//num2
exp= num1**num2
print("Addition:",sum)
print("Subtration:",sub)
print("Multiplication:",mul)
print("Division:",div)
print("Modulus:",mod)
print("Floor Division:",fDiv)
print("Exponetialtion:",exp)

3)      Write a program to enter your first name, middle name and family name and construct your full name.

fName=input("Enter your first name:")
mName=input("Enter your middle name:")
famName=input("Enter your family name:")
fullName= fName+mName+famName
print("Your full name:",fullName)
fullNameX= fName+" "+mName+" "+famName
print("Your full name:",fullNameX)

4)      Write a program print 100 blank lines on your screen.

print("\n"*100)
#Also
print(100*"\n")

5)      Take help from python help() and display all the supported keywords and symbols in python.

>>>help('keywords')
>>>help('symbols')

6)      Write a program to enter your name and display your name n no of times.

yoourName=input("Enter your first name:")
n=int(input("Enter how many times you want your name to be "))
print(yoourName*n)

7)      Write a program to swap two no.

a=4
b=7
print("Before Swap:",a,b)
temp=a
a=b
b=temp
print("After Swap:",a,b)

8)      Write a program to calculate simple interest.

p= int(input("Enter pricipal amount"))
r=float(input("Enter rate of interest"))
t=float(input("Enter time of deposit"))
si= p*r*t/100
print("SI:", si)

9)      Write a program to that prompts the user to enter the first name. Then display the following message.

Hello firstname

Welcome to Python

name = input("Enter your first name:")
print("Hello", name)
print("Welcome to python")
 

10)  Write a Python program which accepts the radius of a circle from the user and compute the area

rad= float(input("Enter radius of the circle"))
PI=3.1415
areaOfCir= PI*rad**2
print("Area of circle:", areaOfCir)

11)  Write a Python program to print the following string in a specific format (see the output)
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

Output :

Twinkle, twinkle, little star,

             How I wonder what you are!

                            Up above the world so high,                  

                            Like a diamond in the sky.

Twinkle, twinkle, little star,

             How I wonder what you are

 
print("""Twinkle, twinkle, little star,

             How I wonder what you are!

                            Up above the world so high,                  

                            Like a diamond in the sky.

Twinkle, twinkle, little star,

             How I wonder what you are """)

# Also

print('''Twinkle, twinkle, little star,

             How I wonder what you are!

                            Up above the world so high,                  

                            Like a diamond in the sky.

Twinkle, twinkle, little star,

             How I wonder what you are ''')

12)  Write a program that calculate no of seconds, minutes, hours in a week.


secInWeek=7*24*60*60
minInWeek=7*24*60
hrInWeek=7*24
print("No of seconds in a Week",secInWeek)
print("No of minutes in a Week",minInWeek)
print("No of hours in a Week",hrInWeek)


# Also
hrInWeek=7*24
minInWeek=hrInWeek*60
secInWeek=minInWeek*60
print("No of seconds in a Week",secInWeek)
print("No of minutes in a Week",minInWeek)
print("No of hours in a Week",hrInWeek)

13)  Write a program to find bytes equivalent of 1KB, 1MB, 1GB, and 1TB.

oneKB=2**10
oneMB=2**20
oneGB=2**30
oneTB=2**40
print("bytes equivalent of 1KB",oneKB)
print("bytes equivalent of 1MB",oneMB)
print("bytes equivalent of 1GB",oneGB)
print("bytes equivalent of 1TB",oneTB)


14)  Write a program to prepare a grocery bill. For that enter the name of items purchaged, quantity in which its is purchages, and its price per unit. Then display the bill in following format.

############################## B I L L##############################

Item Name                       Item Quantity                         Item Price

 

 

*******************************************************************

 

Total Amount to be paid:

*******************************************************************

item=input("Enter the item purchaged")
qty=int(input("Input quantity"))
price=float(input("Enter price"))
amt=qty*price
print("############################## B I L L##############################")
print("Item Name\t\tItem Quantity\t\tItem Price")
print(item,"\t\t\t",qty,"\t\t\t",price)
print("*******************************************************************")
print("Total Amount to be paid:", amt)
print("*******************************************************************")



15)  Write a program that calculates no of weeks in a year.


noOfWeeks = 365//7
print("No of Weeks in a year", noOfWeeks)

16)  Momentum is calculated as e=mc2., where m is the mass of the object and c is its velocity. Write a program that accepts an object’s mass ( in KG) and velocity (in Meters per sec) and displays its momentum.



17)  Demonstrate the use of ‘ ’. “ ”, “”” “”” and ‘’’ ‘’’.

print('Krish Rastogi')
print("The M S University of Baroda")
print("""How
            are
                you""")
print('''The M S
                University
                          of
                              Baroda''')

18)  Write a program to evaluate the value of an expression entered by user

ex=input("enter an expression")
res=eval(ex)
print("The evaulation result of the expression is:", res)

19)  Write a program to display data types of values entered by user.

data=eval(input("Enter any data"))
print("Data Type is", type(data))


20)  Write a program to display

Hello friends\nHow are you
print(r"Hello friends\nHow are you")
#Also
print(R"Hello friends\nHow are you")
#Also
print("Hello friends\\nHow are you")

21)  Write a program to diplay the following

उत्तिष्ठत जाग्रत प्राप्य वरान्निबोधत,
क्षुरासन्न धारा निशिता दुरत्यद्दुर्गम

पथ: तत् कवयो वदन्ति
print("""उत्तिष्ठत जाग्रत प्राप्य वरान्निबोधत,
क्षुरासन्न धारा निशिता दुरत्यद्दुर्गम
पथ: तत् कवयो वदन्ति""")

print(u"उत्तिष्ठत जाग्रत प्राप्य वरान्निबोधत,\
क्षुरासन्न धारा निशिता दुरत्यद्दुर्गम \
पथ: तत् कवयो वदन्ति")


print(u"उत्तिष्ठत जाग्रत प्राप्य वरान्निबोधत,\
क्षुरासन्न धारा निशिता दुरत्यद्दुर्गम \
पथ: तत् कवयो वदन्ति")

print(U"उत्तिष्ठत जाग्रत प्राप्य वरान्निबोधत,\
क्षुरासन्न धारा निशिता दुरत्यद्दुर्गम \
पथ: तत् कवयो वदन्ति")

22)  Write a program to display the following

'Arise, awake, stop not till the goal is reached.' — Swami Vivekananda 

 
print("'Arise, awake, stop not till the goal is reached.' — Swami Vivekananda")
 
print('\'Arise, awake, stop not till the goal is reached.\' — Swami Vivekananda')
 
