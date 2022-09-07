import math
from math import sqrt
a = int(input('Enter the number:'))
count = 0
for i in range(2, 1 + int(sqrt(a))):
    count += 1
    if a % i == 0:
        print(a,'is not prime because',
              i,'x',a//i,'=',a)
        break
else:
    print(a,'is prime')
print('The no.of iterations are:',count)
