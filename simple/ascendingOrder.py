#Write a Python program to read three numbers and print them in ascending order.

#for taking input from the user

numAll= list()

while True:
    num = input('Enter the number  :')
    if num == 'done':
        break
    else:
        num = float(num)
        numAll.append(num)
    
print('\n All the numbers before Ascending order :')
print(numAll)

print('\n All the numbers after in Ascending order :')
numAll.sort()
print(numAll)

#using while loope for sorting in asceding order
numbers =list(map(int,input('Enter the number to be sorted :').split()))

sortedNum=[]
i=0
length=len(numbers)
while(i < length):
	tempo = min(numbers)
	sortedNum.append(tempo)
	numbers.remove(tempo)
	i+=1

print('All Numbers after sorting is::'  ,sortedNum)










