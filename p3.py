# 3. Input integers into a list and remove duplicates while preserving order

numbers=[]
n = int(input("Enter number of integers: "))
for i in range(n):
    numbers.append(int(input("Enter integer: ")))
    unique=[]
    for num in numbers:
        if num not in unique:
            unique.append(num)
print("List after removing duplicates:", unique)
