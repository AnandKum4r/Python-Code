#Reverse string(Palindrome)
string=input("Enter a string : ")
print(string)
rstring="".join(reversed(string))
print(rstring)
if string==rstring:
 print("String is palindrome")
else:
 print("String is not palindrome")