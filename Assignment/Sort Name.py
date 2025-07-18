list=[]
print("Enter names of your five friends : ")
for i in range(0,5):
 n=input()
 list.append(n)
print("Names before sorting :", list)
list.sort()
print("Names after sorted : ", list)