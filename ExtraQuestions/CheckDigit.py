#Question
"""
Given the input "12345" write a python code snippet to check if it is numeric
"""

#Approach 1

STRING ="12345A"
NUMERIC = "123456789"
flag = 0

for i in STRING:
    flag = -1 if i not in NUMERIC else 0        


if flag != 0:
    print("The string is not numeric")
else:
    print("The string is numeric")



#Approach 2

flag = 0

for i in STRING:
    flag = -1 if not i.isdigit() else 0

if flag != 0:
    print("The string is not numeric")
else:
    print("The string is numeric")
