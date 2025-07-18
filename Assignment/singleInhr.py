class Hello:
 def showHello(self):
  print("Hello Mr. Programmer ")
class B(Hello):
 def showB(self):
  print("This is single inheritance example ")
b=B()
b.showHello()
b.showB()