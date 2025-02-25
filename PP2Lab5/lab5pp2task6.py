import re

txt = 'Ab, az. Im oP a123b aXb'

pattern = r"[ ,.]"

result = re.sub(pattern, ":", txt)

print(result)