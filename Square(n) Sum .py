# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum +=num*num
    return sum


def square_sum(numbers):
    return sum(x * x for x in numbers)

a = [1,2,2]
b = [2,2,3,5]
print(square_sum(a))
print(square_sum(b))
