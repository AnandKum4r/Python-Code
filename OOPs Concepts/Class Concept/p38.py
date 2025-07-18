class calculator:
 def sum(self,x,y):
  return(x+y)
 def sub(self,x,y):
  print("Sub =",x-y)
 def mul(self,x,y):
  return(x*y)
 def div(self,x,y):
  return(x/y)
cal=calculator()
print(cal.sum(10,2))
cal.sub(10,2)
print(cal.mul(10,2))
print(cal.div(10,2))