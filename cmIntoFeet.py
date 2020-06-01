#Write a Python program that reads your height in cms and converts your height to feet and inches.
heightCM = float(input('Enter the height in CM: '))
totalInch = heightCM * 0.393701
heightInch = (totalInch % 12)
heightFeet = (totalInch - heightInch)*0.0833333

print('The height is : ',heightFeet,' feet AND 163',heightInch,' inch')