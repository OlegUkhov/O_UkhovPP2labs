#TASK 1
class str1:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("enter str: ")

    def printString(self):
        print(self.s.upper())

sm = str1()
sm.getString()
sm.printString()


#TASK 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
sq = Square(5)
print(sq.area())  


#TASK 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(4, 6)
print(rect.area())


#TASK 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, newpoint):
        return math.sqrt((self.x - newpoint.x) ** 2 + (self.y - newpoint.y) ** 2)

p1 = Point(3, 4)
p2 = Point(6, 8)
p1.show()
print(p1.dist(p2))


#TASK 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"adding: {amount}. new balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough money")
        else:
            self.balance -= amount
            print(f"withdrawals: {amount}. new balance: {self.balance}")

acc = Account("john", 100)
acc.deposit(50)  
acc.withdraw(30) 
acc.withdraw(200)


#TASK 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 17, 19, 22, 23, 29]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)


#FUNC1


#TASK 1
def oun(grams):
    return 28.3495231 * grams

print(oun(100))

#TASK 2
def cel(f):
    return (5 / 9) * (f - 32)

print(cel(100))

#TASK 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if chickens * 2 + rabbits * 4 == numlegs:
            return chickens, rabbits
    return None

print(solve(35, 94))

#TASK 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

print(filter_prime([10, 15, 17, 19, 22, 23, 29])) 

#TASK 5
def permute(s, l=0, r=None):
    if r is None:
        r = len(s) - 1
    
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]

s = list("abc")
permute(s)

#TASK 6
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_sentence("We are ready"))

#TASK 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#TASK 8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#TASK 9
import math

def sphere_volume(r):
    return (4 / 3) * math.pi * r ** 3

print(sphere_volume(3))

#TASK 10
def uniq(lst):
    uniqlst = []
    for item in lst:
        if item not in uniqlst:
            uniqlst.append(item)
    return uniqlst

print(uniq([1, 2, 3, 3, 2, 1, 5]))

#TASK 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("abcba"))

#TASK 12
def histogram(lst):
    for num in lst:
        print("*" * num)

histogram([4, 9, 7])

#TASK 13
import random

def guess_number():
    name = input("Hello! What is your name?\n")
    secret_number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    attempts = 0
    while True:
        guess = int(input("Take a guess.\n"))
        attempts += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guess_number()


#FUNC 2


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#TASK 1
def ishighrated(movie):
    return movie["imdb"] > 5.5

print(ishighrated(movies[0]))
print(ishighrated(movies[8]))

#TASK 2
def highrate(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

print(highrate(movies))  

#TASK 3
def moviecategory(movies, category):
    return [movie for movie in movies if movie["category"] == category]

print(moviecategory(movies, "Romance"))

#TASK 4
def averageimdb(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

print(int(averageimdb(movies))) 

#TASK 5
def avgcategory(movies, category):
    filtered_movies = moviecategory(movies, category)
    return averageimdb(filtered_movies)

print(avgcategory(movies, "Romance"))
