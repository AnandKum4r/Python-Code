basic=float(input("Enter basic salary : "))
if basic<=4000:
 da=basic*0.5
 hra=basic*0.1
elif basic<=8000:
 da=basic*0.6
 hra=basic*0.2
elif basic<=12000:
 da=basic*0.7
 hra=basic*0.25
else:
 da=basic*0.8
 hra=basic*0.3
gross=basic+hra+da
print("Gross Salary : ", gross)
