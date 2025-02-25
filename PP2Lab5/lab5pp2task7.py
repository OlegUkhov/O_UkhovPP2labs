import re

def transform(snake):
    x = snake.split('_')
    camel = x[0]
    for word in x[1:]:
        camel += word.capitalize()
    return camel

txt = 'snake_case_str'

result = transform(txt)

print(result)