def rev(a):
    b=a.split()
    b.reverse()
    return " ".join(b)
a=input()
print(rev(a))