# Exercise 3
#Write a program to prompt the user for hours and rate per
#hour to compute gross pay.
inHours = float(input('Enter Hours:'))
inRate = float(input('Enter Rate:'))

pay = round(inHours * inRate, 2)

print(pay)
