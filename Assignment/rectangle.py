class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def rectArea(self):
        return self.length*self.breadth
    def rectPeri(self):
        return 2*(self.length+self.breadth)
a=int(input("Enter length of rectangle : "))
b=int(input("Enter breadth of rectangle : "))
obj=rectangle(a,b)
print("Area of rectangle :",obj.rectArea())
print("Perimeter of rectangle :",obj.rectPeri())
print()