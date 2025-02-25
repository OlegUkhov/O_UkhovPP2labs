import re

def spl(s):
    return re.split(r'(?=[A-Z])', s)

txt = 'AbcDefGhiJklMno'

res = spl(txt)

print(res)