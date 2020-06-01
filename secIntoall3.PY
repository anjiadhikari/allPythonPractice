#Write a Python program that reads a number of seconds and prints it in the format - hrs:min:secs

totalSec = float(input('Enter the total second : '))
hrs = int(totalSec/3600)
min = int ((totalSec - hrs*3600)/60)
sec = totalSec - (hrs *3600 + min *  60)
print ('Hrs:',hrs,'Min:',min,'Sec:',sec)


