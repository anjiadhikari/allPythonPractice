#printing the sum of the natural numbers taking input from the users
2
def sumNatural(num):
	sum = 0 
#calaculating dum
	while num>0:
		sum+=num
		num-1
		
	return sum

#taking input from the users
num = input("Enter the numbers: ")
num =int(num)
totalSum= sumNatural(num)
print(totalSum)