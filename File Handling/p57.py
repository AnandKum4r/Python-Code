#Append Mode
file=open("employee.doc","a")
eid=int(input("Enter Employee Id : "))
ename=input("Enter Employee Name : ")
esal=int(input("Enter Employee Salary : "))
file.write("Employee Id : "+str(eid)+"\n"+"Employee Name : "+ename+"\n"+"Employee Salary : "+str(esal)+"\n")
file.close()
print("Employee Data Altered !!! ")