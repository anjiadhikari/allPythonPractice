# Write a Python program to print the following series:

# a) 1,4,7,10….n terms

# b) 1,-4,7,-10,…,n terms


# a) 1,4,7,10….n terms

def series1(n):
    for i in range (1,n+1):
        print(1+(i-1)*3)

    
# b) 1,-4,7,-10,…,n terms
def series2(n):
    for i in range (1,n+1):
        print((1+(i-1)*3)*(-1)**(i+1))



num = int(input('Enter the nummber upto :'))
series1(num)
print('\n \n \n')

series2(num)