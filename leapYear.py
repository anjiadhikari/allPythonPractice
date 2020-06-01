#Program  to find leap year

def checkLeapYear(year):
    if (year % 4 == 0 ):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print('It  is  a Leap Year')
            else:
                print('It is not a Leap Year')
        else:
            print('It is a Leap Year')
    else:
        print('It is not a Leap 1Year')

#Taking Year from users
year = int(input('Enter the Year : '))
checkLeapYear(year)
