import re

txt = 'a_ab abb a123b aXb abbb_abbbb a_b'

pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, txt)

print(matches)