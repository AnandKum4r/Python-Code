"""
Ajay Kumar Singh
A.K.Singh
"""
name=input("Enter your full name :")
shortname=name.split(" ")
#print(shortname)
print("Your short name : ",end="")
for n in range(len(shortname)-1):
  print(shortname[n][0]+".",end="")
print(shortname[len(shortname)-1])