#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

def wage(inHours, inRate):
    if inHours > 40:
        otHours = inHours-40
        otPay = ((otHours*1.5)*inRate)
        pay = round((40*inRate)+otPay,2)
    else:
        pay = round(inHours * inRate, 2)
        
    print(pay)

try:
    inHours = float(input('Enter Hours:'))
    inRate = float(input('Enter Rate:'))
    isValidInput = bool(True)
except:
    isValidInput = bool(False)

if isValidInput == False:
    print("Error, please enter numeric input")

elif isValidInput == True:
    wage(inHours,inRate)