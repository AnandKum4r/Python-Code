class Bank():
    def Interest(self):
        return 0
class Sbi(Bank):
    def __init__(self,p,n,r):
        self.p=p
        self.n=n
        self.r=r
    def Interest(self):
        return (self.p*self.n*self.r)/100
class Pnb(Sbi):
    def Interest1(self):
        return (self.p*self.n*self.r)/100
a=float(input("Enter the principle amount of Sbi Bank: "))
b=int(input("Enter the time(years) of Sbi Bank: "))
c=float(input("Enter the rateof Sbi Bank : "))
obj=Sbi(a,b,c)
print("The simple interest of Sbi bank is : ",obj.Interest())
x=float(input("Enter the principle amount of Pnb Bank : "))
y=int(input("Enter the time(years) of Pnb Bank: "))
z=float(input("Enter the rate of Pnb Bank : "))
obj2=Pnb(x,y,z)
print("The simple interest of Pnb bank is : ",obj2.Interest1())