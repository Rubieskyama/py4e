num = list()

while True:
    a = input("Enter a number: ")
    if a == 'done':
        break
    a = int(a)
    num.append(a)
print(num)
print ("The average of the numbers you have entered is: ",sum(num)/len(num))
