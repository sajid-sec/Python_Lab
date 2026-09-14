4. Write a program that reads a sentence from the user and prints the frequency of each word. 
s = input("Enter a sentence: ")
words = s.split()
freq = {}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
        print(f"{word}: {freq[word]}")
