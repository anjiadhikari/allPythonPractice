#print number divide by 5 only but not 10
import numpy as nm
a=[5,10,15,20,25,30,35,36,40,49]
aLen=len(a)
b=nm.empty((1,aLen))
for i in range(aLen):
	if( (a[i]%5==0) and (not(a[i]%10==0))):
		b=a[i]
		print(b)
print("The numbers are :")

for i in range (10):
	print(b)

