'''
Write a function numPattern() that prints the following pattern as per the following condition: 
 
If called without a parameter prints just for 1-5. 
If called with a number n, it prints for numbers 1-n. 
If called with a number m and a number n, it prints from number m-n if m<n else n-m. 
 
The Pattern to print is: 
 
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
'''

def numPattern(n=5,m= 1):
    if m<n:
        for i in range(m,n+1):
            print()
            for j in range(1, i+1):
                print(i, end = " ")
    else:
        for i in range(n,m+1):
            print()
            for j in range(1, i+1):
                print(i, end = " ")
'''    

Another methods
def numPattern(n=5,m= 1):
    if m>n:
        m,n=n,m # Swap if m>n
        for i in range(n,m+1):
            print()
            for j in range(1, i+1):
                print(i, end = " ")

    
