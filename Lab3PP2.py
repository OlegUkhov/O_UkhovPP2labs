#FUNCTION

def f1():
    print('First function in this lab')

f1()

def f1(word):
    print('word: ' + word)

f1('first')
f1('second')
f1('third')

def f2(firstArg, secondArg):
    print(secondArg + " " + firstArg)

f2('Word1', 'Word2')

def f3(*manyArgs):
    print('Set of fruits: ', set(manyArgs))

f3('Mango', 'Banana', 'Pineapple')

def f4(arg3, arg2, arg1):
    print('Second instrument: ' + arg2)

f4(arg2 = 'Piano', arg3 = 'guitar', arg1 = 'ukulele')

def f5(**dictF):
    print('First pet is a ' + dictF["arg1"])

f5(arg1 = 'Cat', arg2 = 'Dog')

def f6(city = 'Almaty'):
    print("The most interesting city in KZ is " + city)

f6('Astana')
f6('Pavlodar')
f6()
f6('Shymkent')

def f7(Pet):
    for i in Pet:
        print(i)

Pets = ['Dog', 'Kit', 'Parrot']
f7(Pets)

def f8(num):
    return 100 // num

print(f8(15))
print(f8(200))
print(f8(10))

def emptyf():
    pass

def f9(pos, /):
    print(pos)
f9('pos = 10 will give an error')

def f9(noPosition):
    print(noPosition)
f9(noPosition = 'Now its possible to use keyword args')

def f10(*, keyw):
    print(keyw)
f10(keyw = 'Only keyword args')

def combine(x, y, /, *, z, t):
    print(x + z + y + t)
combine('one ', 'three ', z = 'two ', t = 'four')

def rec(var):
    if(var > 0):
        res = var + rec(var - 3)
        print(res)
    else:
        res = 0 
    return res
print("First recursion: ")
rec(9)

#LAMBDA

lam = lambda var : var / 10
print(lam(19))

lam = lambda x, y : int(x + y - x / y)
print(lam(15, 5))

lam1 = lambda x, y, z : x - y - z
print(lam1(100, 50, 25))

def f11(num):
    return lambda x : x - num
var = f11(5)
print(var(6))

def f12(firstLambda):
    return lambda fr : fr + firstLambda

firstl = f12(51)
secondl = f12(99)
print(firstl(49), ' ', secondl(1))

#CLASSES AND OBJECTS

class c1:
    num = 10

obj1 = c1()
print(obj1.num)

class c2:
    def __init__(self, Color, material):
        self.Color = Color
        self.material = material

o1 = c2('gray', 'stone')
print(o1.Color, o1.material)

class student:
    def __init__(self, course, school):
        self.course = course
        self.school = school
    
    def __str__(self):
        return f"{self.course}({self.school})"

o2 = student(1, 'site')
print(o2)

class Students:
    def __init__(self, course, school):
        self.course = course
        self.school = school
    
    def f1(self):
        print('Course of the student: ', self.course)
o3 = Students('Second', 'SITE')
o3.f1()

class St:
    def __init__(otherword, course, school):
        otherword.course = course
        otherword.school = school
    
    def f2(other):
        print('school of the student: ', other.school)
o4 = St('third', 'SITE')
o4.f2()

o3.course = 1
o3.f1()

del o4.school

del o3

class empty:
    pass

#INHERITANCE

class pc:
    def __init__(self, cpu, gpu):
        self.processor = cpu
        self.graphic = gpu

    def printname(self):
        print(self.processor, self.graphic)

pc1 = pc('intel', 'radeon')
pc1.printname()

class otherpc(pc):
    pass

pc2 = otherpc('amd', 'geforce')
pc2.printname()

class otherpc1(pc):
    def __init__(self, cpu, gpu):
        self.__init__(self, cpu, gpu)
        self.__init__(self, cpu, gpu)

class otherpc2(pc):
    def __init__(self, cpu, gpu):
        super().__init__(cpu, gpu)

class otherpc3(pc):
    def __init__(self, cpu, gpu):
        super().__init__(cpu, gpu)
        self.ram = '32 gb'
    
class otherpc4(pc):
    def __init__(self, cpu, gpu, ram):
        super().__init__(cpu, gpu)
        self.randaccessmem = ram

o5 = otherpc4('amd', 'radeon', '32 gb')

class otherpc5(pc):
    def __init__(self, cpu, gpu, ram):
        super().__init__(cpu, gpu)
        self.randaccessmem = ram

    def setup(self):
        print('Your pc:', self.processor, self.graphic, self.randaccessmem)

o6 = otherpc5('amd', 'palit', '64 gb')
o6.setup()