#Print out a times table:

#Hint: don’t manually set your code to print each number, one by one. Use a loop.


def table(num):
    table = ""
    for i in range(13):
        table +=(f"{num} * {i} = {i * num} \n")
    return table
number = int(input("please put int number for table: "))
table = table(number)
print(table)