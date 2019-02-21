# Solution for Problem #1
# The program asks user to input any positive integer 
# and outputs the sum of all numbers between one and that number

# asks user to input a positive number
x = int(input("Please input any positive integer: "))

# checks if an entered number is negative
if x < 0:
    print("You have entered a negative integer")

# checks if an entered number is zero
elif x == 0:
    print("You've entered Zero. This's not a positive integer")

# if the number is positive, adding two variables "total" and "i", both equal "x"
else:
    total = x
    i = x

    # the program will sum up all numbers starting i + (i-1)... till i > 0 
    while i > 0:
        total = total + (i - 1)
        i = i - 1

    # prints the Sum of all integers between 1 and entered at the beginning integer
    print("Sum of all numbers between 1 and", x, "equals", total)