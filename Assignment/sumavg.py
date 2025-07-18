list=[]
print("Enter ten number to the list ")
for i in range(0,10):
 n=int(input())
 list.append(n)
avg=sum(list)/len(list)
print("Sum of elements in given list is :", sum(list))
print("Average of elements in given list is :", avg)

