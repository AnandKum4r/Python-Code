class Rectangle:
   def setValue(self,l,b):
     self.l=l
     self.b=b
   def Area(self):
     return self.l*self.b
   def Perimeter(self):
     return 2*(self.l+self.b)
class Square(Rectangle):
   def side(self,s):
     self.s=s
   def area(self):
     return self.s*self.s
   def perimeter(self):
     return 4*self.s
x=int(input("Enter the lenght of Rectangle : "))
y=int(input("Enter the breadth og Rectangle : "))
a=Rectangle()
a.setValue(x,y)
print("Area of rectangle is : ",a.Area())
print("Perimeter of rectangle is : ",a.Perimeter())
z=int(input("Enter the side of Square : " ))
obj=Square()
obj.side(z)
print("Area of Square is : ",obj.area())
print("Perimeter of Square is : ",obj.perimeter())

 
