import re

txt = 'a_ab bbb_abbbb a_b AbcDefGhi JklMno'

pattern = r"[A-Z][a-z]+"

matches = re.findall(pattern, txt)

print(matches)