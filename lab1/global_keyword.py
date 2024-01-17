# x is global 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
