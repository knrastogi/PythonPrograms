'''
Write a program to demonstrate the use of positional arguments, keyword arguments, default 
arguments and variable length arguments (*vargs). 
'''
def add1(a,b):
    return a+b

add2(2,3)
5

def add2(a, b):
    return a+b


add2(a=2, b=9)
11
add2(b=9, a=1)
10


def add3(a, b=2):
    return a+b

add3(3)
5

add3()
def add4(*a):
    sum =0
    for i in a:
        sum= sum+i
    return sum


#Call
add4(2,3,4,8,9,90)
116


def disp(**a):
    for i, j in a.items():
        print("key = {} and value = {}".format(i,j))
        
#Call
##disp(a=5, b=10)
##key = a and value = 5
##key = b and value = 10
