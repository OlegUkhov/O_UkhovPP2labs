#BUILT-IN FUNCTIONS


#TASK 1

l = [14, 12, 10, 8, 6]
res = 1

for num in l:
    res *= num
print(res)

res = eval('*'.join(map(str, l)))
print(res)

#TASK 2

i = input('your str')
up = sum(1 for x in i if x.isupper())
low = sum(1 for x in i if x.islower())
print('upper: ', up, 'lower: ', low)

#TASK 3

i = input('your str')
if i == i[::-1]:
    print('palindrome')
else:
    print('not palindrome')

#TASK 4

import time
num = int(input('number: '))
t = int(input('milliseconds: '))

time.sleep(t/1000)
res = num ** 0.5
print(res)

#TASK 5

tup = (1, True, True, 'Yes')
res = all(tup)
print(res)


        #DIR-AND-FILES


#TASK 1

import os

def l(path):
    dir = []
    files = []
    allit = os.listdir(path)

    for i in allit:
        ipath = os.path.join(path, i)
        if os.path.isdir(ipath):
            dir.append(i)
        elif os.path.isfile(ipath):
            files.append(i)

    return dir, files, allit


path = "C:/Users/brwla/OneDrive/Рабочий стол/"
dir, files, allit = l(path)

print('Directories: ', dir)
for d in dir:
    print(d)

print('Files: ')
for f in files:
    print(f)

print('all items: ')
for a in allit:
    print(a)

#TASK 2

def C(path):

    if os.path.exists(path):
        print("exists")
    else:
        print("does not exist.")
        return

    if os.access(path, os.R_OK):
        print("readable.")
    else:
        print("not readable.")

    if os.access(path, os.W_OK):
        print("writable.")
    else:
        print("not writable.")

    if os.access(path, os.X_OK):
        print("executable.")
    else:
        print("not executable.")

path = "C:/Users/brwla/OneDrive/Рабочий стол/"
C(path)

#TASK 3

import os

def c(path):
    if os.path.exists(path):
        print("exists")
        
        if os.path.isdir(path):
            print("It's a directory.")
        elif os.path.isfile(path):
            print("It's a file.")
        
        dir, name = os.path.split(path)
        print(f"Directory: {dir}")
        print(f"Filename: {name}")
    else:
        print("not exist")

path = "C:/Users/brwla/OneDrive/Рабочий стол/pp2.txt"
c(path)

#TASK 4

def c(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"{path} does not exist.")
        return 0

path = "C:/Users/brwla/OneDrive/Рабочий стол/Lab5PP2.py/lab5pp2task2.py"
l = c(path)
print(f"Number of lines: {l}")

#TASK 5

def l(path, lst):
    with open(path, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")

lst = [1, 2, 3, 4, 5]
path = "C:/Users/brwla/OneDrive/Рабочий стол/output.txt"
l(path, lst)
print(f"List has been written to {path}")

#TASK 6

import string

for l in string.ascii_uppercase:
    name = f"{l}.txt"
    with open(name, "w") as file:
        file.write(f"This is file {name}")
    print(f"Created: {name}")

#TASK 7

def c(s, d):
    try:
        with open(s, 'r') as src, open(d, 'w') as dest:
            dest.write(src.read())
    except FileNotFoundError:
        print("Source file not found")
    except Exception as e:
        print(f"An error occurred: {e}")

c('M.txt', 'destination.txt')

#TASK 8

import os

def rm(fp):
    if not os.path.exists(fp):
        print("No such file")
        return
    if not os.access(fp, os.W_OK):
        print("No permission")
        return
    try:
        os.remove(fp)
        print("Deleted")
    except Exception as e:
        print(f"Error: {e}")

rm("N.txt")
