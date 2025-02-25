import re

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