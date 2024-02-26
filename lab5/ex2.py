import re
# f=open("/Users/raiymbekomarov/Documents/pp2/lab5/row.txt","r",encoding="utf8")

testdata=input()
# text=f.read()
Pattern=r'ab{2,3}'
print(re.search(Pattern,testdata))
