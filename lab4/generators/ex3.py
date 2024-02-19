n=int(input())
gen=(x for x in range(0,n+1,12))
for value in gen:
    print(value,end=',')

#or
def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

# Example usage:
n = int(input())
gen = divisible_by_3_and_4(n)

for value in gen:
    print(value, end=', ')
