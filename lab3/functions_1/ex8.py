def spy_games(nums):
    count=0
    for i in nums:
        if( count==0):
            if(i==0):
                count+=1
        elif(count==1):
            if(i==0):
                count+=1
        elif(count==2):
            if(i==0):
                count=2
            elif(i==7):
                return True
    return False
c=input()
d=[]
for i in c.split():
    d.append(int(i))
print(spy_games(d))