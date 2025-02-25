import re

txt = 'a ab abb a123b aXb'

pattern = r"ab*"

matches = re.findall(pattern, txt)

print(matches)