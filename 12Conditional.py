# Conditional Control Statements
    # control statements: if,else,nested if,ladder if
    # looping statements: for looop,while loop,nested loopnested while loop
    # break
    # continue
    # pass

# # IF ELSE
# x=int(input("Enter the value "))
# if(x%2==0):                   #divide x with given value and gives remainder
#     print("This is Even number ")
# else:
#     print("Odd")

#nested if
# x=int(input("Enter the value "))
# if(x>50 and x<100):
#     if(x%2==0):    #inner loop/nested
#         print("even")
#     else:
#         print("odd")
# else:
#     print("Out of range")

# #Ladder if
# x=int(input("Enter the choice "))
# if(x==1):
#     print("Sunday")
# elif(x==2):
#     print("Monday")
# elif(x==3):
#     print("Tuesday")
# else:
#     print("No choice")

# x=int(input("Enter the first no: "))
# y=int(input("Enter the second no: "))
# z=int(input("Enter the third no: "))

# if(x>y and x>z):
#    print(x,'is largest no')
# elif(y>z and y>x):
#    print(y,'is largest no')
# elif(z>x and z>y):
#    print(z,"is largest no")
# else:
#    print("same")

# Assignment Questions
    # Q1.Write a program to create a calculator

print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")

x=float(input("Enter the choice: "))
if(x==1):
   a=float(input("Enter the value "))
   b=float(input("Enter the second value "))
   c=a+b
   print(c)
elif(x==2):
   a=float(input("Enter the value "))
   b=float(input("Enter the second value "))
   c=a-b
   print(c)
elif(x==3):
   a=float(input("Enter the value "))
   b=float(input("Enter the second value "))
   c=a*b
   print(c)
elif(x==4):
   a=float(input("Enter the value "))
   b=float(input("Enter the second value "))
   c=a//b   
   print(c)
else:
   print("No choice")