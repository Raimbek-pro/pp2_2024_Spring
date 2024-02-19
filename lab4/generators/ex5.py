def listall(b):
    for i in range (b,0,-1):
        yield i
b=int(input())
gen=listall(b)
for value in gen:
    print(value,end=" ")