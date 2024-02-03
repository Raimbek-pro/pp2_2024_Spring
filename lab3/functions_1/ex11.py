def pali(a):
    if a[::-1]==a:
        return True
    return False
a=input()
print(pali(a))