count = dict()
text = input('Enter the text file: ')
fhand = open(text)
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

bigword = None
bigcount = None
for key,val in count.items():
    if bigcount == None or val > bigcount:
        bigword = key
        bigcount = val
print (bigword, bigcount)