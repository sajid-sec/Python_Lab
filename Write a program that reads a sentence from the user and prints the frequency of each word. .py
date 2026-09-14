4. Write a program that reads a sentence from the user and prints the frequency of each word. 
s = input("Enter a sentence: ")
words = s.split()        #split
freq = {}     #empty dictionary
for word in words:     #looping
    if word in freq:
        freq[word]+=1          
    else:
        freq[word]=1
        print(f"{word}: {freq[word]}")         #f for formatted string
