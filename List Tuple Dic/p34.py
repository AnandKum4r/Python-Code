#append
mylist=[]
print("Enter five numbers : ")
for i in range(0,5):
 n=int(input())
 mylist.append(n)
print(mylist)
print("Max no = ",max(mylist))
print("Min no = ",min(mylist))