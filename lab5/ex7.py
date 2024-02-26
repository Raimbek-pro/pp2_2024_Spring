import re
testdata=input()
# text=f.read()
Pattern = r'[ ,.]'
replaced_text = re.sub(Pattern, ':', testdata)
print(replaced_text)