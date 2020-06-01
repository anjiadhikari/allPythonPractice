# Write a Python program that inputs three numbers and calculates two sums as per this:
# Sum 1 as the sum of all numbers.
# Sum 2 as the sum of non-duplicate numbers, if there are duplicates, then ignore them.

sum1= 0.0
sum2 = 0.0

#for taking input from the user

numAll= list()

while True:
    num = input('Enter the number  :')
    if num == 'done':
        break
    else:
        num = float(num)
        numAll.append(num)
    
print('\n All the numbers are :')
print(numAll)

#for finding sum all the numbers enterd by the user
for numb in numAll:
    sum1 =sum1+numb
print('\n The sum of all the numbers is :',sum1)


#converting list into dic so that all duplicate numbers will be removed
numAllNoDup = list(dict.fromkeys(numAll))
print('\n The non duplicate numbers are',numAllNoDup)
#finding sum of  non-duplicate numbers
for numb in numAllNoDup:
    sum2 =sum2+numb
print('\n The sum of non-duplicate numbers is :',sum2)



    