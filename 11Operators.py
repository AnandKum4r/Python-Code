# Data types in python
# We have two types of data types 
# 1.Premitive data types
    # Integer: 8378784
    # Float: 9.455 
    # String: 'anand','ravi','66757'
    # Boolean : true,false
    # complex : 5j+4
    # character : 'A','B','C'
    # real : 0,1

#2.Sequential Data types
    # list,dic,set,tuples

# Data types casting
# Convert one data types to another data types called data type casting
    # We have two types of casting
    # Implicity: by default type casting
    # Explicity: by user

# #Implicity
# a=float(input("Enter a number: "))
# print(a)
# print(type(a))

# #Explicity 
# x=float(input("Enter a number: "))
# t=int(x)
# print(t)
# print(type(t))

#Input function bye default take string value
# v=input("Enter any value: ")
# print(v)
# print(type(v)) #its type will show string by default any value given int float etc

# x=True
# t=int(x)
# print(t)
# a=False
# g=int(a)
# print(g)

# Special operators: #,\t,\n,end,\\,''' '''
    # Hashtag is a single line comment in python
    # ''' ''' it is used for multiline comments
    # \t is a tab of space 
        # One \t= 4 tab space
    # \n This is used for new line
    # if you want to use any special char as a string then use \\ double slash
        # double slash \\ are useful to hide special character
    # end It is used for adding string from diffrent line

''' Hi Akash Bajpai Welcome to Gorakhpur ''' #This is multiline comment
x=10
y=20
z=x+y
h="Hello My Name Is \t Anand Kumar" #use of \t
p="Akash is my best friend \nHe is from Lucknow " #use of \n
print(z)
print(h)
print(p)
print("\n")     #this will be treated as special char
print("\\n")    #but after using \\ is will be treated as string 

print("Prateek here",end=" ")
print("Anand here", end=" ")
print("Huzaifa here")