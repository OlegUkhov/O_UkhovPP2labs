import re

txt = 'a ab abb a123b aXb abbb abbbb'

pattern = r"ab{2,3}"

matches = re.findall(pattern, txt)

print(matches)