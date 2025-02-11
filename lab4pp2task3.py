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
