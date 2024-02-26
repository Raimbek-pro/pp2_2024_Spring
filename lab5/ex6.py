"""
 pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)"""
import re
# f=open("/Users/raiymbekomarov/Documents/pp2/lab5/row.txt","r",encoding="utf8")

testdata=input()
# text=f.read()
Pattern = r'[ ,.]'
replaced_text = re.sub(Pattern, ':', testdata)
print(replaced_text)
