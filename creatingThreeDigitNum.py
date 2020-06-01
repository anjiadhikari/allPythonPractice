#Write a Python program to input a single digit(n) and print a 3 digit number created as <n(n+1)(n+2)>.

#Eg: If you enter 7, then the output should be 789.

num = int(input('Enter the number: '))
num1 = num+1
num2 = num+2
print(num,num1,num2)