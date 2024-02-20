madrid = list()
fhand = open('madrid.txt')
for player in fhand:

    madrid.append(player.rstrip())
print (madrid)