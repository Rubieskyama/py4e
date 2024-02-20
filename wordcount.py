count = dict()
text = input('Enter a text: ')
text = text.split()

print('Counting...')
for word in text:
    count[word] = count.get(word, 0) + 1
print(count)
