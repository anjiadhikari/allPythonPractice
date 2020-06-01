#Palindrome Of Any Numbers


def palindromeNum(num):
    revNum = 0.0
    temp = num
    while (num > 0):
        digit = num % 10
        revNum = (revNum * 10) + digit
        num = num //10
    if temp == revNum:
        print('The number is palindrome')
    else:
        print('The number is not palindrome')
    return revNum



numb = float(input('Enter the Number : '))
print('The Number You Enter: ',numb)

print('The Reverse Of Number You Enter is: ',palindromeNum(numb))




