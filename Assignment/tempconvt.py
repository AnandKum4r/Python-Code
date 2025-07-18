import tempconv
a=int(input("Enter the temperature in celcius :"))
x=tempconv.ctof(a)
print("Temperature in farenheit is :", x)
b=int(input("Now enter the temperature in farenheit :"))
y=tempconv.ftoc(b)
print("Temperature in celcius is :", y)