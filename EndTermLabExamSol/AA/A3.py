d = {"apple": "a round fruit with firm, white flesh and a green, red or yellow skin",
     "seek":["to try to find or get something, especially that is not a phusical object","to ask for advice, help, approval, permission, etc."],
     "abacus": "a square or rectangular frame holding an arrangement of small balls on metal rods or wires, used for counting or for doing calculations"
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

