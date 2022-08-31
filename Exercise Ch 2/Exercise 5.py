
# Exercise 5
#Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the
#converted temperature.

# C to F equation is: (°C × 9/5) + 32 = °F

try:
    inC = float(input('Enter Celsius:'))
except:
    inC = -5000

if inC == -5000:
    print('That is not a valid input.')
else:
    outF = (inC * (9/5)) + 32
    print(outF)
