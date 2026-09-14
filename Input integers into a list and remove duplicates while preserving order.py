# 3. Input integers into a list and remove duplicates while preserving order

numbers=[]
n = int(input("Enter number of integers: "))          #input integer
for i in range(n):          #loop
    numbers.append(int(input("Enter integer: ")))       #append
    unique=[]     #empty list
    for num in numbers: #loop
        if num not in unique:     #checking
            unique.append(num)    #adding
print("List after removing duplicates:", unique) #printing
