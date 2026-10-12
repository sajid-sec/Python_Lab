# print("Hello World!!")
# address=input("Enter your ip address:")
# print("Your IP is :",address)

# print(["SAJID","A...A"])

# Ip= 192
# data_type = type(Ip)
# print(data_type)

# failed_attempts = 8
# if (failed_attempts>5):
#     print("Account Locked")
# else:
#     print("Account Active")

# for i in range (20):
#     print("repeat")

# time = 0
# while time<=10:
#     print(time)
#     time = time+2

# a= int(input("Enter 1t number:"))
# b= int(input("Enter 2nd number:"))
# c= int(input("Enter 3rd number:"))
# largest = a
# if b>largest:
#     largest = b
# if c>largest:
#     largest= c
# print("Largest number is:", largest)

# a= int(input("Enter 1st number:"))
# b= int(input("Enter 2nd number:"))
# c= int(input("Enter 3rd number:"))
# temp = a
# a=c
# c=b
# b=temp

# print("New a=",a)
# print("New b=",b)
# print("New c=",c)

# a=(input("Enter 1st number:"))                                             
# sum = 0                                                 
# for i in a:                                                           #while a!=0:
#     sum = sum + int(i)                                                     #digit = n%10
# print("sum of digits=",sum)                                                #sum = sum+digit
#                                                                            #n = n//10                        PRINT N

# a=int(input("Enter 1st number:"))                                             
# rev =0
# while a!=0:
#     digit = a%10
#     rev = rev*10+digit
#     a=a//10

# print("Reversed number:",rev)
import math
n=int(input("Enter a number:"))
sum = 0
while n!=0:
    digit = n%10
    sum= sum+ math.pow(2,digit)              #OR digit**2    OR pow(digit,2)
    n = n//10
print("sum:",sum)

