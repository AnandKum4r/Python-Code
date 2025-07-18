# Looping statements
    # Loops are useful to print any statements multiple times according your condition
    # For Loop,while loop,nested while loop,nested for loop

# For loop
    # 'for' is a keyword,'i' is a vairable,'in' is a operator,'range' is a function,
    # '0' is a initial vale of loop,'10' is a last value of loop

# for i in range(0,10,2): #(initial value,end value,increment operator)
#                         # In above 0 is a initial value, 10 is end vale and 2 is increament value
#     print(i)

# # Reverse loop
# for i in range(10,0,-1): #n+1 third parameter by default 1 ka increment hota hai
#     print(i)

# # Write a program to calculate factorial of any number
# x=int(input("Enter the number: "))
# total=1
# for i in range(x,0,-1):
#     total=total*i
# print(total)

# While Loop 
    # With the while loop we can execute a set of statements as long as a condition is true.
    # While loop have not by default increment arguments
    # While loop is goes till infinite

# x=0             # intial point of loop
# while x<10:     # Condition
#    # x=x+1      # it will print from 1 to 10    x=0+1=1, x=1+1=2, x=2+1=3, x=3+1=4,.....10
#     print(x)
#     x=x+1       # it will print from 0 to 9     x=0, x=0+1=1, x=1+1=2, x=2+1=3, x=3+1=4,....9
    
# a=10
# while a>0:      # it will check condition from 10
#     a=a-1       # 10=10-1=9, 9=9-1=8, 8=8-1=7, ....0
#     print(a)    # this will print from 9 to 0 


# Calculator program using while loop
while True:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    print("5.Exit")
    x=int(input("Enter the choice: "))
    if(x==1):
        a=int(input("Enter the value: "))
        b=int(input("Enter the 2nd value: "))
        c=a+b
        print(c)
    elif(x==2):
        a=int(input("Enter the value: "))
        b=int(input("Enter the 2nd value: "))
        c=a-b
        print(c)
    elif(x==3):
        a=int(input("Enter the value: "))
        b=int(input("Enter the 2nd value: "))
        c=a*b
        print(c)
    elif(x==4):
        a=int(input("Enter the value: "))
        b=int(input("Enter the 2nd value: "))
        c=a//b
        print(c)
    elif(x>5):
        break