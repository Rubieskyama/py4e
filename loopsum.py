a = 0
total = 0
num = [3, 41, 12, 9, 74, 15]
for i in num:
    a = a + 1
    total = total + i
    print(total, i)
    avg = total / a
print("The sum is: ",total)
print("The count is: ",a)
print("The average is: ",avg)