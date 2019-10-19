'''
Write a function that takes variable number of arguments and returns the sum , sum of squares, sum of 
cubes, average, multiplication, multiplication of squares, multiplication of cubes of that numbers.
'''

def calc(*a):
    sum = 0
    mul = 1
    sumSQR = 0
    sumCubes = 0
    mulSQR = 1
    mulCubes = 1
    
    for i in a:
        sum = sum+i
        mul = mul*i
        sumSQR = sumSQR+(i**2)
        sumCubes  = sumCubes+ (i**3)
        mulSQR = mulSQR*(i**2)
        mulCubes = mulCubes*(i**3)
    return sum,mul,sumSQR,sumCubes,mulSQR,mulCubes

#Call
sum,mul,sumSQR,sumCubes,mulSQR,mulCubes=calc(1,2,4,5,6,7,8)
print("sum = {},mul= {},sumSQR= {},sumCubes={},mulSQR={},mulCubes={}".format(sum,mul,sumSQR,sumCubes,mulSQR,mulCubes))
