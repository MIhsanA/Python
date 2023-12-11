welcome = "welcome to grade Calculator"
print(welcome)
math = int(input("Please enter your Math mark: "))
chemistry = int(input("Please enter your Chemistry mark: "))
physics = int(input("Please enter your Physics mark: "))
total = (math + chemistry + physics) / 300 * 100 
if total >= 70:
    print("A")
elif total >=60:
    print("B")
elif total >= 50:
    print("C")
elif total >= 40:
    print("D")
else:
    print("You Failed")

    