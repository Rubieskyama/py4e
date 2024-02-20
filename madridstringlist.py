madrid = None
fhand = open('madrid.txt')

for a in fhand:
    if madrid == None:
        madrid = a.rstrip()
    else:
        madrid = madrid + " " + a.rstrip()

strmadrid = madrid.split()
print (strmadrid)