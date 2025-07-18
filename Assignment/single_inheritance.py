class A:
 def showA(self):
  print("Hello Mr. Programmer :) ")
class B(A):
 def showB(self):
  print("This is single inheritance example :) ")
class C(B):
 def showC(self):
  print("Hello C")
b=C()
b.showA()
b.showB()
b.showC()