#Write a python function that takes a 4 digit number and a word with 5 letters and scrambles them up.
#Example: scarmble(12345,abcde) ----> 1a2b3c4d5e

def mash(string, intiger):
    if len(string) > 6:
        return "string too long"
    
    int_str = str(intiger)
    string_list = list(string)
    intiger_list = list(int_str)
    print(intiger_list)
    if len(intiger_list) > 4:
        return "too many digit"
    a = 1
    for i in intiger_list:
        string_list.insert(a, i)
        a += 2 
    return "".join(string_list)

word = "abdde"
number = 1234
print(mash(word,number))