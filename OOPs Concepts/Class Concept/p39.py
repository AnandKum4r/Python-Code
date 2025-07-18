class MyMath:
 def greatest(self,a,b):
  if a>b:
   print("Greatest number =",a)
  else:
   print("Greatest number =",b)
 def evenodd(self,n):
  if n%2==0:
   print("Even no =",n)
  else:
   print("Odd no =",n)
MyMath().greatest(15,5)
MyMath().evenodd(23)
MyMath().evenodd(2)