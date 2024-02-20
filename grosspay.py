Hours = input("Enter number of hours: ")
try:
    Hours = float(Hours)
except:
    print("Enter a numeric value")
    exit()
Rate = input("Enter rate per hour: ")
try:
    Rate = float(Rate)
except:
    print("Enter a numeric value")
    exit()
if Hours > 40:
    OTP = (Hours - 40) * Rate * 1.5
    Pay = 40 * Rate + OTP
else:
    Pay = Hours * Rate
print("Gross pay:", Pay)
