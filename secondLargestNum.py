# Write a  Python program to print the second largest number from 3 numbers entered by the user.



#for taking input from the user

numAll= list()

while True:
    num = input('Enter the number  :')
    if num == 'done':
        break
    else:
        num = float(num)
        numAll.append(num)



print('\n All the numbers after in Ascending order :')
numAll.sort()
print(numAll)
sizeOfList = len(numAll)

print('Second Largest number is ::',numAll[sizeOfList-2])