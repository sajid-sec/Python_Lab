# 2. Take 10 integers from user, store in list, then find sum and average without sum()

numbers = []
for i in range(10):
	numbers.append(int(input("Enter integer: ")))
total = 0
for j in numbers:
	total += j
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)
