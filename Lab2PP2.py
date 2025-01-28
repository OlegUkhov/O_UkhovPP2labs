#BOOLEANS

print(30 > 1)
print(2 == 4)
print(49 < 23)

a = 98
b = 35

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(34))

a = "Hello"
b = 24

print(bool(a))
print(bool(b))

print(0 > -1, 0 == 0, 0 > 1)

bool("string")
bool(100)
bool(["one", "two", "three"]) 

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})  #all of these will return false

class mclass():
    def __len__(self):
        return 0
obj = mclass() 
print(bool(obj))

def func():
    return True
print(func()) 

def funct() :
    return False
if funct():
    print("YES!")
else:
    print("NO!") 

varr = 200
print(isinstance(varr, int)) 

a = "Hello"
if isinstance(a, str):
    print('is string?: ', isinstance(a, str))
else:
    print("is string?: ", isinstance(a, str))

#OPERATORS

print(10 + 5)
a = b = 5
a + b
a / b
a * b
a - b
a % b
a ** b
a // b

a += b
a -= b
a *= b
a /= b
a %= b
a //= b
a **= b
#&=  |=  ^=  >>=  <<=
print(a := b)

print(a == 5 and b > 4)
print(a < 5 and b < 10)
print(not(a < 0 or b > 100))

print(a is b)
print(a is not 5.0)

v = [1, 2, 3, 4, 5, 6, 7]

print(a in v, b not in v)

print((10 - a) - (b + 3))

print(19 + 8 * 3)

print(22/7)

print(11 - 45 + 34 - 21)

print(11 ** 3 > 34 ** 2)

#LISTS

liiiiist = ['one', 'two', 'three', 'four']
print(liiiiist)

liiiiist = ['one', 'one', 'zero', 'two', 'one', 'three', 'four']

print(len(liiiiist))

frstlist = ['abc', 'def', 'ghi', 'jkl']
scndlist = [True, True, True, False, False]
thrdlist = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]

mixlist = ['String', 214, False, 'String']

print(type(mixlist))

anotherlist = list(('some', 'body', 'once', 'told', 'me'))
print(anotherlist)

#ACCESS LIST ITEMS

mixlist = ['str', 122, True, 'Str']
print(mixlist[3])
print(mixlist[-2])

onemorelist = ['some', 'might', 'say', 'that', 'sunshine', 'follows', 'thunder']
print(onemorelist[2:4])

print(onemorelist[:3])

print(onemorelist[4:])

print(onemorelist[-7:-4])

newlist = ['1', '2', '3', '4', '5', '6', '7', '8']
if '3' in newlist:
    print('3 is in the list')

#CHANGE LIST ITEMS

a_list = ['strawberry', 'raspberry', 'blsackberry']
a_list[2] = 'cherry'
print(a_list)

b_list = ['a', 'b', 'c', 'd', 'e', 'f']
b_list[0:4] = ['w', 'z']
print(b_list)

b_list[0:1] = ['q', 's', 'p']
print(b_list)

b_list[2:5] = ['i']
print(b_list)

c_list = ['car', 'bike', 'bus']
c_list.insert(1, 'motorbike')
print(c_list)

#ADD LIST ITEMS

c_list.append('scooter')
print(c_list)

d_list = ['guitar', 'piano']
e_list = ['violin', 'drums']
d_list.extend(e_list)
print(d_list)

f_tuple = ('bass', 'flute')
d_list.extend(f_tuple)
print(d_list)

#REMOVE LIST ITEMS

d_list.remove('bass')
print(d_list)

d_list = ['guitar', 'piano', 'violin', 'drums', 'piano', 'flute']
d_list.remove('piano')
print(d_list)

d_list.pop(3)
print(d_list)

d_list.pop()
print(d_list)

del d_list[1]
print(d_list)

del d_list

g_list = ['guitar', 'piano', 'violin', 'drums', 'bass', 'flute']
g_list.clear()
print(g_list)

#LOOP LISTS

h_list = ['guitar', 'piano', 'violin', 'drums', 'bass', 'flute']
for i in h_list:
    print(i)

for j in range(len(h_list)):
    print(h_list[j])

i = 0
while i < len(h_list):
    print(h_list[i])
    i = i + 1

[print(q) for q in c_list ]

#LIST COMPREHENSION

i_list = ['cherry', 'mango', 'melon', 'watermelon']
j_list = []

for i in i_list:
    if 'a' in i:
        j_list.append(i)

print(j_list)

j_list = [c for c in i_list if 'r' in c]
print(j_list)

# list = [expression for iteme in iterable if condition == true]

j_list = [v for v in i_list if v != 'melon']
print(j_list)

j_list = [x for x in i_list]

k_list = [b for b in range(6)]
print(k_list)

k_list = [x for x in range(15) if x < 13]
print(k_list)

upper_list = [x.upper() for x in i_list]
print(upper_list)

k_list = ['what' for x in k_list]
print(k_list)

k_list = [x if x != 'what' else 'yes' for x in k_list]
print(k_list)

#SORT LISTS

l = ['cherry', 'mango', 'melon', 'watermelon']
l.sort()
print(l)

k = [1, 56, 34, 0, -1]
k.sort()
print(k)

l.sort(reverse = True)
print(l)

k.sort(reverse = True)
print(k)


def myf(n):
    return abs(n - 34)

p = [0, 33, 100, 98, 34]
p.sort(key = myf)
print(p)

u = ['A', 'b', 'C', 'a']
u.sort()
print(u)

u.sort(key = str.lower)
print(u)

u.reverse()
print(u)

#COPY LISTS

g = ['guitar', 'piano', 'violin', 'drums', 'bass', 'flute']
g1 = g.copy()
print(g1)

g2 = list(g1)
print(g2)

g3 = g2[:]
print(g3)

#JOIN LISTS

u1 = ['guitar', 'piano', 'violin']
u2 = ['drums', 'bass', 'flute']

u3 = u1 + u2
print(u3)

u4 = u1
for x in u2:
    u4.append(x)

u1 = ['guitar', 'piano', 'violin']

print(u4)

u1.extend(u2)
print(u1)

#TUPLES

t = ('word', 'wor', 'wo', 'w')
print(t)

t = ('a', 'a', 'c', 'b', 'c')
print(t)

print(len(t))

t = ('aaaaaa',) #with comma
print(type(t))

notTuple = ('aaa') #without comma
print(type(notTuple))

t1 = ('str', 'st', 's')
t2 = (True, True, True, True, False)
t3 = (0, 100, 3, -1)

t4 = ('str', 124, 'str', False)

print(type(t4))

t5 = tuple(('woooord', 'woooo'))
print(t5)

#ACCESS TUPLE ITEMS

t = ('word', 'wor', 'wo', 'w')
print(t[2])

print(t[-3])

print(t[1:3])

print(t[:2])

print(t[1:])

print(t[-3:-1])

if 'word' in t:
    print('sure')

#UPDATE TUPLES

t = ('guitar', 'piano', 'violin', 'drums', 'bass', 'flute')
l = list(t)
l[3] = 'singer'
t = tuple(l)
print(t)

l = list(t)
l.append('onemoreinstrument')
t = tuple(l)
print(t)

t = ('guitar', 'piano', 'bass', 'flute')
t1 = ('drums',)
t += t1
print(t)

l = list(t)
l.remove('flute')
t = tuple(l)

del t

#UNPACK TUPLES

tup = ('abc', 'def', 'ghi')

(jkl, mno, pqr) = tup

print(jkl)
print(mno)
print(pqr)

t = ('guitar', 'piano', 'violin', 'drums', 'bass', 'flute')

(t1, t2, *t3) = t

print(t1)
print(t2)
print(t3)

t = ('guitar', 'piano', 'violin', 'drums', 'bass', 'flute')

(t1, *t2, t3) = t

print(t1)
print(t2)
print(t3)

#LOOP TUPLES

t = ('guitar', 'piano', 'violin', 'drums', 'bass', 'flute')
for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

i = 0
while i < len(t):
    print(t[i])
    i = i + 1

#JOIN TUPLES

t1 = ('guitar', 'piano', 'violin')
t2 = ('bass',)

t3 = t1 + t2
print(t3)

t4 = t2 * 2
print(t4)

print(t4.count('bass'))
print(t1.index('piano'))

#SETS

s = {'something', 'in', 'the', 'way'}
print(s)

s = {'a', 'a', 'b', 'c'}
print(s)

s = {True, 1, '1', 'window'}
print(s)

s = {False, 0, '0', 'zero'}
print(s)

print(len(s))

s1 = {'string', 'data', 'type'}
s2 = {100, -100, 0, 12, 43}
s3 = {False, True}

s4 = {False, 134, True, 'word'}

print(type(s4))

s = set(('guitar', 'piano', 'violin', 'drums', 'bass', 'flute'))
print(s)

#ACCESS SET ITEMS

s = {'g', 'u', 'i', 't', 'a', 'r'}
for x in s:
    print(x)

print('y' in s)

print('y' not in s)

#ADD LIST ITEMS

s = {'g', 'u', 'i', 't', 'a', 'r'}

s.add("s")
print(s)

s2 = {'p', 'i', 'a'}
s3 = {'n', 'o'}

s2.update(s3)
print(s2)

s2 = {'p', 'i', 'a'}
s3 = ['o', 'n']

s2.update(s3)
print(s2)

#REMOVE SET ITEMS

s = {'g', 'u', 'i', 't', 'a', 'r'}

s.remove('i')
print(s)

s.discard('r')
print(s)

s.discard('o')

s = {'g', 'u', 'i', 't', 'a', 'r'}

x = s.pop()
print(x)
print(s)

s.clear()
print(s)

del s

#LOOP SETS

s = {'g', 'u', 'i', 't', 'a', 'r'}

for x in s:
    print(x)

#JOIN

s1 = {'a', 'b', 'c'}
s2 = {'c', 'd', 'e'}

s3 = s1.union(s2)
print(s3)

s3.clear()
s3 = s1 | s2
print(s3)

s1 = {'o', 'f', 't'}
s2 = {'car', 'bike'}
s3 = {1, 100, 23, 54}
s4 = {True, False}

s5 = s1.union(s2, s3, s4)
print(s5)

s5 = s1 | s2 | s3 | s4
print(s5)

s = {'s', 'e', 't'}
t = (False, True)

un = s.union(t)
print(un)

s = {'set', 0}
s1 = {'set1', 1}

s1.update(s)
print(s1)

s1 = {'s', 'e', 't', 1}
s2 = {2, 'e', 't', 's'}

s3 = s1.intersection(s2)
print(s3)

s4 = s1 & s2
print(s4)

s1.intersection_update(s2)
print(s1)

s1 = {1, 'word', False}
s2 = {True, 'word', 0}

s3 = s1.intersection(s2)
print(s3)

s1 = {1, 3, 5, 6}
s2 = {5, 6, 7, 9}
s3 = s1.difference(s2)
print(s3)

s4 = s1 - s2
print(s4)

s1.difference_update(s2)
print(s1)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3)

s3 = s1 ^ s2
print(s3)

s1.symmetric_difference_update(s2)
print(s1)

#DICTIONARIES 

d = {
    'num': 123,
    'word': 'cat',
    'bool': True
}
print(d)

print(d['word'])

d = {
    'num': 123,
    'word': 'yoo',
    'bool': True,
    'word': 'cat'
}
print(d)

print(len(d))

d = {
    'num': 123,
    'word': 'cat',
    'bool': True,
    'bool2': False,
    'list': ['aaa', 'bbb']
}

print(type(d))

d1 = dict(a = "word", b = 100, c = False)
print(d1) 

d = {
    'num': 123,
    'word': 'cat',
    'bool': True,
    'bool2': False,
    'list': ['aaa', 'bbb']
}
x = d['bool2']

x = d.get('bool')

x = d.keys()
print(x)

d['bool3'] = True
print(x)

y = d.values()
print(y)

d['word1'] = 'dog'
print(y)

z = d.items()
print(z)

d['num1'] = 321
print(z)

if 'word' in d:
    print('sure')

#CHANGE DICTIONARY ITEMS

d = {
    'num': 123,
    'word': 'cat',
    'bool': True,
    'list': ['aaa', 'bbb']
}
d['num'] = 100
print(d)

d.update({'word': 'kit'})
print(d)

#ADD DICTIONARY 

d = {
    'num': 123,
    'word': 'cat',
    'bool': True,
    'list': ['aaa', 'bbb']
}
d['number'] = 1000
print(d)

d.update({'word1': 'dog'})
print(d)

#REMOVE DICTIONARY ITEMS

d = {
    'num': 123,
    'word': 'cat',
    'bool': True,
    'list': ['aaa', 'bbb']
}
d.pop('bool')
print(d)

d.popitem()
print(d)

del d['num']
print(d)

d.clear()
print(d)

del d

#LOOP DICTIONARIES

d = {
    'num': 123,
    'word': 'cat',
    'bool': True,
    'list': ['aaa', 'bbb']
}
for i in d:
    print(i)

for i in d:
    print(d[i])

for i in d.values():
    print(i)

for i in d.keys():
    print(i)

for a, b in d.items():
    print(a, b)

#COPY DICTIONARIES

d = {
    'num': 123,
    'word': 'cat',
    'bool': True,
    'list': ['aaa', 'bbb']
}
d1 = d.copy()
print(d1)

d2 = dict(d)
print(d2)

#NESTED DICTIONARIES 

d = {
    'd1' : {
        'num1' : 11,
        'word1' : 'aaa'
    },
    'd2' : {
        'num2' : 124,
        'word2' : 'bbb'
    },
    'd3' : {
        'num3' : 432,
        'word3' : 'ccc'
    }
}

d1 = {
    'num1' : 11,
    'word1' : 'aaa'
}
d2 = {
    'num2' : 124,
    'word2' : 'bbb'
},
d3 = {
    'num3' : 432,
    'word3' : 'ccc'
}

d = {
    'd1' : d1,
    'd2' : d2,
    'd3' : d3
}

print(d['d3']['num3'])

d = {
    "d1" : {
    "word1" : "kitten",
    },
    "d2" : {
    "word2" : "kit",
    },
    "d3" : {
    "word3" : "cat",
    }
}

for a, b in d.items():
    print(a)
    
    for i in b:
        print(i + ':', b[i])

#IF ELSE

a = 100
b = 1000

if b == a:
    print('yes')

if a < b:
    print('true')
elif a == b:
    print('equality')

if a > b:
    print('true')
elif a == b:
    print('equality')
else:
    print('b is greater')

a = 'str'
b = 'str1'

if b != a:
    print('not equal')
else:
    print('equal')

if a > b : print('a is greater')

print('a is greater') if a > b else print('b is greater')

print("a is greater") if a > b else print("equal") if a == b else print("b is greater") 

a = 11
b = 22
c = 33
if a < b and b < c:
    print('yooo')

if a > b or b < c:
    print('it works')

if not a == b: 
    print('not equal')

a = 100
if a > 50:
    print('bigger than 50')
    if a > 60:
        print('bigger than 60')
    else: 
        print('less than 60')

a = True
b = False
if a == b:
    pass

#WHILE

i = 0
while i < 10:
    print(i)
    i += 2

i = 5
while i < 30:
    print(i + 4)
    if i == 20:
        break
    i += 5

i = 10
while i < 28:
    i += 3
    if i == 22:
        continue
    print(i)

i = 0
while i <= 19:
    print(i)
    i += 3
else:
    print('now i is bigger than 19')

#FOR LOOPS

l = ['a', 'b', 'c', 'd']
for i in l:
    print(i)

for i in 'abcdefghi':
    print(i)

for j in l:
    print(j)
    if j == 'c':
        break

for j in l:
    if j == 'c':
        break
    print(j)

for t in l:
    if t == 'a':
        continue
    print(t)

for i in range(10):
    print(i)

for i in range(0, 10):
    print(i)

for i in range(0, 101, 10):
    print(i)

for i in range(11):
    print(i)
else:
    print('thats all')

for i in range(15):
    if i == 10:
        print(i)
else:
    print('thats all')

a = [1, 2, 3]
b = [4, 5, 6]

for i in a:
    for j in b:
        print(i, j)

for i in [1, 2, 3]:
    pass