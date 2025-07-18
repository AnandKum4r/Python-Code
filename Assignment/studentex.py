#WAP to demonstare file handling
file=open("Student.txt","w")
eroll=int(input("Enter Student Roll Number : "))
ename=input("Enter Student Name : ")
eadd=input("Enter Student Address : ")
eno=int(input("Enter Student Contact Number : "))
file.write("Student Roll Number is : "+str(eroll)+"\n"+"Student Name is : "+ename+"\n"+
"Student Address is : "+eadd+"\n"+"Student Contact Number is : "+str(eno)+"\n")
file.close()
print("Student Record Saved !!! ")