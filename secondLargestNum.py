# Write a  Python program to print the second largest number from 3 numbers entered by the user.



#for taking input from the user

numbers =list(map(int,input('Enter the number  :').split()))
sett = set(number)

soretedNumber=sorted(sett,reverse=True)

print('Second Largest number is ::',sortedNumber[1])
