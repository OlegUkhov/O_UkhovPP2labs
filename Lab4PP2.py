    #DATE

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

    #GENERATORS

# TASK 1

def sqr(n):
    for i in range(n + 1):
        yield i ** 2

print("num of squares:")
for x in sqr(5):
    print(x, end=" ")
print("\n")

# TASK 2

def evn(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("n pls: "))
print("even nums: " + ", ".join(str(x) for x in evn(n)))

# TASK 3

def d34(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("\ndiv 3 & 4:")
for x in d34(50):
    print(x, end=" ")
print("\n")

# TASK 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print("Squares from 3 to 7:")
for x in squares(3, 7):
    print(x, end=" ")
print()

# TASK 5

def cdown(n):
    while n >= 0:
        yield n
        n -= 1

print("counting down:")
for x in cdown(8):
    print(x, end=" ")

    #MATH 

import math

# TASK 1

def deg_to_rad(deg):
    return deg * (math.pi / 180)

deg = 15
print("Degree:", deg)
print("Radian:", round(deg_to_rad(deg), 6))

# TASK 2

def trap_area(h, b1, b2):
    return ((b1 + b2) / 2) * h

h = 5
b1 = 5
b2 = 6
print("Height:", h)
print("first base:", b1)
print("second base:", b2)
print("Area:", trap_area(h, b1, b2))

# TASK 3

def pol_area(n, s):
    return (n * (s ** 2)) / (4 * math.tan(math.pi / n))

n = 4
s = 25
print("Sides:", n)
print("Lenght:", s)
print("Area:", int(pol_area(n, s)))

# TASK 4

def p_area(b, h):
    return b * h

b = 5
h = 6
print("Base:", b)
print("Height:", h)
print("Area:", p_area(b, h))

    #JSON

import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<5}")
print("-" * 80)

for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    description = item["l1PhysIf"]["attributes"].get("descr", "")
    speed = item["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = item["l1PhysIf"]["attributes"].get("mtu", "")
    
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<5}")
