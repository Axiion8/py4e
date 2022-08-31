#Exercise 1: Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.


#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

#Initial code was made by Ch2 Exercise 3

inHours = float(input('Enter Hours:'))
inRate = float(input('Enter Rate:'))

if inHours > 40:
    otHours = inHours-40
    otPay = ((otHours*1.5)*inRate)
    pay = round((40*inRate)+otPay,2)

else:
    pay = round(inHours * inRate, 2)

print(pay)
