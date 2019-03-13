import datetime as dt
from datetime import date

d = date.strftime(dt.datetime.now(), "%d")
d = int(d)
#checking for ending for the day
if 4 <= d <= 20 or 24 <= d <= 30:
    suf = "th"
else:
# assign one list's values to another (e.g. "st" will be assigned if remainder is 1, "nd" - remainder 2)
    suf = ["st", "nd", "rd"][d % 10 - 1]
# turn d into string to concatenane day with suffix with no space in between
dd = str(d)+suf

z = date.strftime(dt.datetime.now(), "%A, %B")
y = date.strftime(dt.datetime.now(),"%Y at %I:%M%p").replace("AM", "am").replace("PM", "pm")

print(z, dd, y)
