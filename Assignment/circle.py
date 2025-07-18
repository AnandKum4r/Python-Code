def area(r): 
 PI = 3.142
 return PI * (r*r);
def perimeter(r):
 PI=3.142 
 return 2*PI*r;
a=int(input("Enter radius : "))
print("Area of circle is is %.6f " % area(a))
print("Perimeter of circle is %.6f " % perimeter(a))