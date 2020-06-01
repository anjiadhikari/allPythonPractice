
revNum = 0
def palindromeNum(num):
    while num > 0:
        digit = num % 10
        revNum = (revNum * 10) + digit
        num /=10


