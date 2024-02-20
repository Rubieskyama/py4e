num = [3, 41, 12, 9, 74, 15]
largestnum = 0
for i in num:
    if i > largestnum:
        largestnum = i
    print(i)
print("The largest number is", largestnum)