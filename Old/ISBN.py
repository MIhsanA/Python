digits =[]
i = 1
while len(digits) < 2:
    digits.append(int(input(f"put digit {i}")))
    i += 1

print(digits)


count = 0
for i in digits:
    if (i % 2) == 0:
        digits[count] = 3 * i
    count += 1

print(digits)

for i in digits[ : :2]:
    print(i)

print("hi", count)
print(["hi"] + [count])
print(f"hi {count}")

print([count] + ["hi "])
print( digits , count)