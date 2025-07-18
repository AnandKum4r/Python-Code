x=int(input("Enter a value of x : "))
y=int(input("Enter a value of y : "))
if (x>0 and y>0):
 print("Lies in 1st quadrant")
elif (x<0 and y>0):
 print("Lies in 2nd quadrant")
elif (x<0 and y<0):
 print("Lies in 3rd quadrant")
elif (x>0 and y<0):
 print("Lies in 4rh quadrant")
elif (x==0 and y==0):
 print("Lies at origin")
