#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

try:
    inHours = float(input('Enter Hours:'))
    inRate = float(input('Enter Rate:'))
except:
    isValidInput = bool(False)

if isValidInput == False:
    print("Error, please enter numeric input")

elif inHours > 40:
    otHours = inHours-40
    otPay = ((otHours*1.5)*inRate)
    pay = round((40*inRate)+otPay,2)

else:
    pay = round(inHours * inRate, 2)
    print(pay)
