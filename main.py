import re

st = input()
pattern = r"00"
if re.match(pattern, st):
    newstr = re.sub(pattern, "+", st, count=1)
    print(newstr)
else:
    print(st)