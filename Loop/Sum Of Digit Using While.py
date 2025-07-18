#Sum of digits 123=6
num=int(input("Etner a digit :"))
sum=0
while num>0:
 rem=num%10
 sum=sum+rem
 num=int(num/10)
print("Sum of digits = ",sum)