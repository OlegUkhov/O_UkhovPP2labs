#HOME
print("Hello, World!")
print("Woohoo!")

#SYNTAX
if 5 > 2:
    print("Five is greater than two!")

if 5 != 4:
    print("Five is not equal to four")

x = 5
y = "Hello, World"

t = 213
z = "String var"

#COMMENTS
#the comment
print("Hello, World!") #This is a comment
print("Part without a comment") #comment part

#you can prevent python from executing code

#This is a comment
#written in
#more than just one line
print("Hello, World!")

#there's no multiline comments 
#so you need to insert '#' for each line

'''or you can place 
your comment into 
triple quotes like this'''

#VARIABLES
x = 5
y = "John"
print(x)
print(y)

x = "string var"
y = 15
print(x, y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 
x = int(5)
y = float(15)
z = str(6)
print(x, y, z)

x = 5
y = "John"
print(type(x))
print(type(y)) 
x = 511.5
y = '234'
print(type(x), type(y))

x = "John"
# is the same as
x = 'John' 

a = 4
A = "Sally"
#A will not overwrite a
c = 'hello'
C = 'World'
print(c, C)

#VARIABLE NAMES
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = 'camel case'
MyVariableName = 'Pascal case'
my_variable_name = 'Snake case'

#ASSIGN MULTIPLE VALUES
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

a, b, c = 'letters', 324, True
print(a, b, c)

x = y = z = "Orange"
print(x)
print(y)
print(z)

a = b = c = 'banana'
print(a, b, c)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits #unpacking
print(x)
print(y)
print(z) 

nums = [2, 4, 5]
a, b, c = nums
print(a, b, c)

#OUTPUT VARIABLES
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

a, b, c = 'ba', 'na', 'na'
print(a, b, c)
print(a + b + c)

x = 5
y = 10
print(x + y)

a, b = 15, 75
print(a + b)

x = 5
y = "John"
print(x, y)

a = 12
b = 'twelve'
print(a, b)

#GLOBAL VARIABLES
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

a = "cute"
def myfunc():
    print("Cats are " + a)
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x) 

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

def myfunc():
    global a
    a = "cute"
myfunc()
print("Cats are " + a)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
    global x
    x = "good"
myfunc()
print("Python is " + x)

#DATA TYPES
x = 5
print(type(x)) 

a = True
print(type(a))

x = "Hello World" #str
x = 20 	#int 	
x = 20.5 	#float 	
x = 1j 	#complex 	
x = ["apple", "banana", "cherry"] 	#list 	
x = ("apple", "banana", "cherry") 	#tuple 	
x = range(6) 	#range 	
x = {"name" : "John", "age" : 36} 	#dict 	
x = {"apple", "banana", "cherry"} 	#set 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	
x = True 	#bool 	
x = b"Hello" 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview 	
x = None

x = str("Hello World") 	#str 	
x = int(20) 	#int 	
x = float(20.5) 	#float 	
x = complex(1j) 	#complex 	
x = list(("apple", "banana", "cherry")) 	#list 	
x = tuple(("apple", "banana", "cherry")) 	#tuple 	
x = range(6) 	#range 	
x = dict(name="John", age=36) 	#dict 	
x = set(("apple", "banana", "cherry")) 	#set 	
x = frozenset(("apple", "banana", "cherry")) 	#frozenset 	
x = bool(5) 	#bool 	
x = bytes(5) 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview

#NUMBERS
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = 5
b = 5.5
c = 5j

print(type(x), type(y), type(z), type(a), type(b), type(c))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y)) #integers
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y)) #float
print(type(z))

x = 35e3
y = 12E4 #e is power of 10
z = -87.7e100

print(type(x))
print(type(y)) #float
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y)) #complex
print(type(z))

a, b, c = -27j, 15e10, -2523
print(type(a), type(b), type(c))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10)) 
print(random.randrange(90, 99))

#CASTING
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

a = float(45)
b = str(True)
c = int('124')
print(type(a), type(b), type(c))