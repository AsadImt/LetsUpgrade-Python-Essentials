print('Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon as you encounter the first armstrong number. Use while loop')

limit = 1042000

while limit <= 702648265:
    order = len(str(limit))
    sum=0
    num = limit    
    while num > 0:        
        digit = num % 10        
        sum += digit ** order        
        num //= 10
    if limit == sum:
        print("The first armstrong number is :",limit)
        break
    
    limit += 1