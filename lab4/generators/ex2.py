n=int(input())
gen=(x for x in range(0,n+1,2))
for value in gen:
    if value==n:
        print(value)
    else:
        print(value,end=',')