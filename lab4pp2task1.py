from datetime import datetime as dt, timedelta as td

# TASK 1
now = dt.now()
past = now - td(days=5)
print("5 days ago:", past.strftime("%Y-%m-%d"))

# TASK 2
yest = now - td(days=1)
tom = now + td(days=1)
print("Yesterday:", yest.strftime("%Y-%m-%d"))
print("Today:", now.strftime("%Y-%m-%d"))
print("Tommorow:", tom.strftime("%Y-%m-%d"))

# TASK 3
nodt = now.replace(microsecond=0)
print("no microseconds:", nodt)

# TASK 4
d1_str = input("first date")
d2_str = input("second date")

d1 = dt.strptime(d1_str, "%Y-%m-%d %H:%M:%S")
d2 = dt.strptime(d2_str, "%Y-%m-%d %H:%M:%S")

diff = (d2 - d1).total_seconds()
print("Seconds diff:", diff)