sample = input('enter string')
words = sample.split()
word_count = {}

for i in words :
    if i :
        if i in word_count :
            word_count[i] += 1
        else :
            word_count[i] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

print(len(word_count))

