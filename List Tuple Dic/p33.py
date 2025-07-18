#list element input by user
n=int(input("Enter no of elements : "))
list=[]
for i in range(0,n):
 e=int(input())
 list.insert(i,e)
print("Display all elements from list ")
for e in list:
 print(e)