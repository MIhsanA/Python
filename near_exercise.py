#Create a function that when given two strings of letters, 
# #determine whether the second can be made from the first by removing one letter. 
# The remaining letters must stay in the same order.
#Example
#near ("reset", "rest") => true
#near ("dragoon", "dragon") => true
#near ("eave", "leave") => false
#near ("sleet", "lets") => false

def compare(a,b):
    s = ""
    for x in b:
        for y in a:
            if x == y:
                s+=str(x)
            
    return(s)

string_one = input("Please put String 1: ")
string_two = input("Please put String 2: ")

result = compare(string_one,string_two)

print(result)

if len(result) == (len(string_one) - 1) and len(result == len(string_two)):
    print(True)

elif len(result) == len(string_one) and len(string_two) == (len(result) -1):
    print(True)
else:
    print(False)




"""
list_1 = []
list_2 = []

for i in string_one:
    list_1.append(i)

for i in string_two:
    list_2.append(i)
    """