'''
Write a program that performs the following operations using appropriate functions on a 
string. 
a)  Check whether the string is a valid identifier or not. 
b)  Convert the string into title case. 
c)  Get the elements at alternate places. 
d)  Swap the case of the string. 
e)  Find whether a character or a substring is there in your string or not. 
f)  Centrally justify a string with a width of 50 and fill sting '&'. 
g)  Check whether a string is alpha-numeric or not. 
h)  Convert your string to upper after checking the case of the string. 
i)  Change a part of the string with another string. 
j)  Remove all the whitespaces of your string, if any
'''

myStr = "KKrish Rastogii"
##a)  Check whether the string is a valid identifier or not. 
print(myStr.isidentifier())

##b)  Convert the string into title case. 
print(myStr.title())

##c)  Get the elements at alternate places. 
print(myStr[::2])

##d)  Swap the case of the string. 
print(myStr.swapcase())

##e)  Find whether a character or a substring is there in your string or not. 
print(myStr.find("R"))

##f)  Centrally justify a string with a width of 50 and fill sting '&'. 
print(myStr.center(20,'&'))

##g)  Check whether a string is alpha-numeric or not. 
print(myStr.isalnum())

##h)  Convert your string to upper after checking the case of the string.
if myStr.upper()==False:
    print(myStr.upper())
else:
    print("Already in upper")

##i)  Change a part of the string with another string. 
print(myStr.replace('ii','i'))

##j)  Remove all the whitespaces of your string, if any
print(myStr.strip())





