# Solution for Problem #9
# The program reads the text file "Romeo_and_Juliet.txt"
# and outputs every second line

with open("Romeo_and_Juliet.txt", "r") as f:
# reads text line by line:    
    for line in f:
        c = f.readline()
        print(c)
# closing text file
f.close()

