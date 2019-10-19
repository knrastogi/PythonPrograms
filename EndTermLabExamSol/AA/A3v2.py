d = {"disarmament":"निरस्त्रीकरण",
     "petulant":"चिड़चिड़ा",
     "junta":"सैनिक सरकार",
     "incongruous":"असंबद्ध",
     "contrite":"पछताया हुआ",
     "damning":"घातक"
     }
print("Welcome to Oxford English to English Dictionaty")

word = input("Enter the word to find the meaning:\n")
while True:
    w = word.lower()
    if w in d.keys():
        print(d[w])
    elif word=="":
        break
    else:
        print("Sorry! The Meaning of this wors not found in dictionary, Try for an another word")
    
    word = input("Enter the word to find the meaning:\n")

