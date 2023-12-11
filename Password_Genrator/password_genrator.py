import random
import string

def genrate_password(min_Length, numbers=True, spacial_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special =string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if spacial_characters:
        characters += special

    pwd = ""

    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if spacial_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you have to have special characters (y/n)? ").lower() == "y"


pwd = genrate_password(min_length, has_number, has_special)
print("The genrated password is: ", pwd)