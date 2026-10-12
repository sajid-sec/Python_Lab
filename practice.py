#REVERSE A LIST

# n = int(input("Enter no of elements:"))
# print("Enter the Elements:")
# L = []
# for i in range (n):
#     x = int(input())
#     L.append(x)
# L.reverse()                                     USING REVERSE FUNCTION
# print("Reversed List:", L)

# n = int(input("Enter no of elements:"))
# print("Enter the Elements:")
# L =[]
# for i in range(n):
#     x = int(input())
#     L.append(x)
# rev = []                                          WITHOUT USING REVERSE FUNCTION
# for i in range (len(L)-1, -1, -1):
#     rev.append(L[i])
# print("Reversed List:", rev)

# n = int(input("Enter no of elements:"))
# print("Enter the Elements:")
# L =[]
# for i in range(n):
#     x = int(input())
#     L.append(x)
# print ("REVERSED LIST:", L[::-1])

#REVERSE A STRING
# s= input("Enter a string:")
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev = rev+s[i]
# print(rev)

# s= input("Enter a string:")
# print(s[::-1])

#COUNT NUMBER OF WORDS IN STRING
# s= input("Enter a string:")
# print("NO WORDS:",len(s.split()))

#Remove duplicate characters from a string
# s= input("Enter a string:")
# result=""
# for i in s:
#     if i not in result:
#         result=result+i
# print(result)







# 1. Create a list of 5 fruits, print 2nd and 4th items, replace last with "Mango", and print updated list.
# fruits = ["Apple", "Banana", "Orange", "Grapes", "Pineapple"]
# print(fruits[1], fruits[3])
# fruits[-1] = "Mango"
# print(fruits)

# 2. Take 10 integers from user, store in list, then find sum and average without sum()
# numbers = []
# for i in range(10):
# 	numbers.append(int(input("Enter integer: ")))

# total = 0
# for j in numbers:
# 	total += j
# average = total / len(numbers)
# print("Sum:", total)
# print("Average:", average)

# 3. Input integers into a list and remove duplicates while preserving order
# numbers=[]
# n = int(input("Enter number of integers: "))
# for i in range(n):
#     numbers.append(int(input("Enter integer: ")))
#     unique=[]
#     for num in numbers:
#         if num not in unique:
#             unique.append(num)
# print("List after removing duplicates:", unique)

# 4. Write a program that reads a sentence from the user and prints the frequency of each word. 
# s = input("Enter a sentence: ")
# words = s.split()
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word]+=1
#     else:
#         freq[word]=1
#         print(f"{word}: {freq[word]}")

# 5. Write a Python program to remove all punctuation characters from a string using string methods or the string module. 
# import string
# s = input("Enter a string: ")
# result = ""
# for i in s:
#     if i not in string.punctuation:
#         result += i
# print("String without Punctuation:", result)
