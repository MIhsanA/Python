list1 = list(range(2000, 3201))
list2 = []
list3 = []
for i in list1:
    if i % 7 == 0:
        list2.append(i)
for i in list2:
    if i % 5 != 0:
        list3.append(i)
print(list3)
