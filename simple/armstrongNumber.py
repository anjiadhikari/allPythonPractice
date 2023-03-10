#Write a Python program to check if a number is an Armstrong number or not

def armstrongCheck(n):
    sum = 0
    temp = n
    while n > 0:
        digit = n % 10
        sum +=digit**order
        n = n//10
    if (temp == sum):
        print('\n Number is armstrong \n')
    else:
        print('\n Number is not armstrong \n')


    


num = int(input('\n Enter the numbers :: '))
# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))
armstrongCheck(num)

    
