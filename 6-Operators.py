# (4.)Logical Operators
# 1.AND True if both statements are true
# 2.OR True if one of the statements is true
# 3.NOT Reverse the result, returns False if the result is true

# x=10
# y=20
# z=15
# print(x>y and y<z) #AND operators
# print(x<y and y>z)
# print(x>y and y>z)

# print(x<y or y<z) #OR operators 
# print(not(x<y or y<z)) #NOT operators
# #yashwant canecker book lets us pyhton 6th edition

# #use of AND as a login page
# a=input("Enter the username ")
# b=input("Enter the password ")
# print(a=='Anand' and b=='108108')

# a=input("Enter the username ")
# b=input("Enter the password ")
# if(a=='Anand' and b=='108108'):
#     print("Login Successful")
# else:
#     print("Login Failed")

# # Login page as a multiple person using AND OR
# a=input("Enter the username ")
# b=input("Enter the password ")
# if((a=='Anand' or a=='Prateek' or a=='Akash') and b=='108108'):
#     print("Login Successful")
# else:
#     print("Login Failed")

# # Use of NOT
# a=True
# b=False
# c=None
# print(a)
# print(b)
# print(c)
# print(not a)
# print(not b)
# print(not c)

x="Hi I am Anand"
y="Anand"
print(y in x)
print(y not in x)