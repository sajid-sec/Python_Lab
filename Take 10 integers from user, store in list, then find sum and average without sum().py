# 2. Take 10 integers from user, store in list, then find sum and average without sum()

numbers = []
for i in range(10): #looping
	numbers.append(int(input("Enter integer: ")))     #appending
total = 0 #for sum
for j in numbers:
	total += j        #adding
average = total / len(numbers)            #avg
print("Sum:", total)
print("Average:", average)
