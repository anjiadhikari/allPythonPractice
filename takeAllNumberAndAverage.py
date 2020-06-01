#Write a Python program that accepts marks in 5 subjects and outputs the average marks
i = 5

marks = list()
while (i > 1):
    subject = float(input(print('Enter the marks of subject:')))
    marks.append(subject)
    i = i-1
averageValue = sum(marks) / len(marks)
print('Average : ',averageValue)
    
