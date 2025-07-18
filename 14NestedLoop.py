# Nested Loop

# for i in range(0,5):       
#     for j in range(0,5):  
#         print(j)            # this will give output in a single column

# for i in range(0,5):        # this create row
#     for j in range(0,5):    # this create column
#         #print(j)           # this will print in columns
#         print(j, end=" ")   # end is used to print in a row 
#     print()                 # this will print from new line

# # Printing star pattern
# for i in range(0,5):
#     for j in range(0,5):
#         print("*",end=" ")
#     print()

# #triangle print
# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# # Reverse triangle
# for i in range(0,5):
#     for j in range(5,i,-2):
#         print("*",end=" ")
#     print()

# # Number Pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# # Number pattern with global value
# k=0                         #this is global variable
# for i in range(0,5):
#     for j in range(0,i+1):
#         k=k+1
#         print(k,end=" ")
#     print()

# #1
# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# #2
# for i in range(0,5):
#     for k in range(4,i,-1):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# #3 reverse
# for i in range(0,5):
#     for k in range(0,i):
#         print(" ",end=" ")
#     for j in range(5,i,-1):
#         print("*",end=" ")
#     print()

# #4 diamond print
# for i in range(0,5):
#     for k in range(0,i):
#         print(" ",end=" ")
#     for j in range(5,i,-1):
#         print(" * ",end=" ")
#     print()

# #5
# for i in range(0,5):
#     for k in range(4,i,-1):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print(" * ",end=" ")
#     print()
# for i in range(0,5):
#     for k in range(0,i):
#         print(" ",end=" ")
#     for j in range(5,i,-1):
#         print(" * ",end=" ")
#     print()

# #ABC char pattern
# for i in range(65,70):         #ASCCII Value 65
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

# Finding any ASCII value
# x='a'
# y='A'
# z='D'
# print(ord(x))   #ord is used to find ASCCI Value of any char
# print(ord(y))
# print(ord(z))

#6
k=64
for i in range(65,70):
    for j in range(65,i+1):
        k=k+1
        print(chr(k),end=" ")
    print()

#Assignment > Print triangle