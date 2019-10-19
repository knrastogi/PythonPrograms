'''
Write a program that performs the following operations using appropriate functions on a list. 
 
a)  Add Single Element to The List 
b)  Add Elements of a List to Another List 
c)  Inserts Element to The List 
d)  Removes Element from the List 
e)  returns smallest index of element in list 
f)  returns occurrences of element in a list 
g)  Removes Element at Given Index 
h)  Reverses a List 
i)  sorts elements of a List 
j)  Removes all Items from the List 
'''


list1 = ["abc","2",34,89,"ZZ",4.534]
list2 = [1,89,"Krish", "Python", True, 2+8j, (1,2,3), [3,4,5], {3,4,5}, {1:"A"}]
list3 =[1,2,3]

##a)  Add Single Element to The List
list1.append(33)

##b)  Add Elements of a List to Another List 
list1.extend(list2)

##c)  Inserts Element to The List
list1.insert(1,2)


##h)  Reverses a List 
list1[::-1]

##d)  Removes Element from the List 
list1.pop()

##e)  returns smallest index of element in list 
list1.index(89)

##g)  Removes Element at Given Index 
list1.pop(2)

##i)  sorts elements of a List 
list3.sort()

##f)  returns occurrences of element in a list 
list1.count(2)

##j)  Removes all Items from the List 
list1.clear()
