#WAP to demonstare file handling
file=open("anand.pdf","w")
eid=int(input("Enter Employee Id : "))
ename=input("Enter Employee Name : ")
esal=int(input("Enter Employee Salary : "))
file.write("Employee Id : "+str(eid)+"\n"+"Employee Name : "+ename+"\n"+"Employee Salary : "+str(esal)+"\n")
file.close()
print("Employee Record Saved !!! ")