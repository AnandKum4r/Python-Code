#Multiple Inheritance
class A:
 def m1(self):
  print("m1 method from class A")
class B:
 def m2(self):
  print("m2 method from class B")
class C(A,B):
 def m3(self):
  print("m3 method from class C")
c=C()
c.m1()
c.m2()
c.m3()
