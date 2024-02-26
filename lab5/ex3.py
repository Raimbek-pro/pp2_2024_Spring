import re
# f=open("/Users/raiymbekomarov/Documents/pp2/lab5/row.txt","r",encoding="utf8")

testdata=input()
# text=f.read()
Pattern=r'[a-z]+_[a-z]+'
print(re.search(Pattern,testdata))
