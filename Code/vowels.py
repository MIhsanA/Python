#Write a function which returns the integer number of vowels in a given string. 
#You should ignore case.
#seven("Hello") → 2
#seven("hEelLoooO") → 6

def vow(w):
    count = 0
    vowels = ("a", "e", "i", "o", "u")
    for i in w.lower():
        if i == vowels[0]:
            count += 1
        elif i == vowels[1]:
            count += 1
        elif i == vowels[2]:
            count += 1
        elif i == vowels[3]:
            count += 1
        elif i == vowels[4]:
            count =+ 1
        else:
            False
    return count

#word = input("Please type the word: ")
#print(vow(word))