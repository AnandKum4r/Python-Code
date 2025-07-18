#mulitilevel inheritance
class A:
 def SayHello(self):
   print("SayHello method class A ")
 def SayHii(self):
   print("SayHii method from class A")
class B(A):
 def Welcome(self):
  print("Welcome method from class B")
class C(B):
 def Hello(self):
  print("Hello method from class C")
c=C()
c.Hello()
c.Welcome()
c.SayHello()
c.SayHii()
