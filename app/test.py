import re
def check_pattern_in_string(pattern, text):
    if re.match(pattern, text) != None:
        return True
    else:
        return False

l=[]
for i in range(2,20):
    l.append(str(i))
    l.append("a")
    l.append("b")
    l.append(f"{i} / {i**2}")
    l.append("x")

print(l)
pattern = r'^(-|\d+) / \d+$'
print(20*"#")
res=[]
for i in range(len(l)):
    if check_pattern_in_string(pattern,l[i]):
        print(l[i])
        res.append(l[i-2])
        res.append(l[i-1])
        res.append(l[i+1])
print(res)