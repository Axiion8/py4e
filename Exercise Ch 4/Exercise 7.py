#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

# Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
# < 0.6     F

#Enter score: 0.95
#A

#Enter score: perfect
#Bad score

#Enter score: 10.0
#Bad score

#Enter score: 0.75
#C

#Enter score: 0.5
#F

try:
    score = float(input("Enter score: "))
    isValid = bool(True)
except:
    print("Bad score")
    isValid = bool(False)

if isValid != False:
    if score > 1.0:
        print("Bad score")
    elif 1.0 >= score >= 0.9:
        print("A")
    elif 0.9 > score >= 0.8:
        print("B")
    elif 0.8 > score >= 0.7:
        print("C")
    elif 0.7 > score >= 0.6:
        print("D")
    else:
        print("F")