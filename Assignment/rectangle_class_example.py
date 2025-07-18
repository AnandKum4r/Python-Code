class Rectangle:
  def setValue(self,l,b):
   self.l=l
   self.b=b
  def Area(self):
   return self.l*self.b
  def Perimeter(self):
   return 2*(self.l+self.b)
x=int(input("Enter the area of Rectangle "))
y=int(input("Enter the perin og rectan "))
a=Rectangle()
a.setValue(x,y)
print("Area of rec is ",a.Area())
print("Peri of rec is ",a.Perimeter())