b= [1,2,4,5,6,7,3]

a = range(1, 10)
for i in a:
    if i not in b:
        print(i)
        break