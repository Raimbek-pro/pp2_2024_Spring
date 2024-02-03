def solve(numheads, numlegs):
    print(int((numlegs-numheads*2)/2),"rabbits and ",int(numheads-(numlegs-numheads*2)/2)," chickens")
# 35= x+y
# 94=2x+4y
# heads*2=2x+2y
# 94=2x+4y
#(94-heads*2)/2=y
a=int(input())
b=int(input())
solve(a,b)