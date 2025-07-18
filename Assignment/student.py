class student:
 def setValue(self,rollno,name,fee):
  self.rollno=rollno
  self.name=name
  self.fee=fee
 def display(self):
  print("Student roll no : ",self.rollno)
  print("Student name : ",self.name)
  print("Student fee : ",self.fee)
e=student()
erollno=int(input("Enter student roll no : "))
ename=input("Enter student name : ")
efee=int(input("Enter student fee : "))
e.setValue(erollno,ename,efee)
e.display()
