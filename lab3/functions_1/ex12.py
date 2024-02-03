def histogram(a):
    for i in a:
        
        print(i*'*')
c=input()
d=[]
for i in c.split():
    d.append(int(i))
histogram(d)