def has_33(nums):
    count=0
    for i in nums:
        if(i==3):
            count+=1
        else:
            count=0
        if(count==2):
            return True
    return False
c=input()
d=[]
for i in c.split():
    d.append(int(i))
print(has_33(d))
    
