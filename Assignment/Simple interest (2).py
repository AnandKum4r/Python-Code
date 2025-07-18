class interest:
    def __init__ (self,p,n,r):
        self.p=p
        self.n=n
        self.r=r
    def simpleInterest(self):
        return (self.p*self.n*self.r)/100
a=float(input("Enter the principle amount : "))
b=int(input("Enter the time(years) : "))
c=float(input("Enter the rate : "))
obj=interest(a,b,c)
print("The simple interest is : ",obj.simpleInterest())
print()