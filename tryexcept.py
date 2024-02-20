ival = input("Enter a number: ")
try:
    val = int(ival)
except:
    val = -1
if val >= 0:
    print("Nice job")
else:
    print("Not a number")