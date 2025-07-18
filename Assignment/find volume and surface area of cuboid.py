#WAP to find volume and surface area of cuboid

L=eval(input("Enter lenght of cuboid : "))
B=eval(input("Enter width of cuboid : "))
H=eval(input("Enter height of cuboid : "))
print("volume of cuboid is : ", L*B*H)
print("surface of cuboid is : ", 2*(L*B+B*H+H*L))