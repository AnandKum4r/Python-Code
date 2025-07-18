sentence=input("Enter a sentence : ")
word=input("Enter which word you wants to count : ")
a=[]
count=0
a=sentence.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Occurrence of the given word is : ",count)