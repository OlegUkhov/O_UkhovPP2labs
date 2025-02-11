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
