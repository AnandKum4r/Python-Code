try:
 a=int(input("Enter first number :"))
 b=int(input("Enter second number :"))
 c=a/b
 print("Result is =",c)
except ZeroDivisionError:
 print("Are you trying by zero ?")
finally:
 print("Bye Bye")