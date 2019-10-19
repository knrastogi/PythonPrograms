def strLength(string):
    count = 0
    for i in string:
        count+=1
    return count



        
    
def strRev(string):
    string= string[::-1]
    return string




def strSwap(string1, string2):
    string1, string2=string2, string1
    return string1, string2




def strSearch(substring, string):
    if substring in string:
        return True

#Call
print(strLength("Krishna"))
#Call
print(strRev("Krishna"))
#Call
print(strSwap("Kri","Param"))

#Call
if (strSearch("Kri", "Krishna")):
    print("Found")
