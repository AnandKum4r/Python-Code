#WAP to demonstrate concept of inheritance
class A:
 def showA(self):
   print("This message from base class : ")
class B(A):
 def showB(self):
   print("This message from derived class : ")
b=B() #object with reference variable
b.showA()
b.showB()