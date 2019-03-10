# Solution for Problem #3
# The program prints all numbers between 1000 and 10000 that are divisible by 6, but not 12

# define a range:
for x in range(1000, 10000):

    # condition: divisible by 6, but not 12
    if x % 6 == 0 and not x % 12 == 0:
        # print the list of numbers that are matching the condition
        print(x)

