import re

def sp(s):
    return re.sub(r'(?=[A-Z])', ' ', s)
txt = 'AbcDefGhiJklMno'

res = sp(txt)

print(res)