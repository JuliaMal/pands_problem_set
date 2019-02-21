# Solution for Problem #5
# The program asks user to input any positive integer 
# and tells the user whether or not the number is a prime (can be diveded by 1 and itself only)

# asks user to input a positive number
x = int(input("Please input any positive integer: "))

# checks if the User's number can be divided by 2, then 3, etc.. until x (x is not included)
for i in range(2, x):

    # if the number can be diveded by any other number rathen than 1 and iself, then the program breaks the loop 
    # as it was already identified that the entered number is not a prime
    if x % i == 0:
        print(x, "is not a prime number")
        break
else: 
    # prints a prime number
    print(x, "is a prime number")