def uniq(d):
    n=[]
    for i in d:
        if d.count(i)==1:
            n.append(i)
    return n
c=input()
d=[]
for i in c.split():
    d.append(int(i))
print(uniq(d))