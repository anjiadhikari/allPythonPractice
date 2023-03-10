#Write a Python program to compute the factorial of a number.

def factorial(n):
    mul = 1
    if n < 0:
        print("Factorial cannot be found for negative numbers")
    elif n == 0:
        print("Factorial of 0 is 1")
    elif n == 1:
        return n
    else:
        print('hi')
        for i in range (2,n+1):
            mul = mul*i
        return mul
        
num = int(input('Enter the numbers:: '))
print("Factorial of", num, "is: ", factorial(num))


