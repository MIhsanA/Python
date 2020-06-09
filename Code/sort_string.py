#Question: Write a program that accepts a comma separated sequence of words as input 
# and prints the words in a comma-separated sequence after sorting them alphabetically. 
# Suppose the following input is supplied to the program: 
# without,hello,bag,world Then, the output should be: bag,hello,without,world

def s_str(words):
    word_list =list(words.split(","))
    result = ",".join(sorted(word_list))
    return result


#letters = "without,hello,bag,world"
#print(s_str(letters))