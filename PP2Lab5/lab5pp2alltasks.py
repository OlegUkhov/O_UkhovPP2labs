import re


#TASK 1


txt = 'a ab abb a123b aXb'

pattern = r"ab*"

matches = re.findall(pattern, txt)

print(matches)


#TASK 2


txt = 'a ab abb a123b aXb abbb abbbb'

pattern = r"ab{2,3}"

matches = re.findall(pattern, txt)

print(matches)


#TASK 3


txt = 'a_ab abb a123b aXb abbb_abbbb a_b'

pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, txt)

print(matches)


#TASK 4


txt = 'a_ab bbb_abbbb a_b AbcDefGhi JklMno'

pattern = r"[A-Z][a-z]+"

matches = re.findall(pattern, txt)

print(matches)


#TASK 5


txt = 'a_ab bbb_abbbb a_b AbcDefGhi JklMno'

pattern = r"a.*b"

matches = re.findall(pattern, txt)

print(matches)


#TASK 6


txt = 'Ab, az. Im oP a123b aXb'

pattern = r"[ ,.]"

result = re.sub(pattern, ":", txt)

print(result)


#TASK 7


def transform(snake):
    x = snake.split('_')
    camel = x[0]
    for word in x[1:]:
        camel += word.capitalize()
    return camel

txt = 'snake_case_str'

result = transform(txt)

print(result)


#TASK 8


def spl(s):
    return re.split(r'(?=[A-Z])', s)

txt = 'AbcDefGhiJklMno'

res = spl(txt)

print(res)


#TASK 9


def sp(s):
    return re.sub(r'(?=[A-Z])', ' ', s)
txt = 'AbcDefGhiJklMno'

res = sp(txt)

print(res)


#TASK 10


def transform(camel):
    snake = ''
    for char in camel:
        if char.isupper():
            snake += '_' + char.lower()
        else:
            snake += char
    return snake.lstrip('_')

txt = 'AbcDefGhiJklMno'

res = transform(txt)

print(res)