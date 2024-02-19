n=int(input())
gen=(x**2 for x in range(1,n+1))
for value in gen:
    print(value)
