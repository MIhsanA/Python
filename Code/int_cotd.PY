#Write a FUNCTION which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.
#So if 2 was the input, the function should return 2+22+222+2222 which is 2468.
#three(9) → 11106
#three(5) → 6170
#HINT
#What happens if you multiply a string by a number?

def add_int (num):
    n_list = []
    a = str()
    for i in range(4):
        a += str(num)
        n_list.append(int(a))
    print(n_list)
    return sum(n_list)

#n = 2

#print(add_int(n))