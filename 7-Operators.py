#(5)Assignment Operator
# a=500
# a=a+50 #use this
# print(a)

# x=150
# x+=40 #or this both are same used for addition
# print(x)

#(6)Identity Operators
# Identity Operators are useful to compare the address of variables

# #if the both value given same address will be same
# x=110
# y=110
# print(id(x))
# print(id(y))
# print(x is y)

#if both value given different value then address will not be same
a=567
b=890
print(id(a)) #call by reference
print(id(b))
if(a is b):
    print("Address of a and b are same")
else:
    print("Adddress is not same")

#if input given by user and giving same value in input output will be false becoz it is 
#working on address
x=input("Enter the value ")
y=input("Enter 2nd value ")
print(id(x))
print(id(y))
print(x is y)