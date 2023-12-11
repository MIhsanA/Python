# A website requires the users to input username and password to register.
#  Write a function to check the validity of password input by users.
#	Following are the criteria for checking the password:
#	- At least 1 letter between [a-z]
#	- At least 1 number between [0-9]
#	- At least 1 letter between [A-Z]
#	- At least 1 character from [$#@]
#	- Minimum length of transaction password: 6
#	- Maximum length of transaction password: 12
#
#   Your program should accept a list of passwords
#  of an indeterminate length and will check them according to the above criteria.
#  Passwords that match the criteria are to be returned in a list.
#
# 	Example
#	If the following passwords are given as input to the program:
#	["ABd1234@1","a F1#","2w3E*","2We3345"]
#	Then, the output of the program should be:
#	["ABd1234@1"]

def pass_validity(list_of_password):
    valid_password = []
    for i in list_of_password:
        if (any(x.isupper() for x in i) 
        and any(x.islower() for x in i) 
        and any(x.isdigit() for x in i) 
        and len(i) >= 6
        and len(i) <= 12
        and ('$' in i or '#' in i or '@' in i)):
           valid_password.append(i)
    if valid_password == []:
        return ['no valid password']
    else:
        return valid_password


password = ["ABd1234@1","a F1#","2w3E*","2We3345"]
print(pass_validity(password))