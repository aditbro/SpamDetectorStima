import re

s = "Adit kuliah di Itb"
q = "[Ii][Tt][Bb]"

m = re.search(q,s)
if m:
    print (m.group())