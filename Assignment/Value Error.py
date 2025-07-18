try:
 a=int(input("Enter first number :"))
 b=int(input("Enter second number  :"))
 c=a*b
 print("Result is =",c)
except ValueError:
 print("Value Error please enter numbers only")
finally:
 print("Bye Bye")