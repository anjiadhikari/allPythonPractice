#write a Python program to find the largest of 3 numbers.
num1 = float(input('Enter the num1:'))
num2 = float(input('Enter the num2:'))
num3 = float(input('Enter the num3:'))

if ((num1>num2) and (num1>num3) ):
    print('The greatest number is : ',num1)
elif((num2>num1) and (num2>num3)):
    print('The greatest number is : ',num2)
else:
    print('The greatest number is : ',num3)


