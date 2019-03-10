# Solution for Problem #9
# The program reads the text file "Romeo_and_Juliet.txt"
# and outputs every second line

with open("Romeo_and_Juliet.txt", "r") as f:
    count = 1   
    for line in f:
# prints every single line of the text
        if count % 2 == 0:
            print(line.strip())
        count = count + 1

# closing text file
f.close()

