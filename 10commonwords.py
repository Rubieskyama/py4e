count = dict()
text = input('Enter the text file: ')
fhand = open(text)

for line in fhand:
    words = line.split()
    for word in words:
        count[word]=count.get(word, 0) + 1

listcount = list()
for k,v in count.items():
    listcount.append( (v,k) )
sortedcount = sorted(listcount, reverse=True)

for v,k in sortedcount[:10]:
    print(k, v)