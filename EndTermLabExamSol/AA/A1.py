'''
Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics 
and Computer. Calculate percentage and grade according to following: 
Percentage >= 90% : Grade A 
Percentage >= 80% : Grade B 
Percentage >= 70% : Grade C 
Percentage >= 60% : Grade D 
Percentage >= 40% : Grade E 
Percentage < 40% : Grade F
'''
import time
marks = [int(x) for x in input("Enter marks in 5 subjects:\n").split()]
total = 0
for i in marks:
    total +=i
totalAvg = total/5
print("Your Marksheet is generated")
time.sleep(5)
print("----------------------------------------------------")
print("     Gujrat State Board of Education                ")
print("   Marksheet for Intermediate Examination 2019-20   ")
print("----------------------------------------------------")
print("S No     Subject     Max Marks       Marks Obtained")
print("----------------------------------------------------")
print("1     Physics           100              {}".format(marks[0]))
print("2     Chemistry         100              {}".format(marks[1]))
print("3     Mathematics       100              {}".format(marks[2]))
print("4     Hindi             100              {}".format(marks[3]))
print("5     English           100              {}".format(marks[4]))
print("----------------------------------------------------")  
print("                                    ",totalAvg )
print("----------------------------------------------------")      
if totalAvg>=90:
      print("                               Grade-'A'")
elif totalAvg>=80:
    print("                                 Grade-'B'")

elif totalAvg>=70:
    print("                                 Grade-'C'")

elif totalAvg>=60:
    print("                                 Grade-'D'")

elif totalAvg>=40:
    print("                                 Grade-'E'")
    
else:
    print("                                 Grade-'F'")
print("----------------------------------------------------")        
    
    
    
