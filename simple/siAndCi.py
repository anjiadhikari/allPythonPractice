#Write a Python program to compute Simple Interest and Compound Interest.
p = float(input('Enter the p amonut:'))
t = float(input('Enter the time in year:'))
r = float(input('Enter the rate in percentage:'))
s = (p*t*r)/100
g = float(input('no of compounding gone'))
c = (p*(1+(r/100))**g) - p

print('Simple intrest is : ',s)
print('compound intrest is : ',c)
