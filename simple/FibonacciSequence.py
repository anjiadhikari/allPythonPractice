#Write a Python program to print the sum of the following sequence:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377.......... (n terms) [ Fibonacci Sequence]

def Fibonacci(n):


# first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2
                # update values
            n1 = n2
            n2 = nth
            count += 1
    




num = int(input('Enter the numbers of Fibonacci series to be print:: '))
Fibonacci(num)
        
