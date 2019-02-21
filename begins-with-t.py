# Solution for Problem #2
# The program checks whenever today's day begins with the letter T

import datetime

# checks if today is Tuesday or Thursday. If condition is met, then prints "Yes - ..."
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:  
  print("Yes - today begins with T")

# if condition is not met, then prints "No - ..."
else:
  print("No - today doesn't begin with T")