# 5. Write a Python program to remove all punctuation characters from a string using string methods or the string module. 

import string     #importing mstring module
s = input("Enter a string: ") #enter a string
result = ""
for i in s:
    if i not in string.punctuation:       #checking punc
        result += i       #adding
print("String without Punctuation:", result)
