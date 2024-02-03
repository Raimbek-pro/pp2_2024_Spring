def filter_prime(a):
    b=[]
    h=0
    for i in a:
        for j in range(2,i):
            if i%j==0:
                h=1
                break
        if(h==0):
            b.append(i)
        
        h=0
    return b
c=input()
d=[]
for i in c.split():
    d.append(int(i))
print(filter_prime(d))