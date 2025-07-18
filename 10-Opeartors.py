#(9) Binary Operators 1 and 0 value
#         512  256  128  64  32  16  8  4  2  1

# x=27
# print(bin(x))  # bin() function is used to calculate binary number
# #output me 0b ayega uske age ka value consider krna h
# y='A'
# print(ord(y))  # ord() function is used to calculate ASCII value

# x="Anand"
# n=" "
# for i in x:
#     s=ord(i) 
#     t=bin(s) 
#     n=n+str(t)
# print(t)

# a="P"
# b=ord(a)  #it is converted in ASCII value
# c=bin(b)  #now it will be converted from ASCII value to Binary value
# print(c)

# # Right Shifting 
# x=15
# print(x>>2) #right
# print(x<<2) #left
# print(x<<3)

# a=39
# print(a<<3)

# # Single & operaator use
# # Returns True if both statements are true
# # & operator dono value ki binary ko add krke output deta hai
# x=15                 # binary of 15 = 1 1 1 1
# y=10                 # binary of 10 = 1 0 1 0
# z=x&y          # after & operators  = 1 0 1 0
# print(z)    # decimal value of this = 10 (Output)

# x=25            
# y=30
# z=x&y
# print(z)

# # or | operator Returns True if one of the statements is true
# x=15                  # binary of 15 = 1 1 1 1    
# y=10                  # binary of 10 = 1 0 1 0
# z=x|y            # after | operators = 1 1 1 1
# print(z)     # decimal value of this = 15 (Output)

# # EXOR ^ operator if any one statement is true then true
# x=15                    # binary of 15 = 1 1 1 1 
# y=10                    # binary of 10 = 1 0 1 0
# z=x^y              # after ^ operators = 0 1 0 1
# print(z)       # decimal value of this = 5 (Output)

# NOT ~ Operator reverse the result
x=15                 # binary of 15 = 1 1 1 1
print(~x)       # after ~ operators =