try:
 a=eval(input("Enter first number :"))
 b=eval(input("Enter second number :"))
 c=a*b
 print("Result =",c)
except NameError:
 print("Name Error !! Enter number only ")
finally:
 print("Bye Bye Try Again !!! ")