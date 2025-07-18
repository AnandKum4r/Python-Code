# Collection in python 
# collection a collection refers to a group of items that are stored together.
# they are two types : > Similar and Different
# 1. Similar Data types : Array
# 2. Different Data types :
    #List
    #Dic
    #tuples
    #sets

# What is List
    # List is a collection of object type of element
    # list is a mutable(changable)
    # List denoted by square bracket
    # List store the on index
    # List is dynamic
    # List is a class of collection
    # List will work on positive indexing and negative indexing

k=[3,4,5,6,'anand','prateek','huzaifa','huzaifa','huzaifa',88,25.5,True,False,]
print(k)

# Remove > is used to remove any element by its name
k.remove('anand')
print(k)

# Insert > is a in-built method of list to add new element in list at specific postion
k.insert(4,'Anurag')
print(k)

# Append > is a in-built method of list to add new element at last of list
k.append('Noida')
print(k)

# Pop > is a in-built method to remove any element by its index number
k.pop(3)    #it remove last element by default if any index not given
print(k)

# Reverse > is used to reverse whole list
k.reverse()
print(k)

k2=[]          # Empty list
k2=k.copy()
print(id(k))
print(id(k2))
print(k2)

print(k.count('huzaifa'))
print(k.index('huzaifa'))
# finding all index of huzaifa in list
for i in range(0,len(k)):
    if(k[i]=='huzaifa'):
        print(i," ",k[i])