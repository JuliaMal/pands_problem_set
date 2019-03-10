# Solution for Problem #7
# The program asks user to input any positive floating poiny number 
# and outputs an approximation of its square root:

# asks user to input a positive number
x = input("Please input any positive number: ")
# turns the entered number into a floating point number:
y = float(x)

import math
#calculates square root and round it to decimals:
z = round(math.sqrt(y), 1)

print("The square root of", y, "is approx.", z)