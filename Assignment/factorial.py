#WAP to find factorial of given number using recursion 
def fact(n):
 if n==0 or n==1:
  return 1
 else:
  return n*fact(n-1)
x=int(input("Enter a number to find factorial : "))
f=fact(x)
print("Factorial of ",x,"is",f)