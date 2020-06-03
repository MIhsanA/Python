#CHALLENGE OF THE DAY
#Question: Write a program which can compute the factorial of a given numbers. 
#The results should be printed in a comma-separated sequence on a single line. 
#Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

import math 
number = int(input("please type number: "))

factorial_1 = str(math.factorial(number))

answer = []
for i in factorial_1:
    answer.append(i)
    
print(answer)



number2 = int(input("Please put number2: "))

factoria_2 = 1 

for i in range(1, number2+1):
    factoria_2 = factoria_2 * i

answe2 = []
for i in str(factoria_2):
    answe2.append(i)
print(f"factorial of {number2} is {answe2}")
