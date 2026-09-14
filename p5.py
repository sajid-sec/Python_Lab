# 5. Write a Python program to remove all punctuation characters from a string using string methods or the string module. 

import string
s = input("Enter a string: ")
result = ""
for i in s:
    if i not in string.punctuation:
        result += i
print("String without Punctuation:", result)
