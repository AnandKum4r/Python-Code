# Break and Continue

# #Break Statement
# k=[2,3,4,55,66,4,12,14,4,14,88,90,67,4,65,4,55]
# for i in k:
#     if(i==4):
#         print("Element found",i)            #break will stop when condtion will match
#         break                       # Exits the loop when the condition is met
#     print(i)

# #Continue Statement
# k=[2,3,4,55,66,4,12,14,4,14,88,90,67,4,65,4,55]
# for i in k:
#     if(i==4):
#         print("Element found",i)            #Continue will not stop it will contiue at every cond match
#         continue                    # Skips the current iteration and continues with the next one
#     print(i)

# pass keyword
# Pass is a in-bulit keyword for pyhton pass keyword are useful to skip the statement of python code

x=10
y=20
z=x+y
print(z)

for i in range(0,x):
    pass
if(x>y):
    pass
n=x*y
print(n)