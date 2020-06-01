num=1

def divideByAll(num):
    for i in range(2,4):
        if num%i !=0:
            return False
            
    num +=1
    print(num)
    return True

divideByAll()
print('hi')
print(num)
            


