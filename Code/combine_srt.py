#Flask CHALLENGE OF THE DAY
 #Given two Strings of equal length, 'merge' them into one String.
#Do this by 'zipping' the Strings together.
#Start with the first char of the first String.
#Then add the first char from the second String.
#Then add the second char from the first String.
#And so on. 
#Maintain case.
#You will not encounter whitespace.
#four("String","Fridge") → "SFtrriidngge"
#four("Dog","Cat") → "DCoagt"
#Hint:
    #Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    #How would you seperate a string into characters?

def comb_str(word):
    bit1= word[0]
    bit2 = word[1]
    list1 = list(bit1)

    list2 = list(bit2)
    a = 1
    for i in list2:
        list1.insert(a, i)     
        a += 2
    return "".join(list1)

my_str ="String","Fridge"
print(comb_str(my_str))