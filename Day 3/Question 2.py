print('Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE function.')
print("Prime numbers between", 1, "and", 200, "are:")

for num in range(1, 200):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)