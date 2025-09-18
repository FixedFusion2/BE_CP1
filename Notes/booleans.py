# TE 2nd Booleans

# Booleans came from a guy named George Bool, he studied True or False math.
# There are only two values in a boolean.
# In python we capitalize True or False.

import time
import datetime as date

over = False

print(over)

name = "4"

print(name.isnumeric())

name_2 = "Jackson"

print(name.isnumeric())

print(bool(name))
print("")
current_time = time.time()
readable_time = time.ctime(current_time)
print(f"Current Time in seconds since Januray 1, 1970(epoc time): {current_time}")
print(f"Current Time: {readable_time}")

now = date.datetime.now()
hour = now.strftime("%H")
# Month = %m (%b, %B)
# day = %d
# year = %Y, %y
# hour = %H
# minutes = %M
# seconds = %S

print(f"Current time according to datetme: {now}")
print(f"Hour: {hour}")
print(f"My hour variable is a string: {isinstance(hour, str)}")
print(f"My hour variable is a float: {isinstance(hour, float)}")
print(f"My hour variable is a integer: {isinstance(hour, int)}")
