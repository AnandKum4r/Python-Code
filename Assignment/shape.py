class Shape:
 def showShape(self):
  print("This is Shape ")
class Rectangle(Shape):
 def showRectangle(self):
  print("This is Rectangular Shape ")
class Circle(Rectangle):
 def showCircle(self):
  print("This is Circular Shape ")
class Square(Circle):
 def showSquare(self):
  print("Square is a Rectangle ")
x=Square()
x.showShape()
x.showRectangle()
x.showCircle()
x.showSquare() 
