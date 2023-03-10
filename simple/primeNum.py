#Write a Python program to check if the square of a number is prime or not.

# Functions for making numbers square
def square(num):
    return num**2

#Functions for mchecking number is prime or not

def prime(nump):
    if nump > 1:
        for i in range(2,((nump//2)+1)):
            if (nump%i)==0:
                print(nump,' is not prime')
                break            
        else:
            print(nump,' is not prime')


#For taking number from user

number = int(input('Enter the number : '))
squareNum = square(number)
print ('The square of ',number,' is  ',squareNum)
prime(squareNum)


