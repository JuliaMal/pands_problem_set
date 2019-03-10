# Solution for Problem #4
# The program asks user to input any positive integer 
# and outputs the succesive values of the following calculation:
# at each step calculates the next value by taking the current value and,
# if it's even, divides by 2,
# if it's odd, multiplies it by 3 and adds 1

# asks user to input a positive number
x = int(input("Please input any positive integer: "))

# the looping should stop once x value is equal 1
while x > 1:
    # checks if the number is even
    if x % 2 == 0:
        #if yes, divides this number by 2
        x = x // 2
    # otherwise multiplies it by 3 and adds 1
    else:
        x = (x * 3) + 1
    # prints everytime the value of x
    print (x, end = " ")

    

   