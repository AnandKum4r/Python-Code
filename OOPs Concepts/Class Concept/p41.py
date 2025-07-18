class Employee:
 def setEmployee(self,empid,empname,empsalary):
  self.empid=empid
  self.empname=empname
  self.empsalary=empsalary
 def viewEmployee(self):
  print("Employee ID = ",self.empid)
  print("Employee name = ",self.empname)
  print("Employee Salary = ",self.empsalary)
emp=Employee()
emp.setEmployee(101,"Anand",100000)
emp.viewEmployee()
