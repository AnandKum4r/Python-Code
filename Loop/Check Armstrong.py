#Armstrong
num=int(input("Enter a number of three digits : "))
temp=num
sum=0
while num>0:
 rem=num%10
 sum=sum+(rem*rem*rem)
 num=int(num/10)
if temp==sum:
 print("Number is armstrong")
else:
 print("Number is not armstrong")